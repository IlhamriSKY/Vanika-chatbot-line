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

# ANSWER
# List jawaban vanika from .py files
from __future__ import unicode_literals

# Config token
from controler.config import Config

#logic
import random

#Date
import datetime

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError,
)

#list all
from linebot.models import *

#listed
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

import googlemaps
googleapitoken = "AIzaSyDD3MVhIuWKJLFi1xEcMF5VVa4RsenpV98"
# get channel_secret and channel_access_token from your environment variable
# Token
channel_secret = Config.channel_secret
channel_access_token = Config.channel_access_token
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

class Answer:
    def greeting_message(event,user_name):
        line_bot_api.reply_message(
            event.reply_token, [
                ImageSendMessage(original_content_url='https://vanika.tru.io/vanikabot/welcome.jpg',
                                    preview_image_url='https://vanika.tru.io/vanikabot/welcome.jpg'),
                TextSendMessage(
                    text="Hai selamat datang "+user_name+", perkenalkan saya VANIKA\nVirtual Assistant Universitas Katholik SOEGIJAPRANATA"),
                TextSendMessage(
                    text='Ketik "Menu" untuk melihat fitur Vanika',
                    quick_reply=QuickReply(
                        items=[
                    QuickReplyButton(
                        action=MessageAction(label="Menu", text="Menu")),]))
            ])

    def else_message(event,user_name):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text="Maaf Vanika belum mempunyai jawaban untuk pertanyaan kak "+user_name),
                TextSendMessage(
                    text='Ketik "Menu" untuk melihat fitur Vanika',
                    quick_reply=QuickReply(
                        items=[
                    QuickReplyButton(
                        action=MessageAction(label="Menu", text="Menu")),]))
            ])

    def menu(event):
        carousel_template = CarouselContainer(contents=[
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/mahasiswaunika.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/mahasiswaunika.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        SpacerComponent(size="xl"),
                        # info
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Sistem informasi akademik", color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/chat.png", flex=1),
                                TextComponent(
                                    text="Profile, Ipk & Ips, Transkrip, Tagihan, Notifikasi", color="#444444", size='sm',  gravity='center', flex=5, wrap=True),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            offset_bottom='10px',
                            action=MessageAction(
                                label='Menu Mahasiswa', text='Menu mahasiswa')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/birounika.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/birounika.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        SpacerComponent(size="xl"),
                        # info
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Fitur & pertanyaan Biro", color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/chat.png", flex=1),
                                TextComponent(
                                    text="Penerimaan Mahasiswa baru, Akademik, Keuangan, Perpustakaan, Kemahasiswaan, Pusat Karir", wrap=True, color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            offset_bottom='10px',
                            action=MessageAction(
                                label='Tanya Biro', text='Tanya Biro')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/beasiswa.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/beasiswa.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        SpacerComponent(size="xl"),
                        # info
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Informasi Beasiswa di Unika Soegijapranata", wrap=True, color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/chat.png", flex=1),
                                TextComponent(
                                    text="Pertanyaan detail bisa ditanyakan di Biro Kemahasiswaan", wrap=True, color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            offset_bottom='10px',
                            action=MessageAction(
                                label='Informasi Beasiswa', text='Informasi Beasiswa')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/lowongan.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/lowongan.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        SpacerComponent(size="xl"),
                        # info
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Informasi lowongan kerja untuk alumni Unika Soegijapranata", wrap=True, color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/chat.png", flex=1),
                                TextComponent(
                                    text="Pertanyaan detail bisa ditanyakan di Biro Pusat Karir", wrap=True, color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            offset_bottom='10px',
                            action=MessageAction(
                                label='Lowongan kerja', text='Lowongan kerja')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/unikanews.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/unikanews.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        SpacerComponent(size="xl"),
                        # info
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Berita Unika Soegijapranata", color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/chat.png", flex=1),
                                TextComponent(
                                    text="Update", color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            offset_bottom='10px',
                            action=MessageAction(
                                label='Daftar Berita', text='Unika News')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/io.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/io.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        SpacerComponent(size="xl"),
                        # info
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="International office news",wrap=True, color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/chat.png", flex=1),
                                TextComponent(
                                    text="You can get information about Student exchange and the latest news about International office",wrap=True, color="#444444", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            offset_bottom='10px',
                            action=MessageAction(
                                label='International Office', text='international office')
                        ),
                    ]
                ),
            ),
        ])
        template_message = FlexSendMessage(
            alt_text='Menu', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message
            ])

    def menu_mahasiswa(event, user_name):
        carousel_template = CarouselContainer(contents=[
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/profile.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/profile.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #title
                        TextComponent(text="Profile", weight='bold', size='sm', gravity='center', wrap=True),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Data Mahasiswa "+user_name, color="#aaaaaa", size='sm',  gravity='center', flex=5, wrap=True),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            action=MessageAction(
                                label='Profile', text='Profile')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/nilai.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/nilai.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #Titile
                        TextComponent(
                            text="Nilai Mahasiswa Unika", weight='bold', size='sm', gravity='center', wrap=True),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Nilai berupa Ipk, Ips dan Transkrip", color="#aaaaaa", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
                    ],
                ),
                footer=BoxComponent(
                    layout='horizontal',
                    spacing='sm',
                    contents=[
                        ButtonComponent(
                            style='primary',
                            color="#11BBFF",
                            height='sm',
                            action=MessageAction(
                                label='IPK & IPS', text='IPK dan IPS saya')
                        ),
                        ButtonComponent(
                            style='secondary',
                            height='sm',
                            action=MessageAction(
                                label='Transkrip', text='Transkrip')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/tagihan.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/tagihan.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #title
                        TextComponent(text="Tagihan Mahasiswa Unika",weight='bold', size='sm', gravity='center', wrap=True),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Tagihan SKS dan UKP", wrap=True, color="#aaaaaa", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            action=MessageAction(
                                label='Tagihan', text='Tagihan')
                        ),
                    ]
                ),
            ),
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/logout.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/logout.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #title
                        TextComponent(text="Logout",weight='bold', size='sm', gravity='center', wrap=True),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text="Keluar dari fitur Mahasiswa", wrap=True, color="#aaaaaa", size='sm',  gravity='center', flex=5),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            action=MessageAction(
                                label='Logout', text='Logout')
                        ),
                    ]
                ),
            ),
        ])
        template_message = FlexSendMessage(
            alt_text='Menu Fitur Mahasiswa', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message
            ])

    def menu_login(event, username):
        carousel_template = CarouselContainer(contents=[
            BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/mahasiswaunika.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/mahasiswaunika.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #title
                        TextComponent(text="Google Login", weight='bold', size='sm', gravity='center', wrap=True),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text='Login menggunakan akun mahasiswa kak '+username, color="#aaaaaa", size='sm',  gravity='center', flex=5, wrap=True),
                            ]
                        ),
                        SpacerComponent(size="xl"),
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
                            action=URIAction(uri="line://app/1576996487-M635zJRA", label='Login')
                        ),
                    ]
                ),
            )
        ])
        template_message = FlexSendMessage(
            alt_text='Login', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="Silahkan login terlebih dahulu kemudian tekan tombol 'menu mahasiswa'"),
                template_message])    

    def menu_biro(event):
        message = ImagemapSendMessage(
            base_url = 'https://vanika.tru.io/vanikabot/imagemap/menu/',
            alt_text = 'Menu',
            base_size = BaseSize(height=1040, width=1040),
            actions=[
                MessageImagemapAction(
                    text='menu',
                    area=ImagemapArea(
                        x = 719, y = 4, width = 297, height = 102)),
                MessageImagemapAction(
                    text='Mahasiswa baru',
                    area=ImagemapArea(
                        x = 113, y = 155, width = 249, height = 334)),
                MessageImagemapAction(
                    text='Akademik',
                    area=ImagemapArea(
                        x = 385, y = 155, width = 249, height = 334)),
                MessageImagemapAction(
                    text='Keuangan',
                    area=ImagemapArea(
                        x = 704, y = 155, width = 249, height = 334)),
                MessageImagemapAction(
                    text='Perpustakaan',
                    area=ImagemapArea(
                        x = 96, y = 574, width = 249, height = 334)),
                MessageImagemapAction(
                    text='Kemahasiswaan',
                    area=ImagemapArea(
                        x = 417, y = 574, width = 249, height = 334)),
                MessageImagemapAction(
                    text='Pusat karir',
                    area=ImagemapArea(
                        x = 735, y = 574, width = 249, height = 334))
                ])
        line_bot_api.reply_message(
            event.reply_token, [
            TextSendMessage(text="Pilih menu dibawah untuk mendapatkan informasi biro "),
            message])

    def menu_perpustakaan(event, username):
        data = {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Working Hours",
                        "weight": "bold",
                        "color": "#11BBFF",
                        "size": "sm"
                    },
                    {
                        "type": "text",
                        "text": "PERPUSTAKAAN",
                        "weight": "bold",
                        "size": "xxl",
                        "margin": "md"
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
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
                                "text": "Senin",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "8:00 am - 17:30 pm",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Selasa",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "8:00 am - 17:30 pm",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Rabu",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "8:00 am - 17:30 pm",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Kamis",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "8:00 am - 17:30 pm",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Jumat",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "8:00 am - 11:30 pm",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "13:30 am - 15:30 pm",
                                    "size": "sm",
                                    "color": "#111111",
                                    "align": "end"
                                }
                                ]
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Sabtu",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "Closed",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Minggu",
                                "size": "sm",
                                "color": "#555555",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "Closed",
                                "size": "sm",
                                "color": "#111111",
                                "align": "end"
                            }
                            ]
                        }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "Keterangan",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "wrap": True,
                                "text": "Jumat minggu pertama tutup untuk pembenahan koleksi.",
                                "size": "xs",
                                "color": "#aaaaaa",
                                "align": "end"
                            }
                            ]
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
                "hero": {
                    "type": "image",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "url": "https://vanika.tru.io/vanikabot/menu/perpustakaan.jpg"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "Fitur Perpustakaan",
                        "wrap": True,
                        "weight": "bold",
                        "size": "md"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                        {
                            "type": "text",
                            "text": "Pilih menu dibawah",
                            "wrap": True,
                            "weight": "regular",
                            "size": "sm",
                            "flex": 0
                        }
                        ]
                    }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "button",
                        "style": "primary",
                        "action": {
                        "type": "message",
                        "label": "Cari Buku",
                        "text": "Cari buku"
                        },
                        "color": "#11BBFF"
                    }
                    ]
                }
                }
            ]
            }
        template_message = FlexSendMessage(
            alt_text='Menu Perpustakaan', contents=data)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message,
                TextSendMessage(
                    text='Maaf jika Vanika belum mempunyai jawaban tentang pertanyaan kak '+username),
                TextSendMessage(
                    text='Ada yang bisa dibantu mengenai biro Perpustakaan Unika?')
                ])

    def beasiswa(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Beasiswa di Unika Soegijapranata'
                ),
                TextSendMessage(
                    text='1. Beasiswa Bidik Misi\n2. Beasiswa Sandjojo\n3. Beasiswa PPA\n4. Beasiswa Unggulan\n5. Beasiswa Djarum Foundation\n6. Beasiswa AA Rahmat\n7. Beasiswa VDMI\n8. Beasiswa Yayasan Salim\n9. Beasiswa Yayasan Hidup Bahagia\n10. Beasiswa Paroki'
                )
            ])

    def mahasiswa_baru(event):
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='Pilih menu dibawah', title='Info Kuliah', thumbnail_image_url='https://vanika.tru.io/vanikabot/menu/prm.jpg', actions=[
                MessageAction(
                    label='Info Program Studi', text='Tampilkan informasi prodi'),
                MessageAction(
                    label='Lokasi kampus', text='Map kampus'),
                MessageAction(
                    label='Kos & Dormitory', text='Info kos sekitar unika dong')
            ]),
            CarouselColumn(text='Pilih menu dibawah', title='Informasi Pendaftaran', thumbnail_image_url='https://vanika.tru.io/vanikabot/menu/prm.jpg', actions=[
                MessageAction(
                    label='Jadwal Pendaftaran', text='Tampilkan jadwal pendaftaran'),
                MessageAction(
                    label='Cara Pendaftaran', text='Tampilkan cara pendaftaran'),
                MessageAction(label='Biaya', text='Biaya')
            ]),
            CarouselColumn(text='Pilih menu dibawah', title='Pendaftaran', thumbnail_image_url='https://vanika.tru.io/vanikabot/menu/prm.jpg', actions=[
                MessageAction(
                    label='Syarat', text='Syarat pendaftaran'),
                URIAction(
                    label='Formulir',
                    uri='https://pmb.unika.ac.id'),
                MessageAction(
                    label='Pembayaran', text='Cara pembayaran')
            ]),
            CarouselColumn(text='Pilih menu dibawah', title='Pendaftaran', thumbnail_image_url='https://vanika.tru.io/vanikabot/menu/prm.jpg', actions=[
                MessageAction(
                    label='Pengumuman', text='Pengumuman'),
                MessageAction(
                    label='Daftar Ulang', text='Daftar ulang'),
                MessageAction(
                    label='PMB', text='Pembekalan Mahasiswa baru')
            ]),
            CarouselColumn(text='Pilih menu dibawah', title='Hubungi Kami', thumbnail_image_url='https://vanika.tru.io/vanikabot/menu/prm.jpg', actions=[
                MessageAction(
                    label='Hotline', text='Hotline unika'),
                URIAction(
                    label='Line@',
                    uri='https://line.me/R/ti/p/@gvy5809f'),
                MessageAction(
                    label='Email', text='Email unika')
            ])
        ])
        template_message = TemplateSendMessage(
            alt_text='Menu Mahasiswa Baru', template=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text="Hai kak..Salam kenal..Vanika siap berikan informasi yang ingin kakak ketahui seputar PMB Unika SOEGIJAPRANATA"),
                template_message])

    def jawaban_biro(event,biro,user_name):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Maaf jika Vanika belum mempunyai jawaban tentang pertanyaan kak '+user_name),
                TextSendMessage(
                    text='Ada yang bisa dibantu mengenai biro '+biro+' Unika?')
                ])

    def cari_buku(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Ketik "cari buku(spasi)judul buku"\n\ncontoh:\ncari buku Etika Dan Filsafat Komunikasi')
                ])

    def jawaban_login(event, user_name):
         line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Silahkan login dengan email student kak '+user_name, 
                    quick_reply=QuickReply(
                        items=[
                    QuickReplyButton(
                        action=MessageAction(label="Menu Mahasiswa", text="Menu Mahasiswa")),]))
                ])       
    
    ###
    # MAHASISWA BARU
    ###

    def info_prodi(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text='Informasi program studi atau jurusan yang ada di Unika SOEGIJAPRANATA bisa kakak dapatkan di http://www.unika.ac.id/buku-informasi-program/'),
                TextSendMessage(text='Atau ketik program studi yang di inginkan\ncontoh "Sistem Infromasi"')
                ])
    def lokasi(event):
        nama_lokasi = 'Soegijapranata Catholic University'
        gmaps = googlemaps.Client(key='AIzaSyAVNFVvQH2RQ-pxCGblvSCgDraipzHFS1c')
        geocode_result = gmaps.geocode(nama_lokasi)
        gecode_alamatlokasi = geocode_result[0]['formatted_address']
        gecode_lat = geocode_result[0]['geometry']['location']['lat']
        gecode_lng = geocode_result[0]['geometry']['location']['lng']
        line_bot_api.reply_message(
            event.reply_token,
            LocationSendMessage(
                title='Klik untuk melihat lokasi', address='Jl. Pawiyatan Luhur IV No.1, Semarang, Jawa Tengah',
                latitude=gecode_lat, longitude=gecode_lng
            ))
    def infokos(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Unika SOEGIJAPRANATA menyediakan dormitory (asrama) khusus mahasiswi yang berasal dari luar kota dan luar pulau. Fasilitas apa saja yang ingin diketahui, bisa langsung cek http://www.unika.ac.id/accomodation/')
            ])

    def buku_panduan(event,panduan,halaman):
        carousel_template = CarouselContainer(contents=[
            BubbleContainer(
                direction='ltr',
                styles=BubbleStyle(footer=BlockStyle(
                    background_color="#af3bc6")),
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/menu/bukupanduan2020.jpg",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/menu/bukupanduan2020.jpg", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #title
                        TextComponent(text=panduan, weight='bold', size='sm', gravity='center', wrap=True),
                        BoxComponent(
                            layout="baseline",
                            spacing="xl",
                            contents=[
                                IconComponent(
                                    size='sm',  gravity='center',  url="https://vanika.tru.io/vanikabot/icon/plane.png", flex=1),
                                TextComponent(
                                    text='Informasi mengenai '+panduan+' berada pada halaman '+halaman, color="#aaaaaa", size='sm',  gravity='center', flex=5, wrap=True),
                            ]
                        ),
                        SpacerComponent(size="xl"),
                    ],
                ),
                footer=BoxComponent(
                    layout='vertical',
                    spacing='sm',
                    contents=[
                        ButtonComponent(
                            style='primary',
                            color="#af3bc6",
                            height='sm',
                            action=URIAction(uri="line://app/1576996487-ZxYaXoVL", label='Buku Panduan')
                        ),
                    ]
                ),
            )
        ])
        template_message = FlexSendMessage(
            alt_text='Buku Panduan', contents=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                template_message])


    def pembayaran(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='🔖 Pembayaran Formulir Pendaftaran\n\n'+
                    'Pembayaran dapat dilakukan melalui\n'+
                    '📌 Bank Maybank Indonesia Nomor Rekening 2-575-000071 a.n Yayasan Sandjojo.\n'+
                    '📌 Bank Jateng Nomor Rekening 1034024061 a.n Yayasan Sandjojo.\n'
                    '📌 Bank Jateng Nomor Virtual Account 11344023XXXXXXXX (8 digit nomor tes/registrasi pendaftaran)\n'),
                TextSendMessage(
                    text='🔖 Pembayaran Kuliah\n\n'+
                    'Setelah dinyatakan lolos seleksi, camaba diwajibkan melakukan pembayaran biaya studi.\n\nPembayaran dapat dilakukan secara langsung ke Bank Maybank Indonesia kantor Kas Unika SOEGIJAPRANATA atau bank manapun sesuai domisili masing-masing pendaftar dengan jumlah nominal & nomor Virtual Account (VA) yang tercantum pada surat ketetpan diterima yang diunduh melalui https://pmb.unika.ac.id'),
                ])

    def pengumuman(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='📢 Pengumuman hasil seleksi baik JALUR PRESTASI, JALUR ANTARA dan JALUR REGULER\ndapat diakses dan berkas ketetapan diterima diunduh melalui pmb.unika.ac.id (Klik PENGUMUMAN) selanjutnya LOGIN menggunakan Nomor Registrasi/Tes dan Tanggal Lahir atau Nama dan Tanggal Lahir.')
                ])

    def daftar_ulang(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='📝 Proses Daftar Ulang Calon Mahasiswa Baru dilakukan secara Online, dengan langkah-langkah sebagai berikut'),
                TextSendMessage(
                    text='1. Tes buta warna wajib bagi calon mahasiswa yang lulus seleksi di program studi Arsitektur, Desain Komunikasi Visual, Teknologi Pangan, Nutrisi dan Teknologi Kuliner, Teknik Elektro, Teknologi Energi, Psikologi yang dapat dilakukan di Poliklinik Unika SOEGIJAPRANATA (bebas biaya) atau dokter kota asal calon mahasiswa.\n\n'+
                    '2. Pembayaran ke bank sesuai yang tercantum dalam ketetapan pembayaran (pembayaran dengan Virtual Account).\n\n'+
                    '3. Calon mahasiswa yang telah melakukan pembayaran melalui Virtual Account, minimal dalam 2 (dua) hari akan mendapatkan Nomor Induk Mahasiswa (NIM) dan diinformasikan melalui email calon mahasiswa baru sesuai pada data formulir pendaftaran.\n\n'+
                    '4. Melakukan daftar ulang pada sintak.unika.ac.id dengan User Login: nim@student.unika.ac.id & Password: nimunika\nContoh:\nNIM= 18.P1.0001 maka User login= 18p10001@student.unika.ac.id dan Password= 18p10001unika\n\n'+
                    '📌 Catatan: Saat login, NIM diketik tanpa titik dan huruf dikonversi menjadi huruf kecil'),
                TextSendMessage(
                    text='a. Mengupdate data calon mahasiswa.\n\n'+
                    'b. Mengunggah foto (berwarna) dan hasil tes buta warna (untuk program studi yang telah ditentukan).\n\n'+
                    'c. Menyetujui surat pernyataan dengan cara di klik.\n\n'+
                    'd. Memilih ukuran jas almamater yang telah ditetapkan.\n\n'+
                    'e. Setelah melakukan poin a, b, c, d calon mahasiswa dapat mencetak Bukti Registrasi (Daftar Ulang).\n\n'+
                    'f. Kartu Keluarga (KK), Kartu Tanda Penduduk (KTP) dan Ijazah diunggah setelah kelulusan SMA/SMK.\n\n'+
                    'g. Calon mahasiswa yang telah mengunggah ijazah kelulusan akan mendapat verifikasi dari Biro Administrasi Akademik (BAA), selanjutnya dapat mencetak Kartu Tanda Mahasiswa (KTM) sementara.')
                ])
        
    def pmb(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Silahkan install aplikasi Unika Menyapa untuk mendapatkan info kegiatan Pembekalan Mahasiswa Baru https://play.google.com/store/apps/details?id=com.unika.menyapa'),
                ])

    def hotline(event):
        carousel_template = CarouselTemplate(columns=[
            CarouselColumn(text='Admin Unika', title='Hotline', actions=[
                URIAction(label='WhatsApp', uri='https://api.whatsapp.com/send?phone=6285727284162&text=Admin,saya_mau_tanya%20'),
            ])
        ])
        template_message = TemplateSendMessage(
            alt_text='Hotline', template=carousel_template)
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text="📱 No Telp (024) 8505003 ext. 1428, 1429, 1478"),
                template_message
        ])

    def email(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='📧 Email : promosi@unika.ac.id\n\n'+
                    '📧 Email : reg@unika.ac.id'
                    )
                ])

    def admin(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='📱 Untuk berbicara langsung ke staf admin, klik aja line.me/R/ti/p/%40gvy5809f'
                )
            ])

    ###
    # TAGIHAN
    ###
    def tagihan_input_tahun(event,nim_tahun):
        now = datetime.datetime.now()
        years = []
        period = ['GANJIL', 'GENAP']
        for i in reversed(range(int(nim_tahun), now.year+1)):
            period_random = random.choice(period)
            data = QuickReplyButton(action=MessageAction(label=str(i)+" "+period_random, text="Tagihan "+str(i)+" "+period_random))
            years.append(data)
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Ketik "Tagihan(spasi)Tahun(spasi)Period"\n\nContoh\nTagihan 2019 GANJIL\nTagihan 2018 SISIPAN\nTagihan 2017 TRIMESTER3\n\nAtau Tab contoh dibawah',
                    quick_reply=QuickReply(
                        items=years))
            ])
    def tagihan_input_period(event):
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(
                    text='Tab period di bawah',
                    quick_reply=QuickReply(
                        items=[
                            QuickReplyButton(action=MessageAction(label="GANJIL", text="GANJIL")),
                            QuickReplyButton(action=MessageAction(label="GENAP", text="GENAP")),
                            QuickReplyButton(action=MessageAction(label="SISIPAN", text="SISIPAN")),
                            QuickReplyButton(action=MessageAction(label="TRIMESTER1", text="TRIMESTER1")),
                            QuickReplyButton(action=MessageAction(label="TRIMESTER2", text="TRIMESTER2")),
                            QuickReplyButton(action=MessageAction(label="TRIMESTER3", text="TRIMESTER3")),
                            QuickReplyButton(action=MessageAction(label="TRIMESTER4", text="TRIMESTER4"))
                        ]))
            ])

    ###
    # JURUSAN
    ###
