""" Author : Marinos Marios(dai17147)
    Deterministic finite automation, non Deterministic finite automation
    and NFA with e transitions due to the course of automation theory 7th semester.
"""
import sys

def readFile(fname):
    with open(fname) as f:
        for line in f:
            split = line.split(' ')
            if (split[0].startswith('states')):
                states = int(split[1])
            elif (split[0].startswith('initial')):0
                initial = int(split[1])
            elif (split[0].startswith('final_states')):
                final =






if __name__ == "__main__":
    fname = sys.argv[1] # waiting for the user to give the name.
    readFile(fname)
