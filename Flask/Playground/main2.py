from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<x>')
def play_ground(x):
    return render_template("index2.html",repeat=int(x))

if __name__ == "__main__":
    app.run(debug=True)


