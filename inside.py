#data-user-id == unique id

#UI modules
import sys

from functools import partial
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#crolling modules
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PyQt5.QtCore import *

import urllib.request
import urllib.parse
import requests
import webbrowser

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

searchinglist=[]
searchedlist=[]

class Worker(QObject):

    sig_class = pyqtSignal(str,int,int)

    def __init__(self, parent = None):
        super(self.__class__, self).__init__(parent)

    @pyqtSlot(str)
    def conductCrolling(self, text):
        j = 0
        searchingHtml = urlopen('https://www.twitter.com/{}/media'.format(text))
        searchingsoup = BeautifulSoup(searchingHtml, "html.parser")
        searchingres = searchingsoup.find_all("div",{'data-element-context':'platform_photo_card'})

        for n in searchingres:
            searchinglist.append(n['data-image-url'])
            #print('{}'.format(n['data-image-url']))
            self.sig_class.emit(n['data-image-url'],j,0)
            inputURL = "https://www.google.co.kr/searchbyimage?site=search&image_url={}".format(n['data-image-url'])
            searchedHtml = requests.get(inputURL, headers=headers)
            searchedHtml = searchedHtml.text
            searchedsoup = BeautifulSoup(searchedHtml, "html.parser")
            searchedres = searchedsoup.find_all("div",{'class':'r'})
            if len(searchedres) != 0:
                for o in searchedres:
                    searchedlist.append(o.contents[0]['href'])
                    #print('{}'.format(o.contents[0]['href']))
                    self.sig_class.emit(o.contents[0]['href'],j,1)
                    self.sig_class.emit(inputURL,j,2)
                    j += 1
            else: j += 1
            print('\n')