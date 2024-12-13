# Stupid Store and Forward (SSF)

## Introduction

I'm the kind of person who learns best from doing. When I don't fully understand something, I do it myself, from scratch, my way, and I gain an appreciation for why something was done a certain way.

There's a lot I don't understand about Secure Scuttlebutt (SSB).

There's a lot I *do* understand, too. And within that, there's a lot to like: store and forward systems sort of inherently implement associative blocking (which is a great way of lowering trolls' access to vulnerable individuals: unlike moderation and shared blocklists, both of which concentrate power centrally, a friend-of-a-friend store-and-forward system where you and your friends follow trustworthy people and block untrustworthy ones is simply rarely going to show you posts from untrustworthy people, as a form of social filtering and siloization that arises naturally from the social network itself); they are highly decentralized and resistant to attack or manipulation; signature chains solve a lot of the common problems with gossip protocols; petnames + keypairs are a great way to implement decentralized identity; offline-first networking is an interesting and worthy goal.

There are some problems related to SSB that I understand, or partially understand. One is that the initial implementation did not sort hash keys, meaning that the v6 / nodejs default dictionary key sorting behavior is functionally baked into the protocol, making it difficult to implement a compatible scuttlebutt in other languages (though a few rudimentary implementations exist as proof-of-concepts). This tie to node and javascript comes with other baggage: the node ecosystem moves very quickly and scuttlebutt development moves very slowly, so often third party packages will update in a way that breaks ssb; node makes using electron convenient, and so developers are tempted to bring in all that bloat (and those who do not choose electron are often web developers by mentality, choosing bloated web technologies in their implementations). Other problems are difficult to avoid: store and forward networks that do not have many nodes and that have nodes up intermittently are going to take a very long time to update (a problem that pubs and rooms help to resolve, but that dramatically slows the initial launch experience).

There are other problems that I simply don't understand, though. For instance, every SSB implementation I've used has been prone to crashes and database corruption, on top of having simply enormous databases compared to the size of the content stored. Is this downstream of the use of javascript / node? Is it a problem with how the protocol was defined (ex., storing whole expanded json blobs of transient communications)? Similarly, although sbot/ssb-server exists and is a component of many clients, it remains very difficult to build and run sbot alone and most clients appear to ship with a modified one as a single unified application (or, as in the case of Manyverse, rewrite sbot entirely with something else and present as a unified application with no automation capability). The store and forward nature of ssb means you basically always want a daemon (especially if internet connectivity is intermittent): every node that stays online continuously is directly supporting the ability of the other nodes to be connected intermittently without missing messages; the application model is fine for a client layer but having the server start only when the client does means that you have to constantly have a crash-prone memory-hungry GUI in the background if you want to see new posts (and it is worse on phones, where you must keep the blank manyverse window onscreen, restart it when it crashes, and keep the phone from falling asleep during the perhaps hours it takes for new posts to be fetched and the database to be fixed from the last crashes).

On top of this, actually following technical discussion of SSB (beyond the basics of a signed gossip protocol and store and forward and petnames and such) very quickly goes over my head. It becomes difficult to tell what is a part of the protocol, what is specific to nodejs, what is specific to sbot, and what is some kind of general cryptography concept. I love rabbitholes but I haven't been able to find my way far enough down this one to actually participate meaningfully in these discussions. Participating meaningfully in these discussions appears to be the only way to understand the SSB internals well enough to build a compatible client, and building a compatible client appears to be the only way to gain enough understanding to participate meaningfully in these discussions.

Being a jerk, I will instead build an incompatible client.

In my grand tradition of self-deprecating names for toy projects, Stupid Store and Forward (SSF) will be my uninformed outsider's understanding of how to make something a little bit like SSB. In the grand tradition of gossip protocols having gossip-related names, I'll call my example client banter.

## Technical considerations

For ease of study, and because I'm lazy (and because I may want to later integrate this into one of my Xanadu-related projects), I will write banter in python. Python has easy to use libraries for many things I'd like to use, although I don't plan to do anything that wouldn't be easy to port.

Where SSB uses JSON, I would like to use MessagePack. JSON has a number of downsides: being text-based, it's not particularly well-compressed (which bloats both storage and the network); it's technically ambiguous in several ways that lead to incompatible edge cases between parsers; it's not really stream-compatible (which may or may not become a useful performance characteristic in some implementations). MessagePack represents the same kinds of data structures as JSON but it does so in a packed binary format that's easily streamed for both reading and writing. We'll make sure to sort the keys in a consistent and easy to define way, and then, when we encode the message with MessagePack, we'll have a nice dense little nugget that can be quickly hashed and signed and thrown over the network or written to a journal. One thing that's nice about MessagePack is that, if you know hex, it's as readable as JSON in a hex editor, so human readability isn't actually sacrificed. MessagePack has great python support, but is also available for many other languages and is straightforward to implement yourself.

SSB supports large text fields and then has some kind of secondary, incompatible protocol for binary blobs. I frequently run up against the limits of these text fields, and I do not understand the blob protocol (which I only know about because I see developers complain about it). The natural thing to do is develop a single unified protocol. Being lazy, I will use IPFS instead. IPFS is a content-addressable network data store. Its developers are pushing some kind of crypto thing now, but that doesn't appear to be any kind of actual threat to the existing software or network. Give IPFS an arbitrary blob and IPFS will give you a hash; request that hash on any machine and you should, eventually, recieve the original blob. IPFS also caches the things you request and serves them, and you can pin things into the cache to keep them around longer. Let's use IPFS to store all blobs (including multiline text), and on top of that, let's use it to store permanent messages (basically, anything that would show up on your timeline: if you post something, follow or unfollow somebody, or apply or remove a petname).

I don't know how SSB does host discovery. Not well, to be honest. Can I do better? Probably not, but this will be a learning experience. Here's my thinking: we'll adopt SSB's use of public keys as unique peer identifiers, and keep an internal database of associated hostnames / IPs. Every time a peer contacts us from an IP we haven't seen before, we add it to the list (which we can trust because we sign messages). Peers can ask us for the last known addresses of a peer. So far, this is pretty standard; we can expand this with new features (for instance, if three nodes are mutual followers with one another, and one of them changes IP, the first one to notice might inform the other), or with systems like pubs and rooms (which I'd actually like to bring over conceptually from SSB; here, a pub would be an always-online peer with a fixed address, and a room would be an always-online peer with a fixed address that only propagates host discovery messages).

