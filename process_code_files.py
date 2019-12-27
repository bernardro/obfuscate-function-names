import re
import os
from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

from utilz import *


embed_str = "---embedhere---"
regx_prefx_sfx = "(?<=[^a-zA-Z0-9_])"+embed_str+"(?=[^a-zA-Z0-9_])"


def replaceinpath(file_path, cur_replaceza):
    fh, abs_path = mkstemp()
    with fdopen(fh, 'w') as new_file:
        with open(file_path) as old_file:
            for oldline in old_file:
                # first embed the replacer in a whole-word-finding regex
                rgx_word_finder = regx_prefx_sfx.replace(embed_str, cur_replaceza['theformer'])
                newline = re.sub(rgx_word_finder, cur_replaceza['isnow'], oldline)
                # newline = oldline.replace(cur_replaceza['theformer'], cur_replaceza['isnow'])
                new_file.write(newline)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


def walk_replacements(replacers, topdir, exten):
    rgx_rplc = re.compile(r"[a-zA-Z0-9_]+")
    max_num_replacers = len(replacers)
    curr_replacer_indx = 0
    for curr_replacer in replacers:
        for dirpath, dirnames, files in os.walk(topdir):
            for name in files:
                if name.lower().endswith(exten):
                    currpath = os.path.join(dirpath, name)
                    replaceinpath(currpath, curr_replacer)
        curr_replacer_indx = curr_replacer_indx + 1
        curr_percentage = (curr_replacer_indx / max_num_replacers) * 100
        print("File processing at [", round(curr_percentage), "] percent")


prepd_replacerz = loadjsonfile('./DATA/processed_replacers.json')
walk_replacements(prepd_replacerz, "./TARGETFILES", ".js")




