

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# ███╗   ███╗███╗   ███╗██████╗ ██████╗ ███████╗ █████╗     ██████╗ ██████╗ ███╗   ███╗
# ████╗ ████║████╗ ████║██╔══██╗██╔══██╗╚══███╔╝██╔══██╗   ██╔════╝██╔═══██╗████╗ ████║
# ██╔████╔██║██╔████╔██║██║  ██║██████╔╝  ███╔╝ ███████║   ██║     ██║   ██║██╔████╔██║
# ██║╚██╔╝██║██║╚██╔╝██║██║  ██║██╔══██╗ ███╔╝  ██╔══██║   ██║     ██║   ██║██║╚██╔╝██║
# ██║ ╚═╝ ██║██║ ╚═╝ ██║██████╔╝██║  ██║███████╗██║  ██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║
# ╚═╝     ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# pip install colorama lxml
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import time
from colorama import Fore,Style
import requests
from lxml import html


count = 1
while True:
    urlblock = 'https://www.blockchain.com/btc/unconfirmed-transactions'
    respone_block = requests.get(urlblock)
    byte_string_block = respone_block.content
    source_code_block = html.fromstring(byte_string_block)
    xpatchblock_txid = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]'
    xpatchblock_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[3]/div[2]/span'
    xpatchblock_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[2]/div[4]/div[2]/span'
    xpatchblock3_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[1]/div[2]'
    xpatchblock3_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[3]/div[2]/span'
    xpatchblock3_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[4]/div[4]/div[2]/span'
    xpatchblock4_hex = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[1]/div[2]'
    xpatchblock4_btc = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[3]/div[2]'
    xpatchblock4_usd = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div/div[5]/div[4]/div[2]'
    blocktreetxid = source_code_block.xpath(xpatchblock_txid)
    blocktree_btc = source_code_block.xpath(xpatchblock_btc)
    blocktree_usd = source_code_block.xpath(xpatchblock_usd)
    blocktree3_hex = source_code_block.xpath(xpatchblock3_hex)
    blocktree4_hex = source_code_block.xpath(xpatchblock4_hex)
    blocktree3_btc = source_code_block.xpath(xpatchblock3_btc)
    blocktree4_btc = source_code_block.xpath(xpatchblock4_btc)
    blocktree3_usd = source_code_block.xpath(xpatchblock3_usd)
    blocktree4_usd = source_code_block.xpath(xpatchblock4_usd)
    block3btc = str(blocktree3_btc[0].text_content())
    block4hex = str(blocktree4_hex[0].text_content())
    block4btc = str(blocktree4_btc[0].text_content())
    block3usd = str(blocktree3_usd[0].text_content())
    block4usd = str(blocktree4_usd[0].text_content())
    block3hex = str(blocktree3_hex[0].text_content())
    blocktxid = str(blocktreetxid[0].text_content())
    blockbtc = str(blocktree_btc[0].text_content())
    blockusd = str(blocktree_usd[0].text_content())
    chblock1btc = str(blockbtc)[0]
    chblock2btc = str(block3btc)[0]
    chblock3btc = str(block4btc)[0]
    print(str(count),Fore.YELLOW,'TX:',Fore.WHITE ,str(blocktxid),Fore.YELLOW,'Amount:',Fore.GREEN, str(blockbtc), Fore.YELLOW,'Total:',Fore.MAGENTA,str(blockusd),Style.RESET_ALL)
    print(str(count),Fore.YELLOW,'TX:',Fore.WHITE ,str(block3hex),Fore.YELLOW,'Amount:',Fore.GREEN, str(block3btc), Fore.YELLOW,'Total:',Fore.MAGENTA,str(block3usd),Style.RESET_ALL)
    print(str(count),Fore.YELLOW,'TX:',Fore.WHITE ,str(block4hex),Fore.YELLOW,'Amount:',Fore.GREEN, str(block4btc), Fore.YELLOW,'Total:',Fore.MAGENTA,str(block4usd),Style.RESET_ALL)
    count += 3
    time.sleep(1)
    
# ================================================
# DONATE (BTC) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
# Website : Mmdrza.Com
# Email : X4@mmdrza.Com
# Dev.to/Mmdrza
# Github.com/Pymmdrza
# ================================================
