#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   meituan.py    
@Contact :   625711951@qq.com
@License :   (C)Copyright 2019-2020, Zyf-FT

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/10/1 18:01   zyfei      1.0         None
'''
from flask import Flask
from flask import render_template
from flask import Blueprint

mtapp = Blueprint('meituan', __name__)

@mtapp.route('/meituan/login/')
def login():
    '''

    :return:
    '''
    return render_template('./meituan/login.html')
