from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    even_nums, odd_nums = [], []
    if request.method == "POST":
        input_numbers = request.form["numbers"]
        try:
            nums = [int(n.strip()) for n in input_numbers.split(",")]
            even_nums = [n for n in nums if n % 2 == 0]
            odd_nums = [n for n in nums if n % 2 != 0]
        except ValueError:
            return render_template("index.html", error="Invalid input! Enter only numbers separated by commas.")
    return render_template("index.html", even=even_nums, odd=odd_nums)

if __name__ == "__main__":
    app.run(debug=True)
