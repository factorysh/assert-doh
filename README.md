# Assert DNS Over Https

## Install

    python3 -m venv venv
    ./venv/bin/pip install -r requirements.txt

## Usage

```python
from doh import Resolver

r = Resolver("https://cloudflare-dns.com/dns-query")
print(r.query("bearstech.com", "TXT").answer)
```


