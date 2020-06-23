
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
from processing import do_calculation

app = Flask(__name__)
app.config["DEBUG"] = True

"""
This decorator specifies that the following function defines what happens when someone goes to the location “/” on your site – eg. if they go to http://yourusername.pythonanywhere.com/.
If you wanted to define what happens when they go to http://yourusername.pythonanywhere.com/foo then you’d use @app.route('/foo') instead.

If the request used a “get” method, just display the input form
If the request used a “post” method, but one or both of the numbers are not valid, then display the input form with error messages.
If the request used a “post” method, and both numbers are valid, then display the result.
"""
@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None

        #Fetch two numbers
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])
        if number1 is not None and number2 is not None:
            result = do_calculation(number1, number2)
            return '''
                <html>
                    <body align="center">
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>

            <body align="center">

                {errors}
                <p>Enter your numbers:</p>
                <form method="post" action=".">
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
"""
What that means is that previously we had a form,
but now we have a form that has an “action” telling it that when the button that has the type “submit” is clicked,
it should request the same page as it is already on, but this time it should use the “post” method.
"""
