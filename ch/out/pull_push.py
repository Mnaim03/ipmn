#INPUT --> operation, host
#=0 pull
#≠0 push
from datetime import datetime
import sys

def data(): # Ottieni data atuale
 global time
 time = datetime.now()
 time = time.strftime('[ %Y-%m-%d - %H:%M ]') #rimpicciolisco ora 

def print_pull(): #stampa nel file
  with open('pull_push.txt', 'a') as file:
    file.write(f"\n PULL {time} -----> {host}")

def print_push(): #stampa nel file
  with open('pull_push.txt', 'a') as file:
    file.write(f"\n PUSH {time} -----> {host}")

#main
i = sys.argv[1]
host = sys.argv[2]
data()
 
if i == 0:
  print_pull()
else: #i ≠ 0
  print_push()
