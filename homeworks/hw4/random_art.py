# -*- coding: utf-8 -*-
"""
Random_art.py

@author: leo
"""

# you do not have to use these particular modules, but they may help
from random import randint
#import Image
from PIL import Image
import math
#from swampy.TurtleWorld import *
import random

def X(x,y):
    return x
    
def Y(x,y):
    return y

def cos_pi(y):
    return math.cos(math.pi*y)
    
def sin_pi(x):
    return math.sin(math.pi*x)

def times(x,y):  
    return x*y

def square(x):
    return x*x

def root(y):
    return math.sqrt(abs(y))
    
def funct_last_choose():
    k=randint(1,2)
    if k==1:
        t = 'x'
        return t
    elif k==2:
        t = 'y'
        return t

def funct_choose():
    k=randint(1,5)
    if k==1:
        return "sin_pi"
    elif k==2:
        return "cos_pi"
    elif k==3:
        return "times"
    elif k==4 :
        return "root"
    elif k==5 : 
        return "square"
  
def recursive_generate(depth):
    
    if depth == 1 :
        return funct_last_choose()
    elif depth > 1: 
        s = funct_choose()      
        if s == 'times':
            return [s,recursive_generate(depth-1),recursive_generate(depth-1)]
        else:
            return [s,recursive_generate(depth-1)]
         
def build_random_function(min_depth, max_depth):
    
    depth = randint(min_depth,max_depth)   
    return recursive_generate(depth)    
    
    #first i ask the program if it is the last depth in the tree, if it is i choose a variable : 
       # x or y. if the depth is dfunct_choose()eeper, like 1, the program can chose one the fonction thats depth 
       # is one (like cos or sin) and then if the depth is even deeper, it can chose between cos sin 
       # and times. it compute all of this in one equation"""
   
gg = build_random_function(3,6)
print gg

def evaluate_random_function(f, x, y):
    """ your doc string goes here
    """
    if (f[0]=='x'):
        return X(x,y)
    elif (f[0]=='y'):
        return Y(x,y)
    elif (f[0]=='sin_pi'):
        return sin_pi(evaluate_random_function(f[1],x,y))
    elif (f[0]=='cos_pi'):
        return cos_pi(evaluate_random_function(f[1],x,y))
    elif (f[0]=='times'):
        return times(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    elif (f[0]=='root'):
        return root(evaluate_random_function(f[1],x,y))
    elif (f[0]=='square'):
        return square(evaluate_random_function(f[1],x,y))

print evaluate_random_function(gg, 2, 9)


def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
        TODO: please fill out the rest of this docstring
    """
    convert = float (val - input_interval_start) / float ( input_interval_end - input_interval_start)
    output1 = output_interval_start + convert* (output_interval_end - output_interval_start)
    return output1
    
canvas = Image.new("RGB", (350, 350))   
green=build_random_function(5,10)    # build a random function for each color
blue=build_random_function(2,10)
red =build_random_function(5,10)    
for x in range(0, 349):
    for y in range(0,349):
        red1 = remap_interval(evaluate_random_function(red, remap_interval(x, 0, 349, -1,1),remap_interval(y, 0, 349, -1,1)),-1,1 ,0, 254)
        green1 = remap_interval(evaluate_random_function(green ,remap_interval(x, 0, 349, -1,1),remap_interval(y, 0, 349, -1,1)),-1,1 ,0, 254)
        blue1 = remap_interval(evaluate_random_function(blue, remap_interval(x, 0, 349, -1,1),remap_interval(y, 0, 349, -1,1)),-1,1 ,0, 254)
        # remap the interval from 0 to 349 to -1 to 1, for each color and remap again from -1 to 1 to 0 to 254 for the differents colors
        print blue1
        canvas.putpixel((x,y),(int(red1),int(green1),int(blue1)))
        

canvas.save("imgexemple10.png", "PNG")     # save the image in a file called imgexemple.png