import numpy as np
import auxiliary_methods as am

test1_points = np.array([2,5,1])
test1_a = 6
test1_b = 9
test1_phi = np.pi/2

test2_points = np.array([-2,8,1])
test2_a = 5
test2_b = 7
test2_phi = np.pi

print("test 1= {}".format(am.rotate_around_point(test1_points,test1_a,test1_b,test1_phi)))

print("test 2 = {}".format(am.rotate_around_point(test2_points,test2_a,test2_b,test2_phi)))