#-*- coding:utf-8 -*-
import time
from PCA9685 import PCA9685

left_dict = {0:105, 1:95, 2:95, 3:85, 4:95, 5:90, 6:100, 7:105, 8:95}
right_dict = {0:85, 1:90, 2:90, 3:95, 4:86, 5:95, 6:90, 7:85, 8:87}

left_angle_dict = {0:left_dict[0], 1:left_dict[1], 2:left_dict[2], 3:right_dict[3], 4:right_dict[4], 5:right_dict[5], 6:left_dict[6], 7:left_dict[7],8:left_dict[8]}
right_angle_dict = {0:right_dict[0], 1:right_dict[1], 2:right_dict[2], 3:left_dict[3], 4:left_dict[4], 5:left_dict[5], 6:right_dict[6], 7:right_dict[7], 8:right_dict[8]}

def init_site(pwm_left, pwm_right):
    pwm_left.setangle(0, left_angle_dict[0])
    pwm_left.setangle(1, left_angle_dict[1])
    pwm_left.setangle(2, left_angle_dict[2])
    pwm_left.setangle(3, right_angle_dict[3])
    pwm_left.setangle(4, right_angle_dict[4])
    pwm_left.setangle(5, right_angle_dict[5])
    pwm_left.setangle(6, left_angle_dict[6])
    pwm_left.setangle(7, left_angle_dict[7])
    pwm_left.setangle(8, left_angle_dict[8])

    pwm_right.setangle(0, right_angle_dict[0])
    pwm_right.setangle(1, right_angle_dict[1])
    pwm_right.setangle(2, right_angle_dict[2])
    pwm_right.setangle(3, left_angle_dict[3])
    pwm_right.setangle(4, left_angle_dict[4])
    pwm_right.setangle(5, left_angle_dict[5])
    pwm_right.setangle(6, right_angle_dict[6])
    pwm_right.setangle(7, right_angle_dict[7])
    pwm_right.setangle(8, right_angle_dict[8])
    
def left_groups_up(pwm_left, pwm_right):
    pwm_left.setangle(1, left_angle_dict[1]-60)
    pwm_left.setangle(7, left_angle_dict[7]-60)
    pwm_right.setangle(4, left_angle_dict[4]+60)        

    pwm_left.setangle(2, left_angle_dict[2] + 60)
    pwm_left.setangle(8, left_angle_dict[8] + 60)
    pwm_right.setangle(5, left_angle_dict[5] - 60)
    time.sleep(0.3)

    pwm_left.setangle(0 , left_angle_dict[0]+45)
    pwm_left.setangle(6 , left_angle_dict[6]+45)
    pwm_right.setangle(3, left_angle_dict[3]-45)
    time.sleep(0.2)

def left_groups_down(pwm_left, pwm_right):
    pwm_left.setangle(1,left_angle_dict[1])
    pwm_left.setangle(7, left_angle_dict[7])
    pwm_right.setangle(4, left_angle_dict[4])

    pwm_left.setangle(2, left_angle_dict[2])
    pwm_left.setangle(8, left_angle_dict[8])        
    pwm_right.setangle(5, left_angle_dict[5])
    time.sleep(0.3)
    #start move
    pwm_right.setangle(1, right_angle_dict[1] + 60)
    pwm_right.setangle(7, right_angle_dict[7] + 60)
    pwm_left.setangle(4, right_angle_dict[4] - 60)
    #time.sleep(0.1)
    pwm_left.setangle(0 , left_angle_dict[0])
    pwm_left.setangle(6 , left_angle_dict[6])
    pwm_right.setangle(3, left_angle_dict[3])
    time.sleep(0.2)

