from rpiip import RPIIP
import json
import os

JSON_FILE = "./ip.json"
TXT_FILE = "./ip.txt"

if __name__ == '__main__':
    new_ip = False

    '''Try to open existing file for change'''
    try:
        json_data=open(JSON_FILE)
    except IOError:
        new_ip = True

    try:
        old_ip = json.load(json_data)
    except (ValueError, IOError, NameError):
        '''Handles file not found IOError from open,
        no data from file and corrupt data from file'''
        new_ip = True

    ip = RPIIP()

    if ip.ip and new_ip != True and ip.ip != old_ip['ip']:
        '''Checks for change in IP'''
        new_ip = True

    if new_ip == True:
        with open(JSON_FILE, 'w') as outfile:
            json.dump(ip.elements, outfile)
        with open(TXT_FILE, 'w') as outfile:
            outfile.write(ip.ip)
        cmd = "git commit -a -m 'IP changed at %s'" % (ip.timestamp)
        os.system(cmd)
        os.system('git push')

