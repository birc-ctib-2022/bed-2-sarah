# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from filecmp import cmp
import os

# test 1

cmd1 = 'echo "" > data/test-query-1.bed' #Command to create empty file
cmd2 = 'python3.10 src/query_bed.py data/large-sorted.bed data/query-1.txt -o data/test-query-1.bed' #A string with the command to generate our test output
os.system(cmd1) #Calling our commands
os.system(cmd2)

def test_query_bed_1():
    result = cmp('data/test-query-1.bed', 'data/expected-1.txt', shallow = True) #Comparing test- and expected output.
    assert result

# test 2

cmd1 = 'echo "" > data/test-query-2.bed' #Command to create empty file
cmd2 = 'python3.10 src/query_bed.py data/large-sorted.bed data/query-2.txt -o data/test-query-2.bed' #A string with the command to generate our test output
os.system(cmd1) #Calling our commands
os.system(cmd2)

def test_query_bed_2():
    result = cmp('data/test-query-2.bed', 'data/expected-2.txt', shallow = True) #Comparing test- and expected output.
    assert result

# test 3

cmd1 = 'echo "" > data/test-query-3.bed' #Command to create empty file
cmd2 = 'python3.10 src/query_bed.py data/large-sorted.bed data/query-3.txt -o data/test-query-3.bed' #A string with the command to generate our test output
os.system(cmd1) #Calling our commands
os.system(cmd2)

def test_query_bed_3():
    result = cmp('data/test-query-3.bed', 'data/expected-3.txt', shallow = True) #Comparing test- and expected output.
    assert result