from os import path
from sys import argv
import xml.etree.ElementTree as etree

if len(argv) != 3:
    print("usage:")
    print(" ./" + argv[0] + " <in_xml> <out_txt>")
    print("example:")
    print(" ./" + argv[0] + " mynet.xml netlist.txt")
    exit()

if not path.exists(str(argv[1])):
    print("The XML file doesnt exist!")
    exit()

if path.exists(str(argv[2])):
    print("Output file already exists!")
    exit()
    
with open(str(argv[2]), 'w') as txt:
    hosts = etree.parse(str(argv[1])).getroot().findall('host')
    for host in hosts:
        if host.findall('status')[0].attrib['state'] == 'up':
            ip_address = host.findall('address')[0].attrib['addr']
            ports = host.findall('ports')[0].findall('port')
            for port in ports:
                if port.findall('state')[0].attrib['state'] == 'open':
                    txt.write(ip_address + ':' + port.attrib['portid'] + '\n')
    
    txt.flush()

print("Done!")
