import os,requests,time
os.system("clear")
R = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
P = '\u001b[35m'
Y = '\033[1;33m'
W = "\033[0m"

logo=(f"""
  ██████╗ ██████╗ ██╗███╗   ██╗
██╔════╝██╔═══██╗██║████╗  ██║
██║     ██║   ██║██║██╔██╗ ██║
██║     ██║   ██║██║██║╚██╗██║
╚██████╗╚██████╔╝██║██║ ╚████║
 ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝
                              

""")
print(logo)
print('\nBO DASKAWTNE ID : [ https://tools.codeofaninja.com/find-instagram-user-id ]')
userid = input(G+"\nUSER INSTA UP ? : ")
def instaup():
	url=f"http://awl1sh.ir/InstaUp2/index.php?uid={userid}&submit=submit"
	namasteabhi=str(requests.get(url).text)
	if '"status":"Successful"' in namasteabhi:
		print(G+f'[✅]COIN SEND==> {userid} ')
	if 'coins":"' in namasteabhi:
		coin=str(namasteabhi.split('coins":"')[1])
		coins=str(coin.split('"')[0])
		print(G+f'YOUR COIN NOW ==> {coins}')
	if '"coins":null' in namasteabhi:
		print(B+"[🏴‍☠️]ACOUNT INSTA UP HAS BANDED :(")
while True:
	print(Y+"WAIT... :)")
	print (P+'--------------------------------------------------\n')
	time.sleep(10)
	instaup()
	
