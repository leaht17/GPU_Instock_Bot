from __future__ import print_function

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import itertools
import time
from signal import signal, SIGINT
from random import randint
import psycopg2
import os
import twilio
from twilio.rest import Client
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.text import MIMEText
import base64
import copy
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# import config for the database and twilio values
import sys
sys.path.append(os.path.dirname(os.path.abspath('ScrapeQueryNotifierMicroservice/config.py')))
from config import config

RUNNING = True

# The list of Best Buy GPU URLs that will be checked for stock
URLS = [
        "https://www.bestbuy.com/site/pny-geforce-gt-710-2gb-pci-express-2-0-graphics-card-black/5092306.p?skuId=5092306", #this is our test url
        # "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440",
        # "https://www.bestbuy.com/site/pny-xlr8-gaming-single-fan-nvidia-geforce-gtx-1660-super-overclocked-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6407309.p?skuId=6407309",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-580-gts-black-edition-8gb-gddr5-pci-express-3-0-graphics-card-black/6092641.p?skuId=6092641",
        # "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3070-ventus-3x-oc-bv-8gb-gddr6-pci-express-4-0-graphics-card/6438278.p?skuId=6438278",
        # "https://www.bestbuy.com/site/asus-nvidia-geforce-tuf-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439128.p?skuId=6439128",
        # "https://www.bestbuy.com/site/asus-tuf-rtx3060ti-8gb-gddr6-pci-express-4-0-graphics-card/6452573.p?skuId=6452573",
        # "https://www.bestbuy.com/site/pny-geforce-gt1030-2gb-pci-e-3-0-graphics-card-black/5901353.p?skuId=5901353",
        # "https://www.bestbuy.com/site/xfx-speedster-merc319-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6457619.p?skuId=6457619",
        # "https://www.bestbuy.com/site/xfx-speedster-qick319-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6460664.p?skuId=6460664",
        # "https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402",
        # "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442",
        # "https://www.bestbuy.com/site/nvidia-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429434.p?skuId=6429434",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-eagle-8gb-gddr6-pci-express-4-0-graphics-card/6437912.p?skuId=6437912",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-gaming-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191",
        # "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454329.p?skuId=6454329",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432400.p?skuId=6432400",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6800xt-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6441226.p?skuId=6441226",
        # "https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-gray-black/6457624.p?skuId=6457624",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-black-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439300.p?skuId=6439300",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-black-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6432399.p?skuId=6432399",
        # "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-ftw3-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444444.p?skuId=6444444",
        # "https://www.bestbuy.com/site/asus-nvidia-geforce-gtx-1660-super-oc-edition-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6405063.p?skuId=6405063",
        # "https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6700-xt-eagle-12gb-gddr6-pci-express-4-0-gaming-graphics-card/6457994.p?skuId=6457994",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1650-4gb-gddr5-pci-express-3-0-graphics-card-black-gray/6409179.p?skuId=6409179",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-aorus-master-8gb-gddr6-pci-express-4-0-graphics-card/6439384.p?skuId=6439384",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3080-ftw3-ultra-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436196.p?skuId=6436196",
        # "https://www.bestbuy.com/site/msi-amd-radeon-rx-6800-xt-16g-16gb-gddr6-pci-express-4-0-graphics-card-black/6440913.p?skuId=6440913",
        # "https://www.bestbuy.com/site/asus-nvidia-geforce-rog-strix-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439127.p?skuId=6439127",
        # "https://www.bestbuy.com/site/asus-geforce-rtx-3090-24gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432447.p?skuId=6432447",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-eagle-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6430621.p?skuId=6430621",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-super-oc-edition-6gb-gddr6-pci-express-3-0-graphics-card-black/6409171.p?skuId=6409171",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3090-ftw3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6436192.p?skuId=6436192",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3070-ftw3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439301.p?skuId=6439301",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1650-super-oc-edition-4gb-gddr6-pci-express-3-0-graphics-card-black-gray/6409188.p?skuId=6409188",
        # "https://www.bestbuy.com/site/msi-amd-radeon-rx-5500-xt-8gb-gddr6-pci-express-4-0-graphics-card-black-gray/6397797.p?skuId=6397797",
        # "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-xc-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444445.p?skuId=6444445",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-aorus-master-10gb-gddr6x-pci-express-4-0-graphics-card/6436223.p?skuId=6436223",
        # "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454328.p?skuId=6454328",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-570-rs-black-edition-8gb-gddr5-pci-express-3-0-graphics-card-black-red/6202343.p?skuId=6202343",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6800-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6442077.p?skuId=6442077",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-6900-xt-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6444358.p?skuId=6444358",
        # "https://www.bestbuy.com/site/evga-super-sc-ultra-gaming-nvidia-geforce-gtx-1650-super-4gb-gddr6-pci-express-3-0-graphics-card-black-silver/6412939.p?skuId=6412939",
        # "https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-ti-ftw3-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6444449.p?skuId=6444449",
        # "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3080-ventus-3x-10g-oc-bv-gddr6x-pci-express-4-0-graphic-card-black-silver/6430175.p?skuId=6430175",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-gaming-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442484.p?skuId=6442484",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-vision-oc-8gb-gddr6-pci-express-4-0-graphics-card/6439385.p?skuId=6439385",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3080-xc3-gaming-10gb-gddr6-pci-express-4-0-graphics-card/6436194.p?skuId=6436194",
        # "https://www.bestbuy.com/site/asus-dual-geforce-rtx-2060-oc-edition-evo-6gb-gddr6-pci-express-3-0-graphic-card/6439463.p?skuId=6439463",
        # "https://www.bestbuy.com/site/asus-nvidia-geforce-rtx-3060-12gb-gddr6-pci-express-4-0-graphics-card-black/6460665.p?skuId=6460665",
        # "https://www.bestbuy.com/site/msi-amd-radeon-rx-6800-16g-16gb-gddr6-pci-express-4-0-graphics-card-black-black/6441020.p?skuId=6441020",
        # "https://www.bestbuy.com/site/msi-amd-radeon-rx-6900-xt-16g-gddr6-pci-express-4-0-graphics-card-black-silver/6444716.p?skuId=6444716",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3090-ftw3-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6436193.p?skuId=6436193",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-gaming-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6430620.p?skuId=6430620",
        # "https://www.bestbuy.com/site/pny-geforce-rtx-3060ti8gb-uprising-dual-fan-graphics-card/6446660.p?skuId=6446660",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gt-1030-2gb-gddr5-pci-express-3-0-graphics-card-black/6409183.p?skuId=6409183",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3080-vision-oc-10gb-gddr6x-pci-express-4-0-graphics-card/6436219.p?skuId=6436219",
        # "https://www.bestbuy.com/site/asus-tuf-rtx-3090-24gb-gddr6x-pci-express-4-0-graphics-card-black/6432446.p?skuId=6432446",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3070-gaming-oc-8gb-gddr6-pci-express-4-0-graphics-card/6437909.p?skuId=6437909",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6-pci-express-4-0-graphics-card/6434198.p?skuId=6434198",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-gaming-oc-12gb-gddr6-pci-express-4-0-graphics-card/6454688.p?skuId=6454688",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-5700-xt-raw-ii-8gb-gddr6-pci-express-4-0-graphics-card-with-zero-db-black/6375963.p?skuId=6375963",
        # "https://www.bestbuy.com/site/msi-nvidia-geforce-gtx-1650-super-4gb-gddr6-pci-express-3-0-graphics-card-black-gray/6397798.p?skuId=6397798",
        # "https://www.bestbuy.com/site/msi-mech-oc-amd-radeon-rx-5700-xt-8gb-gddr6-pci-express-4-0-graphics-card-black/6374966.p?skuId=6374966",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439299.p?skuId=6439299",
        # "https://www.bestbuy.com/site/msi-amd-radeon-rx-5600-xt-mech-oc-6gb-gddr6-pci-express-4-0-graphics-card-black/6430143.p?skuId=6430143",
        # "https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432655.p?skuId=6432655",
        # "https://www.bestbuy.com/site/evga-sc-ultra-gaming-nvidia-geforce-gtx-1660-ti-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6373500.p?skuId=6373500",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3090-aorus-master-24gb-gddr6x-pci-express-4-0-graphics-card/6437910.p?skuId=6437910",
        # "https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432658.p?skuId=6432658",
        # "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3060-ti-ventus-2x-oc-bv-8gb-gddr6-pci-express-4-0-graphics-card-black/6441172.p?skuId=6441172",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3060-ti-eagle-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6442485.p?skuId=6442485",
        # "https://www.bestbuy.com/site/pny-nvidia-geforce-rtx-3060-12gb-xlr8-gaming-revel-epic-x-rgb-dual-fan-graphics-card/6454319.p?skuId=6454319",
        # "https://www.bestbuy.com/site/msi-gaming-x-nvidia-geforce-gtx-1660-super-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6389333.p?skuId=6389333",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-oc-edition-6gb-gddr5-pci-express-3-0-graphics-card-black/6409181.p?skuId=6409181",
        # "https://www.bestbuy.com/site/evga-geforce-gt-710-2gb-single-slot-dual-dvi-graphics-card-black/5597203.p?skuId=5597203",
        # "https://www.bestbuy.com/site/xfx-merc-319-amd-radeon-rx-6800xt-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6442585.p?skuId=6442585",
        # "https://www.bestbuy.com/site/msi-geforce-gtx-1660-ti-gaming-x-6gb-gddr6-pci-express-3-0-graphics-card/6330461.p?skuId=6330461",
        # "https://www.bestbuy.com/site/xfx-speedster-merc319-amd-radeon-rx-6800-xt-core-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6453268.p?skuId=6453268",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-gtx-1660-ti-6gb-gddr6-pci-express-3-0-graphics-card-black-gray/6409180.p?skuId=6409180",
        # "https://www.bestbuy.com/site/xfx-speedster-merc319-amd-radeon-rx-6900-xt-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6449499.p?skuId=6449499",
        # "https://www.bestbuy.com/site/asus-tuf-gaming-nvidia-geforce-rtx-3060-12gb-gddr6-pci-express-4-0-graphics-card-black/6460666.p?skuId=6460666",
        # "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3060-ventus-3x-12g-oc-12gb-gddr6-pci-express-4-0-graphics-card-black/6452940.p?skuId=6452940",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3090-gaming-oc-24gb-gddr6x-pci-express-4-0-graphics-card/6430623.p?skuId=6430623",
        # "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3090-eagle-oc-24g-gddr6x-pci-express-4-0-graphics-card-black/6430624.p?skuId=6430624",
        # "https://www.bestbuy.com/site/pny-nvidia-geforce-rtx-3060-12gb-xlr8-gaming-revel-epic-x-rgb-single-fan-graphics-card/6454318.p?skuId=6454318",
        # "https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6800-xt-aorus-master-16gb-gddr6-pci-express-4-0-graphics-card/6453895.p?skuId=6453895",
        # "https://www.bestbuy.com/site/pny-geforce-rtx-3070-8gb-dual-fan-graphics-card/6432654.p?skuId=6432654",
        # "https://www.bestbuy.com/site/gigabyte-nvidia-geforce-rtx-3090-vision-24g-gddr6-pci-express-4-0-graphics-card/6445108.p?skuId=6445108",
        # "https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6800-xt-gaming-oc-16gb-gddr6-pci-express-4-0-graphics-card/6453896.p?skuId=6453896",
        # "https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6800-aorus-master-16gb-gddr6-pci-express-4-0-graphics-card/6453894.p?skuId=6453894",
        # "https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3090-ventus-3x-24g-oc-bv-24gb-gddr6x-pci-express-4-0-graphics-card-black-silver/6430215.p?skuId=6430215",
        # "https://www.bestbuy.com/site/xfx-speedster-merc319-amd-radeon-rx-6900-xt-ultra-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6445157.p?skuId=6445157",
        # "https://www.bestbuy.com/site/xfx-speedster-merc319-amd-radeon-rx-6800-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6444357.p?skuId=6444357",
        # "https://www.bestbuy.com/site/pny-geforce-rtx-3090-24gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432656.p?skuId=6432656",
        # "https://www.bestbuy.com/site/msi-amd-radeon-rx-6800-gaming-x-trio-16g-16gb-gddr6-pci-express-4-0-graphics-card/6447182.p?skuId=6447182",
        # "https://www.bestbuy.com/site/pny-geforce-rtx-3070-8gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432653.p?skuId=6432653",
        # "https://www.bestbuy.com/site/pny-xlr8-gaming-single-fan-nvidia-geforce-gtx-1650-super-overclocked-edition-4gb-gddr6-pci-express-3-0-graphics-card-black/6407305.p?skuId=6407305",
        # "https://www.bestbuy.com/site/msi-amd-radeon-rx-6700-xt-mech-2x-12g-oc-12gb-gddr6-pci-express-4-0-graphics-card-black/6457632.p?skuId=6457632",
        # "https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6700-xt-gaming-oc-12gb-gddr6-pci-express-4-0-gaming-graphics-card/6457993.p?skuId=6457993",
        # "https://www.bestbuy.com/site/xfx-speedster-qick319-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6457620.p?skuId=6457620",
        # "https://www.bestbuy.com/site/xfx-amd-radeon-rx-5600-xt-raw-ii-pro-6gb-gddr6-pci-express-4-0-graphics-card/6398005.p?skuId=6398005",
        # "https://www.bestbuy.com/site/evga-geforce-rtx-2080-xc-gaming-8gb-gddr6-pci-express-3-0-graphics-card-with-dual-hdb-fans-rgb-led/6290681.p?skuId=6290681",
        # "https://www.bestbuy.com/site/xfx-thicc-ii-pro-amd-radeon-rx-5500-xt-8gb-gddr6-pci-express-4-0-graphics-card-black/6395411.p?skuId=6395411",
        # "https://www.bestbuy.com/site/pny-geforce-rtx-3090-24gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432657.p?skuId=6432657",
        # "https://www.bestbuy.com/site/gigabyte-amd-radeon-rx-6800-gaming-oc-16gb-gddr6-pci-express-4-0-graphics-card/6453897.p?skuId=6453897",
        # "https://www.bestbuy.com/site/xfx-speedster-swft309-amd-radeon-rx-6700-xt-12gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6457626.p?skuId=6457626",
        # "https://www.bestbuy.com/site/xfx-speedster-qick-319-amd-radeon-rx-6800-16gb-gddr6-pci-express-4-0-gaming-graphics-card-black/6453267.p?skuId=6453267"
    ]

