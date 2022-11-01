# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from filecmp import cmp
import os

cmd1 = 'echo "" > data/test-merge.bed' #Command to create empty file
cmd2 = 'python3.10 src/merge_bed.py data/input-sorted.bed data/input-sorted.bed -o data/test-merge.bed' #A string with the command to generate our test output
os.system(cmd1) #Calling our commands
os.system(cmd2)

def test_merge_bed():
    result = cmp('data/test-merge.bed', 'data/input-merged.bed', shallow = True) #Comparing test- and expected output.
    assert result
