#!/usr/bin/python3
# coding=utf-8
"""
:Copyright: © 2022 Advanced Control Systems, Inc. All Rights Reserved.
@Author: Stephen Hung
@Author: Darren Liang
@Date  : 2022-02-18
"""

import os
import sys
sys.path.append("..")
from adms_api.core.OracleInterface   import OracleInterface
# from acsprism import RtdbAddress, RtdbPoint, rtdb_init
# from core.LinuxInterface    import LinuxInterface

# APP INFO
TITLE  = "ADMS API"
IPADDR = "127.0.0.1"
PORT   = "5000"

# PRISM INFO
# PRISM   = LinuxInterface()

# DB INFO
def connect_database():
    USER  = os.getenv('ORACLE_USER', 'acs_das')
    PSWD  = os.getenv('ORACLE_PW'  , 'acs_das')
    TNS   = os.getenv('ORACLE_DBSTRING', 'ems')
    DASdb = OracleInterface(USER, PSWD, TNS)
    #DASdb.ConnectTest()
    return DASdb

# LOG INFO
LOG_FILENAME = 'ADMS_API.log'
LOG_FORMAT   = '%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s'
LOG_FOLDER   = '/home/acs/tmp'


if __name__ == "__main__":
    USER  = ""
    PSWD  = ""
    TNS   = ""
    DASdb = OracleInterface(USER, PSWD, TNS)
    DASdb.ConnectTest()