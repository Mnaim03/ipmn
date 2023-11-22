#Start-Save-Loop --> S.S.L.
#!/bin/bash
echo ""
echo "\033[35m########################################\033[0m"
echo "\033[35m################ START  ################\033[0m"
echo "\033[35m########################################\033[0m"
#START
  cd /Users/mohamadnaim/Desktop/py-req  #zona attuale dove si trova la mia cartella
  chmod +x main.py  #do i permessi al main.py
  chmod +x ch_call.sh #do i permessi al file bash che chiama ch_get e ch_write
  python3 main.py 
 
  #cd /Users/mohamadnaim/Desktop/py-req/ch
  #open -a VLC mono.m3u8

#SAVE

#LOOP
echo ""
echo "\033[35m########################################\033[0m"
echo "\033[35m################# STOP #################\033[0m"
echo "\033[35m########################################\033[0m"