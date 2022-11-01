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
    
    i_start = 0
    i_end = len(features)
    i_middel = i_start + ((i_end - i_start)//2) # middel of search interval

    while (i_end-i_start) >= 1 and i_middel < len(features):
        if start <= features[i_middel][1] < end:
        # using the assumption that our features are only a single nucleotide long,
        # features within the query can be described with query-start <= feature-start < query-end
        # and that assumption is the first to be checked
            while features[i_middel][1] < end:
                query_results.append(features[i_middel])
                i_middel += 1
            # we keep appending features to our results untill features-start >= query-end
        # if a feature is not inside the query, there are two scenarios
        # feature-start >= query-start
        elif features[i_middel][1] >= end:
            i_end = i_middel
            i_middel = i_start + ((i_end - i_start)//2)
        # feature-start < query-start
        elif features[i_middel][1] < start:
            i_start = i_middel + 1 
            i_middel = i_start + ((i_end - i_start)//2)
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
