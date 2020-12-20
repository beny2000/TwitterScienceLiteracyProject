import csv
import os
import sys
sys.path.insert(1, os.getcwd()+'\scripts')
class Cities:
    def __init__(self):
        self.citiesFile = "canadianCities.csv"
        self.cities = self.__readCities()


    def __readCities(self):
        #print(os.getcwd())
        try:
            file = open(os.getcwd()+'\scripts\\'+self.citiesFile, 'r', encoding="utf8")
            reader = csv.reader(file)
        except Exception as e:
            print(e)
            return "City reading Error",

        cities = []
        next(reader) #skip header
        for row in reader:
            cities.extend(row)

        return cities


    def getCities(self):
        return self.cities