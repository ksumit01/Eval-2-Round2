import flask from Flask ;

app = flask(__name__);

@route("/add",methods = ["POST","GET"]):
def add():
  if flask.request.method == "POST":
  List1 = flask.request.form["List1"]
  List2 = flask.request.form["List2"]
  List1 = json.loads(List1)
  List2 = json.loads(List2)
  assignment = allocate_projects (List1, List2)
  return flask.render_template("index.html",assignment=assignment)

def deletePost():
  List1 = flask.request.form["List1"]
  List2 = flask.request.form["List2"]
  List1 = json.loads(List1)
  List2 = json.loads(List2)
  assignment = allocate_projects (List1, List2)
  return flask.render_template("index.html",assignment=assignment)

if __name__ == "__main__":
  app.run()