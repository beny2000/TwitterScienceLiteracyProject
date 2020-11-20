import csv

class Cities:
    def __init__(self):
        self.citiesFile = "canadaCities.csv"
        self.cities = self.__readCities()


    def __readCities(self):

        try:
            file = open(self.citiesFile, 'r', encoding="utf8")
            reader = csv.reader(file)
        except Exception as e:
            return "Citing readin Error",

        cities = ['canada']
        next(reader) #skip header
        for row in reader:
            cities.extend(row)

        return cities


    def getCities(self):
        return self.cities