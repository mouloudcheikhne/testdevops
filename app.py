from flask import Flask, request, render_template, redirect,session,url_for


app = Flask(__name__)

@app.route('/')
def affichage():
    return "helllll"


if __name__ == '__main__':
    app.run(port=4000, debug=True)
