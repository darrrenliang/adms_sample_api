#!/usr/bin/python3
# coding=utf-8
import os
import sys
sys.path.append("..")
from adms_api.__init__ import connect_database
# from acsprism import RtdbAddress, RtdbPoint, rtdb_init
sys.setrecursionlimit(10**6)
IOxrefATTRS = ['TABLENAME','COLNAME','KEYIDX','ENABLEFLAG','RTDBTYPE','STATION','CATEGORY','POINT','ATTRIBUTE','DESCRIPT']
IOxrefATTRS_str = ",".join(IOxrefATTRS)

class RTDBInfo(object):#RTDB
    def __init__(self):
        print("============RTDB=============")
        self.connection = connect_database()
        self.inputxref_cmd = "SELECT " + IOxrefATTRS_str  +" FROM INPUTXREF "
        self.outputxref_cmd = "SELECT " + IOxrefATTRS_str  +" FROM OUTPUTXREF "

    def getRTDBbyStation(self,Station):
        cmd = self.inputxref_cmd + "WHERE STATION=" + str(Station)
        result = self.connection.ExecQuery(self.inputxref_cmd)
        output = {
            row[2]:{
                "TABLENAME": row[0],
                "COLNAME": row[1],
                "ENABLEFLAG": row[3],
                "KEYIDX": row[2],
                "RTDBTYPE": row[4],
                'STATION' :row[5],
                'CATEGORY':row[6],
                'POINT':row[7],
                'ATTRIBUTE':row[8],
                'DESCRIPT':row[9]


            }
            for row in result if row[5]==Station
        }
        return output if len(output)>0 else {"Message": "No data."}
        # return result
