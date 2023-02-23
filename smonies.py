# -*- coding: utf-8 -*-
"""
Created on %(Date: 18 Feb 2023)s
@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M05 Lab - Case Study: Containers and CI/CD
"""

import emoji

rateOfPay = float(input(emoji.emojize(":money_with_wings: How much do you make per hour? : $")))
hours = float(input(emoji.emojize(":alarm_clock: How many hours did you work for the week? : ")))


if hours > 40:
	grossPay = 40 * rateOfPay + (hours-40) * (rateOfPay * 1.5)
else:
	grossPay = hours * rateOfPay
    
percentage = .20
taxes = grossPay * percentage
netPay = grossPay - taxes

print(emoji.emojize(":heavy_dollar_sign: Before taxes, your gross pay this week so far is $" + format(grossPay, ".2f") + "."))
print(emoji.emojize(":heavy_dollar_sign: After 20% taxes, your net pay will be " + format(netPay, ".2f") + "."))
