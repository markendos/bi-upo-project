from DBConnection import DBConnection
import numpy

class BirthsAndGdpHelper:
    def getBirthNumberPredictionForCountryAndYear(self, countryName, year):
        if countryName in (None, ''):
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

        if countryName in (None, ''):
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
        if countryName in (None, ''):
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

        if countryName in (None, ''):
            return dict

        dateRange = [*range(2008, 2020)]
        dateRange = map(str, dateRange);
        dateRange = map(lambda x: "`{}`".format(x), dateRange)
        
        gdpDataByCountryQuery = "SELECT country,{} FROM gdp WHERE country LIKE '{}'".format(','.join(map(str, dateRange)), countryName)
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

    def getPlotDataBirthsClicks(self, clicks=True):
        connection = DBConnection().db
        cursor = connection.cursor()
        query = ''
        
        if clicks:
            query = clicksByCountriesQueries = "SELECT country, count(*) as count FROM shop GROUP BY country ORDER BY count DESC"
        else:
            query = usersByCountriesQueries = "SELECT country, count(*) AS count FROM (SELECT country, session_id FROM shop GROUP BY country, session_id) AS s GROUP BY s.country ORDER BY count DESC"
        
        cursor.execute(query)
        result = cursor.fetchall()

        data = []
        for row in result:
            country, count = row

            gdpForCountryQuery = "SELECT `2008` FROM gdp where country='" + country + "'"
            cursor.execute(gdpForCountryQuery)
            gdpForCountry = cursor.fetchall()[0][0]

            birthsByCountriesQuery = "SELECT births FROM birth where year = 2008 and entity='" + country + "'"
            cursor.execute(birthsByCountriesQuery)
            birthByCountry = cursor.fetchall()
            birthsNum = birthByCountry[0][0]
            data.append({'x' : [gdpForCountry], 'y' : [birthsNum], 'z': [count], 'name' : country})

        cursor.close()
        connection.close()

        return data

def main():
    info = BirthsAndGdpHelper()
    print(info.getPlotDataBirthsClicks())

if __name__ == "__main__":
    main()