# python-freeipa-json
Tiny/basic module for communicating with the FreeIPA API without having to install their entire toolchain
## Info
This module tries to use a minimal set of dependencies to communicate with FreeIPA through it's json rpc instead of using the official FreeIPA toolchain which is quite dependency heavy. Not all functions are available yet since they're not very well documented.
## Installation
Copy the file to your site-packages directory (I.E /usr/lib/python3.4/site-packages/) or any other python library path
## Dependencies
- requests
- json

## Example usage
```python
ipa = ipahttp.ipa('ipa.example.com')
ipa.login('apiuser', 'secret_password')
reply = ipa.host_find()
for host in reply['result']['result']:
    root.info('Found host %s' % host['fqdn'][0])
```

## License

MIT © [Nordnet Bank AB](https://www.nordnet.se/)
