import requests
import json

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
   response = requests.get("https://reqres.in/api/users")
   data = json.loads(response.content)
   html = "<table>"
   html += "<tr><th>ID</th><th>Name</th><th>Email</th></tr>"
   for user in data["data"]:
      html += f"<tr><td>{user['id']}</td><td>{user['first_name']} {user['last_name']}</td><td>{user['email']}</td></tr>"
   html += "</table>"
   return render_template('index.html', content=html)

if __name__ == '__main__':
   app.run()
