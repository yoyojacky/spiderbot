# coding=utf-8
import sys
import time
from action_groups import *

reload(sys)
sys.setdefaultencoding('utf-8')

RobotWork = TurnUntil()

lr_hand_init(RobotWork.pwm_left, RobotWork.pwm_right)
for i in range(4):
    #left_groups_up(RobotWork.pwm_left, RobotWork.pwm_right)
    #left_groups_down(RobotWork.pwm_left, RobotWork.pwm_right)
    #right_groups_up(RobotWork.pwm_left, RobotWork.pwm_right)
    #right_groups_down(RobotWork.pwm_left, RobotWork.pwm_right)
    #pass
    #left_hand_groups(RobotWork.pwm_left, RobotWork.pwm_right)
    right_hand_groups(RobotWork.pwm_left, RobotWork.pwm_right)
    #rigth_hand_up(RobotWork.pwm_left, RobotWork.pwm_right)
    #time.sleep(0.1)
#lr_hand_init(RobotWork.pwm_left, RobotWork.pwm_right)
#init_site(RobotWork.pwm_left, RobotWork.pwm_right)
#wait_groups(RobotWork.pwm_left, RobotWork.pwm_right)

#lovely_groups(RobotWork.pwm_left, RobotWork.pwm_right)
#hi_run(RobotWork.pwm_left, RobotWork.pwm_right)