I'd like to keep a petname system, maybe as a general feature for describing things about accounts. A message from an arbitrary account makes a claim about a property pertaining to some other account (a name, a description, an avatar image) and clients will be expected to prioritize self-identification & show various identifiers from trusted peers.

## Communicating with the daemon

Let's say the daemon, banterd, is listening for local traffic on some port. Maybe it'll accept json, internally, or maybe we will switch to messagepack. Anyhow, it'll accept simplified versions of certain kinds of messages (such as post, identify, follow, unfollow, and shun) as well as commands that would not be propagated to peers (like block, shutdown, or connect/disconnect peer). It is also listening globally, on some other port, for messages from peers. Messages between peers are in messagepack, and are structured like this:

```
[
	// First, the message body
	{
		"origin": "7a8f4c52d955dbb38d773de5899321d5", // the public key of the originator of this message
		"type": "post", // message type
		"date": "1734111150", // seconds since the epoch UTC
		"body": {
			"address": "e2bca145227de7bd184bbc69dfcc7ead", // IPFS address of payload
			"content": "Hello world", // or, content in any format supported by messagepack
			"mime": "text/plain" // mime type of payload
		},
		"prev": "6d0367ca0ec817120a202e9444f04cec" // the IPFS address of the originator's previous message
	},
	"910c8bc73110b0cd1bc5d2bcae782511" // message hash signed with the private key of the message originator
]
```

That structure is also stored locally on the client (or reconstructed losslessly) and stored in IPFS.

When sending a message to the local port, only the "type" and "body" portions of the first component of this structure should be sent; the rest will be filled in by the daemon before storing and forwarding it. Upon successfully constructing and storing this message, the client will be given back its IPFS address.

When the daemon recieves a message like this from a peer, it first hashes the first portion and checks that the signature matches. If the signature does not match, the message is discarded as fraudulent. If the message is valid, it is added to IPFS, and if it is not a peer discovery related message, the daemon pins it and adds its information to its internal database of post information. Peer discovery related messages have their own behavior, described later.

## Peer discovery messages

Peer discovery messages come in two classes: direct and hearsay. Direct peer discovery messages are about the peer they come from, and involve handshakes. Hearsay messages are about peers of peers.

An example of direct peer discovery is the `hello` message. This is a message with no content, with the type `hello`. A host, upon receiving a valid `hello` message, will reply with a `hello-reply` message (whose content is the original, signed `hello` message), and a host that receives such a reply will update their database of peer information. That database will look something like this:

||peer identifier (public key)||IP address||date seen||direct or hearsay||

We keep only the most recent example of each IP address, and have some configurable upper limit on how many IPs to store in total and for each peer. For peers that we follow, we keep this information indefinitely.

An example of hearsay peer discovery is the `list-peers` message:

```
{ 
	// fill in origin, date, prev, mime
	"type": "list-peers",
	"body": {
		// if content is empty, list all peers; if it is a structure, filter it by any applied options:
		"content": {
			"peers": [peer1, peer2...], // show only these peers
			"since": n, // show only IPs active in the last n seconds
			"max-peers": n, // show at most n peers
			"max-ips": n, // show at most n IPs for each host
			"direct-only": boolean // return only direct entries?
		}
	}
}
```

The host will reply with its own `seen-peers` message:

