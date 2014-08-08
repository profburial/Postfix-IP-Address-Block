# Postfix ip block

Dynamically build your `reject_client` list based on ip blocks of well known assholes. 

## Add new ip block

Simply add the first three octets of the ip addresses that are giving you guff to the `ip_blocks` list in block.py

```python
ip_blocks = [
    '185.45.193.',
    '109.206.177.',
    '62.113.250'
]
```

## Change reject_client path

Based on your os, your `reject_client` file might be someplace special. For centos, the path is `/etc/postfix/reject_client`.

Change the path in both block.py and run.sh

## All setup?

```
chmod a+x run.sh
./run.sh
```


