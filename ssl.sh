#Start-Save-Loop --> S.S.L.
#!/bin/bash
echo ""
echo "\033[35m########################################\033[0m"
echo "\033[35m################ START  ################\033[0m"
echo "\033[35m########################################\033[0m"
#START
  cd /Users/mohamadnaim/Documents/pyreq  #zona attuale dove si trova la mia cartella
  chmod +x main.py  #do i permessi al main.py
  chmod +x ch_call.sh #do i permessi al file bash che chiama ch_get e ch_write
  python3 main.py 
 
  cd /Users/mohamadnaim/Documents/pyreq/ch
  #open -a VLC mono.m3u8

#SAVE
ffmpeg -i "contact:arab.m3u8|mbc.m3u8|sport.m3u8|rotana.m3u8" -c copy mono.m3u8

#LOOP
echo ""
echo "\033[35m########################################\033[0m"
echo "\033[35m################# STOP #################\033[0m"
echo "\033[35m########################################\033[0m"