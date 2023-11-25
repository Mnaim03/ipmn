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

    echo -e "\e[31m !!! Connessione NON stabile !!! \e[0m"
    # Aggiungi un ritardo prima di tentare nuovamente la connessione
    sleep 5  # Ritardo di 5 secondi (modificabile)
done
clear