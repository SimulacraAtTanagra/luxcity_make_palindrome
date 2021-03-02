# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:51:13 2021

@author: shane
"""

"""a function to make a palindrome out of a string that can have one character
dropped, or returns that it can't be done in one step. 

Created in response to challenge for luxcity game
"""

def make_palindrome(s):
    #check if string is already a palindrome
    if s==s[::-1]:
        return('done')
    #for loop to check if removing any single character creates a palindrome
    for ix,i in enumerate(s):
        newstr=''.join([x for yx,x in enumerate(s) if yx!=ix])
        if newstr==newstr[::-1]:
            return(newstr)    
    #if not, return the bad news
    else:
        return('no way')