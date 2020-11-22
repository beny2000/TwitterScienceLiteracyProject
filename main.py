import os
import sys
import argparse
import cleaner
import read_config
from time import time
from time import strftime as format_time
from time import gmtime as get_time

########################################
          #debug var init
debug = True
raw_data_dir = 'raw_data'
cleaned_data_dir = 'cleaned_data'
#########################################
config_file = 'config.csv'
my_parser = argparse.ArgumentParser(description='Data Cleaner Interface')

# Add the arguments
my_parser.add_argument('input',
                       metavar='in_dir',
                       type=str,
                       help='the dir with data to clean')
my_parser.add_argument('-o',
                       '--out_dir',
                       action='store',
                       help='the path to output dir')
my_parser.add_argument('-d',
                       '--debug',
                       action='store_true',
                       help='run debug mode')

# Execute parse_args()
args = my_parser.parse_args()
if args.debug:
    # read params from config file
    start = time()
    rejects = []
    print("Started: ")
    try:
        cleaner_obj = cleaner.Cleaner('sample.csv', cleaned_data_dir)
        rejects, line_count, read_count = cleaner_obj.cleaner()
    except Exception as e:
        print("Error could not clean", 'debug', e)
    finally:
        end = time()
        print('debug', " Finished in ", format_time("%H:%M:%S", get_time(end - start)), "Length: ", line_count,
              "Total Rejected: ", len(rejects), "Lines read:", read_count)
        exit(0)
elif #input is only file, mkdir and write to out_dir
elif #input is dir
elif #input is 2 dirs (in, out)
else #flags for conditions

entries = os.listdir(raw_data_dir)
c=0
#for through raw data dir, run cleaner on each file
enter = time()
line_count = -1
for entry in entries:
    start = time()
    rejects = []
    print("Started: ", entry)
    try:
        cleaner_obj = cleaner.Cleaner('sample.csv', cleaned_data_dir)
        rejects, line_count, read_count = cleaner_obj.cleaner()
        c+=1
    except Exception as e:
        print("Error could not clean", entry, e)
    finally:
        end = time()
        print(entry, " Finished in ", format_time("%H:%M:%S", get_time(end - start)), "Length: ", line_count, "Total Rejected: ", len(rejects),"Lines read:", read_count)

compelete = time()
print(c, 'files cleaned in ', format_time("%H:%M:%S", get_time(enter - compelete)), list(entries))


