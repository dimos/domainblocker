#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#       transporter.py
#       
#       Copyright 2011 Dimos Poupos <dimosrc@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, see <http://www.gnu.org/licenses/>
#		or write to the Free Software Foundation, Inc., 51 Franklin Street,
#		Fifth Floor, Boston, MA 02110-1301, USA.
#       
#       

import os

def cp_progress(fdest):
	if 'sudo ' in fdest:
		fdest = fdest.replace('sudo ', '')
	cp_header = "sudo cp ~/dimos-*/domainblocker.py /usr/local/bin/"
	cp_footer = fdest
	cpcmd = cp_header + cp_footer
	os.system(cpcmd)
	os.system("clear")
	print("[Η διαδικασία ολοκληρώθηκε!]")
	print("Για να τρέξετε το πρόγραμμα δώστε: sudo ",fdest)

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
