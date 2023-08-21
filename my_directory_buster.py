import requests , sys , threading , queue

host = sys.argv[1]
threads = int(sys.argv[2])

try:
    requests.get(host)
except Exception as e:
    print(e)
    exit(0)

dir_list = open('dir_wordlist.txt' , 'r')

q = queue.Queue()


def dir_buster(t_no , q):
    while not q.empty():
        url = q.get()
        try:
            response = requests.get(url , allow_redirects=False)
            if response.status_code == 200:
                print("[+] Directory Found : {}".format(url))
        except:
            pass
        q.task_done()

for dir in dir_list.read().splitlines():
    url = host + '/' + dir
    q.put(url)

for i in range(threads):
    t = threading.Thread(target= dir_buster, args=(i , q))
    t.daemon = True
    t.start()


q.join()