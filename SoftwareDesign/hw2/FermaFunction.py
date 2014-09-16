# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:20:49 2014

@author: leo
"""

def fermat(q, w, e, r):
  
    s = q**r
    f = w**r
    d = e**r
    t = s + f
   
   print "%d + %d = %d = %d" % (s, f, t, d)

    if r > 1:
        if t == d:
            print 'Fermat was wrong!'

        else:
            print "No that doesn't work"

    else:
        print 'No that doesnt work, n<2'


def ask_inputs():
    
    print "WELCOME TO THE FERMAT CHECKER!\n"
    
    q = raw_input('what is a?\n')
    q = int(q)

    w = raw_input('what is b?\n')
    w = int(w)

    e = raw_input('what is c?\n')
    e = int(e)

    r = raw_input('what is n?\n')
    r = int(r)
    
    fermat(q, w, e, r)

ask_inputs()