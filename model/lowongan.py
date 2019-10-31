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

# Info Lowongan Kerja
# Menampilkan Info Lowongan Kerja dari http://www.unika.ac.id/sscc/category/pengumuman/
from __future__ import unicode_literals

# Config token
from controler.config import Config

# Web based
import requests
import json
import os
import sys
import re

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


class Lowongan:
    def lowongan(event):    
        ENDPOINT = "http://www.unika.ac.id/sscc/category/pengumuman/"
        url = urlreq.urlopen(urlreq.Request(ENDPOINT, headers={'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
        udict = url.read().decode('utf-8')
        rawtitels = re.findall('<h4><a href="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
        rawimg = re.findall('<img class="img-responsive" src="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
        
        my_path = "/var/www/html/vanikabot/imagelowongan"
        columns = []
        for i in range(0, 4):
            rawlinks = re.findall('<h4><a href="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
            rawimgs = re.findall('<img class="img-responsive" src="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
            rawtitels = re.findall('<a href="'+rawlinks[i+1]+'">(.*?)</a>', udict, re.DOTALL | re.IGNORECASE)

            urllib.request.urlretrieve(rawimgs[i], os.path.join(my_path, os.path.basename(str(i)+".png")))

            data = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://vanika.tru.io/vanikabot/imagelowongan/"+str(i)+".png",
                        "size": "full",
                        "aspectMode": "cover",
                        "aspectRatio": "1:1",
                        "gravity": "center"
                    },
                    {
                        "type": "image",
                        "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip15.png",
                        "position": "absolute",
                        "aspectMode": "fit",
                        "aspectRatio": "1:1",
                        "offsetTop": "0px",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "size": "full"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": rawtitels[0],
                                    "wrap": True,
                                    "size": "xl",
                                    "color": "#ffffff"
                                    
                                }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "Tab gambar untuk memperbesar",
                                    "color": "#a9a9a9"
                                }
                                ],
                                "spacing": "xs"
                            }
                            ],
                            "spacing": "xs"
                        }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "paddingAll": "20px"
                    }
                    ],
                    "paddingAll": "0px",
                    "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://vanika.tru.io/vanikabot/imagelowongan/"+str(i)+".png"
                    }
                }
                }
            columns.append(data)

        carousel_template = {
            "type": "carousel",
            "contents": columns
        }
        template_message = FlexSendMessage(
            alt_text='Lowongan Kerja', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message])