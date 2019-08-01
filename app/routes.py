from app import app
from flask import render_template, request, session, url_for, redirect
from app.models import model, formopener
from flask_pymongo import PyMongo

app.config['MONGO_DBNAME'] = 'finalProject'
app.config['MONGO_URI'] = 'mongodb+srv://aamin:8FJctF4pbI4BlECv@cluster0-ybive.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)
collection = mongo.db.dataPoints
points = list(collection.find({}))



@app.route('/')
# @app.route('/signup', methods=['POST', 'GET'])
# def signup():
    
#     if 'username' not in session:
#         session['username'] = 'newUser'
#     if request.method == 'POST':
#         users = mongo.db.users
#         existing_user = users.find_one({'name' : request.form['username']})
#         if existing_user is None:
#             users.insert({'name' : request.form['username'], 'password' : request.form['password']})
#             session['username'] = request.form['username']
#             namedisplay = session['username']
#             return redirect(url_for('index'))
#         else:
#             return redirect(url_for('index'))
#     return render_template('signup.html')
@app.route('/index')
def index():
    #reset session variables
    (mongo.db.dataPoints).remove({})
    return render_template('index.html')
    
@app.route('/dataEntry', methods= ['GET','POST'])
def dataEntry():
    userdata = request.form
    xName = userdata["X-axis"]
    yName = userdata["Y-axis"]
    axes = mongo.db.axes
    axes.insert({"xName":xName,"yName":yName})
    return render_template('dataEntry.html', xName = xName, yName = yName)
    
app.secret_key = 'totallySecret'    
@app.route('/data', methods=['GET','POST'])
def data():
    pointdata = request.form
    #print(pointdata)
    dataPoints = mongo.db.dataPoints
    axesPoints = mongo.db.axes
    axes = mongo.db.dataPoints
    xVal = float(pointdata["X-point"])
    yVal = float(pointdata["Y-point"])
    dataPoints.insert({"xVal":xVal, "yVal":yVal})
    xName = axesPoints.find_one('xName')
    yName = axesPoints.find_one('yName')
    return render_template('dataEntry.html', xName = xName, yName = yName)
    
@app.route('/results', methods=['GET','POST'])
def results():
    reallyfinalPointList = model.convert()
    print(reallyfinalPointList)
    return render_template('results.html', reallyfinalPointList = reallyfinalPointList)
    