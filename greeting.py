from flask import Flask
from flask import request

application = Flask(__name__)

@application.route('/')
def root():
<html><body>
<form action="/gree" method="post">
 <input type="text" name="a">
 <input type="submit" value="入力">
</form>
</body></html>

@application.route('/gree', methods=["post"])
def gree():
    a = str(request.form.get("a"))
    {% if a == "good morning" %}
    ret = "おはよう"
    {% else %}
    ret = "わかりません"
    return "{}。".format(ret)
