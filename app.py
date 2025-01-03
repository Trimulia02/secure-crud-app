from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage
data = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_id = len(data) + 1
        name = request.form["name"]
        email = request.form["email"]
        data.append({"id": new_id, "name": name, "email": email})
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    item = next((item for item in data if item["id"] == id), None)
    if request.method == "POST":
        item["name"] = request.form["name"]
        item["email"] = request.form["email"]
        return redirect(url_for("index"))
    return render_template("edit.html", item=item)

@app.route("/delete/<int:id>")
def delete(id):
    global data
    data = [item for item in data if item["id"] != id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
