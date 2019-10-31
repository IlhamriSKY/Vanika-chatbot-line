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

from __future__ import unicode_literals

""" BOT OOP """
# Database
from controler.config import Config
from controler.datasql import Database
from controler.query import Select, Insert, Update, Delete
from controler.endpoint import Endpoint, Req_Header
from controler.operation import prog
# Answer
from model.answer import Answer, Jurusan
# Logic
from model.unikanews import Unikanews
from model.internationaloffice import Internationaloffice
from model.beasiswa import Beasiswa
from model.lowongan import Lowongan
from model.sintakid import Sintak
from model.sendemail import Email

""" Modules """
# System Based
import errno
import os
import sys
import tempfile
import math
import random
import datetime
import time
import re
from datetime import timedelta
from datetime import datetime
from xml.etree import ElementTree
from random import randint

# UrlLib with version python
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

# Web Based
import requests
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# Server Based
import datetime
import feedparser
import binascii
import pymysql
import socket
import smtplib

# API
import googlemaps
from pyowm import OWM
from googletrans import Translator
import aiml

# Bot Based
from argparse import ArgumentParser
from flask import Flask, request, abort, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix

# Line SDK
# https://github.com/line/line-bot-sdk-python
from linebot.models import *

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
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

app = Flask(__name__)

# Debug Protocol
# app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)

# Get channel_secret and channel_access_token from your environment variable
# Token
channel_secret = Config.channel_secret
channel_access_token = Config.channel_access_token
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# My apis token
googleapitoken = Config.googleapitoken #from becatholic
owm_key_list = Config.owm_key
owmkey = random.choice(owm_key_list)
owm = OWM(API_key=owmkey,language='id') #open weather api openweather.com (limited)

# Google Translate URLS
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.id',
      'translate.google.co.jp',
    ])

# Tmp File
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

# function for create tmp dir for download content
def make_static_tmp_dir():
    try:
        os.makedirs(static_tmp_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
            pass
        else:
            raise

@app.route("/callback", methods=['POST'])
def callback():
    """ Get X-Line-Signature header value """
    global user_id, user_name, user_picture
    signature = request.headers['X-Line-Signature']
    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # Try to get user's id
    try:
        user_id = json.loads(body)["events"][0]["source"]["userId"]
    except:
        user_id = "-"
    # Try to get user's name
    try:
        user_name = line_bot_api.get_profile(user_id).display_name
    except:
        user_name = "someone"
    #try to get user's profile picture urls
    try:
        user_picture = line_bot_api.get_profile(user_id).picture_url
    except:
        user_picture = 'https://image.prntscr.com/image/t2BFLWxiRf2OJq_G4kKKtw.png'
    # handle webhook body
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@app.route("/test", methods=['GET'])
def test():
    return ('ok')

""" UNIKA NEWS """
@app.route("/unikatoday", methods=['GET'])
def unikatoday():
    try:
        ENDPOINT = "http://news.unika.ac.id/?s="

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
                    linkimg = ["https://vanika.tru.io/vanikabot/tandatanya.jpg"]
            except:
                linkimg = ["https://vanika.tru.io/vanikabot/tandatanya.jpg"]

            imagename = str(linkimg[0].replace("http://news.unika.ac.id/wp-content/uploads/","").replace("https://vanika.tru.io/vanikabot/imagenews/","").replace(".jpg","").replace(".png",""))
            urllib.request.urlretrieve(linkimg[0], os.path.join(my_path, os.path.basename(imagename+".png")))

            carousel_column = BubbleContainer(
                direction='ltr',
                styles=BubbleStyle(footer=BlockStyle(
                    background_color="#11BBFF")),
                header=BoxComponent(
                    layout='vertical',
                    contents=[
                        TextComponent(text="UNIKA TODAY", weight='bold', color="#11BBFF", size='sm', gravity='center', wrap=True),
                        TextComponent(text=publishDate, color="#aaaaaa", size='xs', gravity='center', wrap=True),
                    ]
                    ),
                hero=ImageComponent(
                    url="https://vanika.tru.io/vanikabot/imagenews/"+imagename+".png",
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri="https://vanika.tru.io/vanikabot/imagenews/"+imagename+".png", label='picture')
                ),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        #titile
                        TextComponent(text=rawtitels[0], weight='bold', size='md', gravity='center', wrap=True),
                        # info
                        TextComponent(text=rawdes[i][:50]+" ...",color="#aaaaaa", size='xs',  gravity='center', wrap=True),
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
            alt_text='UNIKA TODAY', contents=carousel_template)

        result = db.run_query(Select.userid_db_all(), user_name, user_id)
        userid_tosend = prog.split(result,150)
        for data in userid_tosend:
            line_bot_api.multicast(data, template_message)
        return('True')
    except:
        return('False')

