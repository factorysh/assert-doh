#!/bin/env python3

import os
from base64 import b64encode

import httpx
from dns import message, rdatatype

class Resolver:
    def __init__(self, server, client=None):
        self.server = server
        if client is None:
            client = httpx.Client(http2=True)
        self.client = client

    def query(self, queryname, rdtype=rdatatype.ANY, method="POST"):
        q = message.make_query(queryname, rdtype)
        assert method in ['GET', 'POST'], "bad method : %s" % method
        if method == "POST":
            response = self.client.post(
                self.server,
                headers={
                    "Accept": "application/dns-message",
                    "Content-Type": "application/dns-message",
                },
                content=q.to_wire(),
            )
        else:
            response = self.client.get(
                "%s?dns=%s" % (self.server, b64encode(q.to_wire()).decode('ASCII')),
                headers={
                    "Accept": "application/dns-message",
                },
            )

        assert response.status_code == 200
        print(response.headers)
        r = message.from_wire(response.content)
        #print(q.id, r.id)
        return r


if __name__ == "__main__":
    endpoint = os.getenv("RESOLVER", "https://cloudflare-dns.com/dns-query")
    r = Resolver(endpoint)
    print(r.query("bearstech.com", "TXT").answer)
