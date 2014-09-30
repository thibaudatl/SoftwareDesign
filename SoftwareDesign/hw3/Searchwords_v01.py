# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 14:01:33 2014

@author: leo
"""

y = raw_input('In which file would you like to look ? (give the full path of the file)  ')

try :
    liste=file("" +y , "r").readlines()
except IOError :
    print 'There is no such file, sorry'

output = file("/home/leo/SoftwareDesign/hw3/outfile.txt","w") 
x = len(liste)
z = raw_input('press 1 to be polite or press 2 to be a jerk :')   
    
def bepolite(a) :
    curse = {'shit', 'fuck','fucker','ass', 'ass face', 'arsehole', 'asses', 'sucker', 'assfucker', 'butt', 'assshole','bastard','bitch','bitches'} 
    # list of words i want to change
    for word in curse:                      #searching line after line in all the file
        a = a.replace(word, 'peace')        # replace the words by peace
    return a                                #return all lines changed
    
def beajerk(b):
    kind = {'love', 'enjoy', 'like', ' likes', 'loves', 'enjoying', 'happy', 'nice'}  
        # LIST of words i'm looking for    
    for word in kind:
            b = b.replace(word, 'hate')   # replace the words by ...
    return b
   
def main(z):
    if z==1 :    
        for line in liste :
            newline=bepolite(line)    # put all lines into a variable
            output.write(newline)     # writte into a new document called output
            print newline
        print x 
  
    elif z ==2  :
        print (' Thanks for choosing the Be A Jerk option')    
        for line in liste :
            newline1 = beajerk(line)   
            output.write(newline1)
            print newline1
        print x   #number of lines of the document
    else : 
        print ('don t be stupid, reselect')
    
main(int(z))
output.close()
        
        
                            # close the output file
   
    

   
    
