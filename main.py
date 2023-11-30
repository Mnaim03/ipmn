#richiamo ch_write.py per ogni canale
#gli devo passare link pagina web e percoro file
#gestisco tutti i canali 
import subprocess

#mbc4you --> mbc2
#elahmad
#dagav --> mtv, al jadeed
#fomny-tv.com -->lbci

# Chiamata al file bash con valori passati come argomenti

def manar():
  file='ch/arab.m3u8'
  tvgid='manar' #nome canale
  stream="https://www.elahmad.com/tv/almanartv.php" #link pagina da cui estrarre 
  link_m3u8="https://manar.live/iptv/tracks-v1a1/mono.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def alittihad():
  file='ch/arab.m3u8'
  tvgid='al_ittihad' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=alittihad" #link pagina da cui estrarre 
  link_m3u8="https://live.alittihad.tv:444/ittihad/index.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def aljadeed():
  file='ch/arab.m3u8'
  tvgid='al_jadeed' #nome canale
  #stream="http://dagav.com/v/arabic/arab3/aljadeed.php" #DAGAV
  stream="http://www.elahmad.com/tv/newtv.php" #ALAHMAD
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def jarabic():
  file='ch/arab.m3u8'
  tvgid='jazeera_arabic' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=aljazeer_ar1" #link pagina da cui estrarre 
  link_m3u8="https://live-hls-web-aja.getaj.net/AJA/01.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def jlive():
  file='ch/arab.m3u8'
  tvgid='jazeera_live' #nome canale
  stream="https://www.elahmad.com/tv/aljazeera_mubasher.htm" #link pagina da cui estrarre 
  link_m3u8="https://live-hls-web-ajm.getaj.net/AJM/01.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def lbci():
  file='ch/arab.m3u8'
  tvgid='lbci' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=lbc_1" #elahmad
  #stream="http://fomny-tv.com/fomnychannels.com/Ahpop/Ahpop.php?iframe=http://www.elahmad.com/tv/watchtv.php?id=lbc" #fomny-tv.com
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mayadeen():
  file='ch/arab.m3u8'
  tvgid='mayadeen' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=almayadeen1" #link pagina da cui estrarre 
  link_m3u8="https://mdnlv.cdn.octivid.com/almdn/smil:mpegts.stream.smil/chunklist_b3000000_t64NTQwcA==.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mtv():
  file='ch/arab.m3u8'
  tvgid='mtv' #nome canale
  #stream="http://dagav.com/v/arabic/arab3/mtv.php" #DEGAV
  stream="https://www.elahmad.com/tv/mtvlebanon.htm" #ALAHMAD
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mustakbal():
  file='ch/arab.m3u8'
  tvgid='mustakbal' #nome canale
  stream="https://www.elahmad.com/tv/futurelive.php" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def natgeo():
  file='ch/arab.m3u8'
  tvgid='natgeo' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=natgeo_1" #link pagina da cui estrarre 
  link_m3u8="https://admdn2.cdn.mangomolo.com/nagtv/smil:nagtv.stream.smil/chunklist_b4000000_t64MTA4MHA=.m3u8?adtv"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def nbn():
  file='ch/arab.m3u8'
  tvgid='nbn' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=nbn" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def otv():
  file='ch/arab.m3u8'
  tvgid='otv' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=otv_lb1" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def dwarab():
  file='ch/arab.m3u8'
  tvgid='dw_arab' #nome canale
  stream="https://www.elahmad.com/tv/arabic-tv-online.php?id=dwtvarabia" #link pagina da cui estrarre 
  link_m3u8="https://dwamdstream103.akamaized.net/hls/live/2015526/dwstream103/stream05/streamPlaylist.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])


