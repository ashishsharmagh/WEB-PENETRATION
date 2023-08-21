import socket,sys
import time , queue
import threading

usage = "[+] .\\fast_port_scanner.py [host] [start port] [end port] [thread no.]"
size = len(sys.argv)
print(sys.argv)
if size != 5:
    print(usage)
    sys.exit(0)
target = str(sys.argv[1])
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
threads = int(sys.argv[4])


try:
    target = socket.gethostbyname(target) #Resolver
except:
    print("[-] Host resolution failed!! ")
    exit()

print("Scanning target {}".format(target)) 

def get_banner(port ,s):
    return s.recv(1024).decode()

def port_scan(t_no):
    while not q.empty():
        port = q.get()
        # print("Scanning port {}".format(port))
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #socket.AFINET(Address family , Inet = IPv4) SOCKStream = TCP connection)
            s.settimeout(3)
            conn = s.connect_ex((target, port)) #for successful connection connect_ex returns 0
            if not conn:
                # banner = get_banner(port,s)
                print(("[+] Port {} is open".format(port)))
                # print(banner)
            s.close()
        except:
            pass
        q.task_done()


q = queue.Queue()

start_time = time.time()

for j in range(start_port , end_port + 1):
    q.put(j)

for i in range(threads):
    t = threading.Thread(target = port_scan , args=(i,))
    t.start()

q.join()

end_time = time.time()

print(f"Port scanned in ",(end_time - start_time))