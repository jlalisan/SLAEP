#!usr/bin/env python3

"""
Assembler script
"""

# Imports
import re
import sys
import argparse as ap
# Code

reads = []
sequences = []


def file_reader(input_file):
    """ Reads through the Fastq file and extracts the sequences and read numbers. """
    for line in open(input_file):
        # Isolates the sequences.
        sequence = re.compile("^[A-Z]{5,}")
        # Isolates the read numbers.
        read = re.compile("read=\d*")
        # Finds all the matches.
        match = (read.findall(line.strip()))
        seqmatch = (sequence.findall(line.strip()))
        # Removes empty matches
        if match != [] or seqmatch != []:
            reads.append(''.join(match))
            sequences.append(''.join(seqmatch))
        while '' in reads and '' in sequences:
            reads.remove("")
            sequences.remove("")
    # Orders the matches with each other.
    for index in range(len(reads)):
        myread = reads[index]
        # Splits sequence in lines of 70 nucleotides.
        myseq = (re.sub("(.{70})", "\\1\n", sequences[index], 0, re.DOTALL))

        # Prints the sequence (REMOVE LATER)
        print(f"{myread} \n {myseq}".replace(' ', ''))


def main():
    file_reader('test.txt')


if __name__ == '__main__':
    argparser = ap.ArgumentParser(description="Arguments for the Assembly")
    argparser.add_argument("-n", action="store",
                           dest="n", required=True, type=int,
                           help="Amount of cores to be used")
    argparser.add_argument("fastq_files", action="store",
                           nargs='+', help="At least one Minion file")
    argparser.add_argument("-k", action="store", dest="k", required=False, type=int,
                           default=5, help="Size of the k-mers")
    args = argparser.parse_args()

    main()
else:
    sys.exit("Program is ending")