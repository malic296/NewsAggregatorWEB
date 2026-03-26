from flask import Flask, render_template
from app.blueprints import logged, auth

app = Flask(__name__)
app.register_blueprint(logged)
app.register_blueprint(auth)

app.config['SECRET_KEY'] = 'dev-secret-key-change-in-prod'
app.config['API_URL'] = 'http://localhost:8000'

@app.route('/')
def index():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
