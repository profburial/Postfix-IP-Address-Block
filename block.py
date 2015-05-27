#!/usr/bin/env python
""" Build reject_clients list from ip blocks """

import os
import sys

# Add ip blocks
ip_blocks = [
    '185.45.193.',
    '109.206.177.',
    '62.113.250.',
    '144.76.132.',
    '108.163.214.',
    '144.76.249.',
    '109.201.148.',
    '5.178.71.',
    '109.201.148',
    '109.206.177.',
    '62.113.250',
    '109.206.177.',
    '69.39.238.',
    '93.190.95.',
    '69.39.238.',
    '50.2.185',
    '79.142.6',
    '79.142.65',
    '146.185.253.',
    '77.93.204.',
    '217.23.14',
    '109.201.148',
    '217.23.12.',
    '206.190.137.',
    '192.157.213.',
    '148.251.72.',
    '109.201.135.',
    '107.150.31.',
    '172.245.43.',
    '198.23.159.',
    '178.33.19.',
    '107.181.166.'
]

# Build ips to REJECT
ips = []
for ip in ip_blocks:
    for x in range(1, 256):
        ips.append(ip + str(x))

reject = " REJECT \n".join(ips) + " REJECT"

# Create new reject_clients
os.system('touch ' + sys.argv[1])
reject_list = open(sys.argv[1], 'w+')
reject_list.write(reject)

# Restart postfix
os.system('sudo service postfix restart')

print 'Done!'
