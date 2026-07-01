import sqlite3

class Model:

  def __init__(self):
    self.conn = sqlite3.connect(":memory:")
    self.cursor = self.conn.cursor()

  def create(self,name):
    self.cursor.execute(
			"CREATE TABLE IF NOT EXISTS Models (name TEXT)"
		)
    self.cursor.execute(
			"INSERT INTO Models(name) VALUES (?)",
			(name,),
		)
    self.conn.commit()

  def read(self):
    self.cursor.execute("SELECT * FROM Models")
    return self.cursor.fetchall()

  def update(self,name):
    self.cursor.execute(
			"UPDATE Models SET name = ? WHERE name = ?", 
			(name, name,),
		)
    self.conn.commit()
  
  def delete(self, name):
    self.cursor.execute(
			"DELETE FROM Models WHERE name = ?",
			(name,),
		)
    self.conn.commit()