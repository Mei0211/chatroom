import queue
import time
import socket
import threading

class ClientPart(object):
    def __init__(self,addr="127.0.0.1",port=9999):
        self.addr = addr
        self.port = port
        self.username = None
        self.status = True
        self.queue = queue.Queue()
        self.loginStatus = False
        self.loginBack = None
        self.registerBack = None
        self.userlist = []
        self.usermsg = []
        self.sysmsg = []
##
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.addr, self.port))  #发送一个连接
            self.s.settimeout(0.001)
        except Exception as e:
                print(e)
        print("initial successfully!")
    #注册账号
    def register(self, name, password):
        self.s.send(str({"type": "register",
                                "name": name,
                                "password": password,
                                "time": time.time()}).encode())

    
    #登录处理函数
    def login(self,name,password):
        self.username = name
        self.s.send(str({"type": "login",
                                "name": name,
                                "password": password,
                                "time": time.time()}).encode())
    #发送消息处理函数,发送长度消息后再发送具体的数据
    def send_Msg(self, msg_send, destname, mtype = "msg", fname = ""):#destname是用户对象名字
        a = str({"type": "usermsg",
                        "mtype": mtype,
                        "destname": destname,
                        "fname": fname,
                        "name": self.username,
                        "time": time.time(),    #返回当前时间的时间戳
                        "msg": msg_send}).encode()
        constlen = len(a)
        self.s.send(str({"type": "msglen",
                                "destname": destname,
                                "name": self.username,
                                "len": constlen}).encode())
        time.sleep(0.01)
        self.s.send(a)
    #接受消息
    def receive_msg(self):
     while self.status:
        try:
            msg_recv = eval(self.s.recv(1024))
        except socket.timeout:
                pass
        except socket.error as err:
                if err.errno == 10053:
                    print("Software caused connection abort ")
                    self.status = False
        else:
                if msg_recv["type"] == "msglen":
                    self.queue.put(msg_recv)
                    length = msg_recv["len"]
                    mlen = 0
                    while msg_recv["type"] != "usermsg":
                        try:
                            msg_recv = "".encode()

                            while mlen < length:
                                try:
                                    msg_recv_ = self.s.recv(length)
                                    msg_recv = msg_recv + msg_recv_
                                    mlen = mlen + len(msg_recv_)
                                    msg_recv = eval(msg_recv)
                                    time.sleep(length * 0.00000001)
                                except socket.timeout:
                                    continue
                                except SyntaxError:
                                    continue
                                else:
                                    break
                        except socket.timeout:
                            continue
                        except socket.error as err:
                            if err.errno == 10053:
                                print("connection abort ")
                                self.status = False
                    self.queue.put(msg_recv)
                else:
                    self.queue.put(msg_recv)
    #客户端处理消息
    def handle_msg(self):
     while True:
        msg = self.queue.get()
        if msg["type"] == "loginBack":
                self.loginBack = msg
                if msg["info"] == "loginSucc":
                    self.userlist = msg["userlist"]
        elif msg["type"] == "rgtrBack":
                self.registerBack = msg
        elif msg["type"] == "usermsg":
                self.usermsg.append(msg)
        elif msg["type"] == "sysmsg":
                self.sysmsg.append(msg)

    def main(self):
        func1 = threading.Thread(target=self.receive_msg)
        func2 = threading.Thread(target=self.handle_msg)
        func1.start()   #启动线程，即让接受消息和处理消息线程开始执行
        func2.start()

    def __del__(self):
        self.s.close()

    def __del__(self):
        self.s.close()

if __name__ == '__main__':
    client = ClientPart(addr="127.0.0.1", port=11005)
    client.main()
    client.login("0", "0")


                                


                


