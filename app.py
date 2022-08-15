from flask import Flask, session, redirect
import os
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.blog_controller import blog_controller

SECRET_KEY = os.environ.get("SECRET_KEY", "password")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/")
def index():
    if "user_id" in session:
        return redirect("/blog")
    else:
        return redirect("/login")


app.register_blueprint(session_controller)
app.register_blueprint(user_controller)
app.register_blueprint(blog_controller)

if __name__ == "__main__":
    app.run(debug=True)
