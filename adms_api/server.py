#!/bin/python3.6

#uvicorn server:app --reload --host 192.168.62.71 --port 8087

from model.DASDB.FeederInfo import getFeederInfo
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


# @app.get("/feeders/{item_id:int}")
# def read_location(item_id: int, q: str = None):
#       return {"idx":result[item_id][0],"name":result[item_id][1],"COLORCODE":result[item_id][2],"FDTYPE":result[item_id][3]}

# @app.get("/feeder/{name:str}")
# def readbyname(name: str, q: str = None):
#       try:
#             result = getFeeder.getFeederByName(name)
#             return {"idx":result[0][0],"name":result[0][1],"COLORCODE":result[0][2],"FDTYPE":result[0][3]}
#       except:
#             return {"No find any data"}
# @app.get("/feeder/{attri_key:str}={attri_value}")
# def readbystring(attri_key: str,attri_value ):
#       attri_data = attri_key + " = " + "'" + str(attri_value) + "'"
#       result = getFeeder.getFeederByanyAttri(attri_data)
#       try:
#             return {"idx":result[0][0],"name":result[0][1],"COLORCODE":result[0][2],"FDTYPE":result[0][3]}
#       except:
#             return {"No find any data"}








