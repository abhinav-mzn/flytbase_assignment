#!/usr/bin/env python

import time
from flyt_python import api

print '\nAssignment Task 1 by Abhinav Kumar\n'

drone = api.navigation()

time.sleep(5)

sq_side = 5.0
t_off_h = 5.0

print 'taking off'
drone.take_off(t_off_h)

print 'moving in north'
drone.position_set(sq_side, 0, 0, relative=True)
print 'moving in east'
drone.position_set(0, sq_side, 0, relative=True)
print 'moving in south'
drone.position_set(-sq_side, 0, 0, relative=True)
print 'moving in west'
drone.position_set(0, -sq_side, 0, relative=True)

print 'landing'
drone.land()

drone.disconnect()
