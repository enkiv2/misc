#!/usr/bin/env python

import markov
import ircbot

import time, sys, os

from random import Random
random=Random()

TAG_FREQUENCY=20

class YaBot(ircbot.SingleServerIRCBot):
	def __init__(self, server_list, nickname, realname, owners, channels, password=""):
		ircbot.SingleServerIRCBot.__init__(self, server_list, nickname, realname)
		self.owners=owners
		self.channelList=channels
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
		source=e.source()
		nick=source.split("!")[0]
		chan=e.target()
		if(chan[0]!="#"):
			chan=nick	# privmsg
		self.logAndPrint("<-\t"+chan+"\t<"+nick+"> "+line)
		if(nick in self.owners and line[0]=="!"):
			self.handleCmd(chan, nick, line)
		else:
			resp=""
			procLine=line
			try:
				if(line.find(self._nickname)==0 and len(line.split())>1):
					procLine=" ".join(line.split()[1:])
				markov.processLine(chan, procLine)
				if(markov.replyrate and random.choice(range(0, markov.replyrate))==0):
					resp=markov.respondLine(procLine)
				if(not resp):
					if(line.find(self._nickname)>=0 or privmsg):
						resp=markov.respondLine(procLine)
			except:
				print("Error in handleLine")
				print(sys.exc_info())
			if(resp and resp!=procLine):
				if not privmsg:
					if(random.choice(range(0, TAG_FREQUENCY))==0):
						resp=nick+": "+resp
				self.say(chan, resp)
	def handleCmd(self, c, nick, line):
		global TAG_FREQUENCY
		if(c[0]!="#"):
			c=nick
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
		elif (args[0]=="!load"):
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
		elif (args[0]=="!part"):
			try:
				if(args[1] in self.channelList):
					self.channelList.remove(args[1])
					self.connection.part(args[1])
			except:
				self.say(c, "Usage: !part #channel")
		elif (args[0]=="!join"):
			try:
				self.channelList.append(args[1])
				self.connection.join(args[1])
			except:
				self.say(c, "Usage: !join #channel")
		elif (args[0]=="!rmowner"):
			try:
				if(args[1] in self.owners):
					self.owners.remove(args[1])
					self.say(c, "Owner "+args[1]+" removed.")
				else:
					self.say(c, "User "+args[1]+" is not an owner.")
			except:
				self.say(c, "Usage: !rmowner nick")
		elif (args[0]=="!addowner"):
			try:
				self.owners.append(args[1])
				self.say(c, "User "+args[1]+" added to owners list.")
			except:
				self.say(c, "Usage: !addowner")
		elif(args[0]=="!rejoin"):
			self.rejoin()
		elif(args[0]=="!nick"):
			try:
				self.connection.nick(args[1])
			except:
				self.say(c, "Usage: !nick name")
		elif(args[0]=="!saveconfig"):
			self.say(c, "Saving config...")
			f=open("config.py", "a")
			f.write("owners=[\""+("\",\"".join(self.owners))+"\"]\n")
			f.write("channels=[\""+("\",\"".join(self.channelList))+"\"]\n")
			f.write("nick=\""+self._nickname+"\"\n")
			f.flush()
			f.close()
			self.say(c, "Config saved!")
		elif(args[0]=="!say"):
			try:
				self.say(args[1], " ".join(args[2:]))
			except:
				self.say(c, "Usage: !say nick_or_channel message")
		elif(args[0]=="!help"):
			if(len(args)>1):
				if(args[1] in ["quit", "save", "load", "regenLines", "saveconfig"]):
					self.say(c, args[1]+" does not take args")
				else:
					self.say(c, "Please run !"+args[1]+" without any args to see usage information")
			else:
				self.say(c, "Available commands are: quit, save, load, regenLines, replyrate, tagfrequency, join, part, rejoin, nick, say, addowner, rmowner, saveconfig, and help")
	def say(self, c, resp):
		for line in resp.split("\n"):
			time.sleep(1)
			self.logAndPrint("->\t"+c+"\t<"+self._nickname+"> "+line)
			self.connection.privmsg(c, line)
		
	def rejoin(self):
		self.logAndPrint("-- Joining channels: "+(" ".join(self.channelList)))
		for chan in self.channelList:
			self.connection.join(chan)
			time.sleep(1)
	def on_welcome(self, c, e):
		self.logAndPrint("-- Connecting")
		if(self.password):
			self.logAndPrint("-- Identifying")
			self.connection.privmsg("nickserv", "identify "+self.password)
			time.sleep(5)
		markov.load()
		self.rejoin()
	def on_nicknameinuse(self, c, e):
		self._nickname="_"+self._nickname
		self.connection.nick(self._nickname)

try:
	from config import servers, nick, realname, owners, channels, password
except:
	f=open("config.py", "w")
	f.write("""# AUTOGENERATED BY YABOT
servers=[("irc.freenode.com", 6667)]
nick="YeahBot"
realname="Mark V. Shaney"
owners=["enkiv2", "enki-2", "ENKI-]["]
channels=["##politics"]
password=""
""")
	f.close()

def main():
	bot=YaBot(servers, nick, realname, owners, channels, password)
	bot.start()
if __name__=="__main__":
	main()