SCOPES = ['https://www.googleapis.com/auth/gmail.send']
# Global

# Email settings
GMAIL_USERNAME = "gpuinstockbot@gmail.com"
GMAIL_PASSWORD = "cse403group"
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

######################################################################################################
######################################################################################################

def handler(signal_received, frame):
    # Handle any cleanup here
    print('\nSIGINT or CTRL-C detected.')
    print('Cleaning up...')
    global RUNNING
    RUNNING = False

######################################################################################################
######################################################################################################

# Checks if the given GPU is in stock or not.
# args:
# - browser: Chrome webdriver.
# - url: Best Buy GPU URL to check for stock.
# returns:
# - True if the GPU of the URL passed in is in stock & the name of the GPU.
# - False otherwise.
def scraper(browser, url):
    global RUNNING
    try:
        print(f"Accessing: {url}...")

        browser.get(url)
        add_to_cart_btn = browser.find_element_by_class_name("add-to-cart-button")
        sku_title = browser.find_element_by_class_name("sku-title").text
        print(f"Product: {sku_title}")

        if add_to_cart_btn:
            status = add_to_cart_btn.text
            print(f"Status: {status}")

            if status != "Sold Out" and status != "Coming Soon" and status != "Unavailable Nearby": # GPU is in stock
                message = f"Item restocked: {sku_title}\n\nStatus: {status}\n\n"
                return True, message

            else: # GPU is not in stock
                return False, "Null"

    except Exception as e:
        # Print any error messages to stdout
        print(e)
        return False, "Null"

