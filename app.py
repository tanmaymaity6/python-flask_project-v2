from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Angular Developer',
        'location': 'San Fransisco, USA',
        'salary': '$100,000'
    },
    {
        'id': 2,
        'title': 'React Developer',
        'location': 'Dallas, USA',
        'salary': '$200,000'
    },
    {
        'id': 3,
        'title': 'Devops',
        'location': 'Boston, USA',
    },
    {
        'id': 4,
        'title': 'Data Engineer',
        'location': 'Madison, USA',
        'salary': '$175,000'
    },
]


@app.route("/")
def hello_tangent():
    return render_template('home.html', jobs=JOBS, company_name='Tangent')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
