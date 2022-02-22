#!/usr/bin/env python3
import sys, os
import re
try:
		import cPickle as pickle
except:
		print("Could not find cpickle; falling back to pickle")
		import pickle

stopwords=[]
try:
		import pycorpora
		stopwords=pycorpora.words.stopwords.en["stopWords"]
except:
		print("""Could not find stopwords, so will not filter them. Do you have pycorpora installed? Try:\n\tpip3 install pycorpora --install-option="--corpora-zip-url=https://github.com/dariusk/corpora/archive/master.zip"\n""")


global db, db_ctime
global tf, wc
global silent

db={}
db_ctime=0
tf={}
wc=0
silent=False

max_kw=100

def dprint(s, flush=True, lnl=False, tnl=False):
		if not silent:
				if(lnl):
						sys.stdout.write("\n")
				sys.stdout.write(s)
				if(tnl):
						sys.stdout.write("\n")
				if(flush):
						sys.stdout.flush()
def progress():
		dprint(".")

def ingest(fname):	
		global db
		scontent=[]
		with open(fname, "r") as sf:
				ctime=float(os.fstat(sf.fileno()).st_ctime)
				if (not (fname in db)) or ctime>db[fname]["ctime"]:
						scontent=[l.strip() for l in sf.readlines()]
						db[fname]={"content":scontent, "keywords":[], "ctime":ctime}
						dprint(".")
				else:
						dprint("-")
		return db[fname]

def termFreqs():
		global db, wc
		fnames=list(db.keys())
		fnames.sort()
		wordRe=re.compile("([a-z0-9][a-z0-9]*)")
		avg_df=0
		for fname in fnames:
				stf={}
				snippet=db[fname]
				i=0
				for line in snippet["content"]:
						words=wordRe.findall(line.lower())
						for word in words:
								if word in tf:
										tf[word]+=1
								else:
										tf[word]=1
								if word in stf:
										stf[word]+=1
								else:
										stf[word]=1
								i+=1
				snippet["tf"]=stf
				if i>0:
						wc+=i
						# Calculate average frequency for terms in this document
						df=0
						for w in stf:
								df+=stf[w]
						df=(1.0*df)/i
						avg_df+=df
		avg_df=avg_df/len(db) # global average frequency within a document

		ax=0
		for word in list(tf.keys()):
				if tf[word]==1 or word in stopwords:
						del tf[word]
				else:
						ax+=tf[word]
		avg_tf=(1.0*ax)/len(tf) # average frequency between documents
		threshhold=avg_df/avg_tf
		dprint(str(("words", wc, "unique words", len(tf), "snippets", len(db), "avg_df", avg_df, "avg_tf", avg_tf, "threshhold", threshhold)), lnl=True, tnl=True)
		for fname in fnames:
				snippet=db[fname]
				snippet["keywords"]=[]
				stfidf=[]
				stf=snippet["tf"]
				for word in stf:
						if word in tf:
								score=stf[word]/(1.0*tf[word])
								if(score>threshhold):
										stfidf.append( (score, word) )
				snippet["tfidf"]={}
				if len(stfidf):
						stfidf.sort()
						kw=[]
						if len(stfidf)>max_kw:
								kw=stfidf[:max_kw]
						else:
								kw=stfidf
						for item in kw:
								(score, word)=item
								snippet["keywords"].append(word)
								snippet["tfidf"][word]=score
				else:
						snippet["keywords"]=[]

def loadDb(fatal=True):
		global db
		if(os.path.exists("snippet.db")):
				with open("snippet.db", "rb") as f:
						db_ctime=os.fstat(f.fileno()).st_ctime
						db=pickle.load(f)
		elif(fatal):
				sys.stderr.write("Could not open DB -- did you forget to ingest?\n")
				sys.exit(1)

def process(fnames):
		global db, db_ctime
		loadDb(False)
		dprint("Processing files...")
		for fname in fnames:
				try:
						ingest(fname)
				except UnicodeDecodeError:
						dprint("?")
		dprint("\tDONE\nCalculating term frequencies...")
		termFreqs()
		dprint("\tDONE\nWriting database...")
		with open("snippet.db", "wb") as f:
				pickle.dump(db, f)
				db_ctime=os.fstat(f.fileno()).st_ctime
		dprint("\tDONE", tnl=True)
def stat():
		loadDb()
		for f in db:
				print(f)
				kw=db[f]["keywords"]
				kw=[(db[f]["tfidf"][k], k, db[f]["tf"][k]) for k in kw]
				kw.sort(reverse=True)
				if len(kw)>5:
						kw=kw[:5]
				for k in kw:
						print("\t".join([k[1], str(k[0]), str(k[2])]))
				print("")
def search(kw):
		loadDb()
		scores={}
		for f in db:
				scores[f]=0
		for f in db:
				for k in [k.lower() for k in kw]:
						if k in db[f]["tfidf"]:
								scores[f]+=db[f]["tfidf"][k]
		scores=[(scores[f], f) for f in scores]
		scores.sort(reverse=True)
		for score in scores:
				if score[0]==0:
						return
				print("\t".join([score[1], str(score[0])]))
def main():
		global silent
		fnames=[]
		if "-s" in sys.argv:
				silent=True
				sys.argv.remove("-s")
		if sys.argv[1]=="ingest":
				if len(sys.argv)>2:
						fnames=sys.argv[2:]
				else:
						for item in os.listdir("."):
								if len(item)>4 and item[-4:]==".txt":
										fnames.append(item[:-4])
				fnames.sort()
				print(fnames)
				process(fnames)
		elif sys.argv[1]=="stat":
				stat()
		elif sys.argv[1]=="search":
				search(sys.argv[2:])

main()
