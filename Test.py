# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:53:00 2017

@author: akash
"""


#You are given a string S. 
#Your task is to find out if the string  contains: alphanumeric characters, 
#alphabetical characters, digits, lowercase and uppercase characters.

#Output Format
#
#In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
#In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
#In the third line, print True if  has any digits. Otherwise, print False. 
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

#Sample Input:qA2
#Output: 
#    
#True
#True
#True
#True
#True

if __name__ == '__main__':
    string = raw_input()

    list_1 = list()
    
    total = 0
    
    for elem in string:
        list_1.append(elem.isalnum())
        list_2 = list()
        for elem in list_1:
            if elem == True:
                list_2.append(1)
            else:
                list_2.append(0)
                
    total = sum(list_2)
    if total >= 1:
        print(True)
        
    total_alpha = 0
    
    list_alpha = list()
        
    for elem in string:
        list_alpha.append(elem.isalpha())
        list_2_alpha = list()
        for elem in list_alpha:
            if elem == True:
                list_2_alpha.append(1)
            else:
                list_2_alpha.append(0)
                
    total_alpha = sum(list_2_alpha)
    if total_alpha >= 1:
        print(True)
    else:
        print(False)
        
        
    total_digit = 0
    
    list_digit= list()
        
    
    for elem in string:
        list_digit.append(elem.isdigit())
        list_2_digit = list()
        for elem in list_digit:
            if elem == True:
                list_2_digit.append(1)
            else:
                list_2_digit.append(0)
                
    
                
    total_digit = sum(list_2_digit)
    if total_digit >= 1:
        print(True)
    else:
        print(False)  
        
        
        
    total_lower = 0
    
    list_lower= list()
        
    
    for elem in string:
        list_lower.append(elem.islower())
        list_2_lower = list()
        for elem in list_lower:
            if elem == True:
                list_2_lower.append(1)
            else:
                list_2_lower.append(0)
                
    
                
    total_lower = sum(list_2_lower)
    if total_lower >= 1:
        print(True)
    else:
        print(False) 
        
        
    
    total_upper = 0
    
    list_upper= list()
        
    
    for elem in string:
        list_lower.append(elem.islower())
        list_2_upper = list()
        for elem in list_upper:
            if elem == True:
                list_2_upper.append(1)
            else:
                list_2_upper.append(0)
                
    
                
    total_upper = sum(list_2_upper)
    if total_lower >= 1:
        print(True)
    else:
        print(False)
    
    

    


    

    
    
    

    

    


        
        
            

            




