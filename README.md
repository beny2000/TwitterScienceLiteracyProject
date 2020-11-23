# TwitterScienceLiteracyProject

## How to use program
- To run main.py in termnial with arguments to start program `python main.py args` 
- main.py takes 1 required argument which is the input file or directory, of the data to clean
  - eg. `$ python main.py input`
- use `-o output_dir` flag to specify output directory, if not specifyied one is created
- use `-c` to read input and output directories from `config.csv` where `input_dir, output_dir` (see `config.csv`)
- use `-d` to run a debug with `sample.csv`

## How main.py works
- baised on arguments run paramerters are selected
  - either run on single given file
  - or run on each file in given directory
- output is writen to created output directory if none was specifyied

## How cleaning process works
- cleaner.py houses most of the cleaning functionality
- cleaner object is created with the file name, output dir and input directory in main.py
- cleaning method is called with the given input files' csv reader object
  - cleaning method iterates through each row of the input file
  - a new row is created with only the colums to keep selected (`write_row`)
  - new row is check against filter conditions (non-verfied, english, etc)
    - if new row passes filter and is a RT write to RT file
    - if new row passes filter and is not a RT write to reg tweet file
  - update progress bar

## New in v2.0
- command line interface
- progress bar

### Todo:
- try fuzz text macthing for determining user location
- write sort by location method
