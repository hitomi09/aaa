from flask import Flask
from flask import request

application = Flask(__name__)

@app.route('/')
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

@app.route('/gree', methods=["post"])
def gree():
    a = str(request.form.get("a"))
    {% if a == "good morning" %}
      ret = "おはよう"
    {% if a == "Good morning" %}
      ret = "おはよう"
    {% if a == "Good Morning" %}
      ret = "おはよう"
    {% if a == "GOOD MORNING" %}
      ret = "おはよう"
    {% if a == "hello" %}
      ret = "こんにちは"
    {% if a == "Hello" %}
      ret = "こんにちは"
    {% if a == "HELLO" %}
      ret = "こんにちは"
    {% if a == "good evening" %}
      ret = "こんばんは"
    {% if a == "Good evening" %}
      ret = "こんばんは"
    {% if a == "Good Evening" %}
      ret = "こんにちは"
    {% if a == "GOOD EVENING" %}
      ret = "こんにちは"
    {% else %}
      ret = "わかりません"
    return "{}。".format(ret)
