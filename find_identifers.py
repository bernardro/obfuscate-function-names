import os
import re

from utilz import *

# regx_prefix = "(?<=[ \t])"
# regx_infix = "([a-zA-Z0-9_]+)"
# regx_suffix = "(( +=?)|( ?=?))(( +\\()|( ?\\())"
# regx_wrapped_suffix = "(?=(" + regx_suffix + "))"
# func_find_rgx = regx_infix + regx_wrapped_suffix


# func_find_rgx = "((?<=\\.)([A-Z_]{2,}))|(([A-Z_]{2,})(?= ?:))"
# func_find_rgx = "([A-Z_]{2,})(?= ?: ?)"
func_find_rgx = "([A-Z_]+)(?= ?: ?)"


def detect_occurences_in_line(code_line, regx):
    strng_val = ""

    regx_results = re.findall(regx, code_line)
    if regx_results is not None:
        if isinstance(regx_results, (frozenset, list, set, tuple,)):
            if len(regx_results) > 0:
                # strng_val = regx_results[0][0]
                strng_val = regx_results[0]
        else:
            strng_val = regx_results

    return strng_val


def find_function_names_recursive(topdir, exten):
    xcld_lst = getlistfromfile("./DATA/const_names_to_exclude.txt")
    final_lst = []
    for dirpath, dirnames, files in os.walk(topdir):
        for name in files:
            if name.lower().endswith(exten):
                currpath = os.path.join(dirpath, name)
                with open(currpath) as code_file_content:
                    for code_line in code_file_content:
                        func_name_in_line = detect_occurences_in_line(code_line, func_find_rgx)
                        if func_name_in_line not in xcld_lst:
                            if func_name_in_line not in final_lst:
                                if func_name_in_line:
                                    final_lst.append(func_name_in_line)

    return list(set(final_lst))


def run_obfuscator(start_dir, trgt_ext):
    final_lst = find_function_names_recursive(start_dir, trgt_ext)

    outp_fil = './DATA/consts_name_output.txt'
    try:
        os.remove(outp_fil)
    except OSError:
        pass

    with open(outp_fil, 'w') as func_names_file:
        for curr_func_name in final_lst:
            func_names_file.write("%s\n" % curr_func_name)


# remove all server-side files - leave only client files
start_folder = "/ORIGIFILES"
trgt_file_ext = ".js"
run_obfuscator(start_folder, trgt_file_ext)
