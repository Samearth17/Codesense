# Python Backend
# Web server setup
app = Flask(__name__)

# Database setup
db = SQLAlchemy(app)

# Model for tasks
class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  is_completed = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return f'<Task {self.id}: {self.title}>'

# API Endpoint
@app.route('/tasks', methods=['POST'])
def create_task():
  request_data = request.get_json()
  title = request_data.get('title')
  if not title:
    return jsonify({'error': 'Title must be provided.'}), 400

  task = Task(title=title)
  db.session.add(task)
  db.session.commit()

  return jsonify(task.serialize())

# React Frontend
import React, { useState, useEffect } from 'react'
import axios from 'axios'

export const TaskList = () => {
  const [tasks, setTasks] = useState([])

  useEffect(() => {
    getTasks()
  }, [])

  const getTasks = async () => {
    const response = await axios.get('http://localhost:3000/tasks')
    setTasks(response.data)
  }

  return (
    <div>
      {tasks.map(task => (
        <div key={task.id}>
          <input type="checkbox" checked={task.is_complete} />
          <label>{task.title}</label>
        </div>
      ))}
    </div>
  )
}