######################################################################################################
######################################################################################################

# Queries the database for users that are subscribed to a certain GPU.
# args:
# - url: URL associated with a Best Buy GPU.
# returns:
# - A list of emails and phone numbers from the db that were
#   linked to wanting to be notified about this specific GPU being in stock.
def query_module(url):
    """ query subscribers matching the url """
    conn = None
    list_of_emails = []
    list_of_phone_numbers = []

    try:
        # Initialize db stuff
        db_params = config('database.ini', 'database')
        conn = psycopg2.connect(database=db_params['database'], user=db_params['user'], password=db_params['password'], host=db_params['host'], port=db_params['port'])
        print("Database opened successfully")

        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Query the database and obtain data as Python objects
        # subscribers_subscriber: 3 columns: sub_id, email & phone
        # subscriptions_subscription: 3  columns: sus_id, gpu_id, sub_id
        # gpus_gpu: 3 columns: gpu_id, URL, alias (plain english name)
        psql_select_query = 'SELECT DISTINCT subscribers.email, subscribers.phone FROM gpus_gpu as gpus, subscribers_subscriber as subscribers, subscriptions_subscription as subscriptions WHERE subscriptions.sub_gpu_id = gpus.id AND subscriptions.sub_subscriber_id = subscribers.id AND gpus.url = \'' + url + '\';'
        cur.execute(psql_select_query)
        row = cur.fetchone() # returns tuple

        while row is not None:
            # checks if string is empty, users can opt out of either notifying method
            if len(row[0]) != 0: # checks if email is empty
                list_of_emails.append(copy.deepcopy(row[0]))

            if len(row[1]) != 0: # checks if phone_number is empty
                list_of_phone_numbers.append(copy.deepcopy(row[1]))

            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        if conn is not None:
            conn.close()

    return list_of_emails, list_of_phone_numbers

