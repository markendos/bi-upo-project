import mysql.connector

class DBConnection:

  def __init__(self):
      self.db = mysql.connector.connect(host="localhost", user="admin", password="admin", database="bi_solutions")
