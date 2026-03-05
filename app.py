from flask import Flask, render_template

app = Flask(__name__)

# Route halaman utama
@app.route('/')
def home():
    return render_template('login.html')

# Route halaman about
@app.route('/dashboar')
def about():
    return "Ini halaman dashboard"

if __name__ == '__main__':
    app.run(debug=True)