from DBConnection import DBConnection
import numpy

class BirthsAndGdpHelper:
    def __init__(self):
        # purchasesByCountriesQueries = "SELECT country, count(*) as purchasesNum FROM shop GROUP BY country ORDER BY purchasesNum"
        # self.cursor.execute(purchasesByCountriesQueries)
        # purchasesByCountries = self.cursor.fetchall()

        finalData = {}
        # for purchaseByCountry in purchasesByCountries:
        #     country, purchasesNum = purchaseByCountry
        #     birthsByCountriesQuery = "SELECT births FROM birth where year = 2008 and entity='" + country + "'"
        #     self.cursor.execute(birthsByCountriesQuery)
        #     birthByCountry = self.cursor.fetchall()
        #     birthsNum = birthByCountry[0][0]
        #     finalData[country] = (purchasesNum, birthsNum)

        self.data = finalData

    def getBirthsNumber(self, countryName):
        return self.data[countryName][1]

    def getPurchasesNumber(self, countryName):
        return self.data[countryName][0]

    def getAllData(self):
        return self.data

    def getBirthNumberPredictionForCountryAndYear(self, countryName, year):
        if countryName == '':
            return {'x': [], 'y': [], 'name': 'Prediction for next year'}

        points = self.getPlotDataBirths(countryName)

        x = []
        for point in points['x']:
            x.append(point)

        y = []
        for point in points['y']:
            y.append(point)

        model = numpy.poly1d(numpy.polyfit(x, y, 3))
        # line = numpy.linspace(min(x), max(x), 100)
        prediction = model(year)
        return {'x': [year], 'y': [int(prediction)], 'name' : 'Prediction for next year'}

    def getPlotDataBirths(self, countryName):
        connection = DBConnection().db
        cursor = connection.cursor()

        dict = {'x': list(), 'y': list(), 'name': 'Births by year'}

        if countryName == '':
            return dict

        birthDataBYCountryQuery = "SELECT year, births FROM birth WHERE entity='" + countryName + "'"
        cursor.execute(birthDataBYCountryQuery)
        data = cursor.fetchall()

        for row in data:
            dict['x'].append(row[0])
            dict['y'].append(row[1])

        cursor.close()
        connection.close()

        return dict

    def getGDPPredictionByYearAndCountry(self, countryName, year):
        if countryName == '':
            return {'x': [], 'y': [], 'name': 'Prediction for next year'}

        points = self.getPlotDataGDP(countryName)

        x = []
        for point in points['x']:
            x.append(point)

        y = []
        for point in points['y']:
            y.append(point)

        model = numpy.poly1d(numpy.polyfit(x, y, 3))
        # line = numpy.linspace(min(x), max(x), 100)
        prediction = model(year)
        return {'x': [year], 'y': [int(prediction)], 'name': 'Prediction for next year'}

    def getPlotDataGDP(self, countryName):
        connection = DBConnection().db
        cursor = connection.cursor()

        dict = {'x': list(), 'y': list(), 'name': 'GDP by year'}

        if countryName == '':
            return dict

        gdpDataByCountryQuery = "SELECT * FROM gdp WHERE country='" + countryName + "'"
        cursor.execute(gdpDataByCountryQuery)
        data = cursor.fetchall()
        columnNames = [i[0] for i in cursor.description]

        for i in range(1, len(columnNames)):
            if data[0][i] is not None:
                dict['x'].append(int(columnNames[i]))
                dict['y'].append(data[0][i])

        cursor.close()
        connection.close()

        return dict