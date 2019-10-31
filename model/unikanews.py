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

# Unika News
# Menampilkan berita dari http://news.unika.ac.id/
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


class Unikanews:
    def unikanews(event):
        ENDPOINT = "http://news.unika.ac.id/?s="
        ENDPOINT_IKOM = "http://news.unika.ac.id/?s=ikom"

        url = urlreq.urlopen(urlreq.Request(ENDPOINT, headers={
                            'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
        udict = url.read().decode('utf-8')
        rawlink = re.findall('<h6><a href="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
        my_path = "/var/www/html/vanikabot/imagenews"
        columns = []
        for i in range(0, 4):
            url1 = urlreq.urlopen(urlreq.Request(rawlink[i], headers={'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
            udict1 = url1.read().decode('utf-8')
            rawtitels = re.findall('<h6><a href="'+rawlink[i]+'" rel="bookmark" title="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
            rawpublikasi = re.findall('<div class="meta">(.*?)<a', udict, re.DOTALL | re.IGNORECASE)
            publishDate_raw = rawpublikasi[0].replace("Publikasi tanggal ","").replace(" di ","").split(" ")
            publishDate = publishDate_raw[1].replace(",","")+" "+publishDate_raw[0]+" "+publishDate_raw[2]
            rawdes = re.findall('<p>(.*?)<a', udict, re.DOTALL | re.IGNORECASE)
            rawimg = re.findall('src="http://news.unika.ac.id/wp-content/uploads/(.*?)"', udict1, re.DOTALL | re.IGNORECASE)
            try:
                if ('.jpg' in rawimg[0]) or ('.png' in rawimg[0]):
                    linkimg = ["http://news.unika.ac.id/wp-content/uploads/"+rawimg[0]]
                else:
                    linkimg = ["https://vanika.tru.io/vanikabot/imagenews/tandatanya.jpg"]
            except:
                linkimg = ["https://vanika.tru.io/vanikabot/imagenews/tandatanya.jpg"]

            imagename = str(linkimg[0].replace("http://news.unika.ac.id/wp-content/uploads/","").replace("https://vanika.tru.io/vanikabot/imagenews/","").replace(".jpg","").replace(".png",""))
            urllib.request.urlretrieve(linkimg[0], os.path.join(my_path, os.path.basename(imagename+".png")))

            carousel_column = BubbleContainer(
                body=BoxComponent(
                    layout='vertical',
                    padding_all= '0px',
                    contents=[
                        ImageComponent(
                            url="https://vanika.tru.io/vanikabot/imagenews/"+imagename+".png",
                            size='full',
                            aspect_ratio='2:3',
                            aspect_mode='cover',
                            gravity='top',
                        ),
                        BoxComponent(
                            layout='vertical',
                            contents=[
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        #titile
                                        TextComponent(text=rawtitels[0], weight='bold',wrap=True, color='#ffffff', size='md'),
                                    ],
                                ),
                                BoxComponent(
                                    layout='baseline',
                                    contents=[
                                        # info
                                        TextComponent(text=rawdes[i][:50]+" ...", color='#ebebeb', size='xs', gravity='bottom', flex=0),
                                    ],
                                    spacing='lg',
                                ),
                                BoxComponent(
                                    layout='vertical',
                                    contents=[
                                        FillerComponent(),
                                        BoxComponent(
                                            layout='baseline',
                                            contents=[
                                                FillerComponent(),
                                                IconComponent(
                                                    url='https://vanika.tru.io/vanikabot/icon/discover.png'
                                                ),
                                                TextComponent(text='Selengkapnya', color='#ffffff', flex=0, offset_top='-2px'),
                                                FillerComponent(),
                                            ],
                                            spacing='sm',
                                        ),
                                        FillerComponent(),
                                    ],
                                    border_width='1px',
                                    corner_radius='4px',
                                    spacing='sm',
                                    border_color='#ffffff',
                                    margin='xxl',
                                    height='40px',
                                    action=URIAction(uri=rawlink[i], label='picture')
                                ),  
                            ],
                            position= 'absolute',
                            offset_bottom= '0px',
                            offset_start= '0px',
                            offset_end= '0px',
                            background_color= '#11BBFFaa',
                            padding_all= '20px',
                            padding_top= '18px',
                        ),
                        BoxComponent(
                            layout='vertical',
                            contents=[
                                TextComponent(text='UNIKA TODAY', align='start', color='#ffffff', size='md', offset_top='3px', weight='bold', style='normal'),
                                TextComponent(text=publishDate, color='#ffffff', size='sm'),
                            ],
                            position= 'absolute',
                            offset_top= '18px',
                            offset_start= '18px',
                            height= '100px',
                            width= '150px',
                        ),      
                    ],
                )
            )
            columns.append(carousel_column)

        carousel_template = CarouselContainer(contents=columns)
        template_message = FlexSendMessage(
            alt_text='UNIKA NEWS', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message])     