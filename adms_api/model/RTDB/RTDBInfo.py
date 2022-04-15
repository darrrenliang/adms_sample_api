#!/usr/bin/python3
# coding=utf-8
import os
import sys

from _cprism_cffi import lib, ffi
from acsprism import RtdbAddress, RtdbPoint,rtdb_init,stationpointlist
from acsprism import rtdbattribute
from acsprism.common import check_ptr
from acsprism import vde


class RTDBInfo(object):#RTDB
    def __init__(self):
        self.vde_file = vde.BaseVdeFile(read_only = False)
        self.stationlist = stationpointlist.StationPointList()
        self.STATIONLISTresult = list(self.stationlist.stations(names=True))#type = [(),()...]
        self.RTDBtype = ['S','T']
        self.RTDBcatgory =  ['R','I','P','C','S','A','E','D','L']#['Remote','Internal','Pseudo','Calculated','SOE','Accumulator','Estimated','Diagnostic','Lightweight']
    
    def getRTDBStation(self):
        count=0
        output = {}
        for i ,row in enumerate(self.STATIONLISTresult):
            if row[1] != "" :
                output[count] = {}
                output[count]["Station"] = row[0]
                output[count]["Name"] = row[1]    
                count += 1
        return output if len(output)>0 else {"Message": "No data."}
        
    def numbertoStation(self,Station_num):
        try:
            for i in range(len(self.STATIONLISTresult)):
                if Station_num==self.STATIONLISTresult[i][0]:
                    Station = self.STATIONLISTresult[i][1]
                    break
            return Station
        except:
            return {"The Station is not found."}
            
    def getRTDBbyStation(self,Stations):
        Stations_name = self.numbertoStation(Stations)
        if Stations_name == {"The Station is not found."}:
            return { "Message ": "RTDB Address is not found." } 
        else:
            output = { 
                'S':{
                        "Category":{}
                    },
                'T':{
                        "Category":{}
                    }
            }
            for i in range(len(self.RTDBtype)):
                for j in  range(len(self.RTDBcatgory)):
                    try:
                        result =list((a.point, a.point_description()) for a in self.stationlist.points(Stations, self.RTDBcatgory[j], self.RTDBtype[i], addresses=True))
                    except:
                        pass
                    output[self.RTDBtype[i]]["Category"][self.RTDBcatgory[j]] = {}
                    output[self.RTDBtype[i]]["Category"][self.RTDBcatgory[j]]["Points"] = {}

                    for k,v in enumerate(result):
                        if result[k][1]!="":
                            output[self.RTDBtype[i]]["Category"][self.RTDBcatgory[j]]["Points"][result[k][0]] = result[k][1]
            Alloutput = {
                "Stations":Stations,
                "Name": Stations_name,
                "Type":output
            }  
            return Alloutput

    def getAllattributes(self):
        count = lib.cprism_rtdbattribute_list_count()
        All_attri = []
        for i in range(count):
            result = str(rtdbattribute.RtdbAttribute(lib.cprism_rtdbattribute_list_at(i)))
            All_attri.append(result)
        return All_attri

    def getRTDBAllCS(self,Station,Category,RTDBtype,Point):
        All_attri = self.getAllattributes()
        output = {
            "Station": Station, 
            " Category ": Category,  
            "Type": RTDBtype, 
            " Point ":Point,
            "Attributes":{
            }
            }
        try:
            rtdb_init()
            addr = RtdbAddress(Station,Category,Point,RTDBtype)
            point = RtdbPoint(addr)
        except:
            return { "Message ": "RTDB Address is not found." } 
        for k in range(len(All_attri)):
            output["Attributes"][k] = {}
            output["Attributes"][k]["Attribute"] = All_attri[k]
            try:
                rtdb_init()
                addr = RtdbAddress(Station,Category,Point,RTDBtype)
                point = RtdbPoint(addr)
                output["Attributes"][k]["value"] = point.read_attr(All_attri[k])
            except:
                output["Attributes"][k]["value"]= "No found data"

        return output
        
    def getRTDBCS(self,Station,Category,RTDBtype,Point,RTDB_attr):
        try:
            rtdb_init()     
            addr = RtdbAddress(Station,Category,Point,RTDBtype)
            point = RtdbPoint(addr)
            result = point.read_attr(RTDB_attr)
            output = {
            "Station": Station, 
            " Category ": Category,  
            "Type": RTDBtype, 
            " Point ":Point, 
            " Attributes":{ 
            " number":{ 
            " Attribute": RTDB_attr, 
            " value": result

            } 

            }
            }
        except Exception:
            Station_name = self.numbertoStation(Station)
            return  { "Message ": "RTDB Address is not found." } 
        except :
            result = self.getRTDBAllCS(Station,Category,RTDBtype,Point)
            return { "Message ": "RTDB Point is not found" }    
        return {"Message ":output}

    def writeRTDBCS(self,Station,Category,RTDBtype,Point,RTDB_attr,value):
        rtdb_init()
        addr = RtdbAddress(Station,Category,Point,RTDBtype)
        point = RtdbPoint(addr)
        try:
            point.write_attr(RTDB_attr,int(value))
            output =  self.getRTDBCS(Station,Category,RTDBtype,Point,RTDB_attr)
        except NameError:
            Station_name = self.numbertoStation(Station)
            return  { "Message ": "RTDB Address is not found." } 
        except Exception:
            result = self.getRTDBCS(Station,Category,RTDBtype,Point,RTDB_attr)
            return { "Message ": "RTDB Point’s attribute is not found. " } 
        except:
            return { "Message ": "RTDB Point’s value is incorrect." }   
        return {"Message ":output}
      