def get_receiver_addr(event):
    """ Get the address (source of event) weather it's group or personal chat """
    # Enable calling from all functions and methods
    global address
    # If the event was sent from a group
    if isinstance(event.source, SourceGroup):
        address = event.source.group_id
    # If the event was sent from a chat room
    elif isinstance(event.source, SourceRoom):
        address = event.source.room_id
    # If the event was sent from a personal chat
    else:
        address = event.source.user_id
    return address

@handler.add(MessageEvent, message=(TextMessage, LocationMessage))
def handle_text_message(event):
    text = event.message.text
    textlow = event.message.text.lower()
    """ GET DATA FROM DATABASE """
    # Config
    db = Database(Config)
    # Query
    # This query will return array data
    userid_db_all = db.run_query(Select.userid_db_all(), user_name, user_id)
    userid_db = db.run_query(Select.userid_db(user_id), user_name, user_id)
    usertoken_db = db.run_query(Select.usertoken_db(user_id), user_name, user_id)
    useremail_db = db.run_query(Select.useremail_db(user_id), user_name, user_id)
    userstatusemail_db = db.run_query(Select.userstatusemail_db(user_id), user_name, user_id)
    userpasswd_db = db.run_query(Select.userpasswd_db(user_id), user_name, user_id)
    usernick_db = db.run_query(Select.usernick_db(user_id), user_name, user_id)
    userplace_db = db.run_query(Select.userplace_db(user_id), user_name, user_id)
    userprivilege_db = db.run_query(Select.userprivilege_db(user_id), user_name, user_id)
    userready_db = db.run_query(Select.userready_db(user_id), user_name, user_id)
    userbiro_db = db.run_query(Select.userbiro_db(user_id), user_name, user_id)
    user_statusjawab_db = db.run_query(Select.user_statusjawab_db(user_id), user_name, user_id)
    userpush_db = db.run_query(Select.userpush_db(user_id), user_name, user_id)

    """ TRAFFIC MONITOR """
    # Store data Usertext to database
    db.run_query(Insert.usertext(user_id, user_name, text, "yes"), user_name, user_id)
    # Store Count Userpush to database
    try:
        db.run_query(Update.userpush(str(userpush_db[0]+1),user_id), user_name, user_id)
    except:
        pass
    
    """ USER ADD CONTROL """
    if userid_db == []:
        if textlow == 'add':
            db.run_query(Insert.userjoin(user_id,user_name,user_picture), user_name, user_id)
        elif textlow == 'lanjutkan':
            db.run_query(Insert.userjoin(user_id,user_name,user_picture), user_name, user_id)
            Answer.menu(event)
        else:
            bubble = BubbleContainer(
                direction='ltr',
                hero=BoxComponent(),
                body=BoxComponent(
                    layout='vertical',
                    contents=[
                        # Title
                        TextComponent(text="Selamat datang di Vanika",
                                        weight='bold', size='md', gravity='center', wrap=True),
                        # Info
                        TextComponent(text='Hello, '+user_name+'\nSelamat datang di Vanika, tekan "Lanjutkan" untuk ngobrol dengan Vanika', color="#aaaaaa", size='xs',  gravity='center', wrap=True),
                        SeparatorComponent(),
                    ],
                ),
                footer=BoxComponent(
                    layout='horizontal',
                    spacing='sm',
                    contents=[
                        ButtonComponent(
                            style='primary',
                            color='#11BBFF',
                            height='sm',
                            action=MessageAction(
                                label='Lanjutkan', text='lanjutkan'),
                        ),
                    ]
                ),
            )
            message = FlexSendMessage(alt_text="Confirm", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token, [
                message
            ])
    elif userready_db[0] == 'yes':
        if user_statusjawab_db[0] == 'none':
            if textlow == "menu":
                Answer.menu(event)
            elif('!menumahasiswa' in text) or ('menu mahasiswa' in textlow):
                if useremail_db[0] == "none":
                    Answer.menu_login(event,user_name)                                                          
                else:
                    if userstatusemail_db[0] == "notverified":
                        db.run_query(Update.userstatusemail("verified",user_id), user_name, user_id)
                        Email.kirimEmail(useremail_db[0] , user_name, user_id)
                        Answer.menu_mahasiswa(event,user_name)
                    else:
                        Answer.menu_mahasiswa(event,user_name)

            ############################################################
            # MENU MAHASISWA
            ############################################################                                                                                         
            elif ('!profile' in text) or ('profile' in textlow):
                if userstatusemail_db[0] == "verified":
                    raw_nim = useremail_db[0].replace("@student.unika.ac.id","")
                    nim_tahun = raw_nim[0:2]
                    nim_jurusan = raw_nim[2:4]
                    nim_noutur = raw_nim[4:8]
                    nim = nim_tahun+nim_jurusan+nim_noutur
                    ENDPOINT = "http://sintak.unika.ac.id/id/filektm/"+nim.upper()+".jpg"
                    my_path = "/var/www/html/vanikabot/ktmweb"
                    urllib.request.urlretrieve(ENDPOINT, os.path.join(my_path, os.path.basename(nim.upper()+".jpg")))
                    data = {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "image",
                                "url": "https://vanika.tru.io/vanikabot/ktmweb/"+nim.upper()+".jpg",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "20:13",
                                "gravity": "center"
                            }
                            ],
                            "paddingAll": "0px"
                        }
                    }
                    template_message = FlexSendMessage(
                        alt_text='KTM', contents=data)
                    line_bot_api.reply_message(
                        event.reply_token, [
                            template_message])  
                else:
                       Answer.jawaban_login(event,user_name)

            elif("ipk" in textlow) or ("ips" in textlow):
                if userstatusemail_db[0] == "verified":
                    raw_nim = useremail_db[0].replace("@student.unika.ac.id","")
                    nim_tahun = raw_nim[0:2]
                    nim_jurusan = raw_nim[2:4]
                    nim_noutur = raw_nim[4:8]
                    nim = nim_tahun+"."+nim_jurusan+"."+nim_noutur
                    Sintak.ipk_ips(event,user_name,nim)
                else:
                    Answer.jawaban_login(event,user_name)
            
            elif("transkrip" in textlow):
                if userstatusemail_db[0] == "verified":
                    raw_nim = useremail_db[0].replace("@student.unika.ac.id","")
                    nim_tahun = raw_nim[0:2]
                    nim_jurusan = raw_nim[2:4]
                    nim_noutur = raw_nim[4:8]
                    nim = nim_tahun+"."+nim_jurusan+"."+nim_noutur
                    Sintak.transkrip(event,user_name,nim)
                else:
                    Answer.jawaban_login(event,user_name)
            
            elif("tagihan" in textlow):
                if userstatusemail_db[0] == "verified":
                    text_split = text.split(" ")
                    if len(text_split) == 3:
                        raw_nim = useremail_db[0].replace("@student.unika.ac.id","")
                        nim_tahun = raw_nim[0:2]
                        nim_jurusan = raw_nim[2:4]
                        nim_noutur = raw_nim[4:8]
                        nim = nim_tahun+"."+nim_jurusan+"."+nim_noutur
                        tahun = text_split[1]
                        period = text_split[2]
                        Sintak.tagihan(event,user_name,nim,tahun,period)
                    else:
                        raw_nim = useremail_db[0].replace("@student.unika.ac.id","")
                        nim_tahun = raw_nim[0:2]
                        Answer.tagihan_input_tahun(event,"20"+nim_tahun)

                else:
                    Answer.jawaban_login(event,user_name)

            elif("logout" in textlow):
                if userstatusemail_db[0] == "verified":
                    db.run_query(Update.userstatusemail("notverified",user_id), user_name, user_id)
                    db.run_query(Update.user_email("none",user_id), user_name, user_id)
                    Answer.menu(event)
                else:
                    Answer.jawaban_login(event,user_name)
            ############################################################
            # BIRO
            ############################################################
            elif ('!tanyabiro' in text) or ('tanya biro' in textlow):
                Answer.menu_biro(event)            
            elif ('Mahasiswa baru' == text):
                Answer.mahasiswa_baru(event)
            elif ('Akademik' == text):
                Answer.jawaban_biro(event,'Akademik',user_name)
            elif ('Keuangan' == text):
                Answer.jawaban_biro(event,'Keuangan',user_name)
            elif ('Pusat karir' == text):
                Answer.jawaban_biro(event,'Pusat Karir',user_name)
            elif ('Perpustakaan' == text):
                Answer.menu_perpustakaan(event, user_name)
            elif ("cari buku" == textlow):
                Answer.cari_buku(event)  
            elif ('Kemahasiswaan' == text):
                Answer.jawaban_biro(event,'Kemahasiswaan',user_name)   
            ############################################################
            # MAHASISWA BARU
            ############################################################
            elif ('!infoprodi' in text) or ('informasi prodi' in textlow) or ('info program studi' in textlow):
                Answer.info_prodi(event)
            elif ('!lokasi' in text) or ("map" in textlow):
                Answer.lokasi(event)
            elif ('!infokos' in text) or ('info kos' in textlow):
                Answer.infokos(event)
            elif ("!jadwalpendaftaran" in text) or ("jadwal pendaftaran" in textlow):
                Answer.buku_panduan(event,"Jadwal pendaftaran","12")
            elif ('!carapendaftaran' in text) or ('cara pendaftaran' in textlow):
                Answer.buku_panduan(event,"Prosedur pendaftaran","8")
            elif ("!biaya" in text) or ("biaya" in textlow):
                Answer.buku_panduan(event,"Biaya pendaftaran","20")
            elif ("!syarat" in text) or ("syarat pendaftaran" in textlow) or ('syarat kuliah di unika' in textlow):
                Answer.buku_panduan(event,"Syarat pendaftaran","6")
            elif ('!pembayaran' in text) or ("cara pembayaran" in textlow):
                Answer.pembayaran(event)
            elif ('!pengumuman' in text) or ('pengumuman' in textlow):
                Answer.pengumuman(event)
            elif ('!daftarulang' in text) or ('daftar ulang' in textlow):
                Answer.daftar_ulang(event)
            elif ('!pmb' in text) or ('pembekalan mahasiswa baru' in textlow):
                Answer.pmb(event)
            elif ('!hotline' in text) or ('hotline' in textlow) or ("nomor" in textlow):
                Answer.hotline(event)
            elif ('!email' in text) or ('email' in textlow):
                Answer.email(event)
            elif ('!admin' in text) or ('admin' in textlow):
                Answer.admin(event)       
            ############################################################
            # JURUSAN
            ############################################################
            # it's empty space
            ############################################################
            # CHAT
            ############################################################  
            elif ('baik' in textlow) or ('alhamdulillah' in textlow) or ('sangat baik' in textlow):
                line_bot_api.reply_message(
                    event.reply_token,
                        TextSendMessage(text="Puji tuhan \nSemoga harinya lancar kak "+user_name+" ?"))     
            ############################################################
            # WEB SCRAPING
            ############################################################
            elif ('!beasiswa' in text) or ('beasiswa' in textlow):
                Beasiswa.beasiswa(event)

            elif ('!lowongan' in text) or ('lowongan' in textlow):
                Lowongan.lowongan(event)

            elif ("!news" in text) or ("news" in textlow) or ('berita' in textlow):
                Unikanews.unikanews(event)

            elif ("!io" in text) or (textlow == "international office"):
                Internationaloffice.internationaloffice(event)

            elif ("cari buku" in textlow):
                buku = text[0:].split(" ",2)
                try:
                    ENDPOINT = "http://lib.unika.ac.id/index.php?keywords="+buku[2].lower().replace(" ","+")+"&search=Pencarian"
                    url = urlreq.urlopen(urlreq.Request(ENDPOINT, headers={'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
                    udict = url.read().decode('utf-8')
                    rawurl = re.findall('<div class="detail-list"><h4><a href="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
                    rawtitels = re.findall('citationLink" title="Citation for: (.*?)"', udict, re.DOTALL | re.IGNORECASE)
                    my_path = "/var/www/html/vanikabot/imageperpus"

                    columns = []
                    for i in range(0,5):
                        url = urlreq.urlopen(urlreq.Request("http://lib.unika.ac.id/"+rawurl[i], headers={'User-Agent': "Mozilla/5.0 (compatible; MSIE 5.01; Windows NT 5.0)"}))
                        udict = url.read().decode('utf-8')
                        rawimg = re.findall('<img itemprop="image" alt="Image of '+rawtitels[i]+'" src="(.*?)"', udict, re.DOTALL | re.IGNORECASE)
                        if rawimg == []:
                            rawimg = "https://vanika.tru.io/vanikabot/tandatanya.jpg"
                        else:
                            rawimg = "http://lib.unika.ac.id"+rawimg[0]

                        img = rawimg.replace("&amp;width=200","&width=500")

                        urllib.request.urlretrieve(img, os.path.join(my_path, os.path.basename(str(i)+".png")))

                        carousel_column = BubbleContainer(
                            direction='ltr',
                            styles=BubbleStyle(footer=BlockStyle(
                                background_color="#11BBFF")),
                            header=BoxComponent(
                                layout='vertical',
                                contents=[TextComponent(text="HASIL PENCARIAN", weight='bold', color="#11BBFF", size='sm', gravity='center', wrap=True),
                                ]
                                ),
                            hero=ImageComponent(
                                url="https://vanika.tru.io/vanikabot/imageperpus/"+str(i)+".png",
                                size='full',
                                aspect_ratio='20:13',
                                aspect_mode='cover',
                                action=URIAction(
                                    uri="https://vanika.tru.io/vanikabot/imageperpus/"+str(i)+".png", label='picture')
                            ),
                            body=BoxComponent(
                                layout='vertical',
                                contents=[
                                    #titile
                                    TextComponent(text=rawtitels[i], weight='bold', size='md', gravity='center', wrap=True),
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
                                        action=URIAction(label='Detail', uri="http://lib.unika.ac.id"+rawurl[i])
                                    ),
                                ]
                            ),
                        )
                        columns.append(carousel_column)

                    carousel_template = CarouselContainer(contents=columns)
                    template_message = FlexSendMessage(
                        alt_text='Daftar Buku', contents=carousel_template)
                    line_bot_api.reply_message(
                        event.reply_token, [
                            template_message,
                            TextSendMessage(text="Hasil lebih lengkap bisa kunjungi "+ENDPOINT)
                            ])
                except:
                    line_bot_api.reply_message(
                        event.reply_token, [
                            TextSendMessage(
                                text="Tidak ada hasil pencarian untuk "+text+"\nKunjungi situs perpustakaan di lib.unika.ac.id\n",
                                quick_reply=QuickReply(
                                    items=[
                                QuickReplyButton(
                                    action=MessageAction(label="Menu", text="Menu")),
                                ]))])
            ############################################################
            # AIML
            # GET DATA FROM aiml app and DATABASE COMMAND
            ############################################################            
            elif text == text:
                inputan = textlow.replace(" ", "%20")
                #FROM DATABASE
                command_from_db = db.run_query(Select.command_db(text), user_name, user_id)
                userpush_db_command = db.run_query(Select.userpush_db_command(text), user_name, user_id)
                if command_from_db == []:
                    #FROM AIML
                    try:#prm
                        aiml_unika = urlopen("http://app.unika.ac.id/bot/chatbot/conversation_start.php?convo_id="+user_id+"&format=json&bot_id=1&say="+inputan).read()
                    except:
                        bot_say = 'Semoga ke depannya akan selalu baik adanya...'
                    try:#baa
                        aiml_unika = urlopen("http://app.unika.ac.id/bot/chatbot/conversation_start.php?convo_id="+user_id+"&format=json&bot_id=3&say="+inputan).read()
                    except:
                        bot_say = 'Semoga ke depannya akan selalu baik adanya...'
                    try:#bak
                        aiml_unika = urlopen("http://app.unika.ac.id/bot/chatbot/conversation_start.php?convo_id="+user_id+"&format=json&bot_id=4&say="+inputan).read()
                    except:
                        bot_say = 'Semoga ke depannya akan selalu baik adanya...'
                    try:#aacc    
                        aiml_unika = urlopen("http://app.unika.ac.id/bot/chatbot/conversation_start.php?convo_id="+user_id+"&format=json&bot_id=6&say="+inputan).read()
                    except:
                        bot_say = 'Semoga ke depannya akan selalu baik adanya...'
                    try:#perpus    
                        aiml_unika = urlopen("http://app.unika.ac.id/bot/chatbot/conversation_start.php?convo_id="+user_id+"&format=json&bot_id=7&say="+inputan).read()
                    except:
                        bot_say = 'Semoga ke depannya akan selalu baik adanya...'
                    try:#kemahaiswaan    
                        aiml_unika = urlopen("http://app.unika.ac.id/bot/chatbot/conversation_start.php?convo_id="+user_id+"&format=json&bot_id=5&say="+inputan).read()
                    except:
                        bot_say = 'Semoga ke depannya akan selalu baik adanya...'

                    bot_say = json.loads(aiml_unika)['botsay']
                    if ('Semoga ke depannya akan selalu baik adanya...' in bot_say) or ('No answer' in bot_say):
                        Answer.else_message(event, user_name)
                        db.run_query(Update.usertext_update(user_id, text, "no"), user_name, user_id)
                    else:
                        line_bot_api.reply_message(
                            event.reply_token,
                                TextSendMessage(text=bot_say))
                else:
                    bot_say = command_from_db[0]
                    db.run_query(Update.userpush_command(str(userpush_db_command[0]+1),text), user_name, user_id)
                    line_bot_api.reply_message(
                        event.reply_token,
                            TextSendMessage(text=bot_say))
            else:
                Answer.else_message(event, user_name)
                db.run_query(Update.usertext_update(user_id, text, "no"), user_name, user_id)

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title='Location', address=event.message.address,
            latitude=event.message.latitude, longitude=event.message.longitude
        )
    )


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


# Other Message Type
@handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
def handle_content_message(event):
    if isinstance(event.message, ImageMessage):
        ext = 'jpg'
    elif isinstance(event.message, VideoMessage):
        ext = 'mp4'
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
    else:
        return

    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '.' + ext
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Save content.'),
            TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        ])


