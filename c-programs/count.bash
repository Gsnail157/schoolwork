#!/bin/bash

# count.bash -- Prints each filename, # of lines, # of words in working directory

# Gary Wang
# 4/17/2022

ls -1 | while read file ; do
	echo "$file $(wc -l $file | cut -d ' ' -f 1) $(wc -w $file | cut -d ' ' -f 1)"
done

