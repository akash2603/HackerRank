# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:30:29 2018

@author: akash
"""

#You are asked to ensure that the first and last names of people begin with a 
#capital letter in their passports. For example, alison heck should be capitalised 
#correctly as Alison Heck.


def capitalize(string):
    for x in string[:].split():
        string = string.replace(x, x.capitalize())
    return string        



#    

