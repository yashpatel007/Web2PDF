import pdfkit 
from bs4 import BeautifulSoup
import requests
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QHBoxLayout, QWidget, QComboBox, QVBoxLayout, QLineEdit ,QTextEdit, QSystemTrayIcon,QMenu,QAction
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


def savePDF(url, fname):
    pdfkit.from_url(url,fname)
    

def getNextLinks(start_url, depth):
    links =[]
    for i in range(depth):
        page = requests.get(start_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        nextPage = soup.find(class_=elem_class)
        link = nextPage.find('a')
        nxt_link = base_url+link['href']
        links.append(nxt_link)
        start_url = nxt_link
    return links

def webtopdf(full_url):
    links = getNextLinks(full_url,int(depth))
    for idx,link in enumerate(links):
        savePDF(link, "page"+str(idx)+".pdf")

if __name__ == "__main__":
    # base_url = input("please enter base_url: ")
    # elem_class = input("please enter elem class: ")
    # full_url = input("enter url to first page: ")
    # depth = input("how many pages: ")
    # webtopdf()

    def makePDFBaby():
        webtopdf()



    # main window
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Web2PDF')
    #window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    # main -layout
    layout = QVBoxLayout()



    #base url
    page_url = QLineEdit()
    page_url.setFixedWidth(350)
    page_url.setPlaceholderText("Page Url")

    # horizontal layout
    #tag_select = QHBoxLayout()

    search_by = QComboBox()
    search_by.addItems(['class','tag','attribute'])
    search_by.setFixedWidth(350)
    
    search_inp = QLineEdit()
    search_inp.setPlaceholderText("search class or tag or attr")
    search_inp.setFixedWidth(350)

    depth = QLineEdit()
    depth.setPlaceholderText("Num of pages eg 5")
    depth.setFixedWidth(350)

    submit_btn = QPushButton("Submit")


    status = QTextEdit()
    status.setDisabled(True)

    #tag_select.addWidget(search_by)
    #tag_select.addWidget(search_inp)
    
    # --------------- Horizontal layout---------------
    layout.addWidget(page_url)
    layout.addWidget(search_by)
    layout.addWidget(search_inp)
    layout.addWidget(depth)
    layout.addWidget(submit_btn)
    layout.addWidget(status)
    #layout.addLayout(tag_select)
    
    window.setLayout(layout)
    window.setFixedSize(400,300)
    window.show()
    sys.exit(app.exec_())
