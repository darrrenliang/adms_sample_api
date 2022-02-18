#!/usr/bin/python3
# coding=utf-8
"""
:Copyright: © 2022 Advanced Control Systems, Inc. All Rights Reserved.
@Author: Stephen Hung
@Author: Darren Liang
@Date  : 2022-02-18
"""

import os
from adms_api.core.OracleInterface   import OracleInterface
from adms_api.core.LinuxInterface    import LinuxInterface

# APP INFO
TITLE  = "ADMS API"
IPADDR = "127.0.0.1"
PORT   = "5000"


# PRISM INFO
PRISM   = LinuxInterface()

# DB INFO
def connect_database():
    USER  = os.getenv('ORACLE_USER_BASEDB', 'acs_map_jepco72')
    PSWD  = os.getenv('ORACLE_PW_BASEDB'  , 'acs')
    TNS   = os.getenv('ORACLE_DBSTRING_BASEDB', 'dasmap')
    Mapdb = OracleInterface(USER, PSWD, TNS)
    Mapdb.ConnectTest()
    return Mapdb

# LOG INFO
LOG_FILENAME = 'ADMS_API.log'
LOG_FORMAT   = '%(asctime)s [%(process)d] %(levelname)s %(name)s: %(message)s'
LOG_FOLDER   = '/home/acs/tmp'


if __name__ == "__main__":
    USER  = ""
    PSWD  = ""
    TNS   = ""
    Mapdb = OracleInterface(USER, PSWD, TNS)
    Mapdb.ConnectTest()