import os
import cleaner
#main.py
#reads using read_config.py config setting if not found ask user for config settings
#use reader.py to read data from dir, use cleaner.py to clean data,
# use writer.py to write cleaned data to dir.

raw_data_dir = 'raw_data'
cleaned_data_dir = 'cleaned_data'
sample_data_dir = 'sample'

#for thru raw data make cleaner obj with each file run cleaner
#entries = os.listdir(raw_data_dir)
#for entry in entries:
#    print(entry)

cleaner_obj = cleaner.Cleaner('sample.csv','sample-cleaned.csv')
try:
    r = cleaner_obj.cleaner()
    print(r[0][:10], r[1])
except Exception as e:
    print(e)

