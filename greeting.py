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
