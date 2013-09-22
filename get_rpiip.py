import requests

IP_TXT = 'https://raw.github.com/cyriac/rpiip/gh-pages/ip.json'

if __name__ == '__main__':
    r = requests.get(IP_TXT)
    ip = r.json()
    print "IP : %s" % (ip['ip'])
    print "Last Updated : %s" % (ip['timestamp'])
