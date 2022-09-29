import string
import secrets


def genPass():
    symbols=["!","@","#","$","%","&","*","^"]
    length=15
    p=""
    for i in range(length):
        #get random int to figure if char is going to be letter, number, or symbol
        c=secrets.choice(range(0,3))
        
        #takes num c and translates it into what char type it will be
        if(c==0):
            p+=str(secrets.choice(string.ascii_letters))
       
        elif(c==1):
            p+=str(secrets.choice(symbols))
        elif(c==2):
            p+=str(secrets.choice(range(0, 9)))
    
    
    
    return p

#checks to see if a string has numbers.        
def hasNum(s):
    for char in s:
        if char.isdigit():
            return True
    return False

#check to see if string has letters
def hasLetters(s):
    for char in s:
        if char.isalpha():
            return True
    return False

#checks to see if a string has symbols
def hasSym(s):
     symbols=["!","@","#","$","%","&","*","^"]
     for char in s:
         if char in symbols:
             return True
     return False
#tests strength of password by looking at length, letters, numbers, and symbols and returns
#what the results by list
def passTest(p):

    l=hasLetters(p)
   
    n=hasNum(p)
  
    s=hasSym(p)
  
    if(l and n and s):
        return True
    else:
        return False
    
#uses the genPass method and the checks it and makes sure the password meets requirements and if not it will regen
def genCheck():
    while(True):
        p=genPass()
        c=passTest(p)
    
        if (c==True):
            return p
    

