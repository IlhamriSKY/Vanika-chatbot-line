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

# Info Beasiswa
# Menampilkan Info beasiswa dari https://www.unika.ac.id/infobeasiswa/
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


class Beasiswa:
    def beasiswa(event):    
        ENDPOINT = "https://www.unika.ac.id/infobeasiswa/"
        url = urlreq.urlopen(urlreq.Request(ENDPOINT, headers={'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
        udict = url.read().decode('utf-8')
        rawurl = re.findall('<h2 class="postitle"><a href="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
        
        columns = []
        for i in range(0, 4):
            rawtitle = re.findall('<h2 class="postitle"><a href="'+rawurl[i]+'" title="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
            rawimg = re.findall('<img alt="'+rawtitle[0]+'" src="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
            try:
                if ('.jpg' in rawimg[0]) or ('.png' in rawimg[0]):
                    linkimg = [rawimg[0].replace("http","https")]
                else:
                    linkimg = ["https://vanika.tru.io/vanikabot/tandatanya.jpg"]
            except:
                linkimg = ["https://vanika.tru.io/vanikabot/tandatanya.jpg"]

            carousel_column = BubbleContainer(
                direction='ltr',
                styles=BubbleStyle(footer=BlockStyle(
                    background_color="#11BBFF")),
                header=BoxComponent(
                    layout='vertical',
                    contents=[TextComponent(text="INFO BEASISWA", weight='bold', color="#11BBFF", size='sm', gravity='center', wrap=True),
                    ]
                    ),
                hero=ImageComponent(
                    url=linkimg[0],
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri=linkimg[0], label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #titile
                        TextComponent(text=rawtitle[0], weight='bold', size='md', gravity='center', wrap=True),
                    ],
                ),
                footer=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        ButtonComponent(
                            style='primary',
                            color="#11BBFF",
                            height='sm',
                            action=URIAction(label='Detail', uri=rawurl[i])
                        ),
                    ]
                ),
            )
            columns.append(carousel_column)

        carousel_template = CarouselContainer(contents=columns)
        template_message = FlexSendMessage(
            alt_text='INFORMASI BEASISWA', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message])