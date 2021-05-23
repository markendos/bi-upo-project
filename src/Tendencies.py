import datetime
from DBConnection import DBConnection as c

class Datamart:
    def get_variables():
        return [
                {'label': 'Category', 'value': 'category'},
                {'label': 'Color', 'value': 'colour'},
                {'label': 'Country', 'value': 'country'},
                {'label': 'Location', 'value': 'location'},
                {'label': 'Model Photography', 'value': 'model_photography'},
                ]
    
    def get_values(variable):
        con = c.get_instance()
        cursor = con.cursor()
        cursor.execute("SELECT distinct({}) FROM shop ORDER BY 1 ASC".format(variable))
        result = cursor.fetchall()
        
        options = list() 
        for x in result:
            options.append({'label': x[0], 'value': x[0]})
            
        return options

    def get_plot_data(variable, value):
        con = c.get_instance()
        cursor = con.cursor()
        data = list()
        for v in value:
            cursor.execute("SELECT CONCAT('2008-' ,month, '-', day), count(*) FROM shop WHERE {} LIKE ('{}') GROUP BY month, day ORDER BY month ASC, day ASC;".format(variable, v))
            result = cursor.fetchall()
            dict = {'x': list(), 'y': list(), 'name': v}
            
            for r in result:
                date = r[0].split("-")
                dict['x'].append(datetime.datetime(int(date[0]), int(date[1]), int(date[2])))
                dict['y'].append(r[1])
            
            data.append(dict)
          
        return data
