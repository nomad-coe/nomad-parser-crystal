"""
Used to read the Crystal manual and generate the input file structure from it.
From the structure one can automatically generate the metainfo definitions and
the pickle file that is used to validate the structure during parsing.
"""
import re
import json
import pickle
from crystalparser.generic.inputparsing import Section, Keyword, metainfo_data_prefix, metainfo_section_prefix


#===============================================================================
def generate_input_tree(filepath):

    with open(filepath, "r") as fin:
        lines = fin.readlines()

    # Create the sections
    section_regex_string = "\\\> \\\&(\w+) \.\.\.\s+\\\> \\\&END  \\\>  \$"
    section_regex = re.compile(section_regex_string)
    root_section = Section("", "The root section for CPMD input. Contains all the other input sections.")

    for i_line in range(len(lines)):
        line = lines[i_line]
        match = section_regex.match(line)
        if match:
            section_name = match.groups()[0]
            section = Section(section_name)

            desc_end = "\>"
            desc_ended = False
            description = []
            i_line_desc = 1
            while not desc_ended:
                desc_line = lines[i_line + i_line_desc]
                i_line_desc += 1
                if desc_line.startswith(desc_end):
                    desc_ended = True
                else:
                    description.append(desc_line.strip()[0:-2])
            section.description = " ".join(description)
            if section_name in root_section.subsections:
                raise KeyError("Multiple sections with the same name")
            root_section.subsections[section_name] = section

    # Create the keywords
    keyword_regex_string = r"\\keyword\{([\w ]+)\}\{(.*?)\}\{(.*?)\}\{(.*?)\}\{\\&(\w+)\}"
    keyword_regex = re.compile(keyword_regex_string)
    spekeyword_regex_string = r"\\spekeyword\{(\w+)\}\{(.*?)\}\{(.*?)\}\{(.*?)\}\{\\&(\w+)\}\{(\w+)\}"
    spekeyword_regex = re.compile(spekeyword_regex_string)

    for i_line in range(len(lines)):
        line = lines[i_line]
        keywordmatch = keyword_regex.match(line)
        spekeywordmatch = spekeyword_regex.match(line)
        if keywordmatch or spekeywordmatch:
            if keywordmatch:
                groups = keywordmatch.groups()
            elif spekeywordmatch:
                groups = spekeywordmatch.groups()
            keyword_name = groups[0]
            # print(keyword_name)
            # if keyword_name == "OPTIMIZE WAVEFUNCTION":
                # print("FOUND")
            available_options1 = groups[1]
            available_options2 = groups[2]
            parent_section_name = groups[4]
            keyword = Keyword(keyword_name)
            if spekeywordmatch:
                unique_name = groups[5]
                keyword.unique_name = unique_name
            else:
                keyword.unique_name = keyword_name

            # Parse the available options in the first list
            if available_options1:
                available_options = available_options1.split(",")
                for option in available_options:
                    if "=" in option:
                        option_split = option.split("=")
                        option_name = option_split[0]
                    else:
                        option_name = option
                    option_name = re.sub(r"[\{\}\[\]\\ ]", "", option_name)
                    keyword.available_options.append(option_name)
                # print(keyword.available_options)

            # Parse the available options in the second list
            if available_options2:
                available_options = available_options2.split(",")
                for option in available_options:
                    if "=" in option:
                        option_split = option.split("=")
                        option_name = option_split[0]
                    else:
                        option_name = option
                    option_name = re.sub(r"[\{\}\[\]\\ ]", "", option_name)
                    keyword.available_options.append(option_name)
                # print(keyword.available_options)

            # Parse the description
            desc_ended = False
            description = []
            i_line_desc = 1
            n_braces = 0
            while not desc_ended:
                desc_line = lines[i_line + i_line_desc]
                i_line_desc += 1
                for i_char, character in enumerate(desc_line):
                    if character == "{":
                        n_braces += 1
                    elif character == "}":
                        n_braces -= 1
                        if n_braces == 0:
                            # if desc_line.startswith("\desc{"):
                                # desc_line = desc_line
                            description.append(desc_line[0:i_char].strip())
                            desc_ended = True
                if n_braces != 0:
                    full_line = desc_line.strip()
                    # if full_line.startswith("\desc{"):
                        # full_line = full_line[6:]
                    if full_line.endswith(r"\\"):
                        full_line = full_line[:-2]
                    if full_line == "%":
                        full_line = "\n"
                    description.append(full_line)
            keyword.description = " ".join(description)
            if keyword.description.startswith("\desc{"):
                keyword.description = keyword.description[6:]
                # print("DESC")

            parent_section = root_section.subsections[parent_section_name]
            parent_section.keywords[keyword_name].append(keyword)

    return root_section