class Jurusan:
    def gt(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika ada program S-1 Game Technology, kak. Di sana kakak bisa belajar tentang pengembangan game dari sejak non-programming sampai dengan pemrograman tingkat tinggi. Ada pelajaran kewirausahaan dan bisnis untuk mendorong lulusannya mengembangkan start-up sendiri"))
    def si(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Sistem Informasi, kak. Di sana kakak bisa belajar mengenai pemanfaatan dan pengembangan teknologi informasi untuk kepentingan bisnis. Dengan begitu, lulusannya mempunyai keahlian dasar dalam pemrograman, disamping logika bisnis untuk menjembatani kebutuhan sistem di dunia bisnis."))
    def ecommerce(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika membuka program S-1 E-Commerce Technology, kak. Di sana kakak akan mempelajari pengembangan bisnis di dunia digital termasuk mengembangkan sistem yang dapat mendukungnya."))
    def ilmu_lingkungan(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S2 Lingkungan dan Perkotaan serta program S3 Ilmu Lingkungan. Kalau kakak punya fokus pada lingkungan saat ini dan daya dukungnya, silahkan bergabung setelah lulus S1 atau S2"))
    def perkotaan(event):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Unika punya program S2 Lingkungan dan Perkotaan. Kalau kakak punya fokus pada lingkungan saat ini dan daya dukungnya, silahkan bergabung setelah lulus S1"))
    def wirausaha(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Pada hampir semua program studi yang ada di Unika Soegijapranata ada kurikulum tentang kewirausahaan, terutama dalam program S1 Englishpreneurship, S1 E-Commerce Technology, dan S1 Manajemen"))
    def kewirausahaan(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Pada hampir semua program studi yang ada di Unika Soegijapranata ada kurikulum tentang kewirausahaan, terutama dalam program S1 Englishpreneurship, S1 E-Commerce Technology, dan S1 Manajemen"))
    def informatika(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Teknik Informatika, kak. Di sana kakak bisa belajar mengenai dasar logika dan algoritma, bahasa pemrograman, manajemen basis data, sistem informasi komputer hingga jaringan komputer dan pengembangan aplikasi berbasis web/platform khusus"))
    def komunikasi(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Komunikasi, kak. Di sana kakak bisa belajar  mempelajari bagaimana menyampaikan pesan atau berita secara efisien dan efektif dalam bidang periklanan, linguistik, bahasa, jurnalistik dengan pemanfaatan teknologi yang ada. Lulusan jurusan komunikasi akan bekerja di bidang-bidang seperti broadcasting, wartawan, editor, public relations, periklanan, manajemen media, komunikasi pemasaran, komunikasi bisnis, dan sejenisnya"))    
    def hukum(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Ilmu Hukum, kak. Di sana kakak bisa belajar bagaimana cara berpikir dengan logika secara tepat dan benar untuk mengimplementasikan hukum atau perundang-undangan yang berlaku di Indonesia. Selain belajar teori ada juga kuliah praktiknya, seperti simulasi sidang."))    
    def pangan(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S1 dan S2 Teknologi Pangan, kak. Di sana kakak bisa belajar mengenai pengetahuan dan teknologi pemanfaatan maupun pengolahan sumber pangan termasuk bagaimana menjamin keamanannya. Orientasi bidang ini mempelajari Mikrobiologi Pangan dan Bioteknologi, Rekayasa Pengolahan Pangan serta Mutu dan Keamanan Pangan."))
    def nutrisi(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Nutrisi dan Teknologi Kuliner, kak. Di sana kakak bisa belajar mengenai seni kuliner, nutrisi dan ilmu pangan yang terkait dengan pengembangan produk, manajemen bisnis (kewirausahaan) dan teknologi pengolahan serta regulasi pangan sehingga  produk pangan bernilai estetika tinggi dan sehat untuk dikonsumsi")) 
    def kuliner(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Nutrisi dan Teknologi Kuliner, kak. Di sana kakak bisa belajar mengenai teknik pengolahan pangan/pengembangan produk mulai dari persiapan hingga siap dikonsumsi dengan keamanan mutu produk akhir, manajemen bisnis, serta wawasan kewirausahaan")) 
    def sastra(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Sastra Inggris di bawah Fakultas Bahasa dan Seni, kak. Di sana kakak bisa belajar memperdalam kemampuan dalam berbahasa Inggris (lisan dan tulisan), mempelajari sejarah dan budaya negara, mengkaji ilmu sastra meliputi gejala sosial dan budaya yang terdapat dalam sebuah karya sastra (prosa, novel, puisi, dongeng, drama, film, atau lagu baik dalam bentuk tertulis atau bentuk pertunjukkan) serta membahas linguistik berbagai macam teks mulai dari karya sastra, teks pidato, artikel berita, lirik lagu, hingga transkrip serial televisi, iklan, dan film"))
    def inggris(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Sastra Inggris di bawah Fakultas Bahasa dan Seni, kak. Di sana kakak bisa belajar memperdalam kemampuan dalam berbahasa Inggris (lisan dan tulisan), mempelajari sejarah dan budaya negara, mengkaji ilmu sastra meliputi gejala sosial dan budaya yang terdapat dalam sebuah karya sastra (prosa, novel, puisi, dongeng, drama, film, atau lagu baik dalam bentuk tertulis atau bentuk pertunjukkan) serta membahas linguistik berbagai macam teks mulai dari karya sastra, teks pidato, artikel berita, lirik lagu, hingga transkrip serial televisi, iklan, dan film"))  
    def englishpreneurship(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Sastra Inggris di bawah Fakultas Bahasa dan Seni, kak. Di sana kakak bisa belajar memperdalam kemampuan dalam berbahasa Inggris (lisan dan tulisan), mempelajari sejarah dan budaya negara, mengkaji ilmu sastra meliputi gejala sosial dan budaya yang terdapat dalam sebuah karya sastra (prosa, novel, puisi, dongeng, drama, film, atau lagu baik dalam bentuk tertulis atau bentuk pertunjukkan) serta membahas linguistik berbagai macam teks mulai dari karya sastra, teks pidato, artikel berita, lirik lagu, hingga transkrip serial televisi, iklan, dan film. Selain itu kakak akan dibekali ilmu bisnis wirausaha yang akan menjadikan seorang enterpreneur"))
    def arts(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Digital Performing Arts di bawah Fakultas Bahasa dan Seni, kak. Fokus program ini pada karya seni pertunjukan (performing arts) yang memanfaatkan teknologi digital. Selain lulusan akan fasih berbahasa Inggris sekaligus terampil menghasilkan karya seni pertunjukan yang berbasis teknologi digital dengan didukung mata kuliah Public Speaking, Storytelling and Story Writing, Script Writing, maupun Subtitling."))   
    def performing(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Digital Performing Arts di bawah Fakultas Bahasa dan Seni, kak. Fokus program ini pada karya seni pertunjukan (performing arts) yang memanfaatkan teknologi digital. Selain lulusan akan fasih berbahasa Inggris sekaligus terampil menghasilkan karya seni pertunjukan yang berbasis teknologi digital dengan didukung mata kuliah Public Speaking, Storytelling and Story Writing, Script Writing, maupun Subtitling."))   
    def desain(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Desain Komunikasi Visual (DKV), kak. Di sana kakak akan mempelajari bagaimana mengkomunikasikan gambar dengan baik seperti estetika, pengolahan bentuk, warna secara 2Dimensi maupun 3Dimensi dengan dilengkapi fasilitas lab komputer, lab fotografi dan studi desain untuk mendukung perkuliahan"))
    def visual(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Desain Komunikasi Visual (DKV), kak. Di sana kakak akan mempelajari bagaimana mengkomunikasikan gambar dengan baik seperti estetika, pengolahan bentuk, warna secara 2Dimensi maupun 3Dimensi dengan dilengkapi fasilitas lab komputer, lab fotografi dan studi desain untuk mendukung perkuliahan"))    
    def arsitektur(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S1 dan S2 Arsitektur, kak. Di sana kakak tidak hanya belajar merancang bangunan/ menggambar saja tapi juga wawasan kewirausahaan, pengembangan eco-arsitektur pada konsep-konsep pembangunan sehingga mampu menganalisis dan memecahkan permasalahan arsitektur dengan memperhatikan segala aspek yang ada"))    
    def sipil(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Teknik Sipil, kak. Di sana kakak akan mempelajari bagaimana cara membuat struktur bangunan  yang kokoh dan ekonomis dengan mempertimbangkan berbagai faktor seperti fungsi bangunan, keamanan dan ketahanan bangunan, anggaran dan faktor lainnya. Selain mendalami ilmu struktur bangunan juga manajemen konstruksi, geoteknik, transportasi, hidrologi"))
    def elektro(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Teknik Elektro, kak. Di sana kakak akan mempelajari ilmu-ilmu dasar untuk rekayasa dan pemanfaatan gejala-gejala alam terutama sifat-sifat elektron (kelistrikan) yang kemudian diaplikasikan dalam sebuah teknologi dengan fokus pada pengembangan kompetensi di bidang aplikasi industri (teknologi konverter, mesin listrik, instrumentasi industri, otomasi industri) dan robotik mekatronik (robotik, pemrograman visual, pemrograman perangkat keras, sistem multimedia dll)"))  
    def energi(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S-1 Teknologi Energi, kak. Di sana kakak Di sana kakak akan mempelajari kompetensi ekplorasi terkait gejala/fenomena alam, pengembangan teknologi konverter, strategi kendali, analisis dan pengelolaan energi yang ramah lingkungan dan dapat diperbaharui."))  
    def psikologi(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S1 dan S2 Psikologi, kak. Di sana kakak bisa belajar mengenai seluruh aspek ilmu psikologi seperti filosofi dasar pengelompokan kepribadian, masalah-masalah kejiwaan dan cara penanganannya, perkembangan manusia dari lahir sampai tua. Setelah lulus S1 Psikologi, kakak bisa melanjutkan studi S2 Sains Psikologi atau S2 Profesi Psikologi dengan pilihan bidang mayor seperti PsikologiKlinis Dewasa, Psikologi Klinis Anak, Psikologi Industri dan Organisasi, Psikologi Pendidikan"))  
    def manajemen(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S1 dan S2 Manajemen, kak. Di sana kakak tidak hanya belajar mengupas dasar Ilmu Ekonomi dan Manajemen saja tapi juga membahas ilmu yang mendukung Sistem Informasi Manajemen, Komunikasi Bisnis hingga pada mata kuliah konsentrasi seperti Manajemen Pemasaran Kreatif, Manajemen Operasi Terintegrasi, Manajemen Strategi dan Pengembangan SDM, Manajemen Kewirausahaan serta Manajemen Keuangan dan Investasi. Begitu lulus S1 Manajemen, kakak bisa melanjutkan S2 Manajemen dengan pilihan konsentrasi yang dapat disesuaikan dengan peminatan."))                   
    def akuntansi(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program S1 dan S2 Akuntansi, kak. Di sana kakak bisa belajar mengenai siklus akuntansi, proses pembuatan laporan keuangan, serta analisis pada laporan keuangan hingga pada mata kuliah konsentrasi seperti  Akuntansi Keuangan (pasar modal), Akuntansi Manajemen (financial planning), Sistem Informasi (analysis system) dan Audit (fraud dan forensic audit)"))
    def pajak(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program D3 Perpajakan, kak. Di sana kakak bisa belajar memahami dan menguasai peraturan perpajakan yang berlaku serta mampu menghitung, menyetor, dan melaporkan segala jenis pajak dalam berbagai bidang usaha. Lama studi hanya 3 tahun (110 SKS)."))  
    def perpajakan(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Unika punya program D3 Perpajakan, kak. Di sana kakak bisa belajar memahami dan menguasai peraturan perpajakan yang berlaku serta mampu menghitung, menyetor, dan melaporkan segala jenis pajak dalam berbagai bidang usaha. Lama studi hanya 3 tahun (110 SKS)."))
    def aksi(event):
        line_bot_api.reply_message(
            event.reply_token,
                TextSendMessage(text="Merupakan program 2 gelar S1 yang ditempuh dalam waktu 5,5 tahun. Disini kakak bisa belajar ilmu akuntansi yang terkait sistem informasi yang dirancang, diimplementasikan guna mendapatkan informasi yang lebih akurat sehingga meningkatkan kualitas pengambilan keputusan"))                                                  
                                