#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:13:10 2017

@author: victor
"""
from http.client import HTTPConnection
import json

def test_get():
    h1= HTTPConnection('ellimecha.ddns.net:7077')
    r1=h1.request('GET','/')
    conn= h1.getresponse()
    assert conn.status == 200
