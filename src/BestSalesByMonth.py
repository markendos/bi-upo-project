from DBConnection import DBConnection
import dash_table
import numpy as np

class BestSalesByMonth:
    table = None

    def __init__(self) -> None:
        pass


    def getTable(self):
        connection = DBConnection().db
        cursor = connection.cursor()

        monthsDict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8:"August", 9: "September", 10: "October", 11: "November", 12: "December"}
        #cursor.execute("SELECT * FROM (SELECT month, product, count(*) AS clicks FROM shop GROUP BY product, month ORDER BY month ASC, clicks DESC) s GROUP BY s.month")
        cursor.execute("(SELECT * FROM (SELECT month, product, count(*) AS clicks FROM bi_solutions.shop WHERE month = 4 GROUP BY product ORDER BY clicks DESC) s) UNION (SELECT * FROM (SELECT month, product, count(*) AS clicks FROM bi_solutions.shop WHERE month = 5 GROUP BY product ORDER BY clicks DESC) s) UNION (SELECT * FROM (SELECT month, product, count(*) AS clicks FROM bi_solutions.shop WHERE month = 6 GROUP BY product ORDER BY clicks DESC) s) UNION (SELECT * FROM (SELECT month, product, count(*) AS clicks FROM bi_solutions.shop WHERE month = 7 GROUP BY product ORDER BY clicks DESC) s) UNION (SELECT * FROM (SELECT month, product, count(*) AS clicks FROM bi_solutions.shop WHERE month = 8 GROUP BY product ORDER BY clicks DESC) s )")
        result = cursor.fetchall()
        visits = []
        for row in result:
            visits.append({"month_bsbm": monthsDict[row[0]], "product_bsbm": row[1], "visits_bsbm": row[2]})
        self.table = dash_table.DataTable(
            id='best_visits_by_month',
            columns=[{"name": "Month", "id": "month_bsbm"}, {"name": "Product", "id": "product_bsbm"}, {"name": "Visits", "id": "visits_bsbm"}],
            data=visits,
            sort_action='native',
            filter_action='native',
            page_size=5
        )

        cursor.close()
        connection.close()

        return self.table