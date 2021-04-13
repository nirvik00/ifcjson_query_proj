from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS
from pyld import jsonld
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse
import driver
import json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def run_init():
    res = json.dumps(driver.test())
    # return jsonify({"data": res})
    return render_template('rawData.html', data=res)


@app.route('/run', methods=["GET", "POST"])
def run_proc_viewer():
    res = json.dumps(driver.test())
    print("successfully passing data.."+str(len(res)))
    return render_template("viewer.html", data=res)


@app.route('/interactiveQuery', methods=["GET", "POST"])
def run_proc_interative_query():
    res = json.dumps(driver.test2())
    print("successfully passing data.."+str(len(res)))
    return render_template("interactiveQuery.html", data=res)


@app.route('/jsonpathQuery', methods=["GET", "POST"])
def run_proc_jsonpath_query():
    res = json.dumps(driver.test2())
    print("successfully passing data.."+str(len(res)))
    return render_template("jsonpathQuery.html", data=res)


@ app.route('/jsonLdQuery', methods=['GET', 'POST'])
def run_proc_jsonld_query():
    res = json.dumps(driver.test3())
    return render_template("jsonLdQuery.html", data=res)


@app.route('/frame', methods=['GET', 'POST'])
def post_framing():
    print(request.data)
    with open("ifcJsonData.json", "r") as f:
        doc = json.load(f)
    frame = json.load(request.data)
    framed = jsonld.frame(doc, frame)
    return framed


if __name__ == "__main__":
    app.run()
