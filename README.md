# QC filterer

## Description
Reads provided csv file and alerts if any samples of specific origin fails to pass 90% threshold of accepted sequencing runs.

## Usage
```shell
python qc.py filename
```

## Assumptions
The origin of sample always starts from the second character in the sample name.
