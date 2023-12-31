#richiamo ch_write.py per ogni canale
#gli devo passare link pagina web e percoro file
#gestisco tutti i canali 
import subprocess
import sys

# Chiamata al file bash con valori passati come argomenti

def manar():
  file='ch/arab.m3u8'
  tvgid='manar' #nome canale
  stream="https://www.elahmad.com/tv/almanartv.php" #link pagina da cui estrarre 
  link_m3u8="https://e2.manar.live:9000/live/tracks-v1a1/mono.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def alittihad():
  file='ch/arab.m3u8'
  tvgid='al_ittihad' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=alittihad" #link pagina da cui estrarre 
  link_m3u8="https://live.alittihad.tv:444/ittihad/index.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def aljadeed():
  file='ch/arab.m3u8'
  tvgid='al_jadeed' #nome canale
  #stream="http://dagav.com/v/arabic/arab3/aljadeed.php" #DAGAV
  stream="http://www.elahmad.com/tv/newtv.php" #ALAHMAD
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def jarabic():
  file='ch/arab.m3u8'
  tvgid='jazeera_arabic' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=aljazeer_ar1" #link pagina da cui estrarre 
  link_m3u8="https://live-hls-web-aja.getaj.net/AJA/01.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def jlive():
  file='ch/arab.m3u8'
  tvgid='jazeera_live' #nome canale
  stream="https://www.elahmad.com/tv/aljazeera_mubasher.htm" #link pagina da cui estrarre 
  link_m3u8="https://live-hls-web-ajm.getaj.net/AJM/01.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def lbci():
  file='ch/arab.m3u8'
  tvgid='lbci' #nome canale
  stream="https://www.elahmad.com/tv/lbc.php" #elahmad
  #stream="http://fomny-tv.com/fomnychannels.com/Ahpop/Ahpop.php?iframe=http://www.elahmad.com/tv/watchtv.php?id=lbc" #fomny-tv.com
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mayadeen():
  file='ch/arab.m3u8'
  tvgid='mayadeen' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=almayadeen1" #link pagina da cui estrarre 
  link_m3u8="https://mdnlv.cdn.octivid.com/almdn/smil:mpegts.stream.smil/chunklist_b3000000_t64NTQwcA==.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mtv():
  file='ch/arab.m3u8'
  tvgid='mtv' #nome canale
  #stream="http://dagav.com/v/arabic/arab3/mtv.php" #DEGAV
  stream="https://www.elahmad.com/tv/mtvlebanon.htm" #ALAHMAD
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mustakbal():
  file='ch/arab.m3u8'
  tvgid='mustakbal' #nome canale
  stream="https://www.elahmad.com/tv/futurelive.php" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def natgeo():
  file='ch/arab.m3u8'
  tvgid='natgeo' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=natgeo_1" #link pagina da cui estrarre 
  link_m3u8="https://admdn2.cdn.mangomolo.com/nagtv/smil:nagtv.stream.smil/chunklist_b4000000_t64MTA4MHA=.m3u8?adtv"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def nbn():
  file='ch/arab.m3u8'
  tvgid='nbn' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=nbn" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def otv():
  file='ch/arab.m3u8'
  tvgid='otv' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=otv_lb1" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def dwarab():
  file='ch/arab.m3u8'
  tvgid='dw_arab' #nome canale
  stream="https://www.elahmad.com/tv/arabic-tv-online.php?id=dwtvarabia" #link pagina da cui estrarre 
  link_m3u8="https://dwamdstream103.akamaized.net/hls/live/2015526/dwstream103/stream05/streamPlaylist.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def dai3a():
  file='ch/arab.m3u8'
  tvgid='dai3a' #nome canale
  stream="http://live.multies.net/livetv/deiaa-dayea2/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/728.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def dai3a2():
  file='ch/arab.m3u8'
  tvgid='dai3a2' #nome canale
  stream="http://live.multies.net/livetv/deiaa-dayea1/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/832.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def chirba():
  file='ch/arab.m3u8'
  tvgid='chirba' #nome canale
  stream="http://live.multies.net/livetv/al-khirba/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/727.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def alab():
  file='ch/arab.m3u8'
  tvgid='alab' #nome canale
  stream="http://live.multies.net/ent-ch/series-ch/el-leaba/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/788.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i]) 

