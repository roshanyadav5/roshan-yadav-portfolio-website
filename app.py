from flask import Flask, render_template
app= Flask(__name__)



Skills=[
   {'name': 'Python', 'level': 'Advanced'},
   {'name': 'JavaScript', 'level': 'Intermediate'},
   {'name': 'HTML/CSS', 'level': 'Advanced'},
   {'name': 'Flask', 'level': 'Intermediate'},
]


@app.route('/')

def homePage():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)