#!/bin/bash

# Indirizzo IP per il ping (es. 8.8.8.8 per il server DNS di Google)
IP_ADDRESS="8.8.8.8"
# Numero di tentativi di ping
NUM_ATTEMPTS=3
# Variabile per verificare se la connessione è stata stabile
connection_stable=false

echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m######### TENTO CONNESSIONE ############\033[0m"
echo -e "\033[35m########################################\033[0m"
# Esegui il ciclo finché la connessione non è stabile
while [ "$connection_stable" = false ]
do
    # Esegui il ping e controlla la risposta
    for ((i=1; i<=$NUM_ATTEMPTS; i++))
    do
        ping -c 1 -W 2 $IP_ADDRESS > /dev/null
        if [ $? -eq 0 ]; then
            echo "\033[32m Connessione stabile. \033[0m"
            connection_stable=true
            break 2  # Esci completamente dai cicli
        fi
    done

    echo -e "\e[31mConnessione NON stabile\e[0m"
    # Aggiungi un ritardo prima di tentare nuovamente la connessione
    sleep 5  # Ritardo di 5 secondi (modificabile)
done

clear
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
 
clear

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

clear

echo "" 
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################# GIT ##################\033[0m"
echo -e "\033[35m########################################\033[0m"

#installa gh
#git pull #si prende i file modificati più recenti
git add ./*
git commit -m 'Update'
git push
echo -e "\033[32m Commit & Push eseguito \033[0m"

echo ""
echo -e "\033[35m########################################\033[0m"
echo -e "\033[35m################# STOP #################\033[0m"
echo -e "\033[35m########################################\033[0m"