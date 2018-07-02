from flask import Flask
from flask import Request
app = Flask(__name__)
GIT_BASE_URL = "https://github.com"
BUGZILLA_URL = "https://bugzilla.com"


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getHeatMap')
def getHeatMap():
    version = request.args.get('version')
    return {}

@app.route('/getGitBaseURL')
def getGitBaseURL():
    return GIT_BASE_URL

@app.route('/getBugzillaURL')
def getBugzillaURL():
    return BUGZILLA_URL
    
