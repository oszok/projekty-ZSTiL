from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Strona główna"

@app.route("/o-nas")
def o_nas():
    return "Jesteśmy klasą 4 Technik Programista. Robimy sklep."

@app.route("/kontakt")
def kontakt():
    return "Napisz: sklep@example.com"

@app.route("/regulamin")
def regulamin():
    return "Nakaz gnębienia buldaki"

@app.route("/admin")
def admin():
    return "Brak dostępu", 403

@app.route("/api/info")
def api_info():
    retrun {"nazwa":"flask-start", "autor":"Oszok", "wersja":"001"}

if __name__ == "__main__":
    app.run(debug=True)
