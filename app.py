from flask import Flask

app = Flask(__name__)

@app.route("/")         
def hello_world():
    return "<p>Hello Jovian!<p>"

print(__name__)
if __name__ == "__main__":
  print("I'm in if")
  app.run(host='0.0.0.0',debug=True, port=8080)