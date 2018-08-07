#!/usr/bin/env python

history={}

class OSMICDiff:
	def __init__(self, insert=True, offset=0, text="", diffID=[0]):
		self.insert=insert
		self.offset=offset
		self.text=text
		self.diffID=diffID
		history[self.address()]=self
	def address(self, addr=None):
		if addr==None:
			addr=self.diffID
		return ".".join(map(str, addr))
	def nextAddress(self, addr=None):
		if addr==None:
			addr=self.diffID
		if(len(addr)==1):
			return [addr[0]+1]
		return addr[:-1]+[addr[-1]+1]
	def forkAddress(self, addr=None):
		if(addr==None):
			addr=self.diffID
		return addr+[0]
	def repr(self):
		return self.address()
	def str(self):
		mode='d'
		if(self.insert):
			mode='i'
		return self.address()+mode+str(self.offset)+":"+str(len(self.text))+self.text
	def invert(self):
		return OSMICDiff(not self.insert, self.text, self.offset, self.diffID)
	def fork(self, insert, offset, text):
		fa=self.forkAddress()
		while (self.addr(fa) in history):
			fa=self.forkAddress(fa)
		return OSMICDiff(insert, offset, text, fa)
	def commit(self, insert, offset, text):
		na=nextAddress()
		if(self.addr(na) in history):
			return self.fork(insert, offset, text)
		return OSMICDiff(insert, offset, text, na)
	def apply(self, text):
		if(abs(self.offset)>len(text)):
			raise Exception("Index out of bounds")
		if(self.insert):
			return text[0:self.offset]+self.text+text[self.offset:]
		else:
			if text[self.offset:self.offset+len(self.text)]!=self.text:
				raise Exception("Diff-text mismatch")
			return text[0:self.offset]+text[self.offset+len(self.text):]
	def undo(self, text):
		return self.invert().apply(text)
	def fastForward_r(self, text, pfx, addr1, addr2, rewind=False):
		incr=1
		if(rewind):
			incr=-1
		for i in range(addr1, addr2, incr):
			if(rewind):
				text=history[self.address(pfx+[i])].undo(text)
			else:
				text=history[self.address(pfx+[i])].apply(text)
		return text
	def fastForward(self, text, addr1, addr2):
		if(len(addr1)<=len(addr2)):
			pfx=[]
			for i in range(0, len(addr1)):
				if(addr1[i]<addr2[i]):
					text=self.fastForward_r(text, pfx, addr1[i], addr2[i])
					pfx+=[addr2[i]]
				else:
					text=self.fastForward_r(text, pfx, addr1[i], addr2[i], True)
					pfx+=[addr1[i]]
			if(len(addr2)>len(addr1)):
				for i in range(len(addr1), len(addr2)):
					text=self.fastForward_r(text, pfx, 0, addr2[i])
					pfx+=[addr2[i]]
		else:
			text=self.rewind(text, addr1, addr1[:len(addr2)])
			text=self.fastForward(text, addr1[:len(addr2)], addr2)
		return text
	def rewind(self, text, addr1, addr2):
		if(len(addr2)>len(addr1)):
			text=self.fastForward(text, addr1, addr2)
		else:
			pfx=addr1
			if(len(addr1)>len(addr2)):
				while(len(pfx)>len(addr2)):
					tail=pfx[-1]
					pfx=pfx[:-1]
					text=self.fastForward_r(text, pfx, tail, 0, True)
			for i in range(len(pfx), 0, -1):
				if pfx[i]!=addr2[i]:
					tail=pfx[-1]
					pfx=pfx[:-1]
					text=self.fastForward_r(text, pfx, tail, 0, True)
			text=self.fastForward(text, pfx, addr2)
		return text

