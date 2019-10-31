# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


# VANIKA V 2.0
# vanika.tru.io/updatelog

# DATASQL
# Koneksi database ke server vanika di panggil dari app.py

from __future__ import unicode_literals
from random import randint

import errno
import os
import sys
import logging

# GET DATA SQL
import pymysql


class Database:
    """Database connection class."""
    def __init__(self, config):
        self.host = config.db_host
        self.username = config.db_user
        self.password = config.db_password
        self.dbname = config.db_name
        self.conn = None

    def open_connection(self):
        """Connect to MySQL Database."""
        try:
            if self.conn is None:
                self.conn = pymysql.connect(self.host,
                                            user=self.username,
                                            passwd=self.password,
                                            db=self.dbname,
                                            connect_timeout=5)
        except pymysql.MySQLError as e:
            logging.error(e)
            sys.exit()
        finally:
            logging.info('Connection opened successfully.')

    def run_query(self, query, user_name, user_id):
        """Execute SQL query."""
        try:
            self.open_connection()
            with self.conn.cursor() as cur:
                if 'SELECT' in query:
                    records = []
                    cur.execute(query)
                    result = cur.fetchall()
                    for i in range(len(result)):
                        records.append(result[i][0])
                    cur.close()
                    return records
                else:
                    result = cur.execute(query)
                    self.conn.commit()
                    affected = f"{cur.rowcount} rows affected."
                    cur.close()
                    return affected
        except pymysql.MySQLError as e:
            # ERROR LOGS
            errormsg_line = str(sys.exc_info()[-1].tb_lineno)
            errormsg_type = str(type(e).__name__)
            errormsg_text = str(e)
            self.open_connection()
            with self.conn.cursor() as cur:
                try:
                    cur.execute("INSERT INTO `error` (`errorid`, `username`, `userid`, `error_line`, `error_type`, `error_msg`, `date`) VALUES (NULL, '"+user_name+"', '"+user_id+"', '"+errormsg_line+"', '"+errormsg_type+"', '"+errormsg_text.replace("'","")+"', CURRENT_TIMESTAMP);")
                    cur.close()
                except:
                    cur.execute("INSERT INTO `error` (`errorid`, `username`, `userid`, `error_line`, `error_type`, `error_msg`, `date`) VALUES (NULL, 'SOMEONE', 'SOMEID', '"+errormsg_line+"', '"+errormsg_type+"', '"+errormsg_text.replace("'","")+"', CURRENT_TIMESTAMP);")
                    cur.close()
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logging.info('Database connection closed.')
