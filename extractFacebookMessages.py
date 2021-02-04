#!/usr/bin/env python3
import json
import sys

for i in sys.argv[1:]:
		with open(i) as f:
				j=json.load(f)
				for m in j["messages"]:
						if "content" in m:
								try:
										print(m["content"])
								except:
										pass

