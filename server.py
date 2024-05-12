import bottle
import markdown
from os import listdir

app = bottle.Bottle()

@app.route("/")
def home():
    posts = listdir("posts")
    return bottle.template("pages/posts", posts=posts)

@app.route("/post/<filename>")
def post(filename):
    md = open("posts/" + filename).read()
    content = markdown.markdown(md)
    return bottle.template("pages/post.html", content=content)

@app.route("/<filepath:path>")
def server_static(filepath):
    return bottle.static_file(filepath, "./static")

# uncomment on development, comment on deploy
bottle.run(app)