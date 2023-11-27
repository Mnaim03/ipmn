#!/bin/bash
chmod +x ch_call.sh #gli faccio autodare i permessi
#per dare i permessi via shell: chmod +x eseg.py

#i seguenti elementi devono essere passati goni volta da main.py
#metto dei valori prova

file="$1" 
tvg_id="$2"
link_m3u8="$3"
stream="$4" #zone del file del canale
i=0

echo " "
echo "AVVIO $tvg_id"

if [ -z "$link_m3u8" ]; then
  while [ -z "$link_m3u8" ] && ["$i" -ne 10]; do
    #Incremento contatore
    ((i++))

    # Do i permessi al driver chrome
    echo -e "\033[33m ! cerco m3u8 $tvg_id -> tentativo $i \033[0m"
    chmod +x ch_get.py
    link_m3u8=$(python3 ch_get.py "$stream")

  done
else
    echo -e "\033[32m ! m3u8 pre-inserito \033[0m"
fi

#verifico errore 
if [ -z "$link_m3u8" ]; then
    echo "segnalo errore"
    #errore.py   #errore da segnale in error.txt
fi

echo "! scrivo m3u8 $tvg_id su $file"
chmod +x ch_write.py 
python3 ch_write.py "$file" "$tvg_id"  "$link_m3u8"
echo "FINE $tvg_id"