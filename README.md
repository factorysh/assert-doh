# Assert DNS Over Https

DOH client for [RFC 8484](https://tools.ietf.org/html/rfc8484) with HTTP/2,
GET and POST.

## Install

    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt

## Usage

```python
from doh import Resolver

r = Resolver("https://cloudflare-dns.com/dns-query")
print(r.query("bearstech.com", "TXT").answer)
```


