# -*- coding: utf-8 -*-

"""
PC configuration generator.

Author: Eduardo Ferreira
"""

import json
import itertools


_COMPONENT_TYPES = [
    {
        'name': 'Case',
        'file': 'case.json'
    },
    {
        'name': 'Graphics card',
        'file': 'gpu.json',
    },
    {
        'name': 'Memory',
        'file': 'memory.json'
    },
    {
        'name': 'Motherboard',
        'file': 'motherboard.json'
    },
    {
        'name': 'Power supply',
        'file': 'psu.json'
    },
    {
        'name': 'Processor',
        'file': 'cpu.json'
    },
    {
        'name': 'Storage',
        'file': 'storage.json'
    }
]


def load_file(filename: str) -> list:
    """
    Loads a data file.

    :param filename:
        The file name with a relative path

    :return:
        The list of entries in the data file
    """
    try:
        with open('data/' + filename) as fp:
            return json.load(fp)
    except FileNotFoundError:
        print('File "{}" could not be found.'.format(filename))


def load_data() -> list:
    """
    Loads the data from the files and generates all possible combinations for the components.

    :return:
        The list of possible configurations
    """
    components = []

    for ct in _COMPONENT_TYPES:
        components.append(load_file(ct['file']))

    return list(itertools.product(*components))


def build():
    result = [
        {_COMPONENT_TYPES[idx]['name']: value for idx, value in enumerate(configuration)}
        for configuration in load_data()
    ]

    return json.dumps(result, indent=4)


if __name__ == '__main__':
    print(build())
