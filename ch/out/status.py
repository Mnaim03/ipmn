#INPUT --> operazione(=0/≠0), id, stream, host (o user), status(=0/≠0)
from datetime import datetime
import sys

def data(): # Ottieni data atuale
 global time
 time = datetime.now()
 time = time.strftime('[ %Y-%m-%d - %H:%M ]') #rimpicciolisco ora 

def txtprintw(): #stampa nel file
  with open('ch/out/status.txt', 'a') as file:
    file.write(f'\n\n<div class="content container text-center"><p class="h7"><font class="channel h2"> {tvgid} </font>')
    file.write(f'\n<a href="{stream}"><button type="button" class="btn btn-success btnlink">ESTAZIONE m3u8 ESEGUITA(✓)</button></a></p></div>')

def txtprintf(): #stampa nel file
  with open('ch/out/status.txt', 'a') as file:
    file.write(f'\n\n<div class="content container text-center"><p class="h7"><font class="channel h2"> {tvgid} </font>')
    file.write(f'\n<a href="{stream}"><button type="button" class="btn btn-danger btnlink">ESTAZIONE m3u8 NON ESEGUITA(x)</button></a></p></div>')


def txtwipe(): #pulisci file
    with open('ch/out/status.txt', 'r+') as file:
        file.truncate(0) #riduce la lunghezza del file a zero byte

def print_user():
    with open('ch/out/status.txt', 'a') as file:
      file.write(f"\n<div class=""content container text-center""><p><font class=""bigdata"">{time}</font><br><font class=""user"">{user} has done a update</font></p></div>")
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
        txtprintf()
    else: #status ≠ 0
        txtprintw()
else: #i ≠ 0
  txtwipe()
  print_user()