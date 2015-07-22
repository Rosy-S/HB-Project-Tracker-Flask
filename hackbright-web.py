from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student", methods=['POST'])
def get_student():
    """Show information about a student."""

    github = request.form.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""
    return render_template("student_search.html")


@app.route("/student-add")
def student_add():
    return render_template("create_student.html")

@app.route("/student-submit", methods=['POST'])
def student_submit():
    first_name=request.form.get('firstname')
    last_name=request.form.get('lastname')
    git_hub=request.form.get('github')
    html = render_template('student_info.html', first=first_name, last=last_name, github=git_hub)

    return html

if __name__ == "__main__":
    app.run(debug=True)