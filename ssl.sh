#!/bin/bash
  #zona attuale dove si trova la mia cartella
  code="$1"
  #=1 MacOS
  #=2 Linux server
  user="$2"
  
#PING TO GOOGLE
  chomd +x ping.sh
  ./ping.sh

#request save --> ch_status e host_log

  chmod +x ch/out/status.py
  python3 ch/out/status.py 3 "" "" "$user" 3 #i=3≠0 qunindi eseguirà whipe() & print_user()

  chmod +x ch/out/log.py
  python3 ch/out/log.py "$user"

#PULL
chmod +x pull_push.sh
./pull_push.sh 0 "$user" #=0 --> Pull

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################ START  ################\033[0m"
echo -e "\033[35m########################################\033[0m"
#START
 #zona attuale dove si trova la mia cartella
  chmod +x main.py  #do i permessi al main.py
  chmod +x ch_call.sh #do i permessi al file bash che chiama ch_get e ch_write
  python3 main.py $code #gli passo l'info per sceglere il driver chrome
 

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################# SAVE #################\033[0m"
echo -e "\033[35m########################################\033[0m"

 #SAVE
  chmod +x mono.py
  python3 mono.py
  #open -a VLC mono.m3u8
  echo -e "\033[32m File mono aggiornato \033[0m"


#PUSH
chmod +x pull_push.sh 
./pull_push.sh 3 "$user" #≠0 --> push

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################# STOP #################\033[0m"
echo -e "\033[35m########################################\033[0m"