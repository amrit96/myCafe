from flask import Flask
from my_cafe.models import Profile, RawPurchase


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafe.sqlite3'

@app.route("/buy/primary/product/<name>/expiry/<exp_dt>/price/<price>/", methods=['GET'])
def home(name, exp_dt, price):
    return f"hello {name},{exp_dt}, {price}"

@app.route("/")
def test():
    profile.db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)