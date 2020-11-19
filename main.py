import os
import cleaner
import read_config

########################################
          #debug var init
debug = True #False
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
for entry in entries:
    try:
        cleaner_obj = cleaner.Cleaner(entry, 'cleaned-'+entry, cleaned_data_dir, raw_data_dir)
        cleaner_obj.cleaner()
        c+=1
    except Exception as e:
        print("Error could not clean", entry, e)

print(c, 'files cleaned', list(entries))


