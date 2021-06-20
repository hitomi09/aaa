from flask import Flask

application = Flask(__name__)

@app.route('/')
def root():
    s = """
<html><body>
<form action="/calc" method="post">
 <input type="text" name="a">
 <input type="submit" value="入力">
</form>
</body></html>
"""
    return s

@app.route('/calc', methods=["post"])
def calc():
{% if a == "good morning" %}
  return "おはよう".format(ret)
{% if a == "Good morning" %}
  return "おはよう".format(ret)
{% if a == "Good Morning" %}
  return "おはよう".format(ret)
{% if a == "GOOD MORNING" %}
  return "おはよう".format(ret) 
{% if a == "hello" %}
  return "こんにちは".format(ret)
{% if a == "Hello" %}
  return "こんにちは".format(ret)
{% if a == "HELLO" %}
  return "こんにちは".format(ret)
{% if a == "good evening" %}
  return "こんばんは".format(ret)
{% if a == "Good evening" %}
  return "こんばんは".format(ret)
{% if a == "Good Evening" %}
  return "こんばんは".format(ret)
{% if a == "GOOD EVENING" %}
  return "こんばんは".format(ret)
{% else %}
  return "わかりません".format(ret)
