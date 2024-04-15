# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:03:10 2023

@author: mmanc
"""

import sympy
from einsteinpy.symbolic import MetricTensor, ChristoffelSymbols, RiemannCurvatureTensor

sympy.init_printing()  # enables the best printing available in an environment
#%%
# =============================================================================
# Polar coordinates
# =============================================================================
#defining the metric for wich we want to compute the Christoffel symbol
syms = sympy.symbols('r theta ')
metric = [[0 for i in range(2)] for i in range(2)]
metric[1][1] = 1
metric[0][0] = syms[0]**2
# creating metric object
m_obj = MetricTensor(metric, syms)
m_obj.tensor()
print(m_obj) # printing metric 
#%%
#finding christoffel symble 
ch = ChristoffelSymbols.from_metric(m_obj)
ch.tensor()

# note 0 = r and 1 = theta

print(ch.tensor()[0,1,1])
print(ch.tensor()[1,0,0])
print(ch.tensor()[1,1,0])
print(ch.tensor()[0,0,1])

# this is the same as we have obtained by had all the Christoffel symbles are zero given
# the above metric
#%%
# =============================================================================
# Spherical Coordinates
# =============================================================================
syms = sympy.symbols('r theta phi')
# define the metric for 3d spherical coordinates
metric = [[0 for i in range(3)] for i in range(3)]
metric[0][0] = 1
metric[1][1] = syms[0]**2
metric[2][2] = (syms[0]**2)*(sympy.sin(syms[1])**2)
# creating metric object
m_obj = MetricTensor(metric, syms)
m_obj.tensor()
#%%
#finding christoffel symble 
ch = ChristoffelSymbols.from_metric(m_obj)
ch.tensor()

# note 0 = r, 1 = theta and 2 = phi

index_name = {'r':0, 'θ':1, 'φ':2}
print('The non-zero Christoffel symbols are:')
print('')
for i in index_name:
    for j in index_name:
        for k in index_name:
            symbol = ch.tensor()[index_name[i],index_name[j],index_name[k]]
            indices = [i,j,k]
            
            if symbol != 0:
                
                print(indices, '=', symbol)
                print('')
            else:
                print(indices, '=', symbol )
                print('')
            
print('')
print('The rest of the Christoffel symbols are zero')