def right_groups_up(pwm_left, pwm_right):
    pwm_right.setangle(1, right_angle_dict[1] + 60)
    pwm_right.setangle(7, right_angle_dict[7] + 60)
    pwm_left.setangle(4, right_angle_dict[4] - 60)
        
    pwm_right.setangle(2, right_angle_dict[2] - 60)
    pwm_right.setangle(8, right_angle_dict[8] - 60)
    pwm_left.setangle(5, right_angle_dict[5] + 60)        
    time.sleep(0.3)

    pwm_right.setangle(0, right_angle_dict[0] - 45)
    pwm_right.setangle(6, right_angle_dict[6] - 45)
    pwm_left.setangle(3, right_angle_dict[3] + 45)
    time.sleep(0.2)

def right_groups_down(pwm_left, pwm_right):
    pwm_right.setangle(1, right_angle_dict[1])
    pwm_right.setangle(7, right_angle_dict[7])
    pwm_left.setangle(4, right_angle_dict[4])
        
    pwm_right.setangle(2, right_angle_dict[2])
    pwm_right.setangle(8, right_angle_dict[8])
    pwm_left.setangle(5, right_angle_dict[5])     
    time.sleep(0.3)
    #start move
    pwm_left.setangle(1, left_angle_dict[1]-60)
    pwm_left.setangle(7, left_angle_dict[7]-60)
    pwm_right.setangle(4, left_angle_dict[4]+60)
    #time.sleep(0.1)
    pwm_right.setangle(0, right_angle_dict[0])
    pwm_right.setangle(6, right_angle_dict[6])
    pwm_left.setangle(3, right_angle_dict[3])
    time.sleep(0.2)
    
def lr_hand_init(pwm_left, pwm_right):
    pwm_left.setangle(1,left_angle_dict[1] - 60)
    pwm_left.setangle(7, left_angle_dict[7] - 60)
    pwm_right.setangle(4, left_angle_dict[4])

    pwm_left.setangle(2, left_angle_dict[2])
    pwm_left.setangle(8, left_angle_dict[8])        
    pwm_right.setangle(5, left_angle_dict[5])
    
    pwm_left.setangle(0 , left_angle_dict[0] + 45)
    pwm_left.setangle(6 , left_angle_dict[6] - 45)
    pwm_right.setangle(3, left_angle_dict[3])
    time.sleep(0.3)
    pwm_left.setangle(1,left_angle_dict[1])
    pwm_left.setangle(7, left_angle_dict[7])
    pwm_right.setangle(4, left_angle_dict[4])
    time.sleep(0.3)
       
    pwm_right.setangle(1, right_angle_dict[1] + 60)
    pwm_right.setangle(7, right_angle_dict[7] + 60)
    pwm_left.setangle(4, right_angle_dict[4])
        
    pwm_right.setangle(2, right_angle_dict[2])
    pwm_right.setangle(8, right_angle_dict[8])
    pwm_left.setangle(5, right_angle_dict[5])     
    
    pwm_right.setangle(0, right_angle_dict[0] - 45)
    pwm_right.setangle(6, right_angle_dict[6] + 45)
    pwm_left.setangle(3, right_angle_dict[3])
    time.sleep(0.2)     

    pwm_right.setangle(1, right_angle_dict[1])
    pwm_right.setangle(7, right_angle_dict[7])
    pwm_left.setangle(4, right_angle_dict[4])
    time.sleep(0.2)
       

def left_hand_groups(pwm_left, pwm_right):
    #抬起右侧
    pwm_left.setangle(1, left_angle_dict[1]-60)
    pwm_left.setangle(7, left_angle_dict[7]-60)
    pwm_right.setangle(4, left_angle_dict[4]+60)
    #正右
    pwm_left.setangle(2, left_angle_dict[2])
    pwm_left.setangle(8, left_angle_dict[8])    
    pwm_right.setangle(5, left_angle_dict[5])    
    #倾斜左侧
    pwm_right.setangle(2, right_angle_dict[2] + 30)
    pwm_right.setangle(8, right_angle_dict[8] + 30)
    pwm_left.setangle(5, right_angle_dict[5] + 30)
    time.sleep(0.2)
    #落下右侧
    pwm_left.setangle(1, left_angle_dict[1])
    pwm_left.setangle(7, left_angle_dict[7])
    pwm_right.setangle(4, left_angle_dict[4])
    time.sleep(0.2)
    #抬左 正左
    pwm_right.setangle(1, right_angle_dict[1] + 60)
    pwm_right.setangle(7, right_angle_dict[7] + 60)
    pwm_left.setangle(4, right_angle_dict[4] - 60)
    
    pwm_right.setangle(2, right_angle_dict[2])
    pwm_right.setangle(8, right_angle_dict[8])
    pwm_left.setangle(5, right_angle_dict[5])
    #倾斜右侧
    pwm_left.setangle(2, left_angle_dict[2] + 30)
    pwm_left.setangle(8, left_angle_dict[8] + 30)    
    pwm_right.setangle(5, left_angle_dict[5] + 30)
    time.sleep(0.2)
    #落左
    pwm_right.setangle(1, right_angle_dict[1])
    pwm_right.setangle(7, right_angle_dict[7])
    pwm_left.setangle(4, right_angle_dict[4])    
    time.sleep(0.2)
    
