#!/usr/bin/env python
import rospy
import rospkg
import random
import math
import time
import numpy as np
from std_msgs.msg import String, Int16
import rospkg
import pickle
import os, sys

class RouteCreator:
    def __init__(self):
        rospy.init_node('route_creator', anonymous=True)
        self.arm_pub = rospy.Publisher('/arm_cmd', String, queue_size=2)
        self.debug_pub = rospy.Publisher('/arm_debug', String, queue_size=1)
        rospy.Subscriber('/arm_debug', String, self.create_callback, queue_size=2)
        time.sleep(1)

        rospack = rospkg.RosPack()
        self.PACKAGE_PATH = rospack.get_path("edwin")

        self.route_dictionary = {}
        self.create_route_dictionary()

        self.initialized = False
        print "Initializing"

<<<<<<< HEAD
    def create_route_dictionary(self):
        ##Single set routes
        self.route_dictionary["R_stare"] = "R_stare; 3296, 2308, 999, 0, 0, 0"
        self.route_dictionary["R_ttt"] = "R_ttt; 200, 2400, 1800, 720, 240, 21"
        self.route_dictionary["R_look"] = "R_look; 3664, 1774, 3013, 11, 0, 21"
        self.route_dictionary["R_impat"] = "R_impat; 0, 3621, 4860, 545, 120, 21"
        self.route_dictionary["R_laugh"] = "R_laugh; 1000, 700, 7000, -456, 150, 21, 2000, 2000, 2000, 580, 90, 21, 1500, 1500, 3500, 338, 90, 21, 1700, 1700, 3200, 338, 90, 21, 1500, 1500, 3500, 338, 90, 21, 1700, 1700, 3200, 338, 90, 21, 1500, 1500, 3500, 338, 90, 21, 1700, 1700, 3200, 338, 90, 21"
        self.route_dictionary["R_pretentious_look"] = "R_pretentious_look; 2000, 2000, 1300, 165, 90, 21"
        self.route_dictionary["R_curious"] = "R_curious; 3664, 1774, 3013, 0, 0, 0"
        self.route_dictionary["R_nudge"] = "R_nudge; 2200, 2200, 1700, 630, 270, 21, 2700, 2700, 2200, 57, 240, 21, 2400, 2400, 1700, 569, 270, 21, 2900, 2900, 2200, 22, 270, 21"
        self.route_dictionary["R_sad_turn"] = "R_sad_turn; 1000, -2700, 200, 930, 270, 21"
        self.route_dictionary["R_inhale"] = "R_inhale; 1000, -2700, 1000, 547, 300, 21"
        self.route_dictionary["R_sigh_up"] = "R_sigh_up; 1000, -3000, 1700, 209, 180, 21"
        self.route_dictionary["R_sigh_down"] = "R_sigh_down; 1000, -2500, 0, 940, 165, 21"
        self.route_dictionary["R_curl_up"] = "R_curl_up; 1573, 1574, 1262, 760, 150, 21"
        self.route_dictionary["R_look_distance"] = "R_look_distance; 1000, -2500, 6000, 80, 240, 21"
        self.route_dictionary["R_1_sniff"] = "R_1_sniff; 1000, 4000, -700, 358, 240, 21, 1000, 4000, -700, 298, 270, 21, 1000, 4000, -700, 358, 240, 21, 1000, 4000, -700, 298, 270, 21,  1000, 4000, -700, 358, 240, 21"
        self.route_dictionary["R_2_sniff"] = "R_2_sniff; 4000, -100, -500, 346, 240, 21, 4000, -100, -500, 286, 240, 21, 4000, -100, -500, 346, 240, 21, 4000, -100, -500, 286, 240, 21, 4000, -100, -500, 346, 240, 21"
        self.route_dictionary["R_yawn"] = "R_yawn; 1100, 1100, 7000, -850, 210, 21"
        self.route_dictionary["R_slouch"] = "R_slouch; 2400, 2400, 1000, 602, 210, 21, 2400, 2400, 1000, 151, 240, 21"
        self.route_dictionary["R_scrunch_up"] = "R_scrunch_up; 400, 3500, 300, 186, 240, 21"
        self.route_dictionary["R_head_bobble"] = "R_head_bobble; 3600, -100, 3500, 187, 240, 21, 4000, -100, 5000, 310, 240, 21, 4000, -100, 2000, 117, 240, 21, 4000, -100, 5000, 310, 240, 21, 4000, -100, 2000, 117, 240, 21, 3600, -100, 3500, 187, 240, 21"
        self.route_dictionary["R_squirrel"] = "R_squirrel; 4500, -1200, 5000, -195, 240, 21"
        self.route_dictionary["R_follow_squirrel"] = "R_follow_squirrel; 3000, 4000, 3000, 82, 240, 21"
        self.route_dictionary["R_spin_position"] = "R_spin_position; 1500, 1500, 800, 64, 240, 21"
        self.route_dictionary["R_greet1"] = "R_greet1; 3665, 1774, 3013, 0, 0, 0"
        self.route_dictionary["R_leaving"] = "R_leaving; -2689, 2612, 375, 27, 0, 18"
        self.route_dictionary["R_wakeup"] = "R_wakeup; 0, 3523, 5032, 1, 0, 0"
        self.route_dictionary["R_playful"] = "R_playful; 2027, 981, 98, -11, 0, 72"
        self.route_dictionary["R_sleep"] = "R_sleep; 0, 1891, 1732, 48, 0, 0"

        ##Routes with lists
        self.route_dictionary["R_1_lookaround"] = ["R_1_lookaround; 4000, 1500, 3000, 185, 240, 21", "R_2_lookaround; 500, 4000, 2000, 185, 240, 21", "R_3_lookaround; 3000, 2000, 4000, -39, 240, 21"]
        self.route_dictionary["R_1_weep"] = ["R_1_weep; 1000, -2700, 400, 739, 150, 21", "R_2_weep; 1000, -2700, 300, 819, 150, 21", "R_3_weep; 1000, -2700, 200, 870, 150, 21", "R_4_weep; 1000, -2700, 100, 950, 120, 21", "R_5_weep; 1000, -2700, 0, 1030, 120, 21"]

        pickle.dump(self.route_dictionary.keys(), open(self.PACKAGE_PATH + '/params/routes.txt', 'w'))


    def setup_initial_routes(self):
        inital_routes = ["R_ttt", "R_laugh", "R_yawn"]
        for r in inital_routes:
            msg = "create_route:: " + self.route_dictionary[r]
