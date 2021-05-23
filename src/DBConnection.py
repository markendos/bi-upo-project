import mysql.connector

class DBConnection:
  __instance__ = None

  def __init__(self):
    if DBConnection.__instance__ is None:
      DBConnection.__instance__ = self
      self._db = mysql.connector.connect(host="localhost", user="root", password="", database="bi_solutions")

  @staticmethod
  def get_instance():
    if not DBConnection.__instance__:
      DBConnection()
    return DBConnection.__instance__._db