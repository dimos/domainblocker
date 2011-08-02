#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#       domainblocker.py
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

#----------------- Συναρτήσεις -----------------#

def block_site():
		os.system("cd ~")
		os.system('''#!/bin/bash

	######################
	# Ορισμοί μεταβλητών
	hostsfile=/etc/hosts
	redirect="127.0.0.1"
	######################

	user=`whoami`

	if [ $user = "root" ]
	then
	another="Yes"
		while [ $another = "Yes" ]
		do
			site2bblocked=`zenity --entry \
				--title="Block Site" \
				--text="Εισάγετε την διεύθυνση που θέλετε να μπλοκάρετε.
	ΧΩΡΊΣ http:// !!!"`
			if [ $site2bblocked ]
			then
				another=`zenity --list \
					--title="Another site?" \
					--column="Θέλετε να εισάγετε/μπλοκάρετε και άλλο site;" "Yes" "No"`
			else
				another="No"
			fi

		echo "$redirect $site2bblocked" >> $hostsfile
		done
	else
		zenity --info --text="Πρέπει να τρέξετε αυτή την εφαρμογή ως root.\nΔοκιμάστε να προσθέσετε ένα 'sudo' πριν την εντολή."
	fi

	return 0
	''')

def unblock():
	domain_to_unblock = input("Δώστε το domain που θέλετε να ξεμπλοκάρετε: ")
	f = open('/etc/hosts', "r" )
	data_list = [data for data in open('/etc/hosts', "r" )]
	f.close()
	line_to_del = "127.0.0.1 " + domain_to_unblock + "\n"
	i=0
	while data_list[i] != line_to_del:
		i=i+1
	del(data_list[i])
	fout = open("/etc/hosts", "w")
	fout.writelines(data_list)
	fout.close()

def backup_list():
	backup_file = input("Εισάγετε το όνομα του αρχείου με τα μπλοκαρισμένα sites: ")
	srt_sites_to_backup = input("Εισάγετε τον αριθμό τον μπλοκαρισμένων sites που θέλετε να επαναφέρετε: ")
	backup_cmd_head = "cd ~ && sudo tail -"
	backup_cmd_footer = " " + backup_file + " >> /etc/hosts"
	os.system(backup_cmd_head + srt_sites_to_backup + backup_cmd_footer)

def dbinfo():
	os.system("clear")
	print('''
DOMAIN BLOCKER  (Μπλοκάρετε ιστοσελίδες)
-----------------------------------------------------------------------------
Δήμος Πούπος                                                 Έκδοση: 1.0
-----------------------------------------------------------------------------

Με την παρών εφαρμογή μπορείτε να μπλοκάρετε διάφορες ιστοσελίδες ώστε να,
μην είναι ορατές σε κανένα άτομο το οποίο έχει πρόσβαση στον υπολογιστή σας.
Η εφαρμογή είναι γραμμένη σε Python & Bash και τρέχει μόνο σε συστήματα Linux.
Στην ουσία κάνει τροποποιήσεις στο αρχείο /etc/hosts και προσθέτει ή αφαιρεί
από αυτό πράγματα που καθορίζετε εσείς.

To πρόγραμμα διατίθεται δωρεάν υπό την άδεια χρήσης GNU GPL και μπορείτε να 
πειραματιστείτε με αυτό, καθώς και να το επαναδιαθέσετε εάν το επιθυμείτε.
Περισσότερα για την GPL: <http://www.gnu.org/licenses/>
''')

#-------------- Συναρτήσεις Τέλος --------------#

#--------------- Κύρια Συνάρτηση ---------------#
def main():
	os.system("clear")
	print("\n---ΜΕΝΟΥ---\n")
	menuc = int(input("1. Μπλοκάρετε κάποιο site \n2. Διαγραφή μπλοκαρισμένου site \n3. Επαναφορά λίστας μπλοκαρισμένων sites \n4. Πληροφορίες \n\n0. Έξοδος \nΔώστε τον αριθμό της επιλογής σας: "))
	if menuc == 1:
		block_site()

	elif menuc == 2:
		unblock()

	elif menuc == 3:
		backup_list()
		
	elif menuc == 4:
		dbinfo()
		input()
		main()

	#elif !(menuc):
	elif menuc == 0:
		exit(0)
		
if  __name__ == '__main__':
	main()
