from flask import Flask , render_template , session , redirect
app = Flask(__name__)
app.secret_key = '12345'


@app.route('/')
def count_visits():
    if 'visits' in session:
        print("key exists!")
        session['visits'] += 1
    else:
        print("key 'visits' does not exist")
        session['visits'] = 1
    return render_template('index.html')

@app.route('/destroy', methods = ['post'])
def destroy_count():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)

