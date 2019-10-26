""" Author : Marinos Marios(dai17147)
    Deterministic finite automation, non Deterministic finite automation
    and NFA with e transitions due to the course of automation theory 7th semester.
"""


def readFile(fname):
try:
    fh = open(fname)
except Exception as e:
    print ('Sorry your file cannot be opened ')
    quit()


if __name__ == "__main__":
    fname = input("Enter file name: ") # waiting for the user to give the name.
    readFile(fname)
