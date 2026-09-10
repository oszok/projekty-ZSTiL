from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return "Strona główna"

# Zadanie 1

@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć! {imie}"

@app.route("/czesc/<imie>/<int:wiek>")
def czesc2(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat"

# Zadanie 2

@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a,b):
    return f"Wynik to: {a + b}"

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"Wynik to: {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"Wynik to: {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    return f"Wynik to: {a / b}"

@app.route("/potega/<int:a>/<int:b>")
def potega(a, b):
    return f"Wynik to: {a ** b}"

# Zadanie 3

@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    text = ''
    for i in range(1,n+1):
        for j in range(1,n+1):
            text += f"{i} * {j} = {i*j}<br>"
    return text

# Zadanie 4

@app.route("/produkty")
def produkty():
    kat = request.args.get("kat", "Nieznana")
    cena = request.args.get("cena", type=int)
    nazwa = request.args.get("nazwa", "Nieznana")
    return f"Kategoria: {kat}, Sortowanie: {cena}, {nazwa}"

# Zadanie 5
@app.route("/element/<int:id>")
def element(id):
    slownik = {1: "produkty", 2: "ogloszenia", 3: "sale", 4: "posty"}
    return slownik[id]

# Zadanie 6

@app.route("/start")
def start():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
