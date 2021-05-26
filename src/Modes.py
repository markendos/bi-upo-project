import datetime
from DBConnection import DBConnection as c


class ModesDatamart:
    cursor = None

    def __init__(self):
        pass

    def getVariables(self):

        conn = c()
        cursor = conn.db.cursor()

        cursor.execute("SELECT distinct(country) FROM shop ORDER BY 1 ASC")
        result = cursor.fetchall()

        options = list()
        options.append({'label': 'All Countrys', 'value': 'General'})
        for x in result:
            options.append({'label': x[0], 'value': x[0]})

        cursor.close()
        conn.db.close()

        return options

    def getPlotData(self, pais=None):
        conn = c()
        cursor = conn.db.cursor()
        data = list()
        
        if pais == 'General' or pais == None or len(pais.strip())<1:
            query = "SELECT category, COUNT(clicks) FROM shop GROUP BY category"
        else:
            query = "SELECT category, COUNT(clicks) FROM shop WHERE country='{}' GROUP BY category".format(
                pais)

        cursor.execute(query)

        result = cursor.fetchall()
        dict = {'v': list(), 'n': list()}

        for r in result:
            dict['v'].append(r[1])
            dict['n'].append(r[0])

        data.append(dict)

        cursor.close()
        conn.db.close()
        return dict
