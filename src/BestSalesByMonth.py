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
        cursor.execute("select month, product, count(product) AS 'value_occurrence' FROM bi_solutions.shop group by month")
        result = cursor.fetchall()
        sales = []
        for row in result:
            sales.append({"month_bsbm": monthsDict[row[0]], "product_bsbm": row[1], "sales_bsbm": row[2]})
        self.table = dash_table.DataTable(
            id='best_sales_by_month',
            columns=[{"name": "Month", "id": "month_bsbm"}, {"name": "Product", "id": "product_bsbm"}, {"name": "Sales", "id": "sales_bsbm"}],
            data=sales,
            page_size=5
        )

        cursor.close()
        connection.close()

        return self.table