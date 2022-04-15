#!/bin/python3.6
#System
import os
# Non-System  #look for the path of acstw print(acstw.__file__)
# import acstw
# from acstw.OracleInterface import OracleInterface
import core
from core.OracleInterface import OracleInterface
from acsprism import RtdbAddress, RtdbPoint, rtdb_init  #RTDB
# print(acstw.__file__)
ORACLE_USER = 'acs_das'
ORACLE_PW = 'acsacs'
DBSTRING = 'ems'

USER = os.getenv('ORACLE_USER')
PW = os.getenv('ORACLE_PW')
DBSTRING = os.getenv('ORACLE_DBSTRING')
DASdb = OracleInterface(USER, PW, DBSTRING)

# print(dir(DASdb))
result = DASdb.ExecQuery("SELECT IDX, NAME FROM FEEDERPARAM")

'''
result_dict={}
for idx, name in result:
      result_dict[idx]= name
# print(result_dict)
@app.get("/feeder/{name:str}")
def readbyname(name: str, q: str = None):
      print('read:', name)
      result = getFeeder.getFeederByName(name)
      # for i in range(len(result)):
      #       print(name)
      #       if result[i][1] in name: 
      #             return {"id":result[i][0],"name":result[i][1],"COLORCODE":result[i][2],"FDTYPE":result[i][3]}
      # return {"Not find":name }
      return {"idx":result[0][0],"name":result[0][1],"COLORCODE":result[0][2],"FDTYPE":result[0][3]}
@app.get("/feeder/{attri_key:str}={attri_value}")
def readbyname(name: str, q: str = None):
      return {attri_key,attri_key}
# @app.get("/feeder/{colorcode}")
# @app.get("/RTitems/")
# def read_RTdata():
#       return {"data": RTresult}
'''
# STATUS POINT - SWTICH, CAPACITOR, BREAKER,...
rtdb_init()
addr = RtdbAddress(11,'R', 76, 'S')
p = RtdbPoint(addr)
print(p.read_attr('CS'))

# TELEMETRY POINT - LINE, ANALOGPOINT,...
addr = RtdbAddress(601,'P', 178, 'T')
p = RtdbPoint(addr)
print(p.read_attr('CV'))

