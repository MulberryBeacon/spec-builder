# -*- coding: utf8 -*-

from marshmallow import Schema, fields, pprint

#class ComponentSchema(Schema):
class CPUSchema(Schema):
    manufacturer = fields.Str()
    model = fields.Str()
    cores = fields.Str()
    threads = fields.Str()
    base_clock = fields.Str()
    max_boost_clock = fields.Str()
    l1_cache = fields.Str()
    l2_cache = fields.Str()
    l3_cache = fields.Str()
    tdp = fields.Str()
