from flask import Flask, render_template, request, redirect
app = Flask(__name__)

message = ""

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/action_page', methods=['POST'])
def form():
  fname = request.form.get('fname')
  lname = request.form['lname']
  message = fname + ' ' + lname
  return redirect('/page2')

@app.route('/page2')
def page2():
   return render_template("page2.html", text=message)

if __name__ == '__main__':
  app.run()