#!/usr/bin/env python
import json
import urllib

import sys

searx_url=sys.argv[1]
search_terms=sys.argv[2:]

for item in json.load(urllib.urlopen(searx_url+"?q="+("+".join(search_terms))+"&format=json"))["results"]:
        print(item["url"])


