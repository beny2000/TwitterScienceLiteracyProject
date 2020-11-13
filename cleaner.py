import csv
import re

class Cleaner:
    def __init__(self, infile_name, outfile_name):
        self.infile_name = infile_name
        self.outfile_name =outfile_name
        self.counter = 0


    def cleaner(self):
        try:
            return self.__data_spooler(self.__csv_reader())
        except Exception as e:
            return e
    def __csv_reader(self):
        #todo check if csv
        try:
            raw_data = open(self.infile_name, 'r', encoding="utf8")
            reader = csv.reader(raw_data)

            return reader
        except IOError as e:
            print(e)
            #return e

    def __json_reader(self):
        #todo check if json
        #return json reader obj
        pass

    def __data_spooler(self, reader):
        rejects = []
        #reed  in row
        #write cols to keep w text cleaned (self.text_cleaner())
        # if RT write to RT file
        # else write to main tweet file, in same fashion
        try:
            RT_file = open('RT-'+str(self.counter)+'-'+self.outfile_name,'a',encoding="utf8")
            RT_writer = csv.writer(RT_file, delimiter=',')
        except Exception as e:
            print(e)
        try:
            cleaned_tweets_file = open(str(self.counter)+'-'+self.outfile_name,'a',encoding="utf8")
            tweet_writer = csv.writer(cleaned_tweets_file, delimiter=',')
        except Exception as e:
            print(e)
        self.counter +=1
        row_count = 0
        status = 1

        for row in reader:
            write_row = row[1] +','+ row[2] +','+row[5] +','+row[6] +','+row[10] +','+row[13] +','+row[14] +','+row[15] +','+ self.__text_cleaner(row[17]) +','+ row[18] +','+row[20] +','+row[24] +','+row[25] +','+row[27]  +','+ row[33]

            if row_count == 0:
                self.__write(write_row, tweet_writer)
                self.__write(write_row, RT_writer)
                row_count +=1
            else:
                row_count+=1

                if row[33] == 'FALSE' and row[10] == 'en' and row[14] != '':
                    #only write non-verified and english and non-RT tweets to main csv
                    self.__write(write_row, tweet_writer)
                elif row[33] == 'FALSE' and row[10] == 'en' and row[14] == '':
                    #only write non-verified and english and RT tweets to RT csv
                    self.__write(write_row, RT_writer)
                else:
                    rejects.append(write_row)

        return rejects, row_count

    def __text_cleaner(self, text):
        #clean text @ row[]
        #todo clean text
        return text

    def __write(self, row, writer):
        #write row to file

        try:
            writer.writerow([row])
        except Exception as e:
            print(e,' @ '+ row)

