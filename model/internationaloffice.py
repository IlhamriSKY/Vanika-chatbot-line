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

# Info international office
# Menampilkan Info international office dari http://io.unika.ac.id/category/information/announcements/
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


class Internationaloffice:
    def internationaloffice(event):    
        ENDPOINT = "http://io.unika.ac.id/category/information/announcements/"

        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        url = urlreq.urlopen(urlreq.Request(ENDPOINT, headers={
                            'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
        udict = url.read().decode('utf-8')
        rawlink = re.findall('<h4><a href="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
        my_path = "/var/www/html/vanikabot/io"
        columns = []
        for i in range(0, 4):
            url1 = urlreq.urlopen(urlreq.Request(rawlink[i], headers={'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
            udict1 = url1.read().decode('utf-8')
            rawtitels = re.findall('<h4><a href="'+rawlink[i]+'" rel="bookmark" title="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
            rawimg = re.findall('src="http://io.unika.ac.id/wp-content/uploads/(.*?)"', udict1, re.DOTALL | re.IGNORECASE)
            rawdes = re.findall('<div class="at-above-post-cat-page addthis_tool" data-url="'+rawlink[i]+'"></div>(.*?)<!-- AddThis Advanced Settings above via filter on get_the_excerpt -->', udict, re.DOTALL | re.IGNORECASE)
            des = [i.translate(non_bmp_map) for i in rawdes]
            try:
                if ('.jpg' in rawimg[0]) or ('.png' in rawimg[0]):
                    linkimg = ["http://io.unika.ac.id/wp-content/uploads/"+rawimg[0]]
                else:
                    linkimg = ["https://vanika.tru.io/vanikabot/tandatanya.jpg"]
            except:
                linkimg = ["https://vanika.tru.io/vanikabot/tandatanya.jpg"]

            imagename = str(linkimg[0].replace("http://io.unika.ac.id/wp-content/uploads/","").replace("https://vanika.tru.io/vanikabot/imagenews/","").replace(".jpg","").replace(".png",""))
            urllib.request.urlretrieve(linkimg[0], os.path.join(my_path, os.path.basename(imagename+".png")))

            carousel_column = BubbleContainer(
                direction='ltr',
                styles=BubbleStyle(footer=BlockStyle(
                    background_color="#11BBFF")),
                header=BoxComponent(
                    layout='vertical',
                    contents=[TextComponent(text="International Office", weight='bold', color="#11BBFF", size='sm', gravity='center', wrap=True),
                    ]
                    ),
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/io/"+imagename+".png",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/io/"+imagename+".png", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #titile
                        TextComponent(text=rawtitels[0], weight='bold', size='md', gravity='center', wrap=True),
                        # info
                        TextComponent(text=des[0][:50]+" ...",color="#aaaaaa", size='xs',  gravity='center', wrap=True),
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
                            action=URIAction(label='Detail', uri=rawlink[i])
                        ),
                    ]
                ),
            )
            columns.append(carousel_column)

        carousel_template = CarouselContainer(contents=columns)
        template_message = FlexSendMessage(
            alt_text='International Office', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message])