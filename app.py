#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect, make_response, flash, session, send_file

from SetData import *

from datetime import date, datetime

import json

app = Flask(__name__)

app.secret_key = "382f4059460a83b257c53dc001f9b909"

@app.route("/", methods = ['POST', 'GET'])
def test():
    return redirect('/home')

@app.route("/home", methods = ['POST', 'GET'])
def home():
    getData()
    return render_template('home.html', title = "Welcome")

@app.route("/check62", methods = ['POST', 'GET'])
def check62():
    getData()
    return render_template('check62.html', title = "เช็คชื่อนัดหมาย")

@app.route("/check", methods = ['POST', 'GET'])
def check():
    getData()
    try:
        _user = request.form['User']
        testuser = int(_user)
        name = checkDT('6236' + _user)
        flash(name + ' เช็คชื่อสำเร็จ')
        return redirect('/check62')
    except Exception:
        flash('ไม่พบข้อมูล')
        return redirect('/check62')

@app.route("/sumtoDay")
def sumtoDay():
    getData()
    flash('ยอดวันที่ ' + datetime.now().strftime('%d/%m/%Y') + ' มี ' + str(sumtoday()) + ' คน')
    return redirect('/check62')

@app.route("/against_the_rule", methods = ['POST', 'GET'])
def against_the_rule():
    getData_illigal()
    return render_template('against.html', title = 'เช็คชื่อแต่งกายผิดระเบียบ')

@app.route("/check_against", methods = ['POST', 'GET'])
def check_against():
    getData_illigal()
    try:
        _user = request.form['User']
        _comment = request.form['Comment']
        testuser = int(_user)
        name = checkDTil('6236' + _user, _comment)
        flash(name + ' เช็คชื่อสำเร็จ')
        return redirect('/against_the_rule')
    except Exception:
        flash('ไม่พบข้อมูล')
        return redirect('/against_the_rule')

if __name__ == '__main__':
    app.run()
