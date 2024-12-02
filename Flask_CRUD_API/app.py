from flask import Flask, jsonify, request
from laptops_blueprint import laptops_blueprint

app = Flask(__name__)
app.register_blueprint(laptops_blueprint)


# endpoint for home
@app.route('/')
def home():
    return 'Welcome to Flask'




# Have backend server run
if __name__ == '__main__':
    app.run(debug=True)