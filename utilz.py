import json
import string
import random


def getlistfromfile(file_path):
    extractedlist = []
    with open(file_path) as file_with_list:
        for listline in file_with_list:
            extractedlist.append(listline.rstrip())
    return extractedlist


def random_generator_upper(min_char, max_char, chars2=string.ascii_uppercase + string.digits):
    uppercharz = string.ascii_uppercase + "_"
    prefix = "".join(random.choice(uppercharz) for x in range(1))
    suffix = "".join(random.choice(chars2) for x in range(random.randint(min_char, max_char)))
    return prefix + suffix


def dedup(seq):
    deduped_seq = []
    seen = set()
    for list_elem in seq:
        list_elem_added = False
        if list_elem['theformer'] not in seen:
            seen.add(list_elem['theformer'])
            list_elem_added = True
        if list_elem_added:
            deduped_seq.append(list_elem)
    return deduped_seq


def loadjsonfile(source_json_file):
    with open(source_json_file) as json_data:
        unsorted_replacers = json.load(json_data)
        sorted_replacers = sorted(unsorted_replacers, key=lambda x: len(x['theformer']), reverse=True)
        return dedup(sorted_replacers)


def savejsonfile(new_file_name, json_data):
    with open(new_file_name, 'w') as outfile:
        json.dump(json_data, outfile)

