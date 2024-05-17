#!/usr/bin/env python

import ipfsApi
ipfs = ipfsApi.Client("127.0.0.1", 5801)

def fetch(triples):
  chunks=[]
  for (cid, start, length) in triples:
    chunks.append(fetchSingle(cid, start, length))
  return chunks


# TODO: garbage collection or garbage compaction with pins:
# keep database of when things were pinned, source, and reason
# and periodically unpin (but do not remove) the oldest that were just cached
def fetchSingle(cid, start=0, length=-1, pin: bool = False):
  ret = ipfs.get_pyobj(cid)[start][:length]
  if pin:
    ipfs.pin.add(cid)
  return ret

def store(data: bytes, pin: bool = True):
  cid = ipfs.add_pyobj(data)
  if pin:
    ipfs.pin.add(cid)
  return ret

# TODO: permascroll management
# private/working permascroll is stored locally, append-only
# (let's check its integrity upon startup: ensure the version in ipfs is a prefix of it)
# periodically, we wish to publish the private permascroll:
# we perform a store() of the current version, 
# and update our stored "permascroll address" configuration,
# which is used in place of our permascroll at publication time.
# we may want to support transcopyright / obfuscation with a one-time pad (privately stored)