=======
    def create(self):
        r1 = "R_mv2; 3296, 2308, 999, 0, 0, 0, 200, 2400, 1800, 720, 240, 2, 3296, 2308, 999, 0, 0, 0"
        r2 = "R_look; 2500, 2500, 2000, 186, 240, 21"
        # r3 = "R_impat; 0, 3621, 4860, 545, 120, 21, 576, 3574, 4860, 275, 120, 21, 0, 3621, 4860, 545, 120, 21"
        r3 = "R_impat; 0, 3621, 4860, 545, 120, 21"
        r4 = "R_laugh; 1000, 700, 7000, -456, 150, 21, 2000, 2000, 2000, 580, 90, 21, 1500, 1500, 3500, 338, 90, 21, 1700, 1700, 3200, 338, 90, 21, 1500, 1500, 3500, 338, 90, 21, 1700, 1700, 3200, 338, 90, 21, 1500, 1500, 3500, 338, 90, 21, 1700, 1700, 3200, 338, 90, 21"
        r5 = "R_pretentious_look; 2000, 2000, 1300, 165, 90, 21"
        r6 = "R_ttt; 200, 2400, 1800, 720, 240, 21"
        r7 = "R_nudge; 2200, 2200, 1700, 630, 270, 21, 2700, 2700, 2200, 57, 240, 21, 2400, 2400, 1700, 569, 270, 21, 2900, 2900, 2200, 22, 270, 21"
        r8 = "R_sad_turn; 1000, -2700, 200, 930, 270, 21"
        r9 = "R_inhale; 1000, -2700, 1000, 547, 300, 21"
        r10 = "R_1_weep; 1000, -2700, 400, 739, 150, 21"
        r11 = "R_2_weep; 1000, -2700, 300, 819, 150, 21"
        r12 = "R_3_weep; 1000, -2700, 200, 870, 150, 21"
        r13 = "R_4_weep; 1000, -2700, 100, 950, 120, 21"
        r14 = "R_5_weep; 1000, -2700, 0, 1030, 120, 21"
        r15 = "R_sigh_up; 1000, -3000, 1700, 209, 180, 21"
        r16 = "R_sigh_down; 1000, -2500, 0, 940, 165, 21"
        r17 = "R_curl_up; 1573, 1574, 1262, 760, 150, 21"
        r18 = "R_look_distance; 1000, -2500, 6000, 80, 240, 21"
        r19 = "R_1_sniff; 1000, 4000, -700, 358, 240, 21, 1000, 4000, -700, 298, 270, 21, 1000, 4000, -700, 358, 240, 21, 1000, 4000, -700, 298, 270, 21,  1000, 4000, -700, 358, 240, 21"
        r20 = "R_2_sniff; 4000, -100, -500, 346, 240, 21, 4000, -100, -500, 286, 240, 21, 4000, -100, -500, 346, 240, 21, 4000, -100, -500, 286, 240, 21, 4000, -100, -500, 346, 240, 21"
        r21 = "R_yawn; 1100, 1100, 7000, -850, 210, 21"
        r22 = "R_slouch; 2400, 2400, 1000, 602, 210, 21, 2400, 2400, 1000, 151, 240, 21"
        r23 = "R_scrunch_up; 400, 3500, 300, 186, 240, 21"
        r24 = "R_1_lookaround; 4000, 1500, 3000, 185, 240, 21"
        r25 = "R_2_lookaround; 500, 4000, 2000, 185, 240, 21"
        r26 = "R_3_lookaround; 3000, 2000, 4000, -39, 240, 21"
        r27 = "R_head_bobble; 3600, -100, 3500, 187, 240, 21, 4000, -100, 5000, 310, 240, 21, 4000, -100, 2000, 117, 240, 21, 4000, -100, 5000, 310, 240, 21, 4000, -100, 2000, 117, 240, 21, 3600, -100, 3500, 187, 240, 21"
        r28 = "R_squirrel; 4500, -1200, 5000, -195, 240, 21"
        r29 = "R_follow_squirrel; 3000, 4000, 3000, 82, 240, 21"
        r30 = "R_spin_position; 1500, 1500, 800, 64, 240, 21"
        r31 = "R_disbelief; 0, 2000, 5000, 566, 240, 21"
        r32 = "R_pout; -3367, 1977, 2498, -240, 297, 21"
        r33 = "R_look_back; 2000, 1500, 1000, 21, 0, 21"
        r34 = "R_impatient; 0, 2000, 6000, 597, 210, 21, 0, 4700, 2500, 849, 240, 21, 0, 2000, 6000, 597, 210, 21, 0, 4700, 2500, 849, 240, 21, 0, 2000, 6000, 597, 210, 21"
        r35 = "R_annoyed_nudge; 3000, 2800, 4500, 477, 211, 21, 3500, 3300, 4000, 475, 210, 21, 3000, 2800, 4500, 477, 211, 21"
        r36 = "R_bored; 2500, 2500, 5000, -490, -151, 21, -2500, 2500, 5000, -492, 747, 21, 2500, 2500, 5000, -490, -151, 21, -2500, 2500, 5000, -492, 747, 21"
        r37 = "R_stare_away; 4000, -2000, 2000, 41, 270, 21"

        routes = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, r32, r33, r34, r35, r36, r37]


        for r in routes:
            msg = "create_route:: " + r
