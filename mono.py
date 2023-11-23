def replace_and_merge(destination_file, source_files):
    # Svuota il file di destinazione
    open(destination_file, 'w', encoding='utf-8').close()

    with open(destination_file, 'a', encoding='utf-8') as output_file:
        for file_path in source_files:
            with open(file_path, 'r', encoding='utf-8') as input_file:
                for line in input_file:
                    output_file.write(line)

                output_file.write('\n')

# Lista dei file sorgente da unire
source_files = ['ch/arab.m3u8', 'ch/mbc.m3u8', 'ch/sport.m3u8', 'ch/rotana.m3u8']

# File destinazione dove verranno uniti i contenuti dei file sorgente
destination_file = 'ch/mono.m3u8'

# Esegui la sostituzione e l'unione dei file
replace_and_merge(destination_file, source_files)


