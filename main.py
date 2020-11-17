import os
import cleaner
import read_config
#main.py
#reads using read_config.py config setting if not found ask user for config settings
#use reader.py to read data from dir, use cleaner.py to clean data,
# use writer.py to write cleaned data to dir.

debug = True
config_file = 'config.txt'
raw_data_dir = 'raw_data'
cleaned_data_dir = 'cleaned_data'

if not debug:
    try:
        raw_data_dir, cleaned_data_dir = (read_config.Config(config_file)).pass_params()
    except Exception as e:
        raw_data_dir = str(input("Enter raw data folder: "))
        cleaned_data_dir = str(input("Enter cleaned data folder: "))

entries = os.listdir(raw_data_dir)

#for thru raw data make cleaner obj with each file run cleaner
c=0
for entry in entries:
    if c != 3:
        c+=1
        continue
    try:
        cleaner_obj = cleaner.Cleaner(entry, 'cleaned-'+entry, cleaned_data_dir, raw_data_dir)
        cleaner_obj.cleaner()
    except Exception as e:
        print("Error could not clean", entry, e)

print(c, 'files cleaned', list(entries))


