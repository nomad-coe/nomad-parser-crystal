# Copyright 2016-2018 Sami Kivistö, Lauri Himanen, Fawzi Mohamed, Ankit Kariryaa
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from nomadcore.simple_parser import SimpleMatcher as SM
from nomadcore.simple_parser import extractOnCloseTriggers

META_PREFIX = "x_crystal_input"
META_SECTION_PREFIX = "x_crystal_section_input"


class InputMatcher(SM):
    """A subclass of SimpleMatcher that makes the handling of input a bit
    simpler.
    """
    def __init__(self,
            startReStr,
            endReStr=None,
            subMatchers=tuple(),
            sections=tuple(),
            subFlags=SM.SubFlags.Sequenced,
            weak=False,     # this matcher should not "steal" the position
            repeats=False,  # this matcher is expected to repeat
            required=False,  # this value is required to have been matched on section close
            floating=False,  # this section goes not steal the context, useful for example for low level debugging/error messages.
            # valid from the point they are read until the exit from the enclosing section
            forwardMatch=False,  # if start match should not eat input, but be forwarded to adHoc and subMatchers
            name="",
            adHoc=None,
            otherMetaInfo=tuple(),  # The metainfos that are later manually added ot the backend
            fixedStartValues=None,
            fixedEndValues=None,
            dependencies=None,
            defLine=0,
            defFile='',
            coverageIgnore=False,  # mark line as ignored in coverage analysis
            onClose=None,   # A dictionary of onClose callbacks that are specific to this SimpleMatcher
            onOpen=None,   # A dictionary of onOpen callbacks that are specific to this SimpleMatcher
            startReAction=None,  # A callback function that is called with the groups that were matched from the startReStr.
            ):

        if name != "":
            startReStr = r"(?i)(?P<{}_{}>{})".format(META_PREFIX, name, startReStr)

        for i_section, section in enumerate(sections):
            if section:
                sections[i_section] = "{}_{}".format(META_SECTION_PREFIX, section)
            else:
                sections[i_section] = META_SECTION_PREFIX

        super(InputMatcher, self).__init__(
            startReStr,
            endReStr,
            subMatchers,
            sections,
            subFlags,
            weak,
            repeats,
            required,
            floating,
            forwardMatch,
            name,
            adHoc,
            otherMetaInfo,
            fixedStartValues,
            fixedEndValues,
            dependencies,
            defLine,
            defFile,
            coverageIgnore,
            onClose,
            onOpen,
            startReAction,
        )


class CrystalInputParser(object):

    def __init__(self, mainparser):

        # Gather onClose triggers that are defined within this class and add
        # them to the main parser
        on_close = {}
        for attr, callback in extractOnCloseTriggers(self).items():
            on_close[attr] = [callback]
        mainparser.on_close.update(on_close)

        IM = InputMatcher

        # Define root matcher
        self.root_matcher = IM("",
            forwardMatch=True,
            sections=[""],
            subMatchers=[
                IM("CRYSTAL|SLAB|POLYMER|HELIX|MOLECULE|EXTERNAL|DLVINPUT", name="system_type"),
                IM("OPTGEOM|FREQCALC|ANHARM", name="calculation_type"),
                IM("DFT",
                    sections=["dft"],
                    subFlags=SM.SubFlags.Unordered,
                    subMatchers=[
                        IM("SPIN"),
                        IM("EXCHANGE",
                            subMatchers=[
                                IM("LDA|VBH|BECKE|PBE|PBESOL|mPW91|PWGGA|SOGGA|WCGGA", name="dft_exchange"),
                            ]
                        ),
                        IM("CORRELAT",
                            subMatchers=[
                                IM("PZ|VBH|VWN|LYP|P86|PBE|PBESOL|PWGGA|PWLSD|WL", name="dft_correlation")
                            ]
                        ),
                        IM("SVWN|BLYP|PBEXC|PBESOLXC|SOGGAXC|B3PW|B3LYP|PBE0|PBESOL0|B1WC|WCILYP|B97H|PBE0-13|HYBRID|NONLOCAL|HSE06|HSESOL|HISS|RSHXLDA|wB97|wB97X|LC-WPBE|LC-WPBESOL|LC-WBLYP|M05-2X|M05|M062X|M06HF|M06L|M06|B2PLYP|B2GPPLYP|mPW2PLYP|DHYBRID", name="dft_xc_shortcut")
                    ]
                ),
            ]
        )

    def onClose_x_crystal_section_input_dft(self, backend, gIndex, section):
        shortcut = section.get_latest_value("x_crystal_input_dft_xc_shortcut")
        exchange = section.get_latest_value("x_crystal_input_dft_exchange")
        correlation = section.get_latest_value("x_crystal_input_dft_correlation")

        xc_list = []
        xc_summary = []

        # Handle the XC's defined with single shortcut
        if shortcut:
            shortcut = shortcut.upper()
            shortcut_map = {
                "PBE0": "HYB_GGA_XC_PBEH",
                "B3LYP": "HYB_GGA_XC_B3LYP",
                "HSE06": "HYB_GGA_XC_HSE06",
                "M06": "HYB_MGGA_XC_M06",
                "M05-2X": "HYB_MGGA_XC_M05_2X",
                "LC-WPBE": "HYB_GGA_XC_LRC_WPBE",
            }
            norm_xc = shortcut_map.get(shortcut)
            if norm_xc:
                xc_list.append(norm_xc)

        # Handle the exchange part
        if exchange:
            exchange = exchange.upper()
            exchange_map = {
                "PBE": "GGA_X_PBE",
                "PBESOL": "GGA_X_PBE_SOL",
                "BECKE": "GGA_X_B88",
                "LDA": "LDA_X",
                "PWGGA": "GGA_X_PW91",
            }
            norm_x = exchange_map.get(exchange)
            if norm_x:
                xc_list.append(norm_x)

        # Handle the correlation part
        if correlation:
            correlation = correlation.upper()
            correlation_map = {
                "PBE": "GGA_C_PBE",
                "PBESOL": "GGA_C_PBE_SOL",
                "PZ": "LDA_C_PZ",
                "WFN": "LDA_C_VWN",
                "PWGGA": "GGA_C_PW91",
            }
            norm_c = correlation_map.get(correlation)
            if norm_c:
                xc_list.append(norm_c)

        # Go throught the XC list and add the sections and gather a summary
        for xc in xc_list:
            sid = backend.openSection("section_XC_functionals")
            weight = 1.0
            backend.addValue("XC_functional_name", xc)
            backend.addValue("XC_functional_weight", weight)
            backend.closeSection("section_XC_functionals", sid)
            xc_summary.append("{}*{}".format(weight, xc))

        if len(xc_list) == 0:
            print(shortcut)
            print(exchange)
            print(correlation)

        backend.addValue("XC_functional", "+".join(sorted(xc_summary)))

    def debug(self):
        print("DEBUG")
