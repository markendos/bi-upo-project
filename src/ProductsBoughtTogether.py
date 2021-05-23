from DBConnection import DBConnection
import dash_table
import numpy as np

class ProductsBoughtTogether:
    matrix = None
    maxValues = None
    products = None
    table = None


    def __init__(self) -> None:
        pass


    def createMatrix(self):
        db = DBConnection.get_instance()
        cursor = db.cursor()
        cursor.execute("SELECT DISTINCT(product) FROM shop order by product")
        result = cursor.fetchall()
        numProducts = len(result)
        self.matrix = [[0 for y in range(numProducts)] for x in range(numProducts)]
        self.products = ["" for x in range(numProducts)]
        
        i = 0
        for x in result:
            self.products[i] = x[0]
            i += 1

        cursor.execute("SELECT GROUP_CONCAT(s.product SEPARATOR ',') FROM shop as s group by s.session_id")
        result = cursor.fetchall()

        for x in result:
            basket = x[0].split(',')
            for i in range(len(basket)):
                index_x = self.products.index(basket[i])
                for j in range(i+1, len(basket)):
                    index_y = self.products.index(basket[j])
                    if(index_x != index_y):
                        self.matrix[index_x][index_y] += 1
                        self.matrix[index_y][index_x] += 1

    
    def calculateMaxValues(self):
        matrixAux = self.matrix
        self.maxValues = []
        for i in range(0, 25):
            m = np.max(matrixAux)
            a = np.where(matrixAux == m)
            matrixAux[a[0][0]][a[1][0]] = 0
            matrixAux[a[1][0]][a[0][0]] = 0
            self.maxValues.append({"p1": self.products[a[0][0]], "p2":self.products[a[1][0]], "ocu": m})
        

    def createTable(self):
        if self.matrix is None:
            self.createMatrix()
            self.calculateMaxValues()
        self.table = dash_table.DataTable(
            id='products_bought_together',
            columns=[{"name": "Product 1", "id": "p1"}, {"name": "Product 2", "id": "p2"}, {"name": "Occurrences", "id": "ocu"}],
            data=self.maxValues,
            page_size=5
        )
    
    def getTable(self):
        if self.table is None:
            self.createTable()
        return self.table
