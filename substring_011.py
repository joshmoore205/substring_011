#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()

for line in lines:
  line = line.strip().lower().split()
  chars = line[0]
  word = line[1]
  if chars in word:
    print("True")
  else:
    print("False")
