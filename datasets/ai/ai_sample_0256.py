import sqlite3

class StudentDatabase:
 def __init__(self, db):
  self.conn = sqlite3.connect(db)
  self.cur = self.conn.cursor()
  self.cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)")
  self.conn.commit()
  
 def add_student(self, name, email, age):
  self.cur.execute("INSERT INTO students VALUES (NULL, ?, ?, ?)", (name, email, age))
  self.conn.commit()
  
 def delete_student(self, id):
  self.cur.execute("DELETE FROM students WHERE id=?", (id,))
  self.conn.commit()
  
 def update_student(self, id, name, email, age):
  self.cur.execute("UPDATE students SET name=?, email=?, age=? WHERE id=?", (name, email, age, id))
  self.conn.commit()
  
 def list_students(self):
  self.cur.execute("SELECT * FROM students")
  rows = self.cur.fetchall()
  return rows
  
def main():
 db = StudentDatabase('students.db')
 db.add_student('John Doe', 'john@doe.com', 30)
 db.add_student('Adam Smith', 'adam@smith.com', 25)
 db.delete_student(2)
 db.update_student(1, 'John Smith', 'john@smith.com', 40)
 print(db.list_students())
 
if __name__ == '__main__':
 main()