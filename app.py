from flask import Flask, render_template, request, redirect, url_for
from base import get_db_connection

app = Flask(__name__)


@app.route("/menu")
def pizza_menu():
    connection = get_db_connection()
    menu_items = connection.execute("SELECT id, name, description, price FROM pizzas").fetchall()
    connection.close()

    type = request.args.get("sort", "up").lower()
    menu_items = [dict(item) for item in menu_items]

    if type == "desc":
        menu_items.sort(key=lambda item: item["price"], reverse=True)
    else:
        menu_items.sort(key=lambda item: item["price"])

    return render_template("menu.html", menu_items=menu_items)


@app.route('/add', methods=['GET', 'POST'])
def add_pizza():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        connection = get_db_connection()
        connection.execute(
            "INSERT INTO pizzas (name, description, price) VALUES (?, ?, ?)",
            (name, description, price)
        )
        connection.commit()
        connection.close()

        return redirect('/menu')
    return render_template("addpizza.html")


@app.route("/<int:pizza_id>/delete", methods=["POST"])
def delete(pizza_id):
    connection = get_db_connection()
    connection.execute('DELETE FROM pizzas WHERE id = ?', (pizza_id,))
    connection.commit()
    connection.close()
    return redirect(url_for("pizza_menu"))


@app.route("/order", methods=["GET", "POST"])
def order():
    connection = get_db_connection()
    pizzas = connection.execute("SELECT id, name FROM pizzas").fetchall()
    connection.close()
    return render_template("order.html", pizzas=pizzas)


@app.route("/<int:pizza_id>/edit", methods=["GET", "POST"])
def edit_pizza(pizza_id):
    connection = get_db_connection()
    pizza = connection.execute("SELECT * FROM pizzas WHERE id = ?", (pizza_id,)).fetchone()

    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]

        connection.execute("UPDATE pizzas SET name = ?, description = ?, price = ? WHERE id = ?",
                           (name, description, price, pizza_id))
        connection.commit()

        return redirect(url_for("edit_pizza", pizza_id=pizza_id))

    return render_template("edit.html", pizza=pizza)


@app.route("/aboutUs")
def aboutUs():
    return render_template("about.html")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check")
def check():
    return render_template("check.html")


if __name__ == "__main__":
    app.run(debug=True)
