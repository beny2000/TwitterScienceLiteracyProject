import csv
class Config:
    def __init__(self, file):
        '''
        Init method for config class
        :param file: config file name
        '''
        self.config_file = file

    def __read(self):
        '''
        Creates csv reader for given config file
        :return: csv reader obj
        '''
        # todo check if csv
        try:
            file = open(self.config_file, 'r', encoding="utf8")
            reader = csv.reader(file)

            return reader
        except IOError as e:
            return "Config file Read Error", e

    def pass_params(self):
        '''
        Reads params from config file
        :return: tuple containng inital file direcotries (raw data, cleaned data)
        '''
        reader = self.__read()
        for row in reader:
            return (row[0],row[1])

        #print(row[0],row[1])