import csv
class Config:
    def __init__(self, file):
        self.config_file = file

    def __read(self):
        # todo check if csv
        try:
            file = open(self.config_file, 'r', encoding="utf8")
            reader = csv.reader(file)

            return reader
        except IOError as e:
            print(e)
            # return e

    def pass_params(self):
        reader = self.__read()
        for row in reader:
            return (row[0],row[1])

        #print(row[0],row[1])