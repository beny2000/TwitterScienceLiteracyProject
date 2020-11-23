import os
import sys
import argparse
from time import time
from time import strftime as format_time
from time import gmtime as get_time
sys.path.insert(1, os.getcwd()+'\scripts')
from scripts import cleaner
from scripts import read_config

########################################
          #debug var init
debug = True
raw_data_dir = 'raw_data'
cleaned_data_dir = 'cleaned_data'
#########################################

rejects = []
line_count = -1
read_count = -1
config_file = 'scripts/config.csv'
#Create Parser
my_parser = argparse.ArgumentParser(description='Data Cleaner Interface')

# Add the arguments
my_parser.add_argument('input',
                       metavar='input',
                       type=str,
                       help='the file/dir with data to clean')
my_parser.add_argument('-o',
                       '--out_dir',
                       action='store',
                       help='siefy the path to output dir')
my_parser.add_argument('-d',
                       '--debug',
                       action='store_true',
                       help='run debug mode')
my_parser.add_argument('-c',
                       '--config',
                       action='store_true',
                       help='read in dir and out dir from config')

# Execute parse_args()
args = my_parser.parse_args()

if args.out_dir:
    cleaned_data_dir = args.out_dir
else:
    cleaned_data_dir = 'cleaned_dataa'

    try:
        os.mkdir(cleaned_data_dir)
    except OSError:
        print("Creation of the directory %s failed" % cleaned_data_dir)
    else:
        print("Successfully created the directory %s " % cleaned_data_dir)

if args.debug:
    start = time()
    print("Started: ")
    try:
        cleaner_obj = cleaner.Cleaner('sample.csv', cleaned_data_dir, os.getcwd())
        rejects, line_count, read_count = cleaner_obj.cleaner()
    except Exception as e:
        print("Error could not clean", 'debug', e)
    finally:
        end = time()
        print('debug', " Finished in ", format_time("%H:%M:%S", get_time(end - start)), "Length: ", line_count,
              "Total Rejected: ", len(rejects), "Lines read:", read_count)
        exit(0)

elif args.config:
    try:
        raw_data_dir, cleaned_data_dir = (read_config.Config(config_file)).pass_params()
    except Exception as e:
        raw_data_dir = str(input("Enter raw data folder: "))
        cleaned_data_dir = str(input("Enter cleaned data folder: "))

    entries = os.listdir(raw_data_dir)
    c = 0
    enter = time()
    for entry in entries:
        start = time()
        print("Started: ", entry)
        try:
            cleaner_obj = cleaner.Cleaner(entry, cleaned_data_dir, raw_data_dir)
            rejects, line_count, read_count = cleaner_obj.cleaner()
            # print(cleaner_obj.cleaner())
            c += 1
        except Exception as e:
            print("Error could not clean", entry, e)
        finally:
            end = time()
            print(entry, " Finished in ", format_time("%H:%M:%S", get_time(end - start)), "Length: ", line_count,
                  "Total Rejected: ", len(rejects), "Lines read:", read_count)

    compelete = time()
    print(c, 'files cleaned in ', format_time("%H:%M:%S", get_time(enter - compelete)), list(entries))
    exit(0)

elif os.path.isfile(args.input):
    start = time()
    print("Started: ", args.input)
    try:
        cleaner_obj = cleaner.Cleaner(args.input, cleaned_data_dir, os.getcwd())
        rejects, line_count, read_count = cleaner_obj.cleaner()
    except Exception as e:
        print("Error could not clean", args.input, e)
    finally:
        end = time()
        print(args.input, " Finished in ", format_time("%H:%M:%S", get_time(end - start)), "Length: ", line_count,
              "Total Rejected: ", len(rejects), "Lines read:", read_count)
        exit(0)

elif os.path.isdir(args.input):
    entries = os.listdir(args.input)
    c = 0
    enter = time()
    for entry in entries:
        start = time()
        print("Started: ", entry)
        try:
            cleaner_obj = cleaner.Cleaner(entry, cleaned_data_dir, args.input)
            rejects, line_count, read_count = cleaner_obj.cleaner()
            #print(cleaner_obj.cleaner())
            c += 1
        except Exception as e:
            print("Error could not clean", entry, e)
        finally:
            end = time()
            print(entry, " Finished in ", format_time("%H:%M:%S", get_time(end - start)), "Length: ", line_count,
                  "Total Rejected: ", len(rejects), "Lines read:", read_count)

    compelete = time()
    print(c, 'files cleaned in ', format_time("%H:%M:%S", get_time(enter - compelete)), list(entries))
    exit(0)

else:
    print("Parse Error") #flags for conditions
    exit(0)


