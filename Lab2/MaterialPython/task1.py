import numpy as np
import matplotlib.pyplot as plt
import unittest

def rotate_around_point(p, a, b, phi):
    p = np.append(p, 1)
    translation = np.identity(3)
    translation[0:2,2] = np.array([a,b])
    back_translation = np.identity(3)
    back_translation[0:2, 2] = np.array([-a,-b])
    rotation = np.identity(3)
    rotation[0:2, 0:2] = np.array([[np.cos(phi), -np.sin(phi)], [np.sin(phi), np.cos(phi)]])
    return translation.dot(rotation).dot(back_translation).dot(p)[0:2]

def rectangle(x,y,sx,sy,phi):
    x1 = x-sx/2
    x2 = x+sx/2
    y1 = y-sy/2
    y2 = y+sy/2

    x1r, y1r = rotate_around_point([x1,y1], x, y, phi)[0:2]
    x2r, y2r = rotate_around_point([x2,y1], x, y, phi)[0:2]
    x3r, y3r = rotate_around_point([x2,y2], x, y, phi)[0:2]
    x4r, y4r = rotate_around_point([x1,y2], x, y, phi)[0:2]

    return np.array([[x1r,x2r,x3r,x4r,x1r],[y1r,y2r,y3r,y4r,y1r]])



class TestRotateAroundPoint(unittest.TestCase):
    def test_rotate_around_point(self):
        act1 = rotate_around_point(np.array([2,5,1]), 6, 9, np.pi/2) 
        exp1 = np.array([10, 5, 1])
        test1 = act1 == exp1
        act2 = rotate_around_point(np.array([-2 ,8 ,1]), 5, 7, np.pi) 
        exp2 = np.array([12, 6, 1])
        test2 = act2 == exp2 
        self.assertEqual(True, test1.all(), f'act: {act1}, exp: {exp1}')
        self.assertEqual(True, test2.all(), f'act: {act2}, exp: {exp2}')

    def test_rectangle(self):
        act = rectangle(0, 0, 1, 1, 0)
        plt.plot(*act, 'r')
        plt.show()




if __name__ == '__main__':
    unittest.main()