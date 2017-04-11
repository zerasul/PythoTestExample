#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:51:32 2017

@author: victor
"""



from http.server import BaseHTTPRequestHandler
import socketserver
import CollejaController
import json

class CollejasHTTPHandler(BaseHTTPRequestHandler):
    
    ccontroller=None
    
    def setup(self):
        self.ccontroller=CollejaController.collejaController()
        
    def send_simple_resp(self,response, responseCode=200):
        self.send_response_only(responseCode,json.dump(response))
        
    def send_Response(self, response, responseCode=200, responseHeader='Content-type', responseType='text/html'):
        self.send_response(responseCode)
        self.send_header(responseHeader,responseType)
        self.end_headers()
        self.wfile.write(json.dump(response))
    
    def do_GET(self):
        dictionary ={}
        
        dictionary['count']=self.ccontroller.read_Counter()
        super.send_simple_resp(dictionary)
        
    def do_POST(self):
        counter = self.ccontroller.read_Counter()
        counter+=1
        self.ccontroller.write_Counter(data=counter)
        dictionary ={}
        dictionary['result']='OK'
        self.send_simple_resp(dictionary)
        
        
pass


PORT_NUMBER=7077
with socketserver.TCPServer(("", PORT_NUMBER), CollejasHTTPHandler) as httpd:
    print("serving at port", PORT_NUMBER)
    httpd.serve_forever()
