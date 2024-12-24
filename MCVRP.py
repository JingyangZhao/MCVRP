# -*- coding: utf-8 -*-
"""
# calculate the approximation ratio of MCVRP 
@author: Administrator
"""
import math
############################################################################################################################################
def zeta(rho, tau, epsilon):
    return (3*rho+tau-4*tau*rho)/(1-rho) + epsilon/(tau*rho)*(1-tau*rho-(3*rho+tau-4*tau*rho)/(1-rho))
############################################################################################################################################
def function(rho, tau, epsilon):
    theta = 1-tau
    return (1+zeta(rho,tau,epsilon))/theta + (1-tau-theta)/(theta*(1-tau)) + 3*epsilon/(1-theta) + 3*rho/(1-rho)/(1-tau) - 1
############################################################################################################################################
def f(epsilon): # t,r<=1/6
    min_found=1000
    for i in range(1667):
        for j in range(1667):
            rho=(i+1)/10000; tau=(j+1)/10000
            tem = function(rho, tau, epsilon)
            if min_found > tem: min_found = tem
    return min_found
############################################################################################################################################
#""" splittable
if 1:
    epsilon=1/3000
    g=f(epsilon) # f(epsilon) in the paper
    print(3+2*f(epsilon)); print(4-2*epsilon)
    
    if 4-2*epsilon < 3+2*g: print("epsilon should be smaller")
    else: print("epsilon can be bigger")
############################################################################################################################################
### unsplittable
elif 0:
    epsilon=1/100000
    g=f(epsilon) # f(epsilon) in the paper
    print(3+math.log(2)+2*g); print(4-2*epsilon)
    
    if 4-2*epsilon < 3+math.log(2)+2*g: print("epsilon should be smaller")
    else: print("epsilon can be bigger")
############################################################################################################################################
### splittable with fixed capacity
elif 0:
    epsilon=1/9000
    g=f(epsilon) # f(epsilon) in the paper
    print(3+2*g); print(3+math.log(2)-epsilon)
    
    if 3+math.log(2)+math.log(1-epsilon) < 3+2*g: print("epsilon should be smaller")
    else: print("epsilon can be bigger")
#"""