######################################################################################################
######################################################################################################

# Creates and sends a text message.
# args:
# - url: URL associated with a Best Buy GPU.
# - stock_message: Message containing the GPU sku_title and lets users know it's in stock.
# - client: Twilio Client.
# - phone_number: A phone number to send the in stock message to.
# - sender_phone_num: The phone number we're sending the message from.
def send_text(url, stock_message, client, phone_number, sender_phone_num = '+15005550006'):
    # A test number to set phone number to: +12532859052
    # Magic sender number for testing: +15005550006
    # Our live sender phone number: +16782632233

    print(phone_number + " __________ " +sender_phone_num)
    message = client.messages \
                    .create(
                         body= stock_message + "\n\n" + url,
                         from_= sender_phone_num,
                         to=phone_number
                     )
    print(message.sid)

######################################################################################################
######################################################################################################

# Send an email message.
# args:
# - user_id: User's email address. The special value "me" indicates the authenticated user.
# - message: Message to be sent
# - url: URL associated with a Best Buy GPU.
# - stock_message: A stock_message containing the GPU sku_title and letting them know it's in stock.
# returns:
# - Sent email message.
def send_email(url, stock_message, recipient_email):
    email_message = email_body(GMAIL_USERNAME, recipient_email, stock_message, url)

    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.ehlo()  # Can be omitted
        server.starttls()
        server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USERNAME, recipient_email, email_message.as_string())

