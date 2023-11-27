from datetime import datetime
import sys

def data(): # Ottieni data atuale
 global time
 time = datetime.now()
 time = time.strftime('[ %Y-%m-%d - %H:%M ]') #rimpicciolisco ora 

def txtprint(host): #stampa nel file
  with open('log.txt', 'a') as file:
    file.write(f"\n{time} = {host}")

#main
host = sys.argv[1]
data()
txtprint(host)
