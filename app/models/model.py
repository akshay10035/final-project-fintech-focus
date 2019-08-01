from app import app
from flask import render_template, request, session, url_for, redirect
from app.models import model, formopener
from flask_pymongo import PyMongo

def convert():
    app.config['MONGO_DBNAME'] = 'finalProject'
    app.config['MONGO_URI'] = 'mongodb+srv://aamin:8FJctF4pbI4BlECv@cluster0-ybive.mongodb.net/test?retryWrites=true&w=majority'
    mongo = PyMongo(app)
    collection = mongo.db.dataPoints
    axesNames = mongo.db.axes
    #finalPointList = [[list(axesNames.find({'xName'})), list(axesNames.find({'yName'}))]]
    points = list(collection.find({}))
    print(points)
    # for pointdata in points:
    #     thisPair = []
    #     thisPair = pointdata['xVal']
    #     thisPair += pointdata['yVal']
    #     finalPointList += thisPair
    #return(finalPointList)
    return[['x','y'],[0,1],[3,4]]
    
#print(convert())
    