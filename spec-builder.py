# -*- coding: utf8 -*-

from random import choice
from marshmallow import Schema, fields, pprint

import json

from component_type import ComponentType

def choose_component(component: ComponentType, components: list):
    value = choice(components)
    return 'nothing yet!'


def load_file(filename: str) -> list:
    """
    Loads a data file.

    :param filename:
        The file name with a relative path
    :return:
        The list of entries in the data file
    """
    data = []

    try:
        with open('data/' + filename) as fp:
            data = json.load(fp)
    except FileNotFoundError:
        print('ups...')

    return data


if __name__ == '__main__':
    cpu = dict(ComponentType.CPU.value)
    test = load_file(cpu['file'])
    print(test)
