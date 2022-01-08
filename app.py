from flask import Flask, render_template
# import os
import json
app = Flask(__name__)

# ? pages
@app.route("/")
def home():
    data = "teststringjsklgkslf"
    return render_template('index.html', data = json.dumps(data))

if __name__ =='__main__':
    app.run(debug=True)