import sys
import re
#Costatanti (dovranno essere passati dalla run)
file = ''
tvg_id = ''
link = ''

#funzione che importa i dati da bash
def importa_dati():
    global file, tvg_id, link
    file = sys.argv[1]
    tvg_id = sys.argv[2]
    link = sys.argv[3]


#funzione stampa solo per testing
def stampa():
    print("file:", file)
    print("tvg-id:", tvg_id)
    print("Link:", link)



def replace():
    with open(file, 'r') as input_file:
        lines = input_file.readlines()

    with open(file, 'w') as output_file:
        found_channel = False

        for line in lines:
            if found_channel and line.startswith('http'):
                output_file.write(link + '\n')
                found_channel = False
            else:
                if line.strip().startswith('#EXTINF'):
                    tvg_id_find = None
                    segments = line.split(' ')
                    for segment in segments:
                        if segment.startswith('tvg-id='):
                            tvg_id_find = segment.split('"')[1]
                            break
                    if tvg_id_find == tvg_id:
                        found_channel = True
                output_file.write(line)

# Esempio d'uso
importa_dati()
stampa()
replace()