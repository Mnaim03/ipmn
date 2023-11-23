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
 

echo ""
echo "\033[35m########################################\033[0m"
echo "\033[35m################# SAVE #################\033[0m"
echo "\033[35m########################################\033[0m"
 #SAVE
  cd /Users/mohamadnaim/Documents/pyreq
  chmod +x mono.py
  python3 mono.py
  #open -a VLC mono.m3u8
  echo "\033[32m File mono aggiornato \033[0m"
echo "" 
echo "\033[35m########################################\033[0m"
echo "\033[35m################# GIT ##################\033[0m"
echo "\033[35m########################################\033[0m"

git add ./*
git commit -m 'Update'
git push
echo "\033[32m Commit & Push eseguito \033[0m"

echo ""
echo "\033[35m########################################\033[0m"
echo "\033[35m################# STOP #################\033[0m"
echo "\033[35m########################################\033[0m"