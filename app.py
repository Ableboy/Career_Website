from flask import Flask, render_template, jsonify

app = Flask(__name__)

# These are stored as a variable but can be stored as a database.
JOBS = [
  {
    'id': '1',
    'title': 'Data Scientist',
    'location': 'Lagos',
    'salary': 'N 4, 250, 000',
  },
  {
    'id': '2',
    'title': 'AI Software Developer',
    'location': 'San Francisco, USA',
    'salary': '$ 120, 000',
  },
  {
    'id': '3',
    'title': 'Data Analyst',
    'location': 'Abuja',
    'salary': 'N 2, 000, 000',
  },
  {
    'id': '4',
    'title': 'Business Intelligence Analyst',
    'location': 'Remote',
  },
  {
    'id': '5',
    'title': 'AI/ML Engineer',
    'location': 'California, USA',
    'salary': '$ 250, 000',
  },
  {
    'id': '6',
    'title': 'Robotics Engineer',
    'location': 'Texas, USA',
    'salary': '$ 130, 000',
  }
]

@app.route("/")
def hello_world():
  return render_template('index.html', jobs=JOBS)

# Using Json Api to returb the dynamic job data instead of using html rendering template
@app.route("/api/jobs")
def job_list():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
