#import config file
from config import EM_Address, EM_Password

#import gmail data
import imaplib
import email
from email.header import decode_header
import webbrowser
import os


#Connect to IMAP Server
imap = imap.IMAP4_SSL("imap.google.com", 993)
imap.login(EM_Address, EM_Password)