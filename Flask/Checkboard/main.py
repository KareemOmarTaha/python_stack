from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def checkboard():
    some_num=8
    return render_template("index.html",some_num = some_num)

@app.route('/<num>')
def checkboard_1(num=4):
    some_num=int(num)
    return render_template("index.html",some_num = some_num )

@app.route("/<x>/<y>")
def checkboard_2(x,y):
    input_1 = int(x)
    input_2 = int(y)
    return render_template("index2.html", input_1=input_1 , input_2 = input_2)

if __name__=="__main__":
    app.run(debug=True)
