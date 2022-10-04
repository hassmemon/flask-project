# from email.quoprimime import quoted
from flask import Blueprint, request, session, redirect, render_template

# from models.blog import get_all_blogposts, delete_blogpost
from models.blog import (
    delete_blogpost,
    get_all_blogposts,
    get_blogpost,
    insert_blogpost,
    get_user_blogposts,
    get_user_id,
    update_blogpost,
)
from models.user import get_user_by_id

blog_controller = Blueprint(
    "blog_controller", __name__, template_folder="../templates/blog"
)


@blog_controller.route("/blog", methods=["GET"])
def blog():
    user_id = session.get("user_id")
    my_blogposts = get_user_blogposts(user_id)

    return render_template("main.html", my_blogposts=my_blogposts)


@blog_controller.route("/blog/show", methods=["GET"])
def show_all_blogposts():
    all_blogposts = get_all_blogposts()
    return render_template("show.html", all_blogposts=all_blogposts)


@blog_controller.route("/blog/create")
def create():
    if not session.get("user_id"):
        return redirect("/login")
    return render_template("create.html")


@blog_controller.route("/blog", methods=["POST"])
def insert():
    if not session.get("user_id"):
        return redirect("/login")
    user_id = session.get("user_id")
    insert_blogpost(
        request.form.get("blog_post"), request.form.get(
            "blog_title"), user_id, request.form.get("topics")
    )
    return redirect("/")


@blog_controller.route("/blog/<id>")
def show(id):
    blogpost = blogpost(id)
    return render_template("show.html", blogpost=blogpost)


@blog_controller.route("/blog/<id>/edit")
def edit(id):
    if not session.get("user_id"):
        return redirect("/login")
    blog_post = get_blogpost(id)
    return render_template(
        "edit.html", blog_post=blog_post, user_id=session.get('user_id')


    )


@blog_controller.route("/blog/<id>", methods=["POST"])
def update(id):
    if not session.get("user_id"):
        return redirect("/login")
    blog_title = request.form.get("blog_title")
    blog_post = request.form.get("blog_post")

    user_id = session.get("user_id")
    destination = request.form.get("topics")
    print(id)
    update_blogpost(id, blog_title, blog_post, destination)
    return redirect("/")


@blog_controller.route("/blog/<id>/delete")
def delete(id):
    if not session.get("user_id"):
        return redirect("/login")
    delete_blogpost(id)
    return redirect("/")
