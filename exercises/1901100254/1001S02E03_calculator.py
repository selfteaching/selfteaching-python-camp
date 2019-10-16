#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import re

def refresh_formula(formula):
    formula = formula.replace(" ","")
    formula = formula.replace("+-","-")
    formula = formula.replace("--","+")
    return formula

def devide(formula):
    devidestr = re.search('\d+\.?\d*(\/-?\d+\.?\d*)+', formula)
    if devidestr is None:
        return formula
    devidenum = re.findall('-?\d+\.?\d*',devidestr.group())
    devidelist = []
    for i in devidenum:
        devidelist.append(float(i))
    res = devidelist[0]
    for i in range(1,len(devidelist)):
        res = res / devidelist[i]
    formula = re.sub('\d+\.?\d*(\/-?\d+\.?\d*)+', str(res), formula, 1)
    return formula

def multiply(formula):
    multiplystr = re.search('\d+\.?\d*(\*-?\d+\.?\d*)+', formula)
    if multiplystr is None:
        return formula
    multiplynum = re.findall(r'-?\d+\.?\d*', multiplystr.group())
    multiplylist =[]
    res = 1
    for i in multiplynum:
        multiplylist.append(float(i))
    for i in range(len(multiplylist)):
        res = res * multiplylist[i]
    formula = re.sub(r'\d+\.?\d*(\*-?\d+\.?\d*)+', str(res), formula, 1)
    return formula


def total_calc(formula):
    formula = refresh_formula(formula)
    res = 0
    while True:
        if '*' in formula:
            mul = formula.split("*")
            if '/' in mul[0]:
                formula = devide(formula)
            else:
                formula = multiply(formula)
        elif '/' in formula:
            formula = devide(formula)
        elif '+' or '-' in formula:
            addminus = re.findall('-?\d+\.?\d*',formula)
            res = 0
            for digit in addminus:
                res = res + float(digit)
            return str(res)
        else:
            return res

def bracket_calc(bracketstr):
    bracketstr = bracketstr.replace("\(","")
    bracketstr = bracketstr.replace("\)","")
    return total_calc(bracketstr)

def calculate(formula):
    while True:
        bracket = re.search("\(([^()]+)\)",formula)
        #print(formula)
        #print(bracket)
        if bracket:
            bracket = bracket.group()
            #print(bracket)
            res = bracket_calc(bracket)
            formula = formula.replace(bracket,res)
        else:
            res = total_calc(formula)
            print("result is %s" % res)
            break

if __name__ == "__main__":
    while True:
        formula = input("Please input formula: ")
        if formula == "exit" or formula == "Exit":
            exit()
        else:
            formula = refresh_formula(formula)
            calculate(formula)
