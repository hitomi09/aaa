from flask import Flask
from flask import request

application = Flask(__name__)

@application.route('/')
def root():
    s = """
<html><body>
<form action="/gree" method="post">
 <input type="text" name="a">
 <input type="submit" value="入力">
</form>
</body></html>
"""
    return s

@application.route('/gree', methods=["post"])
def gree():
    a = str(request.form.get("a"))
    ret = a
    return "{}。".format(ret)
