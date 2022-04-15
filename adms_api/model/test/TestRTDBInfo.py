#!/usr/bin/python
# coding=utf-8
import sys
import unittest
sys.path.append("../../..") #up to adms_api of dir
from adms_api.model.RTDB.RTDBInfo import RTDBInfo   

class RTDBInfoTestCase(unittest.TestCase):

    def test_getRTDBStation(self):
        getRTDBInfo = RTDBInfo()
        result = getRTDBInfo.getRTDBStation()
        self.assertTrue(len(result)>0)

    def test_getRTDBbyStation(self):
        getRTDBInfo = RTDBInfo()
        Station = str(1) ; Category = 'R' ; RTDBtype = 'S'
        result = getRTDBInfo.getRTDBbyStation(Station,Category,RTDBtype)
        self.assertTrue(len(result)>0)

    def test_getRTDBCS(self):
        getRTDBInfo = RTDBInfo()
        Station =str(1) ; Category = 'R' ; RTDBtype = 'S' ; Point=1
        result = getRTDBInfo.getRTDBCS(Station,Category,RTDBtype,Point)
        self.assertTrue(('State' in str(result)  ))

    def test_writeRTDBCS(self):
        getRTDBInfo = RTDBInfo()
        Station = str(1) ; Category = 'R' ; RTDBtype = 'S' ; Point=1 ; State=1
        result = getRTDBInfo.writeRTDBCS(Station,Category,RTDBtype,Point,State)
        self.assertTrue(('State' in str(result)  ))