# Creates an email message.
# args: 
# - gmail_username: Email address of sender (keep default).
# - recipient_email: Email addresss of recipient.
# - stock_message: Body text of email message.
# - url: URL for GPU.
# returns:
# - MIMEText email message.
def email_body(gmail_username, recipient_email, stock_message, url):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Item found to be in stock at BestBuy!"
    message["From"] = gmail_username
    message["To"] = recipient_email
    html = f"""\
    <html>
        <body>
        <p>
            Your item has been restocked at BestBuy<br><br>

            {stock_message}<br>

            <a href="{url}">{url}</a>
        </p>
        </body>
    </html>
    """

    # Attach message to email
    part1 = MIMEText(html, "html")
    message.attach(part1)
    return message


######################################################################################################
######################################################################################################

# Notifies emails and phone numbers of the gpu being in stock.
# args:
# - list_of_emails: Email addresses to notify.
# - list_of_phone_numbers: Phone numbers to notify.
# - url: The Best Buy URL to link within the message body.
# - stock_message: A stock message containing the GPU sku_title and letting them know it's in stock.
# - client: Twilio client.
# - test: Flag for testing.
def notifier_module(list_of_emails, list_of_phone_numbers, url, stock_message, client, test=False):
    # Loop through and send the emails
    for email in list_of_emails:
        send_email(url, stock_message, email)
    if test:
        # Loop through and send the text messages while using magic number for testing
        for phone_number in list_of_phone_numbers:
            send_text(url, stock_message, client, phone_number)
    else:
        # Get sender phone number from twilio ini file
        sender_phone_num = config('twilio.ini', 'twilio')['sender_phone_num']

        # Loop through and send the text messages
        for phone_number in list_of_phone_numbers:
            send_text(url, stock_message, client, phone_number, sender_phone_num)

