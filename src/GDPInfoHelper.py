from DBConnection import DBConnection
import numpy

class GDPInfoHelper:
    def __init__(self):
        self.cursor = DBConnection.get_instance().cursor()

    def getGDPPredictionByYearAndCountry(self, countryName, year):
        gdpDataByCountryQuery = "SELECT * FROM gdp WHERE country='"+countryName+"'"
        self.cursor.execute(gdpDataByCountryQuery)

        data = self.cursor.fetchall()
        columnNames = [i[0] for i in self.cursor.description]

        x = []
        y = []
        for i in range(1, len(columnNames)):
            if data[0][i] is not None:
                x.append(int(columnNames[i]))
                y.append(data[0][i])

        model = numpy.poly1d(numpy.polyfit(x, y, 3))
        # line = numpy.linspace(min(x), max(x), 100)
        prediction = model(year)
        return prediction

    ##TODO add method for fetching points so they can be represented into graph

## TODO remove
def main():
    info = GDPInfoHelper()
    print(info.getGDPPredictionByYearAndCountry('Afghanistan', 2020))

if __name__ == "__main__":
    main()