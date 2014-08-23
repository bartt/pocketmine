#!/usr/bin/env python3
import argparse, yaml, configparser, re, io, os

parser = argparse.ArgumentParser()
with open('server.properties', 'r') as properties:
    config = configparser.ConfigParser()
    config.read_string('[pocketmine]\n' + properties.read())
    pocketmine = config['pocketmine']

for key in config['pocketmine']:
    parser.add_argument('--' + key)

args = vars(parser.parse_args())

for key in args:
    if args[key]:
        pocketmine[re.sub(r'_', '-', key)] = args[key]

tmp_properties = io.StringIO()
config.write(tmp_properties, False)
tmp_properties.seek(0)

with open('server.properties', 'w') as properties:
    for line in tmp_properties.readlines():
        if not re.search(r'^(\[pocketmine]|\W*)\n$', line):
            properties.write(line)

os.system('./start.sh')
