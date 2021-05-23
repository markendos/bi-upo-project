from DBConnection import DBConnection
import numpy

class BirthInfoHelper:
    def __init__(self):
        self.cursor = DBConnection.get_instance().cursor()

        purchasesByCountriesQueries = "SELECT country, count(*) as purchasesNum FROM shop GROUP BY country ORDER BY purchasesNum"
        self.cursor.execute(purchasesByCountriesQueries)
        purchasesByCountries = self.cursor.fetchall()

        finalData = {}
        for purchaseByCountry in purchasesByCountries:
            country, purchasesNum = purchaseByCountry
            birthsByCountriesQuery = "SELECT births FROM birth where year = 2008 and entity='" + country + "'"
            self.cursor.execute(birthsByCountriesQuery)
            birthByCountry = self.cursor.fetchall()
            birthsNum = birthByCountry[0][0]
            finalData[country] = (purchasesNum, birthsNum)

        self.data = finalData

    def getBirthsNumber(self, countryName):
        return self.data[countryName][1]

    def getPurchasesNumber(self, countryName):
        return self.data[countryName][0]

    def getAllData(self):
        return self.data

    def getBirthNumberPredictionForCountryAndYear(self, countryName, year):
        birthDataBYCountryQuery = "SELECT year, births FROM birth WHERE entity='"+countryName+"'"
        self.cursor.execute(birthDataBYCountryQuery)
        data = self.cursor.fetchall()

        x = []
        y = []
        for row in data:
            x.append(row[0])
            y.append(row[1])

        model = numpy.poly1d(numpy.polyfit(x, y, 3))
        # line = numpy.linspace(min(x), max(x), 100)
        prediction = model(year)
        return int(prediction)

    def getBirthPredictionForYear(self, year):
        return True

    ##TODO add method for fetching points so they can be represented into graph

