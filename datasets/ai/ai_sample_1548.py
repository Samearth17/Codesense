# Google Cloud Platform Application


from google.appengine.api import appinfo

app = appinfo.AppInfoExternal(
 application='myapp',
 version='1',
 runtime='python27',
 api_version='1',
 threadsafe=True,
 )

# Create a handler for the endpoint
def hello_world():
 print("Hello, world!")

# Map the handler to the endpoint
app.handlers.extend([
    ('/', hello_world)
])

# Deploy the application
app.deploy()