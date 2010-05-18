#!/usr/bin/env python3
# Chapter 6: global/local explanation.

def spam(myName):
    print('Hello, ' + myName)
    myName = 'Waffles'
    print('Your new name is ' + myName)

myName = 'Albert'
spam(myName)
print('Howdy, ' + myName)
