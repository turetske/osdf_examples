#!/usr/bin/env python

# Transforms Resource json to have machine name be key
import json

rgs = json.load(open('resource_group_summary'))

rgs['Duke-NCShare']['Resources']['Resource'][0]['Name']

new_
