#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
import socket
import time

from threading import *
from action_groups import *

reload(sys)
sys.setdefaultencoding('utf-8')

RobotWork = TurnUntil()

#端口broacast_dest定时广播地址
def keep_alive(keeptime,run_flag, broacast_dest):
    if run_flag:
        broacast_socket.sendto("KEEP", broacast_dest)
        
        Timer(keeptime, keep_alive, ( keeptime,run_flag, broacast_dest, ) ).start()
        time.sleep(0.1)
        #print "KEEP",broacast_dest
    else:
        return
    
def func_work(rx_address, ntime_out):  
    rx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #rx_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,1)
    rx_socket.bind(rx_address)
    rx_socket.settimeout(ntime_out) 
    
    syn_start = False
    while 1:
        try:
            data, addr = rx_socket.recvfrom(16)        
            if data == "FT" and not syn_start:
                syn_start = True
                RobotWork.set_status(True)
                Timer(0, RobotWork.WorkRun, ( ) ).start()                
                print data
            if data == "TL" and not syn_start:
                syn_start = True
                RobotWork.set_status(True)
                Timer(0, RobotWork.Work_Lefthand, ( ) ).start()                
                print data
            if data == "TR" and not syn_start:
                syn_start = True
                RobotWork.set_status(True)
                Timer(0, RobotWork.Work_Righthand, ( ) ).start()                
                print data
            if data == "GB" and not syn_start:
                syn_start = True
                RobotWork.set_status(True)
                Timer(0, RobotWork.Work_wait, ( ) ).start()                
                print data
            if data == "SB" and not syn_start:
                syn_start = True
                RobotWork.set_status(True)
                Timer(0, RobotWork.Work_Stand, ( ) ).start()                
                print data
            if data == "HI" and not syn_start:
                syn_start = True
                RobotWork.set_status(True)
                Timer(0, RobotWork.Work_hi, ( ) ).start()                
                print data
            if data == "LOVELY" and not syn_start:
                syn_start = True
                RobotWork.set_status(True)
                Timer(0, RobotWork.Work_lovely, ( ) ).start()                
                print data
            elif data == "STOP":
                RobotWork.set_status(False)
                syn_start = False
                print data
            elif data:
                pass
                #print "Have Data:", data,addr
        except socket.timeout:
            RobotWork.set_status(False)
            syn_start = False
            print "Time out!"

if __name__=="__main__":
    broacast_port = 51421
    rx_port = 51423
    run_flag = True
    keep_time = 0.1
    
    broacast_dest = ('<broadcast>', broacast_port)
    broacast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broacast_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    
    Timer(0, keep_alive, ( keep_time,run_flag, broacast_dest ) ).start()
    
    hostname = socket.getfqdn(socket.gethostname())
    hostaddr = socket.gethostbyname(hostname)
    print hostname, hostaddr
    
    
    rx_address = ('',rx_port)
    func_work(rx_address, 0.5)
    
