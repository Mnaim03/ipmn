#ho in input "i", "tvg-id" e "stream"
from datetime import datetime
import sys

def data(): # Ottieni data atuale
 global time
 time = datetime.now()
 time = time.strftime('[ %Y-%m-%d - %H:%M ]') #rimpicciolisco ora 

def txtprint(): #stampa nel file
  with open('error.txt', 'w') as file:
    file.write(f"\n{time} --> Errore canale {tvgid}. Link stream fornito: ")
    file.write(f"\n{stream}")

def txtwipe(): #pulisci file
    with open('error.txt', 'r+') as file:
        file.truncate(0) #riduce la lunghezza del file a zero byte

#main
i = int(sys.argv[1])
#se i=0 --> scrivi
#se i≠0 --> ripulisci
tvgid= sys.argv[2]
stream= sys.argv[3]

if i == 0:
 data()
 txtprint()
else:
  txtwipe()