#===============================================================================
def generate_pickle(filepath):
    input_tree = generate_input_tree(filepath)
    file_name = "../versions/cpmd41/input_data/cpmd_input_tree.pickle"
    fh = open(file_name, "wb")
    pickle.dump(input_tree, fh, protocol=2)


#===============================================================================
def generate_input_metainfos(filepath):

    json_root = {
        "type": "nomad_meta_info_1_0",
        "description": "Metainfo for the values parsed from a CPMD input file.",
        "dependencies": [ {
            "relativePath": "cpmd.general.nomadmetainfo.json"
            }],
    }

    root = generate_input_tree(filepath)
    parent = None
    root.name = ""
    root.description = "Contains the CPMD input file contents."
    container = []
    generate_metainfo_recursively(root, parent, container)
    json_root["metaInfos"] = container
    with open("input_metainfo.json", "w") as f:
        f.write(json.dumps(json_root, indent=2, separators=(',', ': ')))


#===============================================================================
def generate_metainfo_recursively(section, parent, container):

    json = generate_section_metainfo_json(section, parent)
    container.append(json)
    for subsection in section.subsections.values():
        generate_metainfo_recursively(subsection, section, container)
    for keyword_list in section.keywords.values():
        for keyword in keyword_list:
            key_json = generate_keyword_metainfo_json(keyword, section)
            options_json = generate_options_metainfo_json(keyword, section)
            parameter_json = generate_parameter_metainfo_json(keyword, section)
            container.append(key_json)
            container.append(options_json)
            container.append(parameter_json)
    if parent is not None:
        def_json = generate_default_keyword_metainfo_json(section)
    container.append(def_json)


#===============================================================================
def generate_keyword_metainfo_json(keyword, section):
    json_obj = {}
    json_obj["name"] = metainfo_section_prefix + "{}.{}".format(section.name, keyword.unique_name.replace(" ", "_"))
    json_obj["superNames"] = [metainfo_section_prefix + "{}".format(section.name)]

    # Description
    description = keyword.description
    if description is None or description.isspace():
        description = "Settings for {}".format(keyword.unique_name.replace(" ", "_"))
    json_obj["description"] = description
    json_obj["kindStr"] = "type_section"

    return json_obj


#===============================================================================
def generate_parameter_metainfo_json(keyword, section):
    json_obj = {}
    json_obj["name"] = metainfo_data_prefix + "{}.{}_parameters".format(section.name, keyword.unique_name).replace(" ", "_")
    json_obj["description"] = "The parameters for keyword {}.".format(keyword.unique_name.replace(" ", "_"))
    json_obj["superNames"] = [metainfo_section_prefix + "{}.{}".format(section.name, keyword.unique_name.replace(" ", "_"))]
    json_obj["dtypeStr"] = "C"
    json_obj["shape"] = []

    return json_obj


#===============================================================================
def generate_options_metainfo_json(keyword, section):
    json_obj = {}
    json_obj["name"] = metainfo_data_prefix + "{}.{}_options".format(section.name, keyword.unique_name.replace(" ", "_"))
    json_obj["description"] = "The options given for keyword {}.".format(keyword.unique_name.replace(" ", "_"))
    json_obj["superNames"] = [metainfo_section_prefix + "{}.{}".format(section.name, keyword.unique_name.replace(" ", "_"))]
    json_obj["dtypeStr"] = "C"
    json_obj["shape"] = []

    return json_obj


#===============================================================================
def generate_default_keyword_metainfo_json(section):
    json_obj = {}
    json_obj["name"] = metainfo_data_prefix + "{}_default_keyword".format(section.name)
    json_obj["description"] = "The parameters that are present in the section {} even without a keyword.".format(section.name)
    json_obj["superNames"] = [metainfo_section_prefix + "{}".format(section.name)]
    json_obj["dtypeStr"] = "C"
    json_obj["shape"] = []

    return json_obj


#===============================================================================
def generate_section_metainfo_json(section, parent):
    json_obj = {}

    if parent is None:
        json_obj["name"] = "x_cpmd_section_input"
        json_obj["superNames"] = ["section_run"]
    else:
        json_obj["name"] = metainfo_section_prefix + "{}".format(section.name.replace(" ", "_"))
        json_obj["superNames"] = ["x_cpmd_section_input"]
    json_obj["kindStr"] = "type_section"

    description = section.description
    if description is None or description.isspace():
        description = "Settings for {}".format(section.name)
    json_obj["description"] = description

    return json_obj


#===============================================================================
if __name__ == "__main__":
    filepath = "../versions/cpmd41/input_data/manual.tex"
    generate_pickle(filepath)
    # generate_input_metainfos(filepath)
