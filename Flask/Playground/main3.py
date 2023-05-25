from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<x>/<color>')
def play_ground(x , color):
    return render_template("index3.html",repeat=int(x), change_color=color)

if __name__ == "__main__":
    app.run(debug=True)


