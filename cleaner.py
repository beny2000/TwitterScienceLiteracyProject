import csv
import re

class Cleaner:
    counter = 0

    def __init__(self, infile_name, outfile_name, out_dir, in_dir):
        '''
        Init Method for Cleaner class
        :param infile_name: name of file to be cleaned
        :param outfile_name: name of file after cleaning
        :param out_dir: directory where cleaned file goes
        :param in_dir: directory where file to clean is found
        '''

        self.infile_name = infile_name
        self.outfile_name = outfile_name
        self.out_dir = out_dir
        self.in_dir = in_dir


    def cleaner(self):
        '''
        Public method that calls nessary methods to clean file
        :return:
        '''
        try:
            return self.__data_spooler(self.__csv_reader())
        except Exception as e:
            return e

    def __csv_reader(self):
        '''
        Creates csv reader for given file
        :return: csv reader obj
        '''
        #todo check if csv

        try:
            raw_data = open(self.in_dir+'/'+self.infile_name, 'r', encoding="utf8")
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
        '''
        Private method that performs cleaning
        :param reader: csv reader of given file
        :return: list of tweets that where rejected, num. of rows written
        '''
        rejects = []
        tweet_writer = None
        RT_writer = None

        #create nessary files (cleaned tweets and cleaned retweets
        try:
            RT_file = open(self.out_dir+'/'+'RT-'+str(self.counter)+'-'+self.outfile_name,'a',encoding="utf8")
            RT_writer = csv.writer(RT_file, delimiter=',')
        except Exception as e:
            print(e)
        try:
            cleaned_tweets_file = open(self.out_dir+'/'+str(self.counter)+'-'+self.outfile_name,'a',encoding="utf8")
            tweet_writer = csv.writer(cleaned_tweets_file, delimiter=',')
        except Exception as e:
            print(e)
        self.counter +=1
        row_count = 0

        #reads through file gathers cols to keep, checks tweets againts conditions, writes tweet to approite file
        for row in reader:
            write_row = row[1] +','+ row[2] +','+row[5] +','+row[6] +','+row[10] +','+row[13] +','+row[14] +','+row[15] +','+ self.__text_cleaner(row[17]) +','+ row[18] +','+row[20] +','+row[24] +','+row[25] +','+row[27]  +','+ row[33]

            if row_count == 0:
                print(write_row)
                self.__write(write_row, tweet_writer)
                self.__write(write_row, RT_writer)
                row_count += 1
            else:

                if row[33] == 'FALSE' and row[10] == 'en' and row[14] != '' and self.__remove_nonCanadian(row[27]):
                    #only write non-verified and english and non-RT tweets and canadian tweets to main csv
                    self.__write(write_row, tweet_writer)
                    row_count += 1
                elif row[33] == 'FALSE' and row[10] == 'en' and self.__remove_nonCanadian(row[27]) and row[14] == '' :
                    #only write non-verified and english and RT tweets and canadian tweets to RT csv
                    self.__write(write_row, RT_writer)
                    row_count += 1
                else:
                    rejects.append(write_row)

        return rejects, row_count

    def __text_cleaner(self, text):
        #cleans text @ row[17]
        #todo clean text
        return text

    def __remove_nonCanadian(self, text):
        #return true if tweet from Canada else false
        return True

    def sort_tweets(self):
        #return rows sorted by city
        pass

    def __write(self, row, writer):
        '''
        Writes given row to given csv file
        :param row: row to write
        :param writer: csv reader obj of file to write to
        :return: None
        '''
        try:
            writer.writerow([row])
        except Exception as e:
            print(e,' @ '+ row)



