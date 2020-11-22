import csv
import re
import cities
import traceback

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
            return "Cleaning Error", e

    def sort_tweets(self):
        # return rows sorted by city
        pass

    def __csv_reader(self):
        '''
        Creates csv reader for given file
        :return: csv reader obj
        '''
        # todo check if csv

        try:
            raw_data = open(self.in_dir + '/' + self.infile_name, 'r', encoding="utf8", newline='')
            reader = csv.reader(raw_data)

            return reader
        except Exception as e:
            return "Reader Erorr", e
            # return e

    def __json_reader(self):
        # todo check if json
        # return json reader obj
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

        # create nessary files (cleaned tweets and cleaned retweets
        try:
            RT_file = open(self.out_dir + '/' + 'RT-' + str(self.counter) + '-' + self.outfile_name, 'w',
                           encoding="utf8", newline='')
            RT_writer = csv.writer(RT_file, delimiter=',')
        except Exception as e:
            return "RT File creation Error", e
        try:
            cleaned_tweets_file = open(self.out_dir + '/' + str(self.counter) + '-' + self.outfile_name, 'w',
                                       encoding="utf8", newline='')
            tweet_writer = csv.writer(cleaned_tweets_file, delimiter=',')
        except Exception as e:
            print("File creation Error", e)
            return "File creation Error", e
        self.counter += 1
        row_count = 0
        read_count = 0

        # reads through file gathers cols to keep, checks tweets againts conditions, writes tweet to approite file
        for row in reader:
            read_count +=1
            if len(row)!= 34:
                #print(len(row),row)
                continue

            write_row = [row[1], row[2], row[5], row[6], row[10],
                         row[13], row[14], row[15], self.__text_cleaner(row[17]),
                         row[18], row[20], row[24], row[25], str(row[27]), row[33]]

            if row_count == 0:

                self.__write(write_row, tweet_writer)
                self.__write(write_row, RT_writer)
                row_count += 1
            else:

                if row[33].lower() == 'false' and row[10] == 'en' and row[14] == '' and self.__remove_nonCanadian(row[27]):
                    # only write non-verified and english and non-RT tweets and canadian tweets to main csv
                    #write_row.insert(0,'')
                    self.__write(write_row, tweet_writer)
                    row_count += 1
                elif row[33].lower() == 'false' and row[10] == 'en' and self.__remove_nonCanadian(row[27]) and row[14] != '':
                    # only write non-verified and english and RT tweets and canadian tweets to RT csv
                    self.__write(write_row, RT_writer)
                    row_count += 1
                else:
                    rejects.append(write_row)
        #return row_count
        return rejects, row_count, read_count

    def __text_cleaner(self, text):
        """
        Cleans non-ascii char from given string
        :param text: str of text to clean
        :return: text str with non-ascii chars removed
        """
        return re.sub("[^\x00-\x7F]+", "", text)

    def __remove_nonCanadian(self, text):
        """
        Returns True if given text is a name of Canadian city or province (full name or short form) or just Canada
        :param text: user location to check
        :return: True if at least one piece of text is found in canadian_cities list (read from csv)

        Issues/Limitations:
         - cities or provinces/states in other with same name/shot-form as Canada will cause false positive
         - different spellings (such as Montréal for Montreal) or typos will cause false negative
         - possible solution is use only top x cities in canada or the like, use fuzzy text matching
        """
        canadian_cities = cities.Cities().getCities()
        text_split = text.replace(' ', '').split(',')
        c = any([text.lower() in canadian_cities for text in text_split])
        #print(text_split)
        return c

    def __write(self, row, writer):
        '''
        Writes given row to given csv file
        :param row: row to write
        :param writer: csv reader obj of file to write to
        :return: None
        '''
        try:
            writer.writerow(row)
        except Exception as e:
            return e, ' @ ' + row

