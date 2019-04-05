# -*- coding: utf-8 -*-

import json
from random import choice
import itertools

from marshmallow import Schema, fields, pprint

from component_type import ComponentType


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
        print('File "{}" could not be found.'.format(filename))

    return data


def load_data():
    """
    """
    components = []

    for ct in ComponentType:
        component = dict(ct.value)
        #components.append({
        #    component['name']: load_file(component['file'])
        #})
        components.append(load_file(component['file']))

    result = list(itertools.product(*components))

    for idx, subset in enumerate(result):
        print(subset)


if __name__ == '__main__':
    load_data()
