from cProfile import label
from distutils.cmd import Command
from email.policy import default
import json
import random
import getpass
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
root = tkinter.Tk()
root.title("QuizGame")
root.geometry("700x600")
labeltext = Label(root,text="QuizGame",font=("Comic sans MS",24,"bold"),background="#ffffff")
labeltext.pack(pady=(0,50))
radiovar = IntVar()
radiovar.set(-1)
user = []
# def info():
# 	tmsg=showinfo("You are correct",f"Your answer is {radiovar.get()}.")
def home():
	score = 0
	# Play Button method
 
	def play():
		labeltext.destroy()
		btnAbout.destroy()
		btnAdd.destroy()
		btnCreate.destroy()
		btnExit.destroy()
		btnHelp.destroy()
		btnLogin.destroy()
		#	btnLogout.destroy()
		btnstart.destroy()
		
		def load_questions(filename):
			with open(filename, "r") as file:
				return json.load(file)

		def load_next_question():
			nonlocal current_question_index
			if current_question_index < len(questions):
				question = questions[current_question_index]
				question_label.config(text=question["question"])
				for i, answer in enumerate(question["answers"]):
					answer_buttons[i].config(text=answer)
					answer_buttons[i].config(state=NORMAL)  # Enable answer buttons
				next_button.config(state=DISABLED)  # Disable next button
				current_question_index += 1
			else:
				show_results()

		def check_answer(idx):
			nonlocal current_question_index
			nonlocal score
			correct_answer = questions[current_question_index - 1]["correct_answer"]
			if idx == correct_answer:
				print("Correct!")
				score+=1
				# Do something when the answer is correct
			else:
				print("Incorrect!")
				# Do something when the answer is incorrect
			for answer_button in answer_buttons:
				answer_button.config(state=DISABLED)  # Disable answer buttons
			next_button.config(state=NORMAL)  # Enable next button

		def show_results():
			result_label.config(text=f"Your result: {score}")
			

		questions = load_questions("assets/questions.json")
		current_question_index = 0


		question_label = Label(root, text="")
		question_label.pack()

		answer_buttons = []
		for i in range(4):
			answer_button = Button(root, text="", command=lambda idx=i: check_answer(idx))
			answer_button.pack()
			answer_buttons.append(answer_button)

		next_button = Button(root, text="Next", command=load_next_question, state=DISABLED)
		next_button.pack()
		result_label = Label(root, text= '')
		result_label.pack()

		load_next_question()

		
	# Add question 
		

	def quizQuestions():
		labeltext.destroy()
		btnAbout.destroy()
		btnAdd.destroy()
		btnCreate.destroy()
		btnExit.destroy()
		btnHelp.destroy()
		btnLogin.destroy()
		btnstart.destroy()

		def load_questions():
			try:
				with open("assets/questions.json", "r") as file:
					return json.load(file)
			except FileNotFoundError:
				return []

		def save_questions(questions, filename):
			with open(filename, "w") as file:
				json.dump(questions, file, indent=4)

		def add_new_question():
			if is_admin_logged_in():
				question = {
					"question": question_entry.get(),
					"answers": [answer1_entry.get(), answer2_entry.get(), answer3_entry.get(), answer4_entry.get()],
					"correct_answer": int(correct_answer_entry.get())  # Convert to integer
				}
				questions.append(question)
				save_questions(questions, "assets/questions.json")
				status_label.config(text="Question added successfully!")
			else:
				status_label.config(text="Please login as admin first!")

		def is_admin_logged_in():
			# Check if the admin is logged in using user_accounts.json
			global user
			if len(user) != 0:
				return True
			else:
				return False

		questions = load_questions()


		question_label = Label(root, text="Enter the question:")
		question_label.pack()
		question_entry = Entry(root)
		question_entry.pack()

		answer1_label = Label(root, text="Enter answer 1:")
		answer1_label.pack()
		answer1_entry = Entry(root)
		answer1_entry.pack()

		answer2_label = Label(root, text="Enter answer 2:")
		answer2_label.pack()
		answer2_entry = Entry(root)
		answer2_entry.pack()

		answer3_label = Label(root, text="Enter answer 3:")
		answer3_label.pack()
		answer3_entry = Entry(root)
		answer3_entry.pack()

		answer4_label = Label(root, text="Enter answer 4:")
		answer4_label.pack()
		answer4_entry = Entry(root)
		answer4_entry.pack()

		correct_answer_label = Label(root, text="Enter the index of correct answer (0-3):")
		correct_answer_label.pack()
		correct_answer_entry = Entry(root)
		correct_answer_entry.pack()

		add_button = Button(root, text="Add Question", command=add_new_question)
		add_button.pack()

		status_label = Label(root, text="")
		status_label.pack()
		def back():
			question_entry.destroy()
			question_label.destroy()
			answer1_entry.destroy()
			answer1_label.destroy()
			answer2_entry.destroy()
			answer2_label.destroy()
			answer3_entry.destroy()
			answer3_label.destroy()
			answer4_entry.destroy()
			answer4_label.destroy()
			correct_answer_entry.destroy()
			correct_answer_label.destroy()
			add_button.destroy()
			status_label.destroy()
			btnback.destroy()
			home()
		btnback = Button(root,text="Back",command=back)
		btnback.pack()


	# Create Account Panel
 
	def createAccount():
		labeltext.destroy()
		btnAbout.destroy()
		btnAdd.destroy()
		btnCreate.destroy()
		btnExit.destroy()
		btnHelp.destroy()
		btnLogin.destroy()
	#	btnLogout.destroy()
		btnstart.destroy()
		lbh1 = Label(root,text="==========CREATE ACCOUNT=========",font=("Comic sans MS",15,"bold"))
		lbh1.pack()
		print("\n==========CREATE ACCOUNT==========")
		uservalue = StringVar()
		passvalue = StringVar()
		User = Label(root,text = "Username",font=("Comic sans MS",15,))
		User.pack()
		userentry = Entry(root,textvariable=uservalue)
		userentry.pack()
		password1  = Label(root,text="Password",font=("Comic sans MS",15,))
		password1.pack()
		passentry = Entry(root,textvariable=passvalue)
		passentry.pack()
		global usernn
		global password2 
		def sub():
			usern = userentry.get() 
			password2 = passentry.get()
			#username = input("Enter your USERNAME: ")
			#password = getpass.getpass(prompt= 'Enter your PASSWORD: ')
			with open('assets/user_accounts.json', 'r+') as user_accounts:
				users = json.load(user_accounts)
				if usern in users.keys():
					showinfo("failed",f"An account of this Username already exists.\nPlease enter the login panel.")
					print("An account of this Username already exists.\nPlease enter the login panel.")
				else:
					users[usern] = [password2, "PLAYER"]
					user_accounts.seek(0)
					json.dump(users, user_accounts)
					user_accounts.truncate()
					showinfo("success",f"Account created successfully!")
					print("Account created successfully!")
		btnsub = Button(root,text="Submit",command=sub)
		btnsub.pack()
		def back2():
			lbh1.destroy()
			password1.destroy()
			passentry.destroy()
			userentry.destroy()
			User.destroy()
			btnsub.destroy()
			btnback1.destroy()
			home()
		btnback1 = Button(root,text="Back",command=back2)
		btnback1.pack()

	# Login panel Button
	def loginAccount():
		labeltext.destroy()
		btnAbout.destroy()
		btnAdd.destroy()
		btnCreate.destroy()
		btnExit.destroy()
		btnHelp.destroy()
		btnLogin.destroy()
		#btnLogout.destroy()
		btnstart.destroy()
		loginpnl = Label(root,text='\n==========LOGIN PANEL==========',font=("Comic sans MS",24,"bold"),background="#ffffff")
		loginpnl.pack()
		uservalue1 = StringVar()
		passvalue1 = StringVar()
		User = Label(root,text = "Username")
		User.pack()
		entry = Entry(root,textvariable=uservalue1)
		entry.pack()
		password1  = Label(root,text="Password")
		password1.pack()
		passentry1 = Entry(root,textvariable=passvalue1)
		passentry1.pack()

		global user1
		global pass1
		def info():
			user1 = entry.get() 
			pass1 = passentry1.get()
			with open('assets/user_accounts.json', 'r') as user_accounts:
				users = json.load(user_accounts)
				if user1 not in users.keys():
					showinfo("fail",f"An account of that name doesn't exist.\nPlease create an account first.")
				elif user1 in users.keys():
					if users[user1][0] != pass1:
						showinfo("fail",f"Your password is incorrect.\nPlease enter the correct password and try again.")
					elif users[user1][0] == pass1:
						showinfo("success",f"You have successfully logged in.\n")
						user.append(user1)
						user.append(users[user1][1])
						return True

		btnsub1 = Button(root,text="Login",command=info)
		btnsub1.pack()
		def logout():
			global user
			if len(user) == 0:
				showinfo("fail",f"You are already logged out.")
				print("You are already logged out.")
			else:
				user = []
				showinfo(f"You have been logged out successfully.")
		btn1 = Button(root,text="Logout",command=logout)
		btn1.pack()
		def back3():
			loginpnl.destroy()
			password1.destroy()
			entry.destroy()
			passentry1.destroy()
			User.destroy()
			btn1.destroy()
			btnsub1.destroy()
			btnback1.destroy()
			home()
		btnback1 = Button(root,text="Back",command=back3)
		btnback1.pack()

	# help button panel

	def rules():
		labeltext.destroy() 
		btnAbout.destroy() 
		btnAdd.destroy()
		btnCreate.destroy()
		btnExit.destroy()
		btnHelp.destroy()
		btnLogin.destroy()
	#	btnLogout.destroy()
		btnstart.destroy()
		lbh = Label(root,text='''\n==========RULES==========
        1. Each question consists of 1 point. There's no negative point for wrong answers.\n
        2. You can create an account from ACCOUNT CREATION panel.
        3. You can login using the LOGIN PANEL. Currently, the program can only login and not do anything more.\n
	    ''',font=("Comic sans MS",10,"bold"),background="#ffffff")
		lbh.pack()
		
		def back():
			lbh.destroy()
			btnback.destroy()
			home()
		btnback = Button(root,text="Back",command=back)
		btnback.pack()
		
		

	# About us button panel
	def about():
		labeltext.destroy()
		btnAbout.destroy()
		btnAdd.destroy()
		btnCreate.destroy()
		btnExit.destroy()
		btnHelp.destroy()
		btnLogin.destroy()
	#	btnLogout.destroy()
		btnstart.destroy()
		labeltext1 = Label(root,text='''\n==========ABOUT US==========
        This project has been created by Ajay Verma
        It is a basic Python Project for my 3rd Semester.''',font=("Comic sans MS",15,"bold"),background="#ffffff")
		labeltext1.pack()
		def back1():
			labeltext1.destroy()
			btnback1.destroy()
			home()
		btnback1 = Button(root,text="Back",command=back1)
		btnback1.pack()







	btnstart = Button(root,relief=FLAT,border=0,fg="black",text="Play",font=("Comic sans MS",15,"bold"),command=play)
	btnstart.pack()
	btnAdd = Button(root,relief=FLAT,border=0,fg="black",text="ADD QUESTIONS",font=("Comic sans MS",15,"bold"),command=quizQuestions)
	btnAdd.pack()
	btnCreate = Button(root,relief=FLAT,border=0,fg="black",text="CREATE ACCOUNT",font=("Comic sans MS",15,"bold"),command=createAccount)
	btnCreate.pack()
	btnLogin = Button(root,relief=FLAT,border=0,fg="black",text="LOGIN PANEL",font=("Comic sans MS",15,"bold"),command=loginAccount)
	btnLogin.pack()
	#btnLogout = Button(root,relief=FLAT,border=0,fg="black",text="LOGOUT PANEL",font=("Comic sans MS",15,"bold"),command=logout)
	#btnLogout.pack()
	btnHelp = Button(root,relief=FLAT,border=0,fg="black",text="HELP",font=("Comic sans MS",15,"bold"),command=rules)
	btnHelp.pack()
	btnAbout = Button(root,relief=FLAT,border=0,fg="black",text="ABOUT US",font=("Comic sans MS",15,"bold"),command=about)
	btnAbout.pack()
	btnExit = Button(root,relief=FLAT,border=0,fg="black",text="EXIT",font=("Comic sans MS",15,"bold"),command=exit)
	btnExit.pack()

	


		
    


home()
if __name__ == "__main__":
	choice = 1
	while choice != 7:
		print('\n=========WELCOME TO QUIZ MASTER==========')
		print('-----------------------------------------')
		print('1. PLAY QUIZ')
		print('2. ADD QUIZ QUESTIONS')
		print('3. CREATE AN ACCOUNT')
		print('4. LOGIN PANEL')
		print('5. LOGOUT PANEL')
		print('6. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
		print('7. EXIT')
		print('8. ABOUT US')
		choice = int(input('ENTER YOUR CHOICE: '))
		if choice == 1:
			play()
		elif choice == 2:
			quizQuestions()
		elif choice == 3:
			createAccount()
		elif choice == 4:
			loginAccount()
		elif choice == 5:
			logout()
		elif choice == 6:
			rules()
		elif choice == 7:
			break
		elif choice == 8:
			about()
		else:
			print('WRONG INPUT. ENTER THE CHOICE AGAIN')


root.mainloop()

