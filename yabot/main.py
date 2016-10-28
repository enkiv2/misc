#!/usr/bin/env python

import markov
import ircbot

import time, sys, os

from random import Random
random=Random()

TAG_FREQUENCY=20

class YaBot(ircbot.SingleServerIRCBot):
	def __init__(self, server_list, nickname, realname, owners, channels, password=""):
		SingleServerIRCBot.__init__(self, server_list, nickname, realname)
		self.owners=owners
		self.channels=channels
		self.password=password
		self.logfilename="yabot.log"
		self.logfile=open(self.logfilename, "a")
	def on_pubmsg(self, c, e):
		self.processAndReply(c, e)
	def on_privmsg(self, c, e):	
		self.processAndReply(c, e, True)
	def logAndPrint(self, line):
		print(line)
		self.logfile.write(line+"\n")
		if(random.choice(range(0, 200))==0):
			self.autosave()
	def autosave(self):
		print("Autosaving log...")
		self.logfile.flush()
		print("Autosaving markov...")
		markov.save()
		print("Regenerating line metrics...")
		markov.regenerateLineHandling()
	def processAndReply(self, c, e, privmsg=False):
		line=e.arguments()[0]
		nick=e.source()
		logAndPrint("<-\t"+c+"\t<"+nick+"> "+line)
		if(nick in self.owner and line[0]=="!"):
			self.handleCmd(c, nick, line)
		else:
			resp=markov.handleLine(line)
			if(resp):
				if not privmsg:
					if(random.choice(range(0, TAG_FREQUENCY))==0):
						resp=nick+": "+resp
				self.say(c, resp)
	def handleCmd(self, c, nick, line):
		global TAG_FREQUENCY
		args=line.split()
		if(args[0]=="!quit"):
			self.say(c, "Saving...")
			self.autosave()
			self.logfile.close()
			self.say(c, "Saved!\nByebye!")
			os.exit(0)
		elif (args[0]=="!save"):
			self.say(c, "Saving...")
			markov.save()
			self.say(c, "Saved!")
		elif (args[0]=="!load")
			self.say(c, "Loading...")
			markov.load()
			self.say(c, "Loaded!")
		elif (args[0]=="!regenLines"):
			markov.regenerateLineHandling()
		elif (args[0]=="!replyrate"):
			if(len(args)==1):
				self.say(c, "Reply rate is set to "+str(markov.replyrate))
			else:
				try:
					markov.replyrate=int(args[1])
					self.say(c, "I will now reply at most 1/"+args[1]+" of the time.")
				except:
					self.say(c, "Usage: !replyrate <n>\nValue n must be a positive integer & replies will max out at 1/n")
		elif (args[0]=="!tagfrequency"):
			if(len(args)==1):
				self.say(c, "Tag frequency is set to "+str(TAG_FREQUENCY))
			else:
				try:
					TAG_FREQUENCY=int(args[1])
					self.say(c, "I will now use nicks in replies at most 1/"+args[1]+" of the time.")
				except:
					self.say(c, "Usage: !tagfrequency <n>\nValue n must be a positive integer & replies will max out at 1/n")
		elif (args[0]=="!join"):
			try:
				self.channels.add(args[1])
				self.connection.join(args[1])
			except:
				self.say(c, "Usage: !join #channel")
		elif(args[0]=="!rejoin"):
			self.rejoin()
		elif(args[0]=="!nick"):
			try:
				self.connection.nick(args[1])
			except:
				self.say(c, "Usage: !nick name")
		elif(args[0]=="!say"):
			try:
				self.say(args[1], " ".join(args[2:]))
			except:
				self.say(c, "Usage: !say nick_or_channel message")
	def say(self, c, resp):
		for line in resp.split("\n"):
			time.sleep(1)
			logAndPrint("->\t"+c+"\t<"+self._nickname+"> "+line)
			self.connection.privmsg(c, line)
		
	def rejoin(self):
		for chan in self.channels:
			self.connection.join(chan)
			time.sleep(1)
	def on_welcome(self, c, e):
		if(self.password):
			self.connection.privmsg("nickserv", "identify "+self.password)
			time.sleep(5)
		markov.load()
		self.rejoin()
	def on_nicknameinuse(self, c, e):
		self._nickname="_"+self._nickname
		self.connection.nick(self._nickname)

