#!/bin/env python3

import httpx
from dns import message, rdatatype


class Resolver:
    def __init__(self, server, client=None):
        self.server = server
        if client is None:
            client = httpx.Client(http2=True)
        self.client = client

    def query(self, queryname, rdtype=rdatatype.ANY):
        q = message.make_query(queryname, rdtype)
        response = self.client.post(self.server,
                             headers={
                                 "Accept": "application/dns-message",
                                 "Content-Type": "application/dns-message"
                             },
                         content=q.to_wire())
        assert response.status_code == 200
        print(response.headers)
        return message.from_wire(response.content)


if __name__ == '__main__':
    r = Resolver('https://cloudflare-dns.com/dns-query')
    print(r.query('bearstech.com', 'TXT'))
