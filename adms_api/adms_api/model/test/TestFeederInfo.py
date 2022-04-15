#!/usr/bin/python
# coding=utf-8
import sys
import unittest
sys.path.append("../../..") #up to adms_api of dir
from adms_api.__init__ import connect_database
from adms_api.model.DASDB.FeederInfo import getFeederInfo   

class FeederInfoTestCase(unittest.TestCase):

    def test_Connect(self):
        connection = connect_database()
        self.assertTrue(connection)

    def test_Feeders(self):
        getFeeder = getFeederInfo()
        result = getFeeder.getFeederList()
        self.assertTrue(len(result)>0)

    def test_FeedersByName(self):
        name = "Oneida_White_NFD1"
        getFeeder = getFeederInfo()
        result = getFeeder.getFeederByName(name)
        self.assertEqual(name, result[1]['FEEDERNAME'])
    
    def test_FeedersByColorCode(self):
        color = 1
        getFeeder = getFeederInfo()
        result = getFeeder.getFeederByColorCode(color)
        self.assertTrue(len(result)>0)

    def test_FeedersBySubstation(self):
        name = "College"
        getFeeder = getFeederInfo()
        result = getFeeder.getFeedersBySubstation(name) 
        self.assertEqual(name, result[3]['NAME'])

    def test_getFeedersByFDIRLOCKFLAG(self):
        Flag = 1 
        getFeeder = getFeederInfo()
        result = getFeeder.getFeedersByFDIRLOCKFLAG(Flag)
        self.assertTrue(len(result)>0)


    




    
    