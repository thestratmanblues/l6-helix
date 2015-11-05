#!/usr/bin/env python

# This code is used to decode/uncompress the content 
# (JSON format) of a Line 6 - Helix pedal board 
# Bundle (*.hlb) file.

import json
from pprint import pprint
import base64
import zlib

data = None
compress_data = None
data_bundle = None

with open('Bundle_VERSION_1_03.hlb') as file_bundle:
        data = json.load(file_bundle)

if 'encoded_data' in data:
        compress_data = base64.b64decode(data['encoded_data'])
        bundle = zlib.decompress(compress_data)

        data_bundle = json.loads(str(bundle))
        pprint(data_bundle)