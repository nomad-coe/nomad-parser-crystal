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
            endAction=None,  # A function that is called when this SimpleMatcher finishes
            onClose=None,   # A dictionary of onClose callbacks that are specific to this SimpleMatcher
            onOpen=None,   # A dictionary of onOpen callbacks that are specific to this SimpleMatcher
            startReTransform=None,  # A callback function that is called with the groups that were matched from the startReStr.
            ):

        if name != "":
            startReStr = "(?P<{}_{}>{})".format(META_PREFIX, name, startReStr)

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
            endAction,
            onClose,
            onOpen,
            startReTransform,
        )


class CrystalInputParser(object):

    def __init__(self, mainparser):

        # Gather onClose triggers that are defined within this class and add
        # them to the main parser
        on_close = {}
        for attr, callback in extractOnCloseTriggers(self).items():
            on_close[attr] = [callback]
        mainparser.onClose.update(on_close)

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
                        IM("SVWN|BLYP|PBEXC|PBESOLXC|SOGGAXC|B3PW|B3LYP|PBE0|PBESOL0|B1WC|WCILYP|B97H|PBE0-13|HYBRID|NONLOCAL|HSE06|HSESOL|HISS|RSHXLDA|wB97|wB97X|LC-wPBE|LC-wPBESOL|LC-wBLYP|M06L|M05|M052x|M06|M062X|M06HF|B2PLYP|B2GPPLYP|mPW2PLYP|DHYBRID", name="dft_xc_shortcut")
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
            shortcut_map = {
                "PBE0": "HYB_GGA_XC_PBEH",
                "B3LYP": "HYB_GGA_XC_B3LYP",
            }
            norm_xc = shortcut_map.get(shortcut)
            if norm_xc:
                xc_list.append(norm_xc)

        # Handle the exchange part
        if exchange:
            exchange_map = {
                "PBE": "GGA_X_PBE",
                "PBESOL": "GGA_X_PBE_SOL",
            }
            norm_x = exchange_map.get(exchange)
            if norm_x:
                xc_list.append(norm_x)

        # Handle the correlation part
        if correlation:
            correlation_map = {
                "PBE": "GGA_C_PBE",
                "PBESOL": "GGA_C_PBE_SOL",
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

        backend.addValue("XC_functional", "_".join(sorted(xc_list)))

    def debug(self):
        print("DEBUG")
