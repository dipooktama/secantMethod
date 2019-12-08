#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fungsinya(x):
    fx = x**2 - 6*x + 8
    return fx


# In[2]:


def xBaru(x1,fx1,x2,fx2):
    xNew = x2 - ((fx2)*(x2-x1))/(fx2 - fx1)
    return xNew


# In[3]:


def secant(x1,x2,fxVal):
    fxbaru = fxVal-1
    i = 1
    while fxbaru != fxVal:
        fx1 = fungsinya(x1)
        fx2 = fungsinya(x2)
        xB = xBaru(x1,fx1,x2,fx2)
        fxbaru = fungsinya(xB)
        print('\nIterasi ke-',i)
        print('x1 : {} dan F(x1) : {}'.format(x1,fx1))
        print('x2 : {} dan F(x2) : {}'.format(x2,fx2))
        print('x baru : {} dan F(xbaru) : {}'.format(xB,fxbaru))
        if fxbaru == fxVal:
            print('\nakarnya ada di iterasi ke-',i)
            print('di titik x1 : {} dan titik x2 : {}'.format(x1,x2))
            break
        else:
            x1 = x2
            x2 = xB
        i+=1

# In[4]:


def secantError(x1,x2,errHold):
    errVal = errHold+1
    i = 1
    while errVal > errHold:
        fx1 = fungsinya(x1)
        fx2 = fungsinya(x2)
        xB = xBaru(x1,fx1,x2,fx2)
        errVal = abs(xB-x2)
        print('\nIterasi ke-',i)
        print('x1 : {} dan F(x1) : {}'.format(x1,fx1))
        print('x2 : {} dan F(x2) : {}'.format(x2,fx2))
        print('x baru : {} dan nilai errornya : {}'.format(xB,errVal))
        if errVal == errHold:
            print('\nakarnya ada di iterasi ke-',i)
            print('di titik x1 : {} dan titik x2 : {}'.format(x1,x2))
            break
        else:
            x1 = x2
            x2 = xB
        i+=1

# in[5]:

x1Val = float(input('Masukkan nilai x1 : '))
x2Val = float(input('Masukkan nilai x2 : '))
fxValue = float(input('Masukkan patokan nilai F(x) : '))
errValue = float(input('Masukkan nilai error : '))

# in[6]:
print("\n\n==================== Metode Secant, patokan F(x) ==========================")
secant(x1Val,x2Val,fxValue)
print("\n\n==================== Metode Secant, patokan error ==========================")
secantError(x1Val,x2Val,errValue)