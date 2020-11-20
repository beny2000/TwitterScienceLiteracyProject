import os
import cleaner
import read_config
from time import time
from time import strftime as format_time
from time import gmtime as get_time

########################################
          #debug var init
debug = False
raw_data_dir = 'raw_data'
cleaned_data_dir = 'cleaned_data'
#########################################
config_file = 'config.csv'

if not debug:
    # read params from config file
    try:
        raw_data_dir, cleaned_data_dir = (read_config.Config(config_file)).pass_params()
    except Exception as e:
        raw_data_dir = str(input("Enter raw data folder: "))
        cleaned_data_dir = str(input("Enter cleaned data folder: "))
else:
    cleaner_obj = cleaner.Cleaner('sample.csv', 'cleaned-sample.csv', cleaned_data_dir, raw_data_dir)
    cleaner_obj.cleaner()
    print("test complete")
    exit(0)

entries = os.listdir(raw_data_dir)
c=0
#for through raw data dir, run cleaner on each file
enter = time()
line_count = -1
for entry in entries:
    start = time()
    print("Started: ", entry)
    try:
        cleaner_obj = cleaner.Cleaner(entry, 'cleaned-'+entry, cleaned_data_dir, raw_data_dir)
        rejects, line_count = cleaner_obj.cleaner()
        c+=1
    except Exception as e:
        print("Error could not clean", entry, e)
    finally:
        end = time()
        print(entry, " Finished in ", format_time("%H:%M:%S", get_time(end - start)), "Length: ", line_count)

compelete = time()
print(c, 'files cleaned in ', format_time("%H:%M:%S", get_time(enter - compelete)), list(entries))


