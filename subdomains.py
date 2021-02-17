print("░██████╗██╗░░░██╗██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░██╗███╗░░██╗░██████╗")
print("██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██║████╗░██║██╔════╝")
print("╚█████╗░██║░░░██║██████╦╝██║░░██║██║░░██║██╔████╔██║███████║██║██╔██╗██║╚█████╗░")
print("░╚═══██╗██║░░░██║██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║██╔══██║██║██║╚████║░╚═══██╗")
print("██████╔╝╚██████╔╝██████╦╝██████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║██║░╚███║██████╔╝")
print("╚═════╝░░╚═════╝░╚═════╝░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚═════╝░")
import censys.certificates
import socket

print("[SYNTAX]: google.com")
searchDomain = input("[DOMAIN NAME]: ")
updomains = {}
downdomains = {}

UID = "d287690c-99ce-4101-8283-30b7bb6b2d02"
SECRET = "UiQz2prqsn2FNymZiTpdN9XtwVuI0VAL"

certificates = censys.certificates.CensysCertificates(UID, SECRET)
fields = ["parsed.names"]

for c in certificates.search(searchDomain, fields=fields, max_records=1000):
    domain = c["parsed.names"][0].replace("*.","").replace("www.","")
    if not updomains.get(domain) and not downdomains.get(domain) and (("."+searchDomain in domain) or searchDomain == domain):
        try:
            ip = socket.gethostbyname(domain)
            updomains[domain] = ip
        except:
            downdomains[domain] = True

if updomains:
    print("--------------------------")
    print("-=-=-=- DOMAINS UP -=-=-=-")
    print("--------------------------")
    for name in updomains.items():
        print('DOMAIN: {}, IP: {}'.format(name[0],name[1]))

if downdomains:
    print("--------------------------")
    print("=-=-=- DOMAINS DOWN -=-=-=")
    print("--------------------------")
    for name in downdomains.items():
        print('DOMAIN: {}'.format(name[0]))
