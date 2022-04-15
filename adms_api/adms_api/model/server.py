#!/bin/python3.6

#uvicorn server:app --reload --host 192.168.62.71 --port 8087

from model.DASDB.FeederInfo import getFeederInfo
from model.RTDB.RTDBInfo import RTDBInfo
import pkg_resources    #check version
import datetime
from version import __version__
from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
      API_Version = __version__
      time = datetime.datetime.today() 
      time = time.strftime("%Y/%m/%d %H:%M:%S")
      return {"API_Version": API_Version,"Time":time}

@app.get("/feeders/")
def readFeeders():
      Feeder  = getFeederInfo()
      dataSet = Feeder.getFeederList()
      return dataSet

@app.get("/feeders/Name/{name:str}")
def readFeederByName(name):
      Feeder  = getFeederInfo()
      dataSet = Feeder.getFeederByName(name)
      return dataSet

@app.get("/feeders/ColorCode/{Code:int}")
def readFeederByColor(Code):
      Feeder  = getFeederInfo()
      dataSet = Feeder.getFeederByColorCode(Code)
      return dataSet

@app.get("/feeders/Substation/{Name:str}")
def readFeedersBySubstation(Name):
      Feeder  = getFeederInfo()
      dataSet = Feeder.getFeedersBySubstation(Name)
      return dataSet
      
@app.get("/feeders/FDIRLOCKFLAG/{Flag:int}")
def readFeedersByFdirlockflag(Flag):
      Feeder  = getFeederInfo()
      dataSet = Feeder.getFeedersByFDIRLOCKFLAG(Flag)
      return dataSet
      
# @app.get("/feeders/FDIRMODE/{Mode:int}")

#RTDB
@app.get("/RTDB/STATION/{Station:int}")
def reasRTDBbyStation(Station):
      RTDB  = RTDBInfo()
      dataSet = RTDB.getRTDBbyStation(Station)
      return dataSet

@app.get("/RTDB/DEVICE")