######################################################################################################
######################################################################################################

def main():
    # Initialize scraper information
    global RUNNING
    headless = True

    # Selenium Chrome settings
    chromeOptions = Options()
    chromeOptions.headless = headless

    print("Opening browser...")
    browser = webdriver.Chrome(executable_path="./drivers/chromedriver_mac", options=chromeOptions)

    print("Running in background, first page may take longer to load than subsequent pages")
    print("Press CTRL-C to exit")

    # Populate a still_in_stock dictionary to keep track of what is in stock so we do not send
    # repeat emails and/or texts
    is_msg_for_gpu_sent_for_this_stock_cycle = {}
    for url in URLS:
        is_msg_for_gpu_sent_for_this_stock_cycle[url] = False

    # Initialize twilio
    # Your Account Sid and Auth Token from twilio.com/console and set the environment variables.
    # See http://twil.io/secure
    # account_sid = os.environ["AC9d5de46a73c27da46f9c0de98f668e20"]
    # auth_token = os.environ['0000ab4bffd746f96c75e19fe9a52079']

    twilio_params = config('twilio.ini', 'twilio')
    client = Client(twilio_params['account_sid'], twilio_params['auth_token'])

    # Loop through the URLS and check individually if each is in stock
    while RUNNING:
        for url in URLS:
            throttle = randint(7, 14) # This can partially help against being detected as a bot
            is_gpu_in_stock = False
            stock_message = "Null"

            try:
                is_gpu_in_stock, stock_message = scraper(browser, url)

            # I will need to refactor later to deal with cntrl + c behavior when the program is running,
            # i.e. instead of just a clean break, it will quickly print the remaining URL's before exiting.
            except Exception:
                pass

            # Only going to query and send email, text notifications if
            # 1. we have not already sent them a msg for this stock cycle
            #    (i.e. in stock, send msg, still in stock on next loop pass, don't send msg)
            # 2. the gpu is actually in stock for this specific URL
            if (not is_msg_for_gpu_sent_for_this_stock_cycle[url] and is_gpu_in_stock):

                list_of_emails, list_of_phone_numbers = query_module(url)

                # Send the messages to notify the users that this GPU is in stock
                notifier_module(list_of_emails, list_of_phone_numbers, url, stock_message, client)

                # Set to true so we know not to msg them multiple times for this stock cycle
                is_msg_for_gpu_sent_for_this_stock_cycle[url] = True

            # Set to false so we will know to send msg on the next stock cycle when GPU is in stock
            if (not is_gpu_in_stock):
                is_msg_for_gpu_sent_for_this_stock_cycle[url] = False

        if RUNNING:
                print(f"Sleeping for {throttle} seconds...")
                time.sleep(throttle)

    # Exit cleanly
    browser.stop_client()
    browser.quit()

######################################################################################################
######################################################################################################

if __name__ == "__main__":
    signal(SIGINT, handler)
    main()
    print("Program finished successfully!")
