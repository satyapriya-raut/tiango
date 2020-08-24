from flask import Flask, render_template, request, session, redirect, flash, url_for
import sqlite3 as db
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

# The Login Page
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
	
# The Registration Page
@app.route('/signupPage')
def signupPage():
	return render_template('signupPage.html')
    
# From Login Page it will be redirected to check if user is valid or not
@app.route('/validate', methods=["POST"])
def validate():
	id = request.form.get("userID")
	password = request.form.get("pwd")
	try:
		with db.connect("/home/satyapriya/mysite/Database/Tiango.sqlite") as conn:
			cur = conn.cursor()
			cur.execute("SELECT id, password FROM User WHERE id = ?", (id,));
			row = cur.fetchone();
			cur.close()
			if row is None:
				flash("Invalid username or password", "danger")	# Display message to invalid user.
				return redirect(url_for("index"))
			elif (row[0] == id and row[1] == password):
				session["id"] = id
				session["logged_in"] = True
				return redirect(url_for("allQuizes"));
			else:
				flash("Invalid username or password", "danger")	# Display message to invalid user.
				return redirect(url_for("index"))
				
	except:
		flash("Invalid!", "danger")
		return redirect(url_for("index"))
	
# from Registration Page, it will be redirected to check if user already exists
@app.route('/signupValidate', methods=["POST"])
def signupValidate():
	id = request.form.get("userID")
	user = request.form.get("uname")
	password = request.form.get("pwd")
	try:
		with db.connect("/home/satyapriya/mysite/Database/Tiango.sqlite") as conn:
			cur = conn.cursor()
			cur.execute("SELECT id FROM User WHERE id = ?", (id,));
			row = cur.fetchone();
			if row is None:
				cur.execute("INSERT INTO User VALUES(?, ? ,?)", (id, user, password));
				conn.commit()
				cur.close()
				session["id"] = id
				session["logged_in"] = True
				return redirect(url_for("allQuizes"));
			else:
				flash("User already exists.")
				return redirect(url_for("signupPage"))
	except Exception as e:
		flash("Invalid request.")
		return redirect(url_for("signupPage"))
		

@app.route('/allQuizes', methods = ["GET", "POST"])
def allQuizes():
	if session["logged_in"] == True:
		return render_template('allQuizes.html', name = session["id"])
	else:
		return redirect(url_for("index"))
	

"""Check if user has already attempted that quiz or not
If attempted, then display score
"""
@app.route('/check')
def check():
	if session["logged_in"] == True:
		id = session["id"]
		quizName = request.args.get("type")
		session["quizName"] = quizName
		attemptTable = quizName + "Attempted"	# concat "Attempted" word, because thats how I have named the table
		try:
			with db.connect("/home/satyapriya/mysite/Database/Tiango.sqlite") as con:
				cur = con.cursor()
				query = "SELECT id FROM {} WHERE id = ?".format(attemptTable)
				cur.execute(query, (id,));
				row = cur.fetchone()
				cur.close()
				#Quiz not attempted
				if row is None:
					return redirect(url_for("instructions"))
				else:
					return redirect(url_for("display"))
		except Exception as e:
			print(e)
			return redirect(url_for("allQuizes"))
	else:
		return redirect(url_for("index"))
			
		
@app.route('/instructions')
def instructions():
	if session["logged_in"] == True:
		return render_template('instructions.html', quiz = session["quizName"], name = session["id"])
	else:
		return redirect(url_for("index"))

# Display list of questions
@app.route('/questions', methods = ["POST"])
def questions():
	quizName = session["quizName"]
	try:
		with db.connect("/home/satyapriya/mysite/Database/Tiango.sqlite") as conn:
			cur = conn.cursor();
			query = "SELECT * FROM {}".format(quizName)
			cur.execute(query);
			ques_opts = cur.fetchall()
			cur.close()
			return render_template("questions.html", questions = ques_opts, quizName = quizName)
	except:
		return redirect(url_for("allQuizes"))

		
# Calculate score and store in database.
@app.route('/calculate', methods = ["GET", "POST"])
def calculate():
	id = session["id"]
	attemptTable = session["quizName"] + "Attempted"
	scoreTable = session["quizName"] + "Score"
	quiz = session["quizName"]
	try:
		with db.connect("/home/satyapriya/mysite/Database/Tiango.sqlite") as conn:
			cur = conn.cursor();
			query = "SELECT answer FROM {}".format(quiz)
			cur.execute(query);
			rows = cur.fetchall()
			score = 0
			for i in range(10):		# 10 questions
				score += 1 if request.form.get(str(i+1)) == rows[i][0] else 0
			if quiz == "Aptitude":		#Apti has 10 questions 2 marks each
				score *= 2
			query = "INSERT INTO {} VALUES (?, ?)".format(attemptTable)
			cur.execute(query, (id, 1));
			query = "INSERT INTO {} VALUES (?, ?)".format(scoreTable)
			cur.execute(query, (id, score));
			conn.commit()
			cur.close()
		return redirect(url_for("display"))
	except Exception as e:
		return redirect(url_for("allQuizes"))
	
# Display score	
@app.route('/display', methods = ["GET", "POST"])
def display():
	if session["logged_in"] == True:
		id = session["id"]
		scoreTable = session["quizName"] + "Score"	# concat "Score" word because thats how I have named the table
		try:
			with db.connect("/home/satyapriya/mysite/Database/Tiango.sqlite") as conn:
				cur = conn.cursor();
				query = "SELECT * FROM {} WHERE id = ?".format(scoreTable)
				cur.execute(query, (id,))
				row = cur.fetchone()
				query = "SELECT * FROM {} ORDER BY Score DESC, id".format(scoreTable)
				cur.execute(query)
				scores = cur.fetchall()
				cur.close()
				return render_template('display.html', score = row[1], scores = scores)
		except:
			return redirect(url_for("allQuizes"))
	else:
		return redirect(url_for("index"))
	
@app.route('/logout')
def logout():
	session["logged_in"] = False 
	return redirect(url_for("index"))

if __name__ == "__main__":
	app.run(port=5000, debug="True")
