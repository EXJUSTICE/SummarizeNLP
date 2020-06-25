from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

comments = []

#Follow https://pythonprogramming.net/jquery-flask-tutorial/
@app.route("/", methods=["GET"])
def index():

    return render_template("main_page.html", comments=comments)



"""
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=comments)

    comments.append(request.form["contents"])
    return redirect(url_for('index')
"""
@app.route("/background_process")
def background_process():
    try:
        lang = request.args.get('contents')
        if str(lang).lower()=='python':
            return jsonify(result='Nice')
        else:
            return jsonify(result='Crap')
    except Exception as e:
            return (str(e))