def adel_karam():
  file='ch/arab.m3u8'
  tvgid='adelkaram' 
  stream="http://live.multies.net/ent-ch/movies-ch/alzaeem-tv/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/794.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i]) 

def film_arab():
  file='ch/arab.m3u8'
  tvgid='filmarab'
  stream="http://live.multies.net/ent-ch/movies-ch/multies-cinema/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/792.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i]) 

def film_arab2():
  file='ch/arab.m3u8'
  tvgid='filmarab2'
  stream="http://live.multies.net/ent-ch/movies-ch/multies-aflam1/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/751.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i]) 

def film_arab3():
  file='ch/arab.m3u8'
  tvgid='filmarab3'
  stream="http://live.multies.net/ent-ch/movies-ch/multies-aflam2/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/752.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i]) 

def comedy_arab():
  file='ch/arab.m3u8'
  tvgid='comedyarab'
  stream="http://live.multies.net/ent-ch/movies-ch/multies-comedy/" #live.multies.net
  link_m3u8="http://multies.xyz/live/87076BB68235FC3242A4CB05234563EB/793.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i]) 




def mbc1():
  file='ch/mbc.m3u8'
  tvgid='mbc1' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc1_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-live-ak.akamaized.net/out/v1/0965e4d7deae49179172426cbfb3bc5e/index_7.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbc2():
  file='ch/mbc.m3u8'
  tvgid='mbc2' #nome canale
  #stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc2_tv_1" #elahmad
  stream="http://live.multies.net/ent-ch/mbc-ch/mbc2/" #live.multies.net
  link_m3u8="http://212.102.58.251:8080/live/Nroa0AohHn/z3d8ZHNBWt/191.m3u8" 
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbc3():
  file='ch/mbc.m3u8'
  tvgid='mbc3' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc3_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://mbc3-eur-prod-dub-ak.akamaized.net/out/v1/fce09dd6a967431a871efb3b8dec9f82/index_1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbc4():
  file='ch/mbc.m3u8'
  tvgid='mbc4' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc4_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://mbc4-prod-dub-ak.akamaized.net/out/v1/c08681f81775496ab4afa2bac7ae7638/index_1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbc5():
  file='ch/mbc.m3u8'
  tvgid='mbc5' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc5_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-masr2-ak.akamaized.net/out/v1/2720564b6a4641658fdfb6884b160da2/index_1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbcmax():
  file='ch/mbc.m3u8'
  tvgid='mbc_max' #nome canale
  #stream="https://www.elahmad.com/tv/watchtv.php?id=mbc_max" #elahmad 
  stream="http://live.multies.net/ent-ch/mbc-ch/mbc-max/" #live.multies.net 
  link_m3u8="http://multies.xyz/live/68BA1E5E2B26F84339925A947BF1BBEB/135.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbcaction():
  file='ch/mbc.m3u8'
  tvgid='mbc_action' #nome canale
  #stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbcaction_tv_1" #elahmad
  stream="http://live.multies.net/ent-ch/mbc-ch/mbc-action/" #live.multies.net 
  link_m3u8="http://154.58.202.18:8080/mbc2/tracks-v1a1/mono.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbcvariety():
  file='ch/mbc.m3u8'
  tvgid='mbc_variety' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbc_variety" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbcdrama():
  file='ch/mbc.m3u8'
  tvgid='mbc_drama' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbcdrama_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-live-ak.akamaized.net/out/v1/b0b3a0e6750d4408bb86d703d5feffd1/index_20.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def mbcmasr():
  file='ch/mbc.m3u8'
  tvgid='mbc_masr' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=mbcmasr_tv_1" #link pagina da cui estrarre 
  link_m3u8="https://shls-masr-ak.akamaized.net/out/v1/d5036cabf11e45bf9d0db410ca135c18/index_29.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def dubai_one():
  file='ch/mbc.m3u8'
  tvgid='dubaione' #nome canale
  stream="http://live.multies.net/ar-gulf-ch/uae-ch/dubai-one/" #live.multies.net 
  link_m3u8="http://dminnvll.cdn.mangomolo.com/dubaione/smil:dubaione.stream.smil/chunklist_b1800000.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])



