from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rian')
def rian():
    return render_template('rian.html')

@app.route('/fayi')
def fayi():
    return render_template('fayi.html')

@app.route('/bintang')
def bintang():
    return render_template('bintang.html')

@app.route('/iqbal')
def iqbal():  # Perbaikan nama fungsi agar unik
    return render_template('iqbal.html')

if __name__ == '__main__':
    app.run(debug=True)
