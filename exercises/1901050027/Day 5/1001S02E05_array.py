# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 13:47:06 2019

@author: PetalSaya
"""

Array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Array.reverse() #Step1
Step2_1 = [str(element)for element in Array]
Step2_2 = ''.join(Step2_1)
Step3 = Step2_2[2:8]
Step4 = list(Step3)
Step4.reverse() #Step5
Array_new=[]
for element in Step4:
    Array_new.append(int(element)) #Step6
for bin_element in Array_new:
    print (bin_element, bin(bin_element))
for oct_element in Array_new:
    print (oct_element, oct(oct_element))
for hex_element in Array_new:
    print (hex_element, hex(hex_element))