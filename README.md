# **Web-Pentesting**
---
## Package Downloading Requirements
### To install the required packages, follow these steps:

- Clone this repository to your local machine

- Navigate to the project's directory using the command line.
```python
cd Web-Pentesting
```

- Run the following command to install the dependencies:

```python
pip install -r requirements.txt
```

---

## Info Gathering
- To gather info about a domain or ip, run the following command 
```python
python .\info_gather.py -d <targeted domain> -s <targeted ip>
```
---

## Port Scanning

- To perform port scan, run the following command
```python
python .\fast_port_scanner.py <target>  <start_port> <end port> <threads>
```
---

## Subdomain Finder
- To find subdomains, run the following command
```python
python .\subdomain_finder.py <target> <threads>
```
---
## Directory Buster
- To Bust directory, run the following command
```python
python .\my_directory_buster.py <target> <threads> 
```
---
## FTP or SSH Bruteforcing
- To bruteforce FTP or SSH service run the following command
```python
python .\ftp_ssh_Brute_forcer.py <hostname> <username> <type(ftp or ssh)>
```

---
