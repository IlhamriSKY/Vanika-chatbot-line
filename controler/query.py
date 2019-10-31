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

# QUERY
# list QUERY vanika

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

""" SELECT """
class Select:
    def userid_db_all():
        QUERY = "SELECT `userid` FROM `userlist`"
        return(QUERY)
    def userid_db(user_id):
        QUERY = "SELECT userid FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def useremail_db(user_id):
        QUERY = "SELECT user_email FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def usertoken_db(user_id):
        QUERY = "SELECT usertoken FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def userstatusemail_db(user_id):
        QUERY = "SELECT email_status FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def useremail_db_google(user_id):
        QUERY = "SELECT email FROM `user_google` WHERE userid= '%s'" % (user_id)        
        return(QUERY)
    def userpasswd_db(user_id):
        QUERY = "SELECT userpasswd FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def useremail_status_db(user_id):
        QUERY = "SELECT email_status FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def usernick_db(user_id):
        QUERY = "SELECT username FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def userplace_db(user_id):
        QUERY = "SELECT userplace FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def userprivilege_db(user_id):
        QUERY = "SELECT userprivilege FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def userready_db(user_id):
        QUERY = "SELECT user_ready FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def userbiro_db(user_id):
        QUERY = "SELECT status_biro FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def user_statusjawab_db(user_id):
        QUERY = "SELECT statusjawab FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    def userpush_db(user_id):
        QUERY = "SELECT userpush FROM `userlist` WHERE userid= '%s'" % (user_id)
        return(QUERY)
    #Command
    def command_db(command):
        QUERY = "SELECT message FROM `command` WHERE command LIKE '%s'" % (command)
        return(QUERY)
    def userpush_db_command(command):
        QUERY = "SELECT count FROM `command` WHERE command= '%s'" % (command)
        return(QUERY)

class Insert:
    def userjoin(user_id,user_name,user_picture):
        QUERY = "INSERT INTO `userlist` (`no`, `userid`, `usertoken`, `user_email`, `userpasswd`, `email_status`, `username`, `usernick`, `userplace`, `userprivilege`, `user_ready`, `status_biro`, `statusjawab`, `userpush`, `user_pic`, `nilai_tabel`, `dateadd`) VALUES (NULL, '"+user_id+"', '0000', 'none', '0/0/0000', 'notverived', '"+user_name+"', 'none', 'none', 'user', 'yes', 'default', 'none', '0', '"+user_picture+"', '<table> <thead> <tr> <th>No</th> <th>Kode MK</th> <th>Mata Kuliah</th> <th>SKS</th> <th>Nilai</th> <th>SKS X Bobot</th> </tr> </thead> <tbody> <tr> <td> - </td> <td> - </td> <td> - </td> <td> - </td> <td> - </td> <td> - </td> </tr> </tfoot> </table>', current_timestamp());"
        return(QUERY)
    def usertext(user_id,user_name,text,status):
        QUERY = "INSERT INTO `usertext` (`id`, `userid`, `username`, `usermsg`, `status`, `createdate`) VALUES (NULL, '"+user_id+"', '"+user_name+"', '"+text+"', '"+status+"', CURRENT_TIMESTAMP);"
        return(QUERY)

class Update:
    def userpush(userpush_db,user_id):
        QUERY = "UPDATE `userlist` SET `userpush` = '"+userpush_db+"' WHERE `userlist`.`userid` = '"+user_id+"';"
        return(QUERY)
    def userpush_command(userpush_db_command,command):
        QUERY = "UPDATE `command` SET `count` = '"+userpush_db_command+"' WHERE `command`.`command` = '"+command+"';"
        return(QUERY)
    def userstatusjawab(status_jawab,user_id):
        QUERY = "UPDATE `userlist` SET `statusjawab` = '"+status_jawab+"' WHERE `userlist`.`userid` = '"+user_id+"';"
        return(QUERY)
    def userstatusemail(status_email,user_id):
        QUERY = "UPDATE `userlist` SET `email_status` = '"+status_email+"' WHERE `userlist`.`userid` = '"+user_id+"';"
        return(QUERY)
    def user_email(user_email,user_id):
        QUERY = "UPDATE `userlist` SET `user_email` = '"+user_email+"' WHERE `userlist`.`userid` = '"+user_id+"';"
        return(QUERY)
    def usertext_update(user_id,text,status):
        QUERY = "UPDATE `usertext` SET `status` = '"+status+"' WHERE `usertext`.`userid` = '"+user_id+"' AND `usertext`.`usermsg` = '"+text+"';"
        return(QUERY)    

class Delete:
    def userleave(user_id):
        QUERY = "DELETE FROM `userlist` WHERE `userlist`.`userid` = '"+user_id+"'"
        return(QUERY)