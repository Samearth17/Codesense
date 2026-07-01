import unittest
from flask_testing import TestCase
from app import db, Task

class TestModel(TestCase):
 def create_app(self):
 return app

 def setUp(self):
 db.create_all()
 self.task = Task(description='Description')
 db.session.add(self.task)
 db.session.commit()

 def tearDown(self):
 db.session.remove()
 db.drop_all()

class TestTask(TestModel):
 def test_task_creation(self):
 self.assertEqual('Description', self.task.description)

if __name__ == '__main__':
 unittest.main()