# Postfix ip block

Dynamically build your `reject_client` list based on ip blocks of well known assholes. 

## Add new ip block

Simply add the first three octets of the ip addresses that are giving you guff to the `ip_blocks` list in block.py

```python
ip_blocks = [
    '185.45.193.',
    '109.206.177.',
    '62.113.250.'
]
```

## Set the reject_client path

Based on your os, your `reject_client` file might be someplace special. For centos, the path is `/etc/postfix/reject_client`.

Just set your path as the first argument. 

```
python block.py <path/to/reject_client>
```

## All setup?

```
chmod a+x block.py
python block.py /etc/postfix/reject_client
```


