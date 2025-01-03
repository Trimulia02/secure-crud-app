from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management and flash messages

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
        name = request.form.get("name")
        email = request.form.get("email")

        # Simple validation
        if not name or not email:
            flash("Name and email are required!", "error")
            return redirect(url_for("add"))

        new_id = len(data) + 1
        data.append({"id": new_id, "name": name, "email": email})
        flash("Entry added successfully!", "success")
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    item = next((item for item in data if item["id"] == id), None)
    if item is None:
        flash("Item not found!", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        # Simple validation
        if not name or not email:
            flash("Name and email are required!", "error")
            return redirect(url_for("edit", id=id))

        item["name"] = name
        item["email"] = email
        flash("Entry updated successfully!", "success")
        return redirect(url_for("index"))
    
    return render_template("edit.html", item=item)

@app.route("/delete/<int:id>")
def delete(id):
    global data
    data = [item for item in data if item["id"] != id]
    flash("Entry deleted successfully!", "success")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
