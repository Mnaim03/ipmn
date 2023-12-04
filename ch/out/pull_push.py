#INPUT --> operation, host
#=0 pull
#≠0 push
from datetime import datetime
import sys

def data(): # Ottieni data atuale
 global time
 time = datetime.now()
 time = time.strftime('[ %Y-%m-%d - %H:%M ]') #rimpicciolisco ora 

def printinfo(i,host,time): #stampa nel file
  with open('ch/out/pull_push.txt', 'a') as file:
        if i == 0:
            file.write(f'\n<br><p class="txtlog">🔼PULL---<font class="smalldata">{time}</font>:{host}</p><br>')
        else:
            file.write(f'\n<br><p class="txtlog">🔽PUSH---<font class="smalldata">{time}</font>:{host}</p><br>')

#main
try:
  i = int(sys.argv[1])
except ValueError:
  print("Il primo argomento deve essere un numero intero")
  sys.exit(1)
host = sys.argv[2]

data()
printinfo(i,host,time)
