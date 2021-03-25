from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_cors import CORS
import driver 
import json

app=Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def run_init():
    res= driver.test()
    return jsonify({"data":res}) 

@app.route('/run', methods=["GET", "POST"])
def run_proc():
    res=json.dumps(driver.test())
    print("successfully passing data.."+str(len(res)))
    return render_template("index.html", data=res)


if __name__ == "__main__":
    app.run()