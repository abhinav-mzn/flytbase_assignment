#!/usr/bin/env python

import time
from math import pi, sin, cos
from flyt_python import api

print '\nAssignment Task 2 by Abhinav Kumar\n'

drone = api.navigation()

time.sleep(5)

tr_side = 10.0
t_off_h = 10.0

print 'taking off'
drone.take_off(t_off_h)

print 'covering side one'
drone.position_set(tr_side*sin(pi/3), tr_side*cos(pi/3), 0, relative=True)
print 'covering side two'
drone.position_set(tr_side*sin(-pi/3), tr_side*cos(-pi/3), 0, relative=True)
print 'covering side three'
drone.position_set(tr_side*sin(pi), tr_side*cos(pi), 0, relative=True)

print 'landing'
drone.land()

drone.disconnect()
