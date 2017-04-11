#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:45:21 2017

@author: victor
"""
import pytest
import CollejaController

    
def test_Controller_Read():
    collejaContr= CollejaController.collejaController()
    assert  collejaContr.read_Counter() == 0

def test_Controller_Write():
    collejaContr= CollejaController.collejaController()
    collejaContr.write_Counter(2)
    assert collejaContr.read_Counter() == 2
    collejaContr.write_Counter(0)
    assert collejaContr.read_Counter() == 0