```
{
	// fill in origin, date, prev, mime
	"type": "seen-peers",
	"body": {
		"content": [
			{"peer": pubkey 1, "ip": ip address, "seen": date seen, "direct": boolean},
			...
		]
	}
}
```

Upon recieving a `seen-peers` message, the daemon will check this against the database, and add 'hearsay' entries whenever they are newer than (or conflict with) direct entries.

Periodically, `hello` and `list-peers` messages will be sent to any hosts our daemon is following. Additionally, the daemon will attempt to shake hands with any host whose most recent peer entry is hearsay before sending any "push"-type messages to it (including seen-peers). A pub or room will periodically send `seen-peers` messages to all peers, as well.

While it's not exactly about discovering peers, the `list-messages` message also is not permanently stored. It behaves similarly to `list-peers`:

```
{ 
	// fill in origin, date, prev, mime
	"type": "list-messages",
	"body": {
		// if content is empty, list all peers; if it is a structure, filter it by any applied options:
		"content": {
			"from": [peer1, peer2...], // show only messages from these peers
			"since": n, // show only posts from the last n seconds (0 for the maximum the peer will return)
			"max-messages": n, // show at most n messages (0 for the maximum the peer will return)
			"ttl": n // if n>0, fetch recursively from peers, decreasing n by one
		}
	}
}
```

The host will reply with its own `seen-messages` message:

```
{
	// fill in origin, date, prev, mime
	"type": "seen-messages",
	"body": {
		"content": [
			{"peer": pubkey, "message": IPFS address, "seen": date seen},
			...
		]
	}
}
```

These messages can then be added to the queue to be fetched from IPFS, processed, and stored.

## Normalization

Messages, before they are stored or hashed, need to be normalized. We will determine whether to use `content` or `address` based on content length, set the value of any unused buckets (ex., `prev`, `content`, `address`, or `mime`) explicitly to null, and sort the keys lexicographically.

## Storage

You may have noticed that most messages are stored in IPFS *and* sent over the network. If we receive a reference to a message by a peer who isn't currently present, we can get it off IPFS, most of the time. Peer discovery messages should never be pinned, with the exception of hello messages, which should be pinned for the duration of the handshake. Other kinds of messages should generally be pinned for a while if they come from friends & forever if they are local. Pubs pin every message they recieve and rooms pin none.

We also will use a database. I've described how peer information is stored there. It will also contain information about which peers the daemon is following, which peers it has blocked, which peers it is aware are following it, and which peers its followers have declared shunned, as well as the hashes of the messages the daemon has already processed and some meta-information about them (like the origin and date).

## Queues and periodic behaviors

We have several different kinds of periodic behaviors. For instance, we want to periodically check for new peers, inaccessible peers, and new messages. We also want to check for missed messages, but in a way that is gradual enough not to spam the network. On top of that, we also would like to be able to retry push-type operations that have failed, possibly after very long periods.

The natural way to handle this is to have a number of queues for different types of operations, along with code that runs periodically to check whether it is appropriate to reorder the queue or process the object on its top.

I think we ought to have a queue of peers we haven't heard from in a while, to handle handshakes and similar peer discovery stuff. We probably ought to have it sorted by a function of how long it's been since we've gotten a message from them: too recent and we eliminate them entirely, then up to a certain point, the longer it's been the more we will want to catch up, until we get to the point where they're probably permanently inaccessible, at which point we want to check in rarely. So, perhaps, something along the lines of:

```
	(time - 1 hour)%(1 day) + ((time - 1 hour)%(3 weeks) / 1000)
```

We should have a similar queue for messages we are trying to send (for instance, to inform our followers of a new post), and messages we are trying to fetch. When we have not yet processed the message referenced in the "prev" section of a message, we should not start fetching and processing it immediately in a blocking fashion, but add it to the end of a message-fetch queue.

## Networking

As much as I complain about webtech, I see no particular problem exposing the daemon's two listeners as HTTP servers that accept POST requests. This is well-supported by python and most other stacks, and allows us to transparently gzip requests and responses.

It would be very cool to also support bluetooth or mesh networking, like many SSB implementations try to do, but I don't have much motivation to work out how that would function.

## Security and correctness

A client should reject any message that fails signature checking. A client should reject any message dated later than its 'prev' message, although this does not need to be done immediately -- such messages, when identified, should be quarantined. Similarly, if a fork in a peer's gossip log is discovered, it is up to the daemon to directly determine canonical order from the peer and quarantine messages from the alternate fork. Quarantined messages should be processed but not stored or passed to peers, and anything after a quarantined message is also quarantined.

## Block vs shun

Block is a purely internal operation: no message is sent to peers. Instead, all messages originating from that user will be ignored by the daemon.

Shunning, on the other hand, is a network operation: the `shun` message indicates to peers that they should not tell you anything about some user, and that said user should not be told anything about you. Shun takes as its content the public key of the user you wish to shun.

## Private messages

There are no private messages. Secure private communication would require such a dramatically different protocol that there's no point having public and private communication in the same application.


