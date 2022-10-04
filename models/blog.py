import database


# def insert_blogpost(blog_title, blog_post, user_id, tags, destination):
#     database.sql_write(
#         "INSERT into blog_entries (blog_title, blog_post, user_id, tags, destination) VALUES (%s, %s, %s, %s, %s);",
#         [blog_post, blog_title, user_id, tags, destination],
#     )

def insert_blogpost(blog_title, blog_post, user_id, topics):
    database.sql_write(
        "INSERT into blog_entries (blog_title, blog_post, user_id, topics) VALUES (%s, %s, %s, %s);",
        [blog_post, blog_title, user_id, topics],
    )




def get_blogpost(id):
    results = database.sql_select("SELECT * FROM blog_entries WHERE id = %s", [id])
    result = results[0]
    return result


def get_all_blogposts():
    results = database.sql_select(
        "SELECT blog_entries.*, users.name as user_name FROM blog_entries LEFT JOIN users ON blog_entries.user_id = users.id",
        [],
    )
    return results


def get_user_id():
    results = database.sql_select("SELECT user_id FROM blog_entries", [])
    return results


def get_user_blogposts(user_id):
    results = database.sql_select(
        "SELECT * FROM blog_entries WHERE user_id = %s", [user_id]
    )
    return results


# def update_blogpost(id, blog_title, blog_post, tags, destination):
#     database.sql_write(
#         "UPDATE blog_entries set blog_post = %s, blog_title = %s, tags = %s, destination = %s WHERE id = %s",
#         [blog_title, blog_post, tags, destination, id],
#     )

def update_blogpost(id, blog_title, blog_post, topics):
    database.sql_write(
        "UPDATE blog_entries set blog_post = %s, blog_title = %s, topics = %s WHERE id = %s",
        [blog_title, blog_post, topics, id],
    )

def delete_blogpost(id):
    database.sql_write("DELETE FROM blog_entries WHERE id = %s", [id])