>>>>>>> 242f4c7c7b7afed541c35ec8e622c39fc76ece12
            print "Sending message: ", msg
            self.arm_pub.publish(msg)
            time.sleep(.5)

        self.debug_pub.publish("ROUTE CREATE DONE")


    def create_callback(self, cmd_raw):
        # self.create_route_dictionary()
        if "HOMING DONE" in cmd_raw.data:
            self.setup_initial_routes()
            self.initialized = True
            return

        if self.initialized == False:
            return

        if "RUN FAILED" in cmd_raw.data:
            missed_route = cmd_raw.data.split(" ")[1]
        elif "NOT DEFINED" in cmd_raw.data:
            missed_route = cmd_raw.data.split(" ")[1][:-1]
        else:
            return

        print "MISSED ROUTE: ", missed_route
        route = self.route_dictionary.get(missed_route, None)

        if route == None:
            print "Route: " + missed_route + " not found"
            return
        elif type(route) == list:
            for r in routes:
                msg = "create_route:: " + r
                print "Sending message: ", msg
                self.arm_pub.publish(msg)
        elif type(route) == str:
            msg = "create_route:: " + route
            print "Sending message: ", msg
            self.arm_pub.publish(msg)

        time.sleep(1.5)
        self.arm_pub.publish("run_route:: " + route.split(";")[0])

    def run(self):
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            r.sleep()

if __name__ == '__main__':
    rc = RouteCreator()
    rc.run()