def mbc1():
  file='ch/mbc.m3u8'
  tvgid='mbc1' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc1_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-live-ak.akamaized.net/out/v1/0965e4d7deae49179172426cbfb3bc5e/index_7.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbc2():
  file='ch/mbc.m3u8'
  tvgid='mbc2' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc2_tv_1" #elahmad
  #stream="https://www.mbc4you.com/mbc-2-shahid-movies-radan-2023_6.html" #mbc4you
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbc3():
  file='ch/mbc.m3u8'
  tvgid='mbc3' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc3_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://mbc3-eur-prod-dub-ak.akamaized.net/out/v1/fce09dd6a967431a871efb3b8dec9f82/index_1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbc4():
  file='ch/mbc.m3u8'
  tvgid='mbc4' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc4_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://mbc4-prod-dub-ak.akamaized.net/out/v1/c08681f81775496ab4afa2bac7ae7638/index_1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbc5():
  file='ch/mbc.m3u8'
  tvgid='mbc5' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc5_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-masr2-ak.akamaized.net/out/v1/2720564b6a4641658fdfb6884b160da2/index_1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbcmax():
  file='ch/mbc.m3u8'
  tvgid='mbc_max' #nome canale
  stream="https://www.elahmad.com/tv/watchtv.php?id=mbc_max" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbcaction():
  file='ch/mbc.m3u8'
  tvgid='mbc_action' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbcaction_tv_1" #link pagina da cui estrarre 
  link_m3u8=""
# subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbcvariety():
  file='ch/mbc.m3u8'
  tvgid='mbc_variety' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc_variety" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbcdrama():
  file='ch/mbc.m3u8'
  tvgid='mbc_drama' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbcdrama_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-live-ak.akamaized.net/out/v1/b0b3a0e6750d4408bb86d703d5feffd1/index_20.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def mbcmasr():
  file='ch/mbc.m3u8'
  tvgid='mbc_masr' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbcmasr_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-masr-ak.akamaized.net/out/v1/d5036cabf11e45bf9d0db410ca135c18/index_29.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])



def bein1():
  file='ch/sport.m3u8'
  tvgid='bein1' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_1" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/beinsport1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def bein2():
  file='ch/sport.m3u8'
  tvgid='bein2' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_2" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/beinsport2.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def bein3():
  file='ch/sport.m3u8'
  tvgid='bein3' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_3" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/beinsport3.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def bein4():
  file='ch/sport.m3u8'
  tvgid='bein4' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_4" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/beinsport4.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def bein5():
  file='ch/sport.m3u8'
  tvgid='bein5' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_5" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/beinsport5.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def ssc1():
  file='ch/sport.m3u8'
  tvgid='ssc1' #nome canale
  stream="https://ayas.ir/sp/ayasktv.php?link=https://af.ayassport.ir/hls2/ssc1.m3u8&title=Ayas%20sport" #link pagina da cui estrarre 
  link_m3u8="https://af.ayassport.ir/hls2/ssc1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def ssc2():
  file='ch/sport.m3u8'
  tvgid='ssc2' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=ssc_sports_2" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def ssc3():
  file='ch/sport.m3u8'
  tvgid='ssc3' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=ssc_sports_3" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def ads1():
  file='ch/sport.m3u8'
  tvgid='ads1' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=abudhabi_sports1" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def ads2():
  file='ch/sport.m3u8'
  tvgid='ads2' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=abudhabi_sports2" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])



def cinema():
  file='ch/rotana.m3u8'
  tvgid='cinema' #nome canale
  stream="https://www.elahmad.com/tv/watchtv.php?id=rotana_cinema" #link pagina da cui estrarre 
  link_m3u8="https://daiconnect.com/live/hls/rotana/cinema-ksa/088fc425900dc92b37981c5043d969dd/.m3u8?requestuid=c70abcb5-64bb-4596-9d36-9f8c25032fe4"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def aflam():
  file='ch/rotana.m3u8'
  tvgid='aflam+' #nome canale
  stream="https://www.elahmad.com/tv/live/live_stream.php?id=rotana_aflam_plus" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])

def comedy():
  file='ch/rotana.m3u8'
  tvgid='comedy' #nome canale
  stream="https://www.elahmad.com/tv/watchtv.php?id=rotana_comedy" #link pagina da cui estrarre 
  link_m3u8="https://rotanastudios-rotanacomedy-1-eu.xiaomi.wurl.tv/8b19722f7772362323148961d5a4c446.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream ])


#main
manar()
alittihad()
aljadeed()
jarabic()
jlive()
lbci()
mayadeen()
mtv()
mustakbal()
natgeo()
nbn()
otv()
dwarab()

mbc1()
mbc2()
mbc3()
mbc4()
mbc5()
mbcmax()
mbcaction()
mbcvariety()
mbcdrama()
mbcmasr()

bein1()
bein2()
bein3()
bein4()
bein5()
ssc1()
ssc2()
ssc3()
ads1()
ads2()

cinema()
aflam()
comedy()