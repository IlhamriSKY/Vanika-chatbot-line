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

# SINTAK ID
# Menampilkan data sintak dari ENDPOINT
from __future__ import unicode_literals

# Config token
from controler.config import Config

# OOP
from controler.endpoint import Endpoint, Req_Header

# Operation
from controler.operation import prog

#web based
import requests
import json
import os
import sys
import re
from bs4 import BeautifulSoup

# UrlLib with version
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq

if sys.version_info[0] < 3:
  class urllib:
    parse = __import__("urllib")
    request = __import__("urllib2")
else:
  import urllib.request
  import urllib.parse

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError,
)

# Line SDK
# https://github.com/line/line-bot-sdk-python
from linebot.models import *

# Listed
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

# Token
channel_secret = Config.channel_secret
channel_access_token = Config.channel_access_token
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


class Sintak:
    def transkrip(event, user_name, nim):
      HEADERS = Req_Header.HEADERS
      NIM = nim.upper()
      URL_BASE = Endpoint.SINTAKID_URL_BASE_TRANSKRIP
      logindata = {'thnn': '2019', 'semm': 'G1', 'tpilihh': 'TRANSKRIP', 'ipk3': 'Transkrip', 'nimy': NIM}
      session = requests.Session()
      response = session.post(URL_BASE, data=logindata, headers=HEADERS)
      soup = BeautifulSoup(response.content, 'html.parser')

      #STORE
      columns1 = []
      columns2 = []
      columns3 = []
      columns4 = []
      columns5 = []
      tables = [
          [
              [td.get_text(strip=True) for td in tr.find_all('td')] 
              for tr in table.find_all('tr')
          ] 
          for table in soup.find_all('table')
      ]
      
      tables[2] = [x for x in tables[2] if x[0].isdigit()]

      for i in range (0, 50): # tambah range sesuai makul
          tables[2].append(['99', '-', '-', '-', '-', '-'])

      for i in range(0,10):
        if tables[2][i][0].isdigit() == True:
          if tables[2][i][0] == "99":
            color = "#FFFFFF"
          else:
            color = "#000000"
          data = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": tables[2][i][0],
                "size": "xxs",
                "color": color,
                "flex": 2,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "size": "xxs",
                "color": color,
                "flex": 8,
                "align": "center",
                "text": tables[2][i][2],
                "wrap": True,
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][3],
                "size": "xxs",
                "color": color,
                "flex": 3,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][4],
                "color": color,
                "flex": 3,
                "align": "center",
                "size": "xxs",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][5],
                "size": "xxs",
                "color": color,
                "flex": 4,
                "align": "center",
                "gravity": "center"
              }
            ]
          }
          columns1.append(data)

      for i in range(10, 20):
        if tables[2][i][0].isdigit() == True:
          if tables[2][i][0] == "99":
            color = "#FFFFFF"
          else:
            color = "#000000"
          data = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": tables[2][i][0],
                "size": "xxs",
                "color": color,
                "flex": 2,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "size": "xxs",
                "color": color,
                "flex": 8,
                "align": "center",
                "text": tables[2][i][2],
                "wrap": True,
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][3],
                "size": "xxs",
                "color": color,
                "flex": 3,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][4],
                "color": color,
                "flex": 3,
                "align": "center",
                "size": "xxs",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][5],
                "size": "xxs",
                "color": color,
                "flex": 4,
                "align": "center",
                "gravity": "center"
              }
            ]
          }
          columns2.append(data)

      for i in range(20, 30):
        if tables[2][i][0].isdigit() == True:
          if tables[2][i][0] == "99":
            color = "#FFFFFF"
          else:
            color = "#000000"
          data = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": tables[2][i][0],
                "size": "xxs",
                "color": color,
                "flex": 2,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "size": "xxs",
                "color": color,
                "flex": 8,
                "align": "center",
                "text": tables[2][i][2],
                "wrap": True,
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][3],
                "size": "xxs",
                "color": color,
                "flex": 3,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][4],
                "color": color,
                "flex": 3,
                "align": "center",
                "size": "xxs",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][5],
                "size": "xxs",
                "color": color,
                "flex": 4,
                "align": "center",
                "gravity": "center"
              }
            ]
          }
          columns3.append(data)

      for i in range(30, 40):
        if tables[2][i][0].isdigit() == True:
          if tables[2][i][0] == "99":
            color = "#FFFFFF"
          else:
            color = "#000000"
          data = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": tables[2][i][0],
                "size": "xxs",
                "color": color,
                "flex": 2,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "size": "xxs",
                "color": color,
                "flex": 8,
                "align": "center",
                "text": tables[2][i][2],
                "wrap": True,
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][3],
                "size": "xxs",
                "color": color,
                "flex": 3,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][4],
                "color": color,
                "flex": 3,
                "align": "center",
                "size": "xxs",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][5],
                "size": "xxs",
                "color": color,
                "flex": 4,
                "align": "center",
                "gravity": "center"
              }
            ]
          }
          columns4.append(data)

      for i in range(40, 50):
        if tables[2][i][0].isdigit() == True:
          if tables[2][i][0] == "99":
            color = "#FFFFFF"
          else:
            color = "#000000"
          data = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": tables[2][i][0],
                "size": "xxs",
                "color": color,
                "flex": 2,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "size": "xxs",
                "color": color,
                "flex": 8,
                "align": "center",
                "text": tables[2][i][2],
                "wrap": True,
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][3],
                "size": "xxs",
                "color": color,
                "flex": 3,
                "align": "center",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][4],
                "color": color,
                "flex": 3,
                "align": "center",
                "size": "xxs",
                "gravity": "center"
              },
              {
                "type": "text",
                "text": tables[2][i][5],
                "size": "xxs",
                "color": color,
                "flex": 4,
                "align": "center",
                "gravity": "center"
              }
            ]
          }
          columns5.append(data)

      carousel_template = {
        "type": "carousel",
        "contents": [
        {
          "type": "bubble",
          "size": "mega",
          "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TRANSKRIP",
                "size": "md",
                "color": "#FFFFFF",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": nim.upper(),
                "size": "sm",
                "color": "#ffffff66"
              }
            ]
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "NO",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 2,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "MATAKULIAH",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 8,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "NILAI",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS X BOBOT",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 4,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "sm",
                    "color": "#000000"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": columns1
                  }
                ]
              }
            ]
          },
          "styles": {
            "header": {
              "backgroundColor": "#11BBFF"
            },
            "footer": {
              "separator": True
            }
          }
        },
        {
          "type": "bubble",
          "size": "mega",
          "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TRANSKRIP",
                "size": "md",
                "color": "#FFFFFF",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": nim.upper(),
                "size": "sm",
                "color": "#ffffff66"
              }
            ]
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "NO",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 2,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "MATAKULIAH",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 8,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "NILAI",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS X BOBOT",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 4,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "sm",
                    "color": "#000000"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": columns2
                  }
                ]
              }
            ]
          },
          "styles": {
            "header": {
              "backgroundColor": "#11BBFF"
            },
            "footer": {
              "separator": True
            }
          }
        },
        {
          "type": "bubble",
          "size": "mega",
          "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TRANSKRIP",
                "size": "md",
                "color": "#FFFFFF",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": nim.upper(),
                "size": "sm",
                "color": "#ffffff66"
              }
            ]
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "NO",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 2,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "MATAKULIAH",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 8,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "NILAI",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS X BOBOT",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 4,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "sm",
                    "color": "#000000"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": columns3
                  }
                ]
              }
            ]
          },
          "styles": {
            "header": {
              "backgroundColor": "#11BBFF"
            },
            "footer": {
              "separator": True
            }
          }
        },
        {
          "type": "bubble",
          "size": "mega",
          "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TRANSKRIP",
                "size": "md",
                "color": "#FFFFFF",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": nim.upper(),
                "size": "sm",
                "color": "#ffffff66"
              }
            ]
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "NO",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 2,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "MATAKULIAH",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 8,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "NILAI",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS X BOBOT",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 4,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "sm",
                    "color": "#000000"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": columns4
                  }
                ]
              }
            ]
          },
          "styles": {
            "header": {
              "backgroundColor": "#11BBFF"
            },
            "footer": {
              "separator": True
            }
          }
        },
        {
          "type": "bubble",
          "size": "mega",
          "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "TRANSKRIP",
                "size": "md",
                "color": "#FFFFFF",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": nim.upper(),
                "size": "sm",
                "color": "#ffffff66"
              }
            ]
          },
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "NO",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 2,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "MATAKULIAH",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 8,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "NILAI",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 3,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      },
                      {
                        "type": "text",
                        "text": "SKS X BOBOT",
                        "size": "sm",
                        "color": "#000000",
                        "weight": "bold",
                        "flex": 4,
                        "align": "center",
                        "wrap": True,
                        "gravity": "center"
                      }
                    ]
                  },
                  {
                    "type": "separator",
                    "margin": "sm",
                    "color": "#000000"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": columns5
                  }
                ]
              }
            ]
          },
          "styles": {
            "header": {
              "backgroundColor": "#11BBFF"
            },
            "footer": {
              "separator": True
            }
          }
        }       
        ]
      }
      template_message = FlexSendMessage(
          alt_text='TRANSKRIP', contents=carousel_template)
      line_bot_api.reply_message(
          event.reply_token, [
              template_message])      

    def tagihan(event, user_name, nim, tahun_input, period_input):
      HEADERS = Req_Header.HEADERS
      NIM = nim.upper()
      URL_BASE = Endpoint.URL_TAGIHAN_DIMAS+NIM
      
      tahun = tahun_input
      tahun1 = int(tahun)+1
      period = period_input

      if period == "GANJIL":
        semester = "G1"
      elif period == "GENAP":
        semester = "G2"
      elif period == "SISIPAN":
        semester = "S1" 
      elif period == "TRIMESTER1":
        semester = "G1" 
      elif period == "TRIMESTER2":
        semester = "G2" 
      elif period == "TRIMESTER3":
        semester = "G3" 
      elif period == "TRIMESTER4":
        semester = "G4"
      else:
        semester = "G1" 

      dataPayload = {
        "th" : tahun,
        "uji": semester
      }

      temp = {
          "kode_mk" : [],
          "nama_mk" : [],
          "sks" : [],
          "kelas": [],
          "status": [],
          "jumlah":[],
          "total": ""
      }

      tableBotTemp = {
          "tagihan" : [],
          "jumlah": [],
          "total" : ""
      }


      session = requests.Session()
      resp = session.post(URL_BASE, data=dataPayload, headers=HEADERS).text
      soup = BeautifulSoup(resp, 'html.parser')
      tables = soup.findAll("table", {"cellspacing": 2,"cellpadding":2})
      tableTop = tables[0]
      tableBot = tables[1]

      trData = tableTop.findAll("tr")
      trDataBot = tableBot.findAll("tr")

      # DATA
      #======================================= PARSING TABLE BAGIAN ATAS ============================
      for i in range(1, len(trData)-1):
          temp['kode_mk'].append(trData[i].findAll("td")[0].text)
          temp['nama_mk'].append(trData[i].findAll("td")[1].text)
          temp['sks'].append(trData[i].findAll("td")[2].text)
          temp['kelas'].append(trData[i].findAll("td")[3].text)
          temp['status'].append(trData[i].findAll("td")[4].text)
          temp['jumlah'].append(prog._parseCurrency(trData[i].findAll("td")[5].text))

      total = prog._parseCurrency(trData[len(trData)-1].findAll("td")[1].text)
      temp['total'] = total
      #======================================= PARSING TABLE BAGIAN BAWAH ===========================
      for i in range(1, len(trDataBot)-1):
          tableBotTemp['tagihan'].append(trDataBot[i].findAll("td")[0].text)
          tableBotTemp['jumlah'].append(prog._parseCurrency(trDataBot[i].findAll("td")[1].text))

      totalBot = prog._parseCurrency(trDataBot[len(trDataBot)-1].findAll("td")[1].text)
      tableBotTemp['total'] = totalBot

      # STORE
      columns1 = []
      columns2 = []

      for i in range(len(temp['nama_mk'])):
        data = {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "text",
              "text": temp['nama_mk'][i],
              "size": "sm",
              "color": "#000000",
              "flex": 8,
              "align": "start",
              "wrap": True,
              "gravity": "center"
            },
            {
              "type": "text",
              "text": temp['sks'][i],
              "size": "sm",
              "color": "#000000",
              "flex": 3,
              "align": "center",
              "wrap": True,
              "gravity": "center"
            },
            {
              "type": "text",
              "text": temp['status'][i],
              "size": "sm",
              "color": "#000000",
              "flex": 5,
              "align": "center",
              "wrap": True,
              "gravity": "center"
            },
            {
              "type": "text",
              "text": prog.formatrupiah(temp['jumlah'][i]),
              "size": "sm",
              "color": "#000000",
              "flex": 6,
              "align": "center",
              "wrap": True,
              "gravity": "center"
            }
          ]
        }
        columns1.append(data)

      for i in range(len(tableBotTemp['tagihan'])):
        data = {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "text",
              "text": tableBotTemp['tagihan'][i],
              "size": "sm",
              "color": "#000000",
              "flex": 8,
              "align": "start",
              "wrap": True,
              "gravity": "center"
            },
            {
              "type": "text",
              "text": prog.formatrupiah(tableBotTemp['jumlah'][i]),
              "size": "sm",
              "color": "#000000",
              "flex": 6,
              "align": "end",
              "wrap": True,
              "gravity": "center"
            }
          ]
        }
        columns2.append(data)

      carousel_template = {
        "type": "carousel",
        "contents": [
          {
            "type": "bubble",
            "size": "mega",
            "header": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Tagihan SKS Tahun Ajaran "+tahun+"/"+str(tahun1)+" Semester "+period.capitalize(),
                  "size": "md",
                  "color": "#FFFFFF",
                  "weight": "bold",
                  "wrap": True
                },
                {
                  "type": "text",
                  "text": nim.upper(),
                  "size": "sm",
                  "color": "#ffffff66",
                  "wrap": True
                }
              ]
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "xxl",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "MATAKULIAH",
                          "size": "sm",
                          "color": "#000000",
                          "weight": "bold",
                          "flex": 8,
                          "align": "center",
                          "wrap": True,
                          "gravity": "center"
                        },
                        {
                          "type": "text",
                          "text": "SKS",
                          "size": "sm",
                          "color": "#000000",
                          "weight": "bold",
                          "flex": 3,
                          "align": "center",
                          "wrap": True,
                          "gravity": "center"
                        },
                        {
                          "type": "text",
                          "text": "STATUS",
                          "size": "sm",
                          "color": "#000000",
                          "weight": "bold",
                          "flex": 5,
                          "align": "center",
                          "wrap": True,
                          "gravity": "center"
                        },
                        {
                          "type": "text",
                          "text": "JUMLAH",
                          "size": "sm",
                          "color": "#000000",
                          "weight": "bold",
                          "flex": 6,
                          "align": "center",
                          "wrap": True,
                          "gravity": "center"
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "sm",
                      "color": "#000000"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": columns1
                    }
                  ]
                }
              ]
            },
            "footer": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Jumlah",
                      "size": "sm",
                      "color": "#000000",
                      "align": "start",
                      "wrap": True,
                      "gravity": "center"
                    },
                    {
                      "type": "text",
                      "text": prog.formatrupiah(temp['total']),
                      "size": "sm",
                      "color": "#000000",
                      "flex": 0,
                      "align": "end",
                      "wrap": True,
                      "gravity": "center"
                    }
                  ]
                }
              ]
            },
            "styles": {
              "header": {
                "backgroundColor": "#11BBFF"
              },
              "footer": {
                "separator": True
              }
            }
          },
          {
            "type": "bubble",
            "size": "mega",
            "header": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "Tagihan UKP Tahun Ajaran "+tahun+"/"+str(tahun1)+" Semester "+period.capitalize(),
                  "size": "md",
                  "color": "#FFFFFF",
                  "weight": "bold",
                  "wrap": True
                },
                {
                  "type": "text",
                  "text": nim.upper(),
                  "size": "sm",
                  "color": "#ffffff66",
                  "wrap": True
                }
              ]
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "xxl",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "horizontal",
                      "contents": [
                        {
                          "type": "text",
                          "text": "TAGIHAN",
                          "size": "sm",
                          "color": "#000000",
                          "weight": "bold",
                          "flex": 8,
                          "align": "center",
                          "wrap": True,
                          "gravity": "center"
                        },
                        {
                          "type": "text",
                          "text": "JUMLAH",
                          "size": "sm",
                          "color": "#000000",
                          "weight": "bold",
                          "flex": 6,
                          "align": "center",
                          "wrap": True,
                          "gravity": "center"
                        }
                      ]
                    },
                    {
                      "type": "separator",
                      "margin": "sm",
                      "color": "#000000"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": columns2
                    }
                  ]
                }
              ]
            },
            "footer": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "text",
                      "text": "Jumlah",
                      "size": "sm",
                      "color": "#000000",
                      "align": "start",
                      "wrap": True,
                      "gravity": "center"
                    },
                    {
                      "type": "text",
                      "text": prog.formatrupiah(tableBotTemp['total']),
                      "size": "sm",
                      "color": "#000000",
                      "flex": 0,
                      "align": "end",
                      "wrap": True,
                      "gravity": "center"
                    }
                  ]
                }
              ]
            },
            "styles": {
              "header": {
                "backgroundColor": "#11BBFF"
              },
              "footer": {
                "separator": True
              }
            }
          }
        ]
      }
      template_message = FlexSendMessage(
          alt_text='Tagihan', contents=carousel_template)
      line_bot_api.reply_message(
          event.reply_token, [
              template_message])

    def ipk_ips(event, user_name, nim):
      HEADERS = Req_Header.HEADERS
      NIM = nim.upper()
      URL_BASE = Endpoint.SINTAKID_URL_BASE+NIM
      URL_BAR = Endpoint.SINTAKID_URL_DATA_BAR_CHART
      URL_PIE = Endpoint.SINTAKID_URL_DATA_PIE_CHART
      
      session = requests.Session()
      resp = session.post(URL_BASE, headers=HEADERS)

      page = requests.get(URL_BASE)
      soup = BeautifulSoup(page.content, 'html.parser')

      # DATA
      raw_barchart = session.get(URL_BAR, headers=HEADERS).json()
      raw_piechart = session.get(URL_PIE, headers=HEADERS).json()
      raw_prediksi = soup.find("div", {"id": "prediksi"})
      prediksi = str(raw_prediksi).replace('<div class="alert alert-success alert-dismissable" id="prediksi"><a class="close" href="#predikat"><i class="fa fa-caret-down"></i></a>','').replace('</div>','')
      raw_predikat = soup.find("div", {"id": "predikat"})
      predikat = str(raw_predikat).replace('<br/>','').replace('\n','').replace('                      ','').replace('                    ','').replace('<div class="alert alert-info alert-dismissable" id="predikat">','').replace('<a class="close" href="#prediksi"><i class="fa fa-caret-up"></i></a>','').replace('</div>','')
      raw_ipk = soup.findAll("div", {"class": "huge"})
      ipk = str(raw_ipk[2]).replace('<div class="huge">','').replace('                                      ','').replace('                                    </div>','').replace('\n','')
      
      # STORE
      columns = []
      jumlah = []

      for i in range(len(raw_barchart[0]['data'])):
        progres_bar = (100/4)*raw_barchart[1]['data'][i]
        bar = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": raw_barchart[0]['data'][i],
                "size": "sm",
                "gravity": "center"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "filler"
                          }
                        ],
                        "width": str(progres_bar)+"%",
                        "height": "6px",
                        "backgroundColor": "#11BBFF",
                        "cornerRadius": "30px"
                      }
                    ],
                    "cornerRadius": "30px",
                    "height": "6px",
                    "backgroundColor": "#9FD8E36E",
                    "width": "130px"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "flex": 0
              },
              {
                "type": "text",
                "text": str(raw_barchart[1]['data'][i]),
                "gravity": "center",
                "flex": 0,
                "size": "sm"
              }
            ],
            "spacing": "sm",
            "cornerRadius": "30px",
            "margin": "sm"
          }
        columns.append(bar)

      for i in range(len(raw_piechart[0]['data'])):
        data = {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "text",
              "text": raw_piechart[0]['data'][i][0],
              "size": "sm",
              "color": "#555555",
              "flex": 0
            },
            {
              "type": "text",
              "text": str(raw_piechart[0]['data'][i][1]),
              "size": "sm",
              "color": "#111111",
              "align": "end"
            }
          ]
        }
        jumlah.append(data)

      carousel_template = {
        "type": "carousel",
        "contents": [
          {
            "type": "bubble",
            "header": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "IPK",
                  "size": "xl",
                  "color": "#FFFFFF",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": user_name,
                  "size": "md",
                  "color": "#ffffff66"
                }
              ],
              "backgroundColor": "#11BBFF"
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": ipk,
                  "size": "5xl",
                  "offsetTop": "20px",
                  "align": "center"
                }
              ]
            }
          },
          {
            "type": "bubble",
            "size": "mega",
            "header": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "GRAFIK IPS",
                  "size": "xl",
                  "color": "#FFFFFF",
                  "weight": "bold"
                },
                {
                  "type": "text",
                  "text": nim.upper(),
                  "size": "md",
                  "color": "#ffffff66"
                }
              ],
              "backgroundColor": "#11BBFF"
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": columns
            }
          },
          {
            "type": "bubble",
            "header": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "NILAI MAHASISWA",
                  "size": "xl",
                  "weight": "bold",
                  "color": "#FFFFFF"
                },
                {
                  "type": "text",
                  "text": nim.upper(),
                  "size": "md",
                  "color": "#ffffff66"
                }
              ],
              "backgroundColor": "#11BBFF"
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "xxl",
                  "spacing": "sm",
                  "contents": jumlah
                }
              ]
            },
            "styles": {
              "footer": {
                "separator": True
              }
            }
          },
          {
            "type": "bubble",
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "image",
                          "url": "https://vanika.tru.io/vanikabot/vanikaprofile.jpg",
                          "aspectMode": "cover",
                          "size": "full"
                        }
                      ],
                      "cornerRadius": "100px",
                      "width": "72px",
                      "height": "72px"
                    },
                    {
                      "type": "box",
                      "layout": "vertical",
                      "contents": [
                        {
                          "type": "text",
                          "contents": [
                            {
                              "type": "span",
                              "text": prediksi
                            }
                          ],
                          "size": "sm",
                          "wrap": True
                        },
                        {
                          "type": "separator"
                        },
                        {
                          "type": "text",
                          "contents": [
                            {
                              "type": "span",
                              "text": predikat
                            }
                          ],
                          "size": "sm",
                          "wrap": True
                        }
                      ],
                      "spacing": "md"
                    }
                  ],
                  "spacing": "xl",
                  "paddingAll": "20px"
                }
              ],
              "paddingAll": "0px"
            }
          }
        ]
      }
      template_message = FlexSendMessage(
          alt_text='IPK & IPS', contents=carousel_template)
      line_bot_api.reply_message(
          event.reply_token, [
              template_message])