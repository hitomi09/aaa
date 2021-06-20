from flask important Flask

application = Flask(__name__)

@app.route('/')
def root():
    aisatsu = """
<html><body>
<form action="/greeting" method="post">
 <input type="text" name="a">
 <input type="submit" value="入力">
</form>
</body></html>
"""
    return aisatsu

@app.route('/greeting', methods=["post"])
def greeting():
{% if aisatsu == "good morning" %}
  return "おはよう".format(ret)
{% if aisatsu == "Good morning" %}
  return "おはよう".format(ret)
{% if aisatsu == "Good Morning" %}
  return "おはよう".format(ret)
{% if aisatsu == "GOOD MORNING" %}
  return "おはよう".format(ret) 
{% if aisatsu == "hello" %}
  return "こんにちは".format(ret)
{% if aisatsu == "Hello" %}
  return "こんにちは".format(ret)
{% if aisatsu == "HELLO" %}
  return "こんにちは".format(ret)
{% if aisatsu == "good evening" %}
  return "こんばんは".format(ret)
{% if aisatsu == "Good evening" %}
  return "こんばんは".format(ret)
{% if aisatsu == "Good Evening" %}
  return "こんばんは".format(ret)
{% if aisatsu == "GOOD EVENING" %}
  return "こんばんは".format(ret)
{% else %}
  return "わかりません".format(ret)
