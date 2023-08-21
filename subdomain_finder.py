import requests , sys , threading , queue

host = sys.argv[1]
threads = int(sys.argv[2])

q = queue.Queue()

def subBruteforcer():
    while not q.empty():
        subdomain = q.get()
        url = f"https://{subdomain}.{host}"
        try:
            response = requests.get(url , allow_redirects=False , timeout= 2)
            if response.status_code == 200:
                print("[+] Subdomain found : {}".format(url))
        except:
            pass
        q.task_done()


with open('Wordlists/subdomains.txt' , 'r') as file:
    subdomains = file.read().splitlines()
    for subdomain in subdomains:
        q.put(subdomain)


for i in range(threads):
    t = threading.Thread(target= subBruteforcer , daemon=True)
    t.start()

q.join()