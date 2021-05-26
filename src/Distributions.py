import datetime
from DBConnection import DBConnection as c

class DistributionsDatamart:
    cursor = None
    
    def __init__(self):
        pass
        
    def getVariables(self):
        return [
                {'label': 'Clicks', 'value': 'clicks'},
                {'label': 'Price', 'value': 'price'},
                {'label': 'Page number', 'value': 'page'},
                ]
    
    def getValues(self, variable):
        return [
                {'label': 'Average Value', 'value': 'avg'},
                {'label': 'Maximun value', 'value': 'max'},
                ]

    def getPlotData(self, variable, operation):
        conn=c()
        cursor = conn.db.cursor()
        data = list()
        if operation=="Avg":
            query = "SELECT session_id, AVG({}) FROM shop GROUP BY session_id;"
        else:
            query = "SELECT session_id, MAX({}) FROM shop GROUP BY session_id;"

        cursor.execute(query.format(variable))
        
        result = cursor.fetchall()
        

        for r in result:
            data.append(int(r[1]))
            
        cursor.close()
        conn.db.close()
        return dict({'x':data})
