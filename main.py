#import config file
from config import EM_Address, EM_Password, ACC_Server

#import gmail data
import imaplib
import email
from email.header import decode_header
import webbrowser
import os


#Connect to IMAP Server
mail = imaplib.IMAP4_SSL(ACC_Server, 993)
mail.login(EM_Address, EM_Password)

#Select Inbox
mail.select("INBOX")

#Searches through emails
type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.splits()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]

#converts byte literal to string
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

# download the attachments (if applicable)
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join('Users\berke\Desktop\VS Code Projects\WMCDiscordBot', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        
            subject = str(email_message).split("Subject: ", 1)
            [1].split("\nTo:", 1) [0]
            print ('Downloaded "{file}" from email titled "{subject}" with UID {uid}.'.format(file=fileName, subject=subject, uid=latest_email_uid.decode('utf-8')))

# print subject
for response_part in data:
        if isinstance(response_part, tuple) :
            msg = email.message_from_string(response_part[1].decode('utf-8'))
email.message_from_string(response_part[1].decode('utf-8'))
email_subject = msg['subject']
email_from = msg['from']
print ('From :' + email_from + '\n')
print ('Subject :' + email_subject + '\n')
print (msg.get_payload(decode=True))
