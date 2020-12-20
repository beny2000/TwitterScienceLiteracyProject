# Twitter Science Literacy Project

## How to use program
- Run `main.py` in termnial with arguments to start program, `python main.py *arguments*` 
- `main.py` takes 1 required argument which is the input file or directory, of the data to clean
  - eg. `$ python main.py *input*`
- use `-o output_dir` flag to specify output directory, if not specifyied one is created
- use `-c` to read input and output directories from `config.csv` where `input_dir, output_dir` (see `config.csv`)
- use `-d` to run a debug with `sample.csv`

### Runing on single file to default output folder
- run with python command in terminal `main.py *file_name*`

### Runing on single file to custom output folder
- run with python command in terminal `main.py *file name* -o *output folder*`

### Runing on mulitple files to default output folder
- all files to clean must be in the same folder with only the files to clean inside
- works best when folder with files to clean is in the same location as `main.py` (see raw_data folder)
- run with python command in terminal `main.py *folder_name*`

### Runing on mulitple files to custom outfolder
- all files to clean must be in the same folder with only the files to clean inside
- works best when folder with files to clean is in the same location as `main.py` (see raw_data folder)
- run with python command in terminal `main.py *folder_name* -o *output folder`


## How main.py works
- baised on arguments run paramerters are selected
  - either run on single given file
  - or run on each file in given directory
- output is writen to created output directory if none was specifyied

## How cleaning process works
- `cleaner.py` houses most of the cleaning functionality
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

## New in v3.0
- adds cleaned tweets to master file
- prints list of locations and number of tweets found
