from flask import Flask, request, render_template_string

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "<h1>Welcome to the Demo Flask App</h1><p>Visit /hello, /add, or /sum to try things out.</p>"

# A simple hello route
@app.route("/hello")
def hello():
    return "<h2>Hello from Flask!</h2>"

# A route to add two numbers via form submission
@app.route("/add", methods=["GET", "POST"])
def add_numbers():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1 + num2
            return f"<h3>Result: {num1} + {num2} = {result}</h3><br><a href='/add'>Go back</a>"
        except ValueError:
            return "<h3>Please enter valid numbers.</h3><br><a href='/add'>Try again</a>"

    # Render a simple form if GET request
    return render_template_string('''
        <h2>Add Two Numbers (Form)</h2>
        <form method="POST">
            Number 1: <input type="text" name="num1"><br><br>
            Number 2: <input type="text" name="num2"><br><br>
            <input type="submit" value="Add">
        </form>
    ''')

# A route to add two numbers via query parameters
@app.route("/sum")
def sum_numbers():
    try:
        num1 = float(request.args.get("num1", ""))
        num2 = float(request.args.get("num2", ""))
        result = num1 + num2
        return f"<h3>Result: {num1} + {num2} = {result}</h3>"
    except ValueError:
        return "<h3>Please provide valid query parameters: /sum?num1=5&num2=3</h3>"

if __name__ == "__main__":
    app.run(debug=True)
