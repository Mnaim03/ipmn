#INPUT --> operazione(=0/≠0), id, stram, host (o user), status(=0/≠0)
from datetime import datetime
import sys

def data(): # Ottieni data atuale
 global time
 time = datetime.now()
 time = time.strftime('[ %Y-%m-%d - %H:%M ]') #rimpicciolisco ora 

def txtprintw(): #stampa nel file
  with open('status.txt', 'w') as file:
    file.write(f"\n\n {tvgid} --> Estrazione m3u8 ESEGUITA CORRETTAMENTE (✓).")
    file.write(f"\n Link stream fornito: {stream}")

def txtprintf(): #stampa nel file
  with open('status.txt', 'w') as file:
    file.write(f"\n\n {tvgid} --> Estrazione m3u8 ANDATA MALE (x). ")
    file.write(f"\n Link stream fornito: {stream}")

def txtwipe(): #pulisci file
    with open('status.txt', 'r+') as file:
        file.truncate(0) #riduce la lunghezza del file a zero byte

def print_user()
    with open('status.txt', 'w') as file:
      file.write(f"\n {time} -->{user} has done a update: ")
#main
i = int(sys.argv[1])
#se i=0 --> scrivi
#se i≠0 --> ripulisci
tvgid= sys.argv[2]
stream= sys.argv[3]
user= sys.argv[4]
status= sys.argv[5] #status of channel
# status=0 --> working
# status=1 --> NOT working

 data()
if i == 0:
  if status == 0:
      txtprintw()
  else: 
      txtprintf()
else: #i ≠ 0
  txtwipe()
  print_user()