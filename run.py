#! /usr/bin/env python
import os
from flask import render_template
from flask import Flask
from app import app
import time

#@app.route('/profile/')
#def profile():
 # return render_template('profile.html', now = timeinfo())

#def timeinfo():
 # now = time.strftime("%a, %d %b %Y")
  #return now

app.run(debug=True,host="0.0.0.0",port=8080)
