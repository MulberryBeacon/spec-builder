# -*- coding: utf8 -*-

from enum import Enum

class ComponentType(Enum):
    #CASE = { 
    #    'name': 'Case',
    #    'file': 'case.json'
    #} 
    CPU = {
        'name': 'Processor',
        'file': 'cpu.json'
    }
    GPU = {
        'name': 'Graphics card',
        'file': 'gpu.json'
    }
    STORAGE = {
        'name': 'Storage',
        'file': 'storage.json'
    }
    #PSU = {
    #    'name': 'Power supply',
    #    'file': 'psu.json'
    #}
    #RAM = {
    #    'name': 'Memory',
    #    'file': 'memory.json'
    #}
    MOTHERBOARD = {
        'name': 'Motherboard',
        'file': 'motherboard.json'
    }
