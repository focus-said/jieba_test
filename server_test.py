#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author: focus
# @Time : 2019/2/21 3:02 PM
# @Software: PyCharm
from flask import request, jsonify
from flask import Flask
import jieba
import jieba.analyse
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main_entrance():
    req_data = request.values.to_dict()
    req_data = req_data['res']
    seg_list = jieba.cut(req_data, cut_all=False)
    resa = []
    for i in seg_list:
        resa.append(i)
    return jsonify(resa)


if __name__ == "__main__":
    app.run("0.0.0.0", 8889, debug=True)