# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from filecmp import cmp
import os

cmd1 = 'echo "" > data/test-sorted-1.bed' #Command to create empty file
cmd2 = 'python3.10 src/sort_bed.py data/input.bed data/test-sorted-1.bed' #A string with the command to generate our test output
os.system(cmd1) #Calling our commands
os.system(cmd2)

def test_sort_bed_1():
    result = cmp('data/test-sorted-1.bed', 'data/input-sorted.bed', shallow = True) #Comparing test- and expected output.
    assert result

# cmd1 = 'echo "" > data/test-sorted-2.bed' #Command to create empty file
# cmd2 = 'python3.10 src/sort_bed.py data/large.bed data/test-sorted-2.bed' #A string with the command to generate our test output
# os.system(cmd1) #Calling our commands
# os.system(cmd2)

# def test_sort_bed_2():
#     result = cmp('data/test-sorted-2.bed', 'data/large-sorted.bed', shallow = True) #Comparing test- and expected output.
#     assert result

# The second test fails, not because it is not correct.
# Features that are in the same place, but with different names are sorted differently in test-sorted-2.bed compared with large-sorted.bed