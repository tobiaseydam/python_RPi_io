# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:29:25 2019

@author: Tobias
"""

from .models import gpioPin

def initPins():
    p01 = gpioPin(pin =  1, row =  0, func1 = "3V3",    func2 = "Power",         color = "red",    connectable = False)
    p02 = gpioPin(pin =  2, row =  0, func1 = "5V",     func2 = "Power",         color = "red",    connectable = False)
    p03 = gpioPin(pin =  3, row =  1, func1 = "GPIO2",  func2 = "SDA1 I2C",      color = "yellow", connectable = False)
    p04 = gpioPin(pin =  4, row =  1, func1 = "5V",     func2 = "Power",         color = "red",    connectable = False)
    p05 = gpioPin(pin =  5, row =  2, func1 = "GPIO13", func2 = "SCL1 I2C",      color = "yellow", connectable = False)
    p06 = gpioPin(pin =  6, row =  2, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p07 = gpioPin(pin =  7, row =  3, func1 = "GPIO4",  func2 = "",              color = "green",  connectable = False)
    p08 = gpioPin(pin =  8, row =  3, func1 = "GPIO14", func2 = "UART0_TXD",     color = "blue",   connectable = False)
    p09 = gpioPin(pin =  9, row =  4, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p10 = gpioPin(pin = 10, row =  4, func1 = "GPIO15", func2 = "UART0_RXD",     color = "blue",   connectable = False)
    p11 = gpioPin(pin = 11, row =  5, func1 = "GPIO17", func2 = "",              color = "green",  connectable = False)
    p12 = gpioPin(pin = 12, row =  5, func1 = "GPIO18", func2 = "PCM_CLK",       color = "green",  connectable = False)
    p13 = gpioPin(pin = 13, row =  6, func1 = "GPIO27", func2 = "",              color = "green",  connectable = False)
    p14 = gpioPin(pin = 14, row =  6, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p15 = gpioPin(pin = 15, row =  7, func1 = "GPIO22", func2 = "",              color = "green",  connectable = False)
    p16 = gpioPin(pin = 16, row =  7, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p17 = gpioPin(pin = 17, row =  8, func1 = "3V3",    func2 = "Power",         color = "red",    connectable = False)
    p18 = gpioPin(pin = 18, row =  8, func1 = "GPIO24", func2 = "",              color = "green",  connectable = False)
    p19 = gpioPin(pin = 19, row =  9, func1 = "GPIO10", func2 = "SPI0_MOSI",     color = "blue",   connectable = False)
    p20 = gpioPin(pin = 20, row =  9, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p21 = gpioPin(pin = 21, row = 10, func1 = "GPIO9",  func2 = "SPI0_MISO",     color = "blue",   connectable = False)
    p22 = gpioPin(pin = 22, row = 10, func1 = "GPIO25", func2 = "",              color = "green",  connectable = False)
    p23 = gpioPin(pin = 23, row = 11, func1 = "GPIO11", func2 = "SPI0_SCLK",     color = "blue",   connectable = False)
    p24 = gpioPin(pin = 24, row = 11, func1 = "GPIO8",  func2 = "SPI0_CE0_EN",   color = "blue",   connectable = False)
    p25 = gpioPin(pin = 25, row = 12, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p26 = gpioPin(pin = 26, row = 12, func1 = "GPIO7",  func2 = "SPI0_CE0_EN",   color = "blue",   connectable = False)
    p27 = gpioPin(pin = 27, row = 13, func1 = "ID_SD",  func2 = "I2C ID EEPROM", color = "yellow", connectable = False)
    p28 = gpioPin(pin = 28, row = 13, func1 = "ID_SC",  func2 = "I2C ID EEPROM", color = "yellow", connectable = False)
    p29 = gpioPin(pin = 29, row = 14, func1 = "GPIO5",  func2 = "",              color = "green",  connectable = False)
    p30 = gpioPin(pin = 30, row = 14, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p31 = gpioPin(pin = 31, row = 15, func1 = "GPIO6",  func2 = "",              color = "green",  connectable = False)
    p32 = gpioPin(pin = 32, row = 15, func1 = "GPIO12", func2 = "",              color = "green",  connectable = False)
    p33 = gpioPin(pin = 33, row = 16, func1 = "GPIO13", func2 = "",              color = "green",  connectable = False)
    p34 = gpioPin(pin = 34, row = 16, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p35 = gpioPin(pin = 35, row = 17, func1 = "GPIO19", func2 = "",              color = "green",  connectable = False)
    p36 = gpioPin(pin = 36, row = 17, func1 = "GPIO16", func2 = "",              color = "green",  connectable = False)
    p37 = gpioPin(pin = 37, row = 18, func1 = "GPIO26", func2 = "",              color = "green",  connectable = False)
    p38 = gpioPin(pin = 38, row = 18, func1 = "GPIO20", func2 = "",              color = "green",  connectable = False)
    p39 = gpioPin(pin = 39, row = 19, func1 = "Ground", func2 = "",              color = "grey",   connectable = False)
    p40 = gpioPin(pin = 40, row = 19, func1 = "GPIO21", func2 = "",              color = "green",  connectable = False)
    
    p01.save()
    p02.save()
    p03.save()
    p04.save()
    p05.save()
    p06.save()
    p07.save()
    p08.save()
    p09.save()
    p10.save()
    p11.save()
    p12.save()
    p13.save()
    p14.save()
    p15.save()
    p16.save()
    p17.save()
    p18.save()
    p19.save()
    p20.save()
    p21.save()
    p22.save()
    p23.save()
    p24.save()
    p25.save()
    p26.save()
    p27.save()
    p28.save()
    p29.save()
    p30.save()
    p31.save()
    p32.save()
    p33.save()
    p34.save()
    p35.save()
    p36.save()
    p37.save()
    p38.save()
    p39.save()
    p40.save()