#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:51:32 2017

@author: victor
"""

from flask import Flask, request
import CollejaController
import json



class CollejasHTTPHandler():
    
    ccontroller=None
    
    def setup(self):
        self.ccontroller=CollejaController.collejaController()
        
    
    def do_GET(self):
        dictionary ={}
        
        count=self.ccontroller.read_Counter()
        return json.dumps({'count':count},sort_keys=True)
        
    def do_POST(self):
        counter = self.ccontroller.read_Counter()
        counter+=1
        self.ccontroller.write_Counter(data=counter)
        dictionary ={}
        dictionary['result']='OK'
        return json.dump(dictionary)
        
        
pass

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    collejaHandler = CollejasHTTPHandler()
    collejaHandler.setup()
    
    if request.method == 'GET':
        return collejaHandler.do_GET()
    else:
        return collejaHandler.do_POST()

app.run(host='0.0.0.0',port=7077)