@handler.add(MessageEvent, message=FileMessage)
def handle_file_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix='file-', delete=False) as tf:
        for chunk in message_content.iter_content():
            tf.write(chunk)
        tempfile_path = tf.name

    dist_path = tempfile_path + '-' + event.message.file_name
    dist_name = os.path.basename(dist_path)
    os.rename(tempfile_path, dist_path)

    line_bot_api.reply_message(
        event.reply_token, [
            TextSendMessage(text='Save file.'),
            TextSendMessage(text=request.host_url + os.path.join('static', 'tmp', dist_name))
        ])


@handler.add(FollowEvent)
def handle_follow(event):
    try:
        user_picture = line_bot_api.get_profile(user_id).picture_url
    except:
        user_picture = 'https://image.prntscr.com/image/t2BFLWxiRf2OJq_G4kKKtw.png'

    if user_picture == None:
        user_picture = "https://vanika.tru.io/vanikabot/tandatanya.jpg" 
    else:
        user_picture = user_picture
        
    # INSERT DATA TO DATABASE
    """ config """
    db = Database(Config)
    """ query """
    db.run_query(Insert.userjoin(user_id,user_name,user_picture), user_name, user_id)
    """ log """
    app.logger.info("Got Follow event:" + event.source.user_id)
    """ answer """
    Answer.greeting_message(event,user_name)


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    # INSERT DATA TO DATABASE
    """ config """
    db = Database(Config)
    """ query """
    db.run_query(Delete.userleave(user_id), user_name, user_id)
    """ log """
    app.logger.info("Got Unfollow event:" + event.source.user_id)


@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Joined this ' + event.source.type))


@handler.add(LeaveEvent)
def handle_leave():
    app.logger.info("Got leave event")


@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'ping':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='pong'))
    elif event.postback.data == 'datetime_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
    elif event.postback.data == 'date_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['date']))


@handler.add(BeaconEvent)
def handle_beacon(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got beacon event. hwid={}, device_message(hex string)={}'.format(
                event.beacon.hwid, event.beacon.dm)))


@handler.add(MemberJoinedEvent)
def handle_member_joined(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got memberJoined event. event={}'.format(
                event)))


@handler.add(MemberLeftEvent)
def handle_member_left(event):
    app.logger.info("Got memberLeft event")


@app.route('/static/<path:path>')
def send_static_content(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=options.debug, port=options.port)