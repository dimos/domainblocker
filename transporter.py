#!/usr/bin/python3

import os

def cp_progress(fdest):
	if 'sudo ' in fdest:
		fdest = fdest.replace('sudo ', '')
	cp_header = "sudo cp ~/dimos-*/domainblocker.py /usr/local/bin/"
	cp_footer = fdest
	cpcmd = cp_header + cp_footer
	os.system(cpcmd)

def main():
	os.system("clear")
	print('''***********************************************
* 0. Πατήστε <0> για βοήθεια και επεξήγηση    *
***********************************************
	''')
	program_name = input("Εισάγετε το όνομα με το οποίο θέλετε να τρέχετε το domainblocker: ")
	if program_name == "0":
		os.system("clear")
		print('''Κάθε φορά που θα χρειαστεί να τρέξετε το πρόγραμμα πρέπει να πληκτρολογείτε
το όνομα του με την εντολή sudo μπροστά.Πχ sudo domainblocker.Οπότε πρέπει
να καθορίσετε το όνομα του προγράμματος στο σύστημά σας για να το χρησιμο-
ποιείτε με:

	sudo [όνομα προγράμματος]
	
Πατώντας <Enter> θα βγείτε από αυτή την οθόνη.Διαλέξτε ένα όνομα και πλη-
κτρολογείστε το στην νέα οθόνη χωρίς το "sudo " μπροστά.''')
		input()
		main()
	else:
		 cp_progress(program_name)

if __name__ == '__main__':
	main()
