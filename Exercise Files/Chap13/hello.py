#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys
import os
print('Hello, World.')
a = (1,2,3,4,5)
b=(6,7,8,9)
c = zip(a,b)
for a,b in c: print(f'{a} , {b}')

print(sys.platform)
print(os.name)