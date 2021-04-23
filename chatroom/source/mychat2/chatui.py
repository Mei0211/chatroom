import os
import sys
import time
import base64
import threading
import webbrowser
from PyQt5.QtCore import Qt
from client import ClientPart
from PyQt5 import QtCore, QtGui, QtWidgets


class loginWindow(QtWidgets.QDialog):
    def __init__(self):
        super(loginWindow, self).__init__()
        self.setupUi()
    #绘制图形界面
    def setupUi(self):
        self.setObjectName("LoginWindow")
        self.setStyleSheet("#LoginWindow{border-image:url(./images/window/loginwindow/l1.png);}")
        self.resize(450, 300)
        #用户名标签
        self.user_lable = QtWidgets.QLabel(self)
        self.user_lable.setGeometry(QtCore.QRect(40, 90, 80, 20))
        self.user_lable.setObjectName("user_lable")
        #密码标签
        self.pwd_lable = QtWidgets.QLabel(self)
        self.pwd_lable.setGeometry(QtCore.QRect(40, 130, 80, 20))
        self.pwd_lable.setObjectName("pwd_lable")
        #用户名输入
        self.user_lineEdit = QtWidgets.QLineEdit(self)
        self.user_lineEdit.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.user_lineEdit.setObjectName("user_lineEdit")
        #用户密码输入
        self.pwd_lineEdit = QtWidgets.QLineEdit(self)
        self.pwd_lineEdit.setGeometry(QtCore.QRect(130, 130, 113, 20))
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        #注册按钮
        self.rgs_button = QtWidgets.QPushButton(self)
        self.rgs_button.setGeometry(QtCore.QRect(40, 180, 80, 30))
        self.rgs_button.setObjectName("rgs_button")
        self.rgs_button.clicked.connect(self.registerButtonClicked)##添加注册按钮信号和槽
        #登录按钮
        self.login_button = QtWidgets.QPushButton(self)
        self.login_button.setGeometry(QtCore.QRect(150, 180, 80, 30))
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.loginButtonClicked)#添加登录按钮信号和槽
        #显示信息框
        self.print_textBrowser = QtWidgets.QTextBrowser(self)
        self.print_textBrowser.setGeometry(QtCore.QRect(260, 90, 100, 100))
        self.print_textBrowser.setObjectName("print_textBrowser")
        self.print_textBrowser.setStyleSheet("background-color: white;background-color: white;font-size:15px;border:none;")
        self.print_textBrowser.setPlaceholderText("参与聊天需要先注册哦 ~")
        #self.print_textBrowser.setStyleSheet("{border-image:url(./images/window/loginwindow/l3.png);}")
        #头部信息
        self.title_lable = QtWidgets.QLabel(self)
        self.title_lable.setGeometry(QtCore.QRect(100, 20, 221, 50))
        self.title_lable.setObjectName("title_lable")
        self.title_lable.setStyleSheet("background-color: white;font-size:40px;color:rgb(252, 72, 159);")
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LoginWindow", "welcome to chat！"))
        self.user_lable.setText(_translate("LoginWindow", "用户名"))
        self.pwd_lable.setText(_translate("LoginWindow", "密码"))
        self.rgs_button.setText(_translate("LoginWindow", "注册"))
        self.login_button.setText(_translate("LoginWindow", "登录"))
        self.title_lable.setText(_translate("registerWindow", "Have a chat！"))

    #登录按钮事件函数 
    def loginButtonClicked(self):
        Username = self.user_lineEdit.text()
        Password = self.pwd_lineEdit.text()
        if len(Username) == 0 or len(Password) == 0:
            self.print_textBrowser.setText("账号或密码未输入哦！")
        else:
            client.login(Username, Password)
            while client.loginBack == None:
                pass
            flag = False
            if client.loginBack["info"] == "loginSucc":
                self.print_textBrowser.setText("Login successfully!")
                self.hide()
                self.chatWindow = chatWindow(Username)      #登录成功，调出聊天界面
                self.chatWindow.show()
                self.chatWindow.main()
            elif client.loginBack["info"] == "loginFail":
                self.print_textBrowser.setText("Login failed, please retry!")
            else:
                self.print_textBrowser.setText("Account is already logged in!")
            client.loginBack = None

    #注册按钮函数
    def registerButtonClicked(self):
        self.registerWindow = registerWindow()
        self.registerWindow.show()

class registerWindow(QtWidgets.QDialog):
    def __init__(self):
        super(registerWindow, self).__init__()
        self.setupUi()


    def setupUi(self):
        self.setObjectName("registerWindow")
        self.setStyleSheet("#registerWindow{border-image:url(./images/window/registerwindow/rgs4.png);}")
        self.resize(409, 300)
        #用户账号标签
        self.newname_label = QtWidgets.QLabel(self)
        self.newname_label.setGeometry(QtCore.QRect(60, 75, 70, 25))
        self.newname_label.setObjectName("newname_label")
        #密码标签
        self.newpd_label = QtWidgets.QLabel(self)
        self.newpd_label.setGeometry(QtCore.QRect(60, 110, 70, 25))
        self.newpd_label.setObjectName("newpd_label")
        #确认密码标签
        self.check_label = QtWidgets.QLabel(self)
        self.check_label.setGeometry(QtCore.QRect(60, 145, 70, 25))
        self.check_label.setObjectName("check_label")
        #账号输入
        self.newname_lineEdit = QtWidgets.QLineEdit(self)
        self.newname_lineEdit.setGeometry(QtCore.QRect(140, 75, 113, 25))
        self.newname_lineEdit.setText("")
        self.newname_lineEdit.setObjectName("newname_lineEdit")
        #密码输入
        self.newpwd_lineEdit = QtWidgets.QLineEdit(self)#密码
        self.newpwd_lineEdit.setGeometry(QtCore.QRect(140, 110, 113, 25))
        self.newpwd_lineEdit.setObjectName("newpwd_lineEdit")
        #密码确认
        self.check_lineEdit = QtWidgets.QLineEdit(self)#密码确认
        self.check_lineEdit.setGeometry(QtCore.QRect(140, 145, 113, 25))
        self.check_lineEdit.setObjectName("check_lineEdit")
        #注册按钮
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(150, 210, 80, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registerButtonClicked)
        #欢迎标签
        self.welcome_label = QtWidgets.QLabel(self)
        self.welcome_label.setGeometry(QtCore.QRect(145, 30, 200, 30))
        self.welcome_label.setObjectName("welcome_label")
        self.welcome_label.setStyleSheet("background-color: white;font-size:20px;color:rgb(252, 72, 159);")

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(270, 75, 111, 95))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setPlaceholderText("确认密码需和新密码一致哦~")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("registerWindow", "注册账号"))
        self.newname_label.setText(_translate("registerWindow", "新账号"))
        self.newpd_label.setText(_translate("registerWindow", "新密码"))
        self.check_label.setText(_translate("registerWindow", "确认密码"))
        self.pushButton.setText(_translate("registerWindow", "注册"))
        self.welcome_label.setText(_translate("registerWindow", "欢迎你，新用户~"))
        
    def registerButtonClicked(self):
        Username = self.newname_lineEdit.text()
        password = self.newpwd_lineEdit.text()
        passwordAgain = self.check_lineEdit.text()
        if len(Username) == 0 or len(password) == 0 or len(passwordAgain) == 0:
           self.textBrowser.setText("您还没有输入账号或密码！")  
        elif password != passwordAgain:
            self.textBrowser.setText("您两次输入的密码不同！")
        else:
            client.register(Username, password)
            while client.registerBack == None:
                pass
            if client.registerBack["info"] == "rgtrSucc":
                self.textBrowser.setText("注册成功，请返回登陆界面~")
            else:
                self.textBrowser.setText("该账号已存在！")
            client.registerBack = None

class chatWindow(QtWidgets.QDialog):
    def __init__(self, name):
        self.Username = name
        super(chatWindow, self).__init__()
        self.setupUi()
        try:
            os.mkdir(self.Username)         #创建对应的文件夹
        except FileExistsError:
            pass

    def setupUi(self):

        self.setObjectName("MyChat")
        self.setStyleSheet("#MyChat{border-image:url(./images/window/chatwindow/chat15.png);}")
        #self.setWindowIcon(QtGui.QIcon("./images/window/icon.png"))
        self.resize(1005, 463)
        #群聊
        self.grprecvText = QtWidgets.QTextEdit(self)        
        self.grprecvText.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.grprecvText.setObjectName("textRecv")
        self.grprecvText.setAlignment(QtCore.Qt.AlignTop)
        #self.grprecvText.setStyleSheet("border-image:url(./images/window/chatwindow/chat15.png);")
        self.grprecvText.setReadOnly(True)
        #私聊1
        self.prtrecvText1 = QtWidgets.QTextEdit(self)       
        self.prtrecvText1.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.prtrecvText1.setAlignment(QtCore.Qt.AlignTop)
        #self.prtrecvText1.setStyleSheet("border-image:url(./images/window/chatwindow/recvtext.png);")
        self.prtrecvText1.setReadOnly(True)
        self.prtrecvText1.hide()
        #私聊2
        self.prtrecvText2 = QtWidgets.QTextEdit(self)       
        self.prtrecvText2.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.prtrecvText2.setAlignment(QtCore.Qt.AlignTop)
        #self.prtrecvText2.setStyleSheet("border-image:url(./images/window/chatwindow/recvtext.png);")
        self.prtrecvText2.setReadOnly(True)
        self.prtrecvText2.hide()
        
        self.prtrecvText3 = QtWidgets.QTextEdit(self)       
        self.prtrecvText3.setGeometry(QtCore.QRect(200, 20, 670, 280))
        self.prtrecvText3.setAlignment(QtCore.Qt.AlignTop)
        #self.prtrecvText3.setStyleSheet("border-image:url(./images/window/chatwindow/recvtext.png);")
        self.prtrecvText3.setReadOnly(True)
        self.prtrecvText3.hide()
        self.prtrecvText = [self.prtrecvText1, self.prtrecvText2, self.prtrecvText3]
        #发送消息的编辑框
        self.sendText = QtWidgets.QTextEdit(self)           
        self.sendText.setGeometry(QtCore.QRect(200, 335, 670, 85)) #
        self.sendText.setObjectName("textSend")
        self.sendText.setAlignment(QtCore.Qt.AlignTop)
       
        self.destsend = 'all'
        #发送消息的按钮
        self.sendtxtButton = QtWidgets.QPushButton(self)    
        self.sendtxtButton.setGeometry(QtCore.QRect(905, 425, 65, 27))
        self.sendtxtButton.setObjectName("txtsendButton")
        self.sendtxtButton.clicked.connect(self.txtsendButtonClicked)


        self.grpButton = QtWidgets.QPushButton(self)        #将聊天框切换至群聊的按钮
        self.grpButton.setGeometry(QtCore.QRect(20, 20, 150,30))
        self.grpButton.setObjectName("grpButton")
        self.grpButton.setStyleSheet("border-image:url(./images/window/chatwindow/gr1.png);")
        self.grpButton.clicked.connect(self.grpbuttonClicked)

        self.destprtbutton = {}
        self.prtbutton1 = QtWidgets.QPushButton(self)       #将聊天框切换至私聊1的按钮
        self.prtbutton1.setGeometry(QtCore.QRect(20, 120, 150, 30))
        self.prtbutton1.setStyleSheet("border-image:url(./images/window/chatwindow/chat15.png);")
        self.prtbutton1.clicked.connect(self.prtbutton1Clicked)

        self.prtbutton2 = QtWidgets.QPushButton(self)       #将聊天框切换至私聊2的按钮
        self.prtbutton2.setGeometry(QtCore.QRect(20, 180, 150, 30))
        self.prtbutton2.setStyleSheet("border-image:url(./images/window/chatwindow/chat15.png);")
        self.prtbutton2.clicked.connect(self.prtbutton2Clicked)

        self.prtbutton3 = QtWidgets.QPushButton(self)       #将聊天框切换至私聊3的按钮
        self.prtbutton3.setGeometry(QtCore.QRect(20, 240, 150, 30))
        self.prtbutton3.setStyleSheet("border-image:url(./images/window/chatwindow/chat15.png);")
        self.prtbutton3.clicked.connect(self.prtbutton3Clicked)

        self.buttontotext = {}                              #按钮和聊天框的字典
        self.buttontotext[self.prtbutton1] = self.prtrecvText1
        self.buttontotext[self.prtbutton2] = self.prtrecvText2
        self.buttontotext[self.prtbutton3] = self.prtrecvText3
        self.prtbutton = [self.prtbutton1, self.prtbutton2, self.prtbutton3]

        self.fileButton = QtWidgets.QPushButton(self)       #发送文件的按钮
        self.fileButton.setGeometry(QtCore.QRect(900, 20,100,70))
        self.fileButton.setStyleSheet("border-image:url(./images/window/chatwindow/wenjianjia1.png);")
        self.fileButton.clicked.connect(self.fileButtonClicked)

        #self.fileButton = QtWidgets.QPushButton(self)       #发送文件的按钮
        #self.fileButton.setGeometry(QtCore.QRect(200, 300, 35, 35))
        #self.fileButton.setStyleSheet("border-image:url(./images/window/chatwindow/filebutton.png);")
        #self.fileButton.clicked.connect(self.fileButtonClicked)

        
        self.imageButton = QtWidgets.QPushButton(self)      #发送图片的按钮
        self.imageButton.setGeometry(QtCore.QRect(900, 110, 100, 70))
        self.imageButton.setObjectName("图片")
        self.imageButton.setStyleSheet("border-image:url(./images/window/chatwindow/tupian1.png);")
        self.imageButton.clicked.connect(self.imageButtonClicked)

        self.emojiButton = QtWidgets.QPushButton(self)      # 发送表情的按钮
        self.emojiButton.setGeometry(QtCore.QRect(900, 200, 100, 70))
        self.emojiButton.setObjectName("表情")
        self.emojiButton.setStyleSheet("border-image:url(./images/window/chatwindow/biaoqing.png);")
        self.emojiButton.clicked.connect(self.emojiButtonClicked)

        self.friendlist = QtWidgets.QComboBox(self)       #在线好友列表
        self.friendlist.setGeometry(QtCore.QRect(200, 300, 100, 35))
        self.friendlist.setObjectName("friendlist")
        self.friendlist.addItems(client.userlist)
        self.friendlist.setPlaceholderText("好友列表")
        #self.friendlist.setStyleSheet("border-image:url(./images/window/chatwindow/friendlist.png);")
        self.friendlist.activated[str].connect(self.friendlistDoubleClicked)
        


        self.fileselect = QtWidgets.QFileDialog(self)       #文件选择界面
        self.fileselect.setGeometry(QtCore.QRect(248, 341, 500, 62))

        self.emoji = QtWidgets.QTableWidget(self)           #表情列表
        self.emoji.setGeometry(QtCore.QRect(850, 200, 120, 120))
        self.emoji.verticalHeader().setVisible(False)       # 隐藏垂直表头
        self.emoji.horizontalHeader().setVisible(False)     # 隐藏水平表头
        self.emoji.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)   # 隐藏垂直滚动条
        self.emoji.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)     # 隐藏水平滚动条
        self.emoji.setColumnCount(3)
        self.emoji.setRowCount(3)
        label = []
        #发送表情
        for i in range(9):
            icon = QtWidgets.QLabel()
            icon.setMargin(4)
            movie = QtGui.QMovie()
            movie.setScaledSize(QtCore.QSize(30, 30))
            movie.setFileName("./images/emoji/"+str(i)+".gif")
            movie.start()
            icon.setMovie(movie)
            self.emoji.setCellWidget(int(i/3), i%3, icon)
            self.emoji.setColumnWidth(i%3, 40)          # 设置列的宽度
            self.emoji.setRowHeight(int(i/3), 40)       # 设置行的高度
        self.emoji.hide()
        self.emoji.cellClicked.connect(self.emojiClicked)

        for i in self.prtbutton:
            self.destprtbutton[i] = None

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MyChat", "MyChat"))
        self.sendtxtButton.setText(_translate("txtsendButton", "发送"))
        self.grpButton.setText(_translate("grpButton", "群聊"))
        #self.friendlistHeader.setText(_translate("friendlistHeader", "在线好友列表"))

    def txtsendButtonClicked(self):
        text = self.sendText.toPlainText()
        if len(text):
            client.send_Msg(text, self.destsend)
            self.sendText.clear()

 

    def friendlistDoubleClicked(self):
        name = self.friendlist.currentText()     #聊天对象
        if name == self.Username:#是自己的话就返回
            return
        for i in self.prtbutton:
            if self.destprtbutton[i] == None or self.destprtbutton[i] == name:
                self.destprtbutton[i] = name
                i.setText(name)#对左边列的私聊实例化
                break

    def grpbuttonClicked(self):
        for i in self.prtrecvText:
            i.hide()#私聊框隐藏
        #self.grpButton.setStyleSheet("border-image:url(./images/window/chatwindow/nowfriendbutton.png);")
        #self.prtbutton1.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
        #self.prtbutton2.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
        #self.prtbutton3.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
        self.grprecvText.show()
        self.destsend = "all"

    def prtbutton1Clicked(self):
        if self.destprtbutton[self.prtbutton1] != None:
            for i in self.prtrecvText:
                i.hide()
            #self.grpButton.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            #self.prtbutton1.setStyleSheet("border-image:url(./images/window/chatwindow/nowfriendbutton.png);")
            #self.prtbutton2.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            #self.prtbutton3.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            self.grprecvText.hide()
            self.buttontotext[self.prtbutton1].show()
            self.destsend = self.destprtbutton[self.prtbutton1]

    def prtbutton2Clicked(self):
        if self.destprtbutton[self.prtbutton2] != None:
            for i in self.prtrecvText:
                i.hide()
            #self.grpButton.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            #self.prtbutton1.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            #self.prtbutton2.setStyleSheet("border-image:url(./images/window/chatwindow/nowfriendbutton.png);")
            #self.prtbutton3.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            self.grprecvText.hide()
            self.buttontotext[self.prtbutton2].show()
            self.destsend = self.destprtbutton[self.prtbutton2]

    def prtbutton3Clicked(self):
        if self.destprtbutton[self.prtbutton3] != None:
            for i in self.prtrecvText:
                i.hide()
            #self.grpButton.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            #self.prtbutton1.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            #self.prtbutton2.setStyleSheet("border-image:url(./images/window/chatwindow/friendbutton.png);")
            #self.prtbutton3.setStyleSheet("border-image:url(./images/window/chatwindow/nowfriendbutton.png);")
            self.grprecvText.hide()
            self.buttontotext[self.prtbutton3].show()
            self.destsend = self.destprtbutton[self.prtbutton3]

    def fileButtonClicked(self):
        # self.fileselect.show()
        fileinfo = self.fileselect.getOpenFileName(self, 'OpenFile', "e:/")
        print(fileinfo)
        filepath, filetype = os.path.splitext(fileinfo[0])
        filename = filepath.split("/")[-1]
        if fileinfo[0] != '':
            with open(fileinfo[0], mode='rb') as f:
                r = f.read()
                f.close()
            file_r = base64.encodebytes(r).decode("utf-8")
            client.send_Msg(file_r, self.destsend, filetype, filename)
        # while self.fileselect.getOpenFileName() == None:

    def imageButtonClicked(self):
        fileinfo = self.fileselect.getOpenFileName(self,'OpenFile',"e:/","Image files (*.jpg *.gif *.png)")
        print(fileinfo)
        filepath, filetype = os.path.splitext(fileinfo[0])
        filename = filepath.split("/")[-1]
        if fileinfo[0] != '':
            with open(fileinfo[0], mode='rb') as f:
                r = f.read()
                f.close()
            file_r = base64.encodebytes(r).decode("utf-8")
            client.send_Msg(file_r, self.destsend, filetype, filename)

    def emojiButtonClicked(self):
        self.emoji.show()

    def emojiClicked(self, row, column):
        client.send_Msg(row*3+column , self.destsend, "emoji")
        self.emoji.hide()

    def recv(self):
        '''
        用于将接收到的消息显示出来
        '''
        while True:
            while len(client.usermsg):
                msg_recv = client.usermsg.pop()
                msgtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(msg_recv["time"]))
                if msg_recv["mtype"] == "msg":
                    msg_recv["msg"] = msg_recv["msg"].replace("\n","\n  ")
                    if msg_recv["name"] == self.Username:       #从本地发送的消息打印
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.green)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            self.grprecvText.setTextColor(Qt.black)
                            self.grprecvText.insertPlainText(msg_recv["msg"] + "\n")
                        else:
                            for i in self.prtbutton:
                                print(msg_recv["destname"])
                                print(self.destprtbutton[i])
                                if msg_recv["destname"] == self.destprtbutton[i]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.green)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    self.buttontotext[i].setTextColor(Qt.black)
                                    self.buttontotext[i].insertPlainText(msg_recv["msg"] + "\n")
                    elif msg_recv["destname"] in (self.Username, "all"):        #本地接收到的消息打印
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            self.grprecvText.setTextColor(Qt.black)
                            self.grprecvText.insertPlainText(msg_recv["msg"] + "\n")
                        else:
                            for i in self.prtbutton:
                                if self.destprtbutton[i] == msg_recv["name"]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    self.buttontotext[i].setTextColor(Qt.black)
                                    self.buttontotext[i].insertPlainText(msg_recv["msg"] + "\n")
                                    break
                                elif self.destprtbutton[i] == None:
                                    self.destprtbutton[i] = msg_recv["name"]
                                    i.setText(msg_recv["name"])
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    self.buttontotext[i].setTextColor(Qt.black)
                                    self.buttontotext[i].insertPlainText(msg_recv["msg"] + "\n")
                                    break
                elif msg_recv["mtype"] == "emoji":
                    if msg_recv["name"] == self.Username:  # 从本地发送的消息打印
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.green)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./images/emoji/"+ str(msg_recv["msg"]) +".gif"
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            img.setName(path)
                            img.setHeight(28)
                            img.setWidth(28)
                            tcursor.insertImage(img)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                print(msg_recv["destname"])
                                print(self.destprtbutton[i])
                                if msg_recv["destname"] == self.destprtbutton[i]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.green)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./images/emoji/" + str(msg_recv["msg"]) + ".gif"
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    img.setName(path)
                                    img.setHeight(28)
                                    img.setWidth(28)
                                    tcursor.insertImage(img)
                                    self.buttontotext[i].insertPlainText("\n")
                    elif msg_recv["destname"] in (self.Username, "all"):  # 本地接收到的消息打印
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./images/emoji/"+ str(msg_recv["msg"]) +".gif"
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            img.setName(path)
                            img.setHeight(28)
                            img.setWidth(28)
                            tcursor.insertImage(img)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                if self.destprtbutton[i] == msg_recv["name"]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./images/emoji/" + str(msg_recv["msg"]) + ".gif"
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    img.setName(path)
                                    img.setHeight(28)
                                    img.setWidth(28)
                                    tcursor.insertImage(img)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break
                                elif self.destprtbutton[i] == None:
                                    self.destprtbutton[i] = msg_recv["name"]
                                    i.setText(msg_recv["name"])
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./images/emoji/" + str(msg_recv["msg"]) + ".gif"
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    img.setName(path)
                                    img.setHeight(28)
                                    img.setWidth(28)
                                    tcursor.insertImage(img)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break
                else:
                    if msg_recv["name"] == self.Username:  # 从本地发送的消息打印
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.green)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                            with open(path,"wb") as f:
                                f.write(base64.b64decode(msg_recv["msg"]))
                                f.close()
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                img.setName(path)
                                img.setHeight(100)
                                img.setWidth(100)
                                tcursor.insertImage(img)
                            else:
                                img.setName("./images/window/chatwindow/filebutton.png")
                                img.setHeight(30)
                                img.setWidth(30)
                                tcursor.insertImage(img)
                                self.grprecvText.insertPlainText("文件已下载到：" + path)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                print(msg_recv["destname"])
                                print(self.destprtbutton[i])
                                if msg_recv["destname"] == self.destprtbutton[i]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.green)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                                    with open(path, "wb") as f:
                                        f.write(base64.b64decode(msg_recv["msg"]))
                                        f.close()
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                        img.setName(path)
                                        img.setHeight(100)
                                        img.setWidth(100)
                                        tcursor.insertImage(img)
                                    else:
                                        img.setName("./images/window/chatwindow/filebutton.png")
                                        img.setHeight(30)
                                        img.setWidth(30)
                                        tcursor.insertImage(img)
                                        self.buttontotext[i].insertPlainText("文件已下载到："+path)
                                    self.buttontotext[i].insertPlainText("\n")
                    elif msg_recv["destname"] in (self.Username, "all"):  # 本地接收到的消息打印
                        if msg_recv["destname"] == "all":
                            self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                            self.grprecvText.setTextColor(Qt.blue)
                            self.grprecvText.insertPlainText(
                                " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                            path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                            with open(path, "wb") as f:
                                f.write(base64.b64decode(msg_recv["msg"]))
                                f.close()
                            tcursor = self.grprecvText.textCursor()
                            img = QtGui.QTextImageFormat()
                            if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                img.setName(path)
                                img.setHeight(100)
                                img.setWidth(100)
                                tcursor.insertImage(img)
                            else:
                                img.setName("./images/window/chatwindow/filebutton.png")
                                img.setHeight(30)
                                img.setWidth(30)
                                tcursor.insertImage(img)
                                self.grprecvText.insertPlainText("文件已下载到：" + path)
                            self.grprecvText.insertPlainText("\n")
                        else:
                            for i in self.prtbutton:
                                if self.destprtbutton[i] == msg_recv["name"]:
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                                    with open(path, "wb") as f:
                                        f.write(base64.b64decode(msg_recv["msg"]))
                                        f.close()
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                        img.setName(path)
                                        img.setHeight(100)
                                        img.setWidth(100)
                                        tcursor.insertImage(img)
                                    else:
                                        img.setName("./images/window/chatwindow/filebutton.png")
                                        img.setHeight(30)
                                        img.setWidth(30)
                                        tcursor.insertImage(img)
                                        self.buttontotext[i].insertPlainText("文件已下载到："+path)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break
                                elif self.destprtbutton[i] == None:
                                    self.destprtbutton[i] = msg_recv["name"]
                                    i.setText(msg_recv["name"])
                                    self.buttontotext[i].moveCursor(QtGui.QTextCursor.End)
                                    self.buttontotext[i].setTextColor(Qt.blue)
                                    self.buttontotext[i].insertPlainText(
                                        " " + msg_recv["name"] + "  " + msgtime + "\n  ")
                                    path = "./" + self.Username + "/" + msg_recv["fname"] + msg_recv["mtype"]
                                    with open(path, "wb") as f:
                                        f.write(base64.b64decode(msg_recv["msg"]))
                                        f.close()
                                    tcursor = self.buttontotext[i].textCursor()
                                    img = QtGui.QTextImageFormat()
                                    if msg_recv["mtype"] in (".png", ".gif", ".jpg"):
                                        img.setName(path)
                                        img.setHeight(100)
                                        img.setWidth(100)
                                        tcursor.insertImage(img)
                                    else:
                                        img.setName("./images/window/chatwindow/filebutton.png")
                                        img.setHeight(30)
                                        img.setWidth(30)
                                        tcursor.insertImage(img)
                                        self.buttontotext[i].insertPlainText("文件已下载到："+path)
                                    self.buttontotext[i].insertPlainText("\n")
                                    break

            while len(client.sysmsg):
                msg_recv = client.sysmsg.pop()
                # msgtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(msg_recv["time"]))
                if msg_recv["info"] == "userlogin":
                    if msg_recv["name"] not in client.userlist:
                        client.userlist.append(msg_recv["name"])
                        self.friendlist.clear()
                        self.friendlist.addItems(client.userlist)
                elif msg_recv["info"] == "userexit":
                    if msg_recv["name"] in client.userlist:
                        client.userlist.remove(msg_recv["name"])
                        self.friendlist.clear()
                        self.friendlist.addItems(client.userlist)
                self.grprecvText.moveCursor(QtGui.QTextCursor.End)
                self.grprecvText.setTextColor(Qt.gray)
                self.grprecvText.insertPlainText("      "+msg_recv["msg"]+"\n")

    def main(self):
        func1 = threading.Thread(target=self.recv)
        func1.start()



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)  #
    client = ClientPart(addr="localhost", port=11005)
    client.main()
    login = loginWindow()
    login.show()
    sys.exit(app.exec_())
