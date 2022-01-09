from flask import Flask, jsonify

app = Flask(__name__)

students = [{'name': "Sai Keerthi",
			 'St_id': "55",
			 'Address': "Attapur"},
			{'name': "Jyothirmayee",
			 'St_id': "22",
			 'Address': "Bhavani Colony"},
			{'name': "Swarna",
			 'St_id': "46",
			 'Address': "Budvel"},
			{'name': "Ravi Kumar",
			 'St_id': "11",
			 'Address': "Uppal"},
			{'name': "Sai Krishna",
			 'St_id': "35",
			 'Address': "Secunderabad"},
			{'name': "Tejuu",
			 'St_id': "06",
			 'Address': "Warangal"}
			]


@app.route('/')
def index():
	return "Welcome To The Course API"


@app.route("/students", methods=['GET'])
def get():
	return jsonify({'Students': students})

@app.route("/students/<int:St_id>", methods=['GET'])
def get_student(St_id):
	return jsonify({'student':students[St_id]})

@app.route("/students", methods=['POST'])
def create():
    student = {'name': "Heyansh",
             'St_id': "24",
             'Address': "Mangalagiri"}
    students.append(student)
    return jsonify({'Created' : student})


if __name__ == "__main__":
	app.run(debug=True)

