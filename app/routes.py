from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.forms import RecipeForm, LoginForm, RegisterForm
from app.models import Recipe, User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    recipes = Recipe.query.all()
    return render_template("index.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful. You can now log in.")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in successfully!")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/recipe/new", methods=["GET", "POST"])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            description=form.description.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            author=current_user
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("new_recipe.html", form=form)


@app.route("/recipe/<int:recipe_id>")
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe_detail.html", recipe=recipe)


@app.route("/recipe/<int:recipe_id>/delete")
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        abort(403)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))





