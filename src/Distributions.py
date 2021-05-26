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
    
    def getAggregationOperations(self):
        return [
                {'label': 'Avg', 'value': 'avg'},
                {'label': 'Min', 'value': 'min'},
                {'label': 'Max', 'value': 'max'},
                ]

    def getPlotData(self, variable, operation):
        conn=c()
        cursor = conn.db.cursor()
        data = list()
        
        query = "SELECT session_id, {}({}) FROM shop GROUP BY session_id;"

        cursor.execute(query.format(operation, variable))
        
        result = cursor.fetchall()
        

        for r in result:
            data.append(int(r[1]))
            
        cursor.close()
        conn.db.close()
        return dict({'x':data})
