# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:55:08 2019

@author: Tobias
"""

from django import template

register = template.Library()

@register.filter
def pinIndex(List, i):
    return List[int(i)]