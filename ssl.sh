#!/bin/bash
cd /Users/mohamadnaim/Documents/pyreq  #zona attuale dove si trova la mia cartella
  chomd +x ping.sh
  ./ping.sh

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m######### PULL GIT REPO ################\033[0m"
echo -e "\033[35m########################################\033[0m"
echo ""

git pull  
echo -e "\033[32m Pull eseguita correttamente. \033[0m"

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################ START  ################\033[0m"
echo -e "\033[35m########################################\033[0m"
#START
  cd /Users/mohamadnaim/Documents/pyreq  #zona attuale dove si trova la mia cartella
  chmod +x main.py  #do i permessi al main.py
  chmod +x ch_call.sh #do i permessi al file bash che chiama ch_get e ch_write
  python3 main.py 
 

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################# SAVE #################\033[0m"
echo -e "\033[35m########################################\033[0m"

 #SAVE
  cd /Users/mohamadnaim/Documents/pyreq
  chmod +x mono.py
  python3 mono.py
  #open -a VLC mono.m3u8
  echo -e "\033[32m File mono aggiornato \033[0m"


echo "" 
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################# GIT ##################\033[0m"
echo -e "\033[35m########################################\033[0m"

#installa gh
 git add ./*
 git commit -m 'Update'
 git push
 echo -e "\033[32m Commit & Push eseguito \033[0m"

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################# STOP #################\033[0m"
echo -e "\033[35m########################################\033[0m"