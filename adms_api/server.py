#!/usr/bin/python3
# coding=utf-8
"""
:Copyright: © 2022 Advanced Control Systems, Inc. All Rights Reserved.
@Author: Stephen Hung
@Author: Darren Liang
@Date  : 2022-02-18
"""

from adms_api.__init.__ import (IPADDR, PORT)
from adms_api.core.LoggerInterface import setupLogger

from flask import Flask, render_template, request, jsonify, json

app=Flask(__name__)

import os
from flask import send_from_directory

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template('index.html')


# @app.route("/api/substinfo/<string:__subst>", methods=['GET'])
# def get_info_by_subst(__subst):
#     if request.method == 'GET':
#         json_url = os.path.join(app.root_path, "static/json", "ga.json")
#         return jsonify(json.load(open(json_url, encoding="utf8")))


if __name__ == '__main__':
    setupLogger()

    app.config['JSON_AS_ASCII'] = False
    app.run(host=IPADDR,port=PORT,debug=True)
