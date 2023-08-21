import whois
import dns.resolver
import shodan
import requests
import sys
import argparse
argparse = argparse.ArgumentParser(description="It is a info gathering tool" , usage="Python3 info_gather.py -d domain [-s IP]")
argparse.add_argument("-d" , "--domain" , help="Enter domain for footprinting")
argparse.add_argument("-s" , "--shodan" , help="Enter ip for shodan search")

args = argparse.parse_args()
domain = args.domain
ip = args.shodan

print("[+] Domain {} and IP {}".format(domain , ip))

print("Getting whois info.....")

py = whois.whois(domain)

try:
    print("Info gathered")
    print("Name : {}".format(py.name))
    print(f"Registrar : {py.registrar}")
    print("Creation date : {}".format(py.creation_date))
    print("Expiration Date {}".format(py.expiration_date))
    print("Registrant : {}".format(py.registrant))
    print("Country : {}".format(py.registrant_country))
except:
    pass