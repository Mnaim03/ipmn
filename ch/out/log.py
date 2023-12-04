from datetime import datetime
import sys

def data(): # Ottieni data atuale
 global time
 time = datetime.now()
 time = time.strftime('[ %Y-%m-%d - %H:%M ]') #rimpicciolisco ora 

def txtprint(host): #stampa nel file
  with open('ch/out/log.txt', 'a') as file:
    file.write(f'\n <br><p class="txtlog">🔋<font class="smalldata">{time}</font>:{host}</p><br>')

#main
host = sys.argv[1]
data()
txtprint(host)
