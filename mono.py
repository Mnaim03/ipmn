def replace_and_merge(destination_file, source_files):
    # Svuota il file di destinazione
    open(destination_file, 'w', encoding='utf-8').close()

    with open(destination_file, 'a', encoding='utf-8') as output_file:
        for file_path in source_files:
            with open(file_path, 'r', encoding='utf-8') as input_file:
                for line in input_file:
                    output_file.write(line)

                output_file.write('\n')

def delete_live(destination_file):
    # Apro il file in lettura
    with open(destination_file, 'r') as file:
       lines = file.readlines()  # Leggo tutte le righe del file

    # Rimuovo le righe che contengono la stringa '#EXTM3U'
    lines = [line for line in lines if '#EXTM3U' not in line]

    # Sovrascrivo il file originale con le righe modificate
    with open(destination_file, 'w') as file:
       file.writelines(lines)

def add_live(destination_file):
    # Definisco la riga da aggiungere all'inizio del file
    line_to_add = "#EXTM3U\n"

    # Leggo il contenuto del file esistente
    with open(destination_file, 'r') as file:
        content = file.read()

    # Scrivo il contenuto del file con la riga aggiunta all'inizio
    with open(destination_file, 'w') as file:
       file.write(line_to_add + content)

    

# Lista dei file sorgente da unire
source_files = ['ch/arab.m3u8', 'ch/mbc.m3u8', 'ch/sport.m3u8', 'ch/rotana.m3u8']

# File destinazione dove verranno uniti i contenuti dei file sorgente
destination_file = 'ch/mono.m3u8'

# Esegui la sostituzione e l'unione dei file
replace_and_merge(destination_file, source_files)

#elimini ogni #EXTM3U
delete_live(destination_file)

#aggiungi #EXTM3U all'inzio
add_live(destination_file)

