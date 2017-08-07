#!/usr/bin/env python

import sys
import fileinput
from transliterate import translit

source_lang = 'ru'

def is_ascii_str(test):
    try: test.decode('ascii')
    except: return False
    else: return True

for line in fileinput.input(sys.argv[1], inplace=True):
    if line.split()[1] == 'NAME':
        if not is_ascii_str(line):
            line = line.decode('utf8')
            line = translit(line, source_lang, reversed=True)
            line = line.replace("'", "").encode('ascii')

    sys.stdout.write(line)