def right_hand_groups(pwm_left, pwm_right):
    #抬左
    pwm_right.setangle(1, right_angle_dict[1] + 60)
    pwm_right.setangle(7, right_angle_dict[7] + 60)
    pwm_left.setangle(4, right_angle_dict[4] - 60)
    
    pwm_right.setangle(2, right_angle_dict[2])
    pwm_right.setangle(8, right_angle_dict[8])
    pwm_left.setangle(5, right_angle_dict[5])  
    #倾斜右侧
    pwm_left.setangle(2, left_angle_dict[2] - 30)
    pwm_left.setangle(8, left_angle_dict[8] - 30)    
    pwm_right.setangle(5, left_angle_dict[5] - 30)
    time.sleep(0.2)
    #落左
    pwm_right.setangle(1, right_angle_dict[1])
    pwm_right.setangle(7, right_angle_dict[7])
    pwm_left.setangle(4, right_angle_dict[4])    
    time.sleep(0.2)
    
    #抬起右侧
    pwm_left.setangle(1, left_angle_dict[1] -60)
    pwm_left.setangle(7, left_angle_dict[7] -60)
    pwm_right.setangle(4, left_angle_dict[4]+60)
    #正右
    pwm_left.setangle(2, left_angle_dict[2])
    pwm_left.setangle(8, left_angle_dict[8])    
    pwm_right.setangle(5, left_angle_dict[5])
    #斜左
    pwm_right.setangle(2, right_angle_dict[2] - 30)
    pwm_right.setangle(8, right_angle_dict[8] - 30)
    pwm_left.setangle(5, right_angle_dict[5] - 30)
    time.sleep(0.2)
    #落右
    pwm_left.setangle(1, left_angle_dict[1])
    pwm_left.setangle(7, left_angle_dict[7])
    pwm_right.setangle(4, left_angle_dict[4])
    time.sleep(0.2)

def wait_groups(pwm_left, pwm_right):
    pwm_left.setangle(0, left_angle_dict[0])
    pwm_left.setangle(1, left_angle_dict[1] - 60)
    pwm_left.setangle(2, left_angle_dict[2] )
    pwm_left.setangle(3, right_angle_dict[3])
    pwm_left.setangle(4, right_angle_dict[4] - 60)
    pwm_left.setangle(5, right_angle_dict[5])
    pwm_left.setangle(6, left_angle_dict[6])
    pwm_left.setangle(7, left_angle_dict[7] - 60)
    pwm_left.setangle(8, left_angle_dict[8])

    pwm_right.setangle(0, right_angle_dict[0])
    pwm_right.setangle(1, right_angle_dict[1] + 60)
    pwm_right.setangle(2, right_angle_dict[2])
    pwm_right.setangle(3, left_angle_dict[3])
    pwm_right.setangle(4, left_angle_dict[4] + 60)
    pwm_right.setangle(5, left_angle_dict[5])
    pwm_right.setangle(6, right_angle_dict[6])
    pwm_right.setangle(7, right_angle_dict[7] + 60)
    pwm_right.setangle(8, right_angle_dict[8])


