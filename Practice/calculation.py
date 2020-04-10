# -*- coding: utf-8 -*-
# author: Guangqiang Lu time:2019/12/4
# all the codes below are written by myself.

import numpy as np

def angle(x, y):

    if len(x) != len(y):
        raise Exception('The two vectors have unequal numbers of dimensions!' )

    else:
        X = np.array(x)
        Y = np.array(y)

        dot = np.dot(X,Y)
        abs_x = np.sqrt(np.dot(X,X))
        abs_y = np.sqrt(np.dot(Y,Y))
        cos_value = dot / (abs_x * abs_y)
        angle = np.arccos(cos_value)
        return angle * 180 / np.pi

def main():

    x_axis = [(1,0,0), (0,1,0), (0,0,1), (2,2,1), (1,2,0), (3,1,0)] #Sb2S3 planes
    y_axis = [(1,0,0), (0,1,0), (0,0,1), (1,0,1), (2,1,1),(3,0,1),(1,3,0)] #Sb2S3 planes

    print('            ', x_axis)
    for y in y_axis:
        print(str(y), end="  ")
        for x in x_axis:
            print('%9.2f' %angle(y, x), end = "  ")
        print()
    print()

    x_axis = [(1,0,0), (0,1,0), (0,0,1), (1,0,1)]#TiO2 planes
    y_axis = [(1,0,0), (0,1,0), (0,0,1), (1,0,1), (1,1,0), (0,1,1)]#TiO2 planes

    print('            ', x_axis)
    for y in y_axis:
        print(str(y), end = "  ")
        for x in x_axis:
            print('%9.2f' %angle(y, x), end = "  ")
        print()

if __name__ == "__main__":
    main()
