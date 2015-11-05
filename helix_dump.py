#!/usr/bin/env python

# This code is used to decode/uncompress the content 
# (JSON format) of a Line 6 - Helix pedal board 
# Bundle (*.hlb) or Setlist (*.hls) file.
#
# Tested only with Python 2.6.7
# 
# Usage: python helix_dump.py -i <inputfile> -o <outputfile>
#
# Note: The output file is not mandatory, will create an 
#       inputfile_JSON_dump.out if not provided.
#
# Developer : thestratmanblues
# https://github.com/thestratmanblues/l6-helix.git
#
# Version 1.0	2015/11/04	Initial release
# Version 1.1 	2015/11/05	Add input/output file params

import sys
import getopt
import json
import yaml
from pprint import pprint
import base64
import zlib

def main(argv):
	inputfile = ''
	outputfile = ''
	data = None
	compress_data = None
	data_bundle = None
	app_name = sys.argv[0]

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print  app_name,' -i <inputfile> -o <outputfile>'
	  	sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
		 	print app_name,' -i <inputfile> -o <outputfile>'
	 		sys.exit()
		elif opt in ("-i", "--ifile"):
	 		inputfile = arg
		elif opt in ("-o", "--ofile"):
	 		outputfile = arg
	
	if outputfile is '':
		outputfile = inputfile + '_JSON_dump.out'
	
	print ' Input file is:', inputfile
	print 'Output file is:', outputfile

	with open(inputfile) as file_bundle:
		data = json.load(file_bundle)

	if 'encoded_data' in data:
		compress_data = base64.b64decode(data['encoded_data'])
		bundle = zlib.decompress(compress_data)

		data_bundle = json.loads(bundle)
		data_bundle_str = yaml.safe_load(bundle)

		# yaml instead of json to remove the unicode 'u' char in output only
		with open(outputfile, "w") as file_out:
			pprint(data_bundle_str, file_out)   	
				#	pprint(data_bundle, file_out)

	print 'Helix dump completed.'

if __name__ == "__main__":
	main(sys.argv[1:])
