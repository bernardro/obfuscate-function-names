from utilz import *


def pre_process_replacers(replazers):
    randkeez = []
    for replacerpair in replazers:

        unique_rand = random_generator_upper(1, 2)
        while unique_rand in randkeez:
            unique_rand = random_generator_upper(1, 2)

        randkeez.append(unique_rand)
        replacerpair['isnow'] = unique_rand


deduped_replacerz = loadjsonfile('./DATA/replacers.json')
pre_process_replacers(deduped_replacerz)
savejsonfile("./DATA/processed_replacers.json", deduped_replacerz)
