import mysql.connector

class DBConnection:

  def __init__(self):
      self.db = mysql.connector.connect(host="localhost", user="root", password="", database="bi_solutions")
