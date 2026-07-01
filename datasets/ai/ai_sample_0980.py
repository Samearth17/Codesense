from flask import Flask, render_template
from googleapiclient.discovery import build

app = Flask(__name__)

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/notify')
def notify():
 # Create a Google Calendar service object.
 service = build('calendar', 'v3')
 
 # Create the notification.
 notification = {
  'type': 'notification',
  'title': 'Reminder',
  'body': 'Don\'t forget to do your task!'
 }
 
 service.events().insert(calendarId='primary', body=notification).execute()
 
 return 'Reminder set successfully!'

if __name__ == '__main__':
 app.run(debug=True)