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

# CONFIG
# Koneksi database ke server vanika

from __future__ import unicode_literals
"""Config values."""
from os import environ

class Config:

    # Database config
    db_user = environ.get('DATABASE_USERNAME')
    db_password = environ.get('DATABASE_PASSWORD')
    db_host = environ.get('DATABASE_HOST')
    db_name = environ.get('DATABASE_NAME')

    #token line config
    channel_secret = environ.get('DATABASE_CHANNEL_SECRET')
    channel_access_token = environ.get('DATABASE_CHANNEL_TOKEN')

    #google token
    googleapitoken = environ.get('DATABASE_GOOGLE_APIS') #from becatholic

    #owm
    owm_key = environ.get('DATABASE_OWM')

    #email
    email = environ.get('DATABASE_EMIAL')
    password = environ.get('DATABASE_EMAIL_PASSWORD')