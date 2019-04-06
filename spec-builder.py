# -*- coding: utf-8 -*-

import json
import itertools

from component_type import ComponentType


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

    return None


def load_data() -> list:
    """
    Loads the data from the files and generates all possible combinations for the components.
    """
    components = []

    for ct in ComponentType:
        component = dict(ct.value)
        components.append(load_file(component['file']))

    return list(itertools.product(*components))


def transform_data():
    #for subset in result:
    #    print(json.dumps(subset, indent=4))


if __name__ == '__main__':
    transform_data()
