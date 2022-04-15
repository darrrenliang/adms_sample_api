#!/bin/python3.6
# coding=utf-8
# Return JSON Format data
# Path1: /Feeders           --> Show all feeder list (NAME, COLORCODE, FDTYPE)
# Path2: /Feeders/Name      --> Show feeder's attributes  (NAME, FDIRMODE, FDIRLOCKFLAG,FDIRARMFLAG ,RECLOSERDELAY ,PEAKLOAD ,FDTYPE ,COLORCODE)
# Path2: /Feeders/ColorCode --> Show feeder's attributes  (NAME, FDIRMODE, FDIRLOCKFLAG,FDIRARMFLAG ,RECLOSERDELAY ,PEAKLOAD ,FDTYPE ,COLORCODE)

import os
import sys
sys.path.append("..")
from adms_api.__init__ import connect_database
import adms_api.core

FeedeerParamATTRS  = ['IDX','NAME','COLORCODE','FDTYPE','RECLOSERDELAY']
FeederInputATTRS = ['IDX','FDIRLOCKFLAG','FDIRARMFLAG','PEAKLOAD']
SubParamATTRS = ['IDX','NAME','ZONEIDX','NUMFD','SRVSTATUS','PROPOSEFLAG','NETWORKTYPE','ALIASNAME']

FedeerParam_str = ",".join(FeedeerParamATTRS)
FedeerInput_str = ",".join(FeederInputATTRS)
SubParam_str = ",".join(SubParamATTRS)


class getFeederInfo(object):
    def __init__(self):
        self.connection = connect_database()
        self.FEEDERPARAM_cmd = "SELECT " + FedeerParam_str  +" FROM FEEDERPARAM ORDER BY IDX"
        self.FEEDERINPUT_cmd =  "SELECT " + FedeerInput_str  +" FROM FEEDERINPUT ORDER BY IDX"
        self.SUBPARAM_cmd = "SELECT " + SubParam_str  +" FROM SUBSTATIONPARAM ORDER BY IDX"
        
        self.FEEDERPARAMresult = self.connection.ExecQuery(self.FEEDERPARAM_cmd)
        self.FEEDERINPUTresult = self.connection.ExecQuery(self.FEEDERINPUT_cmd)
        self.SUBPARAMresult = self.connection.ExecQuery(self.SUBPARAM_cmd)


    def getFeederList(self) :   #-> dict
        output = {
            row[2]:{
                "IDX": row[0],
                "FEEDERNAME": row[1],
                "FDTYPE": row[3],
                "COLORCODE": row[2],
            }
            for row in self.FEEDERPARAMresult
        }
        return output if len(output)>0 else {"Message": "No data."}

    def getFeederByName(self, name) :#-> dict
        output = {
            row[2]:{
                "IDX": row[0],
                "FEEDERNAME": row[1],
                "FDTYPE": row[3],
                "COLORCODE": row[2],
            }
            for row in self.FEEDERPARAMresult if name.upper() in row[1].upper()
        }

        return output if len(output)>0 else {"Message": "No data."}

    def getFeederByColorCode(self,color) :#-> dict
        output = {
            row[2]:{
                "IDX": row[0],
                "FEEDERNAME": row[1],
                "FDTYPE": row[3],
                "COLORCODE": row[2],
            }
            for row in self.FEEDERPARAMresult if int(row[2])==color       
        }

        return output if len(output)>0 else {"Message": "No data."}

    def getSubstationParam(self) : #-> dict
        output = {
            row[0]:{
                SubParamATTRS[0]: row[0],
                SubParamATTRS[1]: row[1],
                SubParamATTRS[3]: row[3],
                SubParamATTRS[2]: row[2],
                SubParamATTRS[4]: row[4],
                SubParamATTRS[5]: row[5],
                SubParamATTRS[6]: row[6],
                SubParamATTRS[7]: row[7],
            }
            for row in self.SUBPARAMresult 
        }
        return output if len(output)>0 else {"Message": "No data."}

    def getFeedersBySubstation(self,name): # -> dict
        output = {
            row[0]:{
                SubParamATTRS[0]: row[0],
                SubParamATTRS[1]: row[1],
                SubParamATTRS[3]: row[3],
                SubParamATTRS[2]: row[2],
                SubParamATTRS[4]: row[4],
                SubParamATTRS[5]: row[5],
                SubParamATTRS[6]: row[6],
                SubParamATTRS[7]: row[7],
            }
            for row in self.SUBPARAMresult if name.upper() in row[1].upper()
        }
        return output if len(output)>0 else {"Message": "No data."}
    
    def getFeedersByFDIRLOCKFLAG(self,Flag) :#-> dict
        output = {
            row[0]:{
                FeederInputATTRS[0]: row[0],
                FeederInputATTRS[1]: row[1],
                FeederInputATTRS[3]: row[3],
                FeederInputATTRS[2]: row[2]
            }
            for row in self.FEEDERINPUTresult if Flag == row[1]
        }

        return output if len(output)>0 else {"Message": "No data."}
    
    def getFeedersByFDIRMODE(self,Mode) :#-> dict
        pass


