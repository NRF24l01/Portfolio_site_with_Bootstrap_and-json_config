from flask import Flask, render_template, send_file
from projects import projects

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', projects=projects)




if __name__ == '__main__':
    app.run(debug=True, port=80)