import os
from os.path import exists
import sys

os.system("clear")
print("------------------------------------------------")
print("| MeltOS                                       |")
print("| It's not really an OS, just a python script! |")
print("------------------------------------------------")
def read_cmd(cmd):
	if(cmd[0:4]=="exit" and len(cmd)==4):
		print("Exiting gracefully...")
		os.system("clear")
		exit()
	elif(cmd[0:3]=="dir" and len(cmd)==3):
		print(os.listdir(cwd))
	elif(cmd[0:3]=="cd " and len(cmd)>=4):
		try:
			os.chdir(cmd[3:len(cmd)])
		except FileNotFoundError:
			print("E: " + cmd[3:len(cmd)] + " does not exist")
		except NotADirectoryError:
			print("E: " + cmd[3:len(cmd)] + " is not a directory")
		except PermissionError:
			print("E: " + cmd[3:len(cmd)] + " is beyond your permissions")
	elif(cmd[0:5]=="clear" or cmd[0:3]=="cls"):
		if(len(cmd)==3 or len(cmd)==5):
			os.system("clear")
		else:
			print("E: \"" + cmd + "'| not found or improper")
	elif(cmd[0:5]=="wget " and len(cmd)>=5):
		os.system("wget " + cmd[5:len(cmd)] + " >> " + homedir + "/tmp.txt")
		with open(homedir + "/tmp.txt", "r") as out:
			print(out.read())
	elif(cmd[0:6]=="shell " and len(cmd)>=6):
		os.system(cmd[6:len(cmd)] + " >> " + homedir + "/tmp.txt")
		with open(homedir + "/tmp.txt", "r") as out:
			print(out.read())
	elif(cmd[0:5]=="echo " and len(cmd)>=5):
		print(cmd[5:len(cmd)])
	elif(cmd[0:4]=="scr " and len(cmd)>=4):
		filepath = cmd[4:len(cmd)]
		with open(filepath) as fp:
			for index, line in enumerate(fp):
				read_cmd(line.strip())
	elif(cmd[0:5]=="read " and len(cmd)>=5):
		filepath = cmd[5:len(cmd)]
		with open(filepath) as fp:
			for index, line in enumerate(fp):
				print(line.strip())
	else:
		print("E: \"" + cmd + "\" not found or improper")
homedir = os.getcwd()
while True:
	cwd = os.getcwd() 
	username = os.getlogin()
	tmpexists = exists(homedir + "/tmp.txt")
	if(tmpexists):
		os.remove(homedir + "/tmp.txt")
	pcmd = input(username + "@" + cwd + ": ")
	read_cmd(pcmd)
