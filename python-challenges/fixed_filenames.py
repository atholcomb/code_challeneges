#!/usr/bin/python3
# written by: atholcomb
# fixed_filenames.py

import os
from pathlib import Path

def fixed_filenames(list_of_names):
    
    fixed_names = { lon : lon for lon in list_of_names }
    fixed_names = [(z, Path(z).stem + '.h') if '.hpp' in z else (z, z) for z in fixed_names]
    
    return fixed_names


# Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
print(fixed_filenames(["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]))
