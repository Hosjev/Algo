#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = sorted(line.split())
    for word in words:
        print(f"{word}\t1")
