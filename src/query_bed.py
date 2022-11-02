"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    read_bed_file, print_line, BedLine
)


def extract_region(features: list[BedLine],
                   start: int, end: int) -> list[BedLine]:
    """Extract region chrom[start:end] and write it to outfile."""

    query_results = []

    # we find the lower bound    
    s = 0 # start of search interval
    e = len(features) # end of search interval

    while s < e: # while our search interval is bigger or equl to 1
        bound = (s+e)//2 # lower bound is set to the middel of the interval
        if start <= features[bound][1]: # start of query is bigger than our feature start
            e = bound # the search intervall is halfed, to the left
        else: # start query is smaller or equal to our query start
            s = bound + 1 # search interval is halfed, to the right
    
    # our lower bound is now s
    if s >= len(features): # no features are in query if s >= len(features)
        return query_results

    while features[s][1] < end: # while features start are smaller to query end, they are added to result
        #print("s = {} ::: end = {} ::: feature index s = {}".format(s, end, features[s]))
        #print(features[112])
        query_results.append(features[s]) # could be optimized with upper bound?
        s += 1 # remember to itterate
        if s == len(features): # if all features up to len(featres) are < end, we can return early
            return query_results

    return query_results



def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    features = read_bed_file(args.bed)
    for query in args.query:
        chrom, start, end = query.split()
        # Extract the region from the chromosome, using your extract_region()
        # function. If you did your job well, this should give us the features
        # that we want.
        region = extract_region(
            features.get_chrom(chrom), int(start), int(end))
        for line in region:
            print_line(line, args.outfile)


if __name__ == '__main__':
    main()