def bein1():
  file='ch/sport.m3u8'
  tvgid='bein1' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_1" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/ayas1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def bein2():
  file='ch/sport.m3u8'
  tvgid='bein2' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_2" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/ayas2.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def bein3():
  file='ch/sport.m3u8'
  tvgid='bein3' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_3" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/ayas3.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def bein4():
  file='ch/sport.m3u8'
  tvgid='bein4' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_4" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/ayas4.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def bein5():
  file='ch/sport.m3u8'
  tvgid='bein5' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=bein_m_5" #link pagina da cui estrarre 
  link_m3u8="https://stream.ayas.ir/hls2/ayas5.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def ssc1():
  file='ch/sport.m3u8'
  tvgid='ssc1' #nome canale
  stream="https://ayas.ir/sp/ayasktv.php?link=https://af.ayassport.ir/hls2/ssc1.m3u8&title=Ayas%20sport" #link pagina da cui estrarre 
  link_m3u8="https://af.ayassport.ir/hls2/ssc1.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def ssc2():
  file='ch/sport.m3u8'
  tvgid='ssc2' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=ssc_sports_2" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def ssc3():
  file='ch/sport.m3u8'
  tvgid='ssc3' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=ssc_sports_3" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def ads1():
  file='ch/sport.m3u8'
  tvgid='ads1' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=abudhabi_sports1" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def ads2():
  file='ch/sport.m3u8'
  tvgid='ads2' #nome canale
  stream="https://www.elahmad.com/tv/mobiletv/glarb.php?id=abudhabi_sports2" #link pagina da cui estrarre 
  link_m3u8=""
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])



def cinema():
  file='ch/rotana.m3u8'
  tvgid='cinema' #nome canale
  stream="https://www.elahmad.com/tv/watchtv.php?id=rotana_cinema" #link pagina da cui estrarre 
  link_m3u8="https://daiconnect.com/live/hls/rotana/cinema-ksa/088fc425900dc92b37981c5043d969dd/.m3u8?requestuid=c70abcb5-64bb-4596-9d36-9f8c25032fe4"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def rhd():
  file='ch/rotana.m3u8'
  tvgid='hd+' #nome canale
  stream="https://www.elahmad.com/tv/live/live_stream.php?id=rotana_hd_plus" #link pagina da cui estrarre 
  link_m3u8="https://playback2.akamaized.net/streams/29325975_9091635_lsik6fsyv9ueokqwpim_1/exp=1702415992~acl=%2f*~data=hdntl~hmac=ea922cd42c8a4b94364571a25442a7ee3b3ae9d8bdb71133f7059a54600ff5ca/media/29325975_9091635_lsik6fsyv9ueokqwpim_1@5256000p.m3u8?dw=80&ts=1702328400"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])

def comedy():
  file='ch/rotana.m3u8'
  tvgid='comedy' #nome canale
  stream="https://www.elahmad.com/tv/watchtv.php?id=rotana_comedy" #link pagina da cui estrarre 
  link_m3u8="https://rotanastudios-rotanacomedy-1-eu.xiaomi.wurl.tv/8b19722f7772362323148961d5a4c446.m3u8"
  subprocess.run(["./ch_call.sh", file, tvgid, link_m3u8, stream, i])


#main
global i
i = sys.argv[1]

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
dai3a()
dai3a2()
chirba()
alab()
adel_karam()
film_arab()
film_arab2()
film_arab3()
comedy_arab()

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
dubai_one()

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
rhd()
comedy()