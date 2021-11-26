# QC filterer

## Description
Reads provided csv file and alerts if any samples of specific origin fails to pass 90% threshold of accepted sequencing runs.

## Usage
```shell
python qc.py filename origin_length
```
The two arguments are filename: self explanatory,  and origin_length: length of the origin names used in the samples.


## Assumptions
The origin of sample always starts from the second character in the sample name and that the input file is always a csv file.