def lovely_groups(pwm_left, pwm_right):
    pwm_left.setangle(0, left_angle_dict[0])
    pwm_left.setangle(1, left_angle_dict[1] - 60)
    pwm_left.setangle(2, left_angle_dict[2] + 60)
    pwm_left.setangle(3, right_angle_dict[3] + 60)
    pwm_left.setangle(4, right_angle_dict[4])
    pwm_left.setangle(5, right_angle_dict[5])
    pwm_left.setangle(6, left_angle_dict[6] + 30)
    pwm_left.setangle(7, left_angle_dict[7] - 60)
    pwm_left.setangle(8, left_angle_dict[8])

    pwm_right.setangle(0, right_angle_dict[0])
    pwm_right.setangle(1, right_angle_dict[1] + 60)
    pwm_right.setangle(2, right_angle_dict[2] - 60)
    pwm_right.setangle(3, left_angle_dict[3] - 60)
    pwm_right.setangle(4, left_angle_dict[4])
    pwm_right.setangle(5, left_angle_dict[5])
    pwm_right.setangle(6, right_angle_dict[6] - 30)
    pwm_right.setangle(7, right_angle_dict[7] + 60)
    pwm_right.setangle(8, right_angle_dict[8])
    
def lovely_run(pwm_left, pwm_right):
    for i in xrange(2):
        pwm_left.setangle(8, left_angle_dict[8] + 60)
        pwm_right.setangle(8, right_angle_dict[8] - 60)
        time.sleep(0.2)
        pwm_left.setangle(8, left_angle_dict[8])
        pwm_right.setangle(8, right_angle_dict[8])
        time.sleep(0.2)

def hi_run(pwm_left, pwm_right):
    for i in xrange(2):
        pwm_left.setangle(7, left_angle_dict[7])
        pwm_right.setangle(8, right_angle_dict[8] - 90)
        time.sleep(0.2)
        #pwm_left.setangle(8, left_angle_dict[8])
        pwm_right.setangle(8, right_angle_dict[8])
        time.sleep(0.2)

class TurnUntil:
    pwm_left=0
    pwm_right = 0
    turn_bool = True
    
    def __init__(self):
        print "Init"
        pwm_left = PCA9685(0x40)
        pwm_right = PCA9685(0x41)
        pwm_left.init()
        pwm_right.init()
        pwm_left.setsq(50)
        pwm_right.setsq(50)
        pwm_right.allinit()
        pwm_left.allinit()
        
        self.pwm_left = pwm_left
        self.pwm_right = pwm_right
        #return pwm_left, pwm_right 
    def set_status(self,run_status):
        self.turn_bool = run_status
        

    def WorkRun(self):
        init_site(self.pwm_left, self.pwm_right)
        while(1):
            if self.turn_bool:
                print "Turning"
                left_groups_up(self.pwm_left, self.pwm_right)
                left_groups_down(self.pwm_left, self.pwm_right)
                right_groups_up(self.pwm_left, self.pwm_right)
                right_groups_down(self.pwm_left, self.pwm_right)
            else:
                return
    def Work_Lefthand(self):
        lr_hand_init(self.pwm_left, self.pwm_right)
        while(1):
            if self.turn_bool:
                left_hand_groups(self.pwm_left, self.pwm_right)
            else:
                return
    
    def Work_Righthand(self):
            lr_hand_init(self.pwm_left, self.pwm_right)
            while(1):
                if self.turn_bool:
                    right_hand_groups(self.pwm_left, self.pwm_right)
                else:
                    return 
    def Work_wait(self):
        lovely_groups(self.pwm_left, self.pwm_right) 
        wait_groups(self.pwm_left, self.pwm_right)
    
    def Work_hi(self):
        hi_run(self.pwm_left, self.pwm_right)
    
    def Work_lovely(self):
        lovely_groups(self.pwm_left, self.pwm_right) 
        lovely_run(self.pwm_left, self.pwm_right)
    
    def Work_Stand(self):
        init_site(self.pwm_left, self.pwm_right)
            
        