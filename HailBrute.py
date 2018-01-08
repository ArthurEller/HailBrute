import requests
import sys
import dns.resolver


print "\033[1;31m" + """
  _    _       _ _ ____             _       
 | |  | |     (_) |  _ \           | |      
 | |__| | __ _ _| | |_) |_ __ _   _| |_ ___ 
 |  __  |/ _` | | |  _ <| '__| | | | __/ _ :
 | |  | | (_| | | | |_) | |  | |_| | ||  __/
 |_|  |_|\__,_|_|_|____/|_|   \__,_|\__\___|
                            HailBrute v1.0
 Twitter: @Thuur1337 / Github: https://github.com/ArthurHMES
 
 """ + "\033[0;0m"
select=int(raw_input("""   Select one Function:
   [1] BruteForce on the site directory ( Works to Find ADM )
   [2] BruteForce on the subdomain of site
   [3] BruteForce on the DNS of site
   Function: """))

if (select == 1) :
    print "\033[1;31m" +"""
    Welcome! 
    """ + "\033[0;0m"
    site = raw_input("Input your target: ")
    wordlist = raw_input("Name of your worldlist? ")
    print + "\033[0;0m"
    arq = open(wordlist)
    listas = arq.read().splitlines()

    for linha in listas:
        url = site + "/" + linha
        req = requests.get (url)
    codigo = req.status_code

    if codigo == 200:
        print url + " PAGE FOUND! " + str(codigo)
    else:
        print url + " NOT FOUND! " + str(codigo)


elif (select == 2) :
    print "\033[1;31m" +"""
    Welcome! 
    """ + "\033[0;0m"
    site = raw_input("Input your target: ")
    wordlist = raw_input("Name of your worldlist? ")

    arq = open(wordlist)
    listas = arq.read().splitlines()

    for linha in listas:
        url = "http://" + linha + "." + site
        req = requests.get(url)
    codigo = req.status_code

    if codigo == 200:
        print url + " PAGE FOUND! " + str(codigo)
    else:
        print url + " NOT FOUND! " + str(codigo)

elif (select == 3)  :
    print "\033[1;31m" +"""
    Welcome! 
    """ + "\033[0;0m"
    dominio = raw_input("Input your target: ")
    nome_arquivo = raw_input("Name of your worldlist? ")
    arq = open(nome_arquivo)
    listas = arq.read().splitlines()

    for lista in listas:

        subdom = lista + "." + dominio
        try:
            resultados = dns.resolver.query(subdom, "a")
            for resultado in resultados:
                    print subdom, resultado
        except:
            pass








