#!/usr/bin/env python
import sys
import re

global snippetdb, docBy
global tf, wc
global silent, sids, maxMenuItems

maxMenuItems=10

snippetdb={}
docBy={}
docByCategories=["keyword", "tag", "title", "source", "type"]
for item in docByCategories:
		docBy[item]={}

tf={}
wc=0
silent=False
sids=[]

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

def snippetIngest(sid):	
		global snippetdb, docBy
		stype="text"
		ssource="notes"
		stitle="[no title]"
		scontent=[]
		stags=[]

		sf=open("snippets/"+sid+".txt", "r")
		for line in sf.readlines():
				if line.find("Type: ")==0:
						stype=line[6:].strip()
				elif line.find("Source: ")==0:
						ssource=line[8:].strip()
				elif line.find("Title: ")==0:
						stitle=line[7:].strip()
				elif line.find("* ")==0:
						stags.append(line[2:].strip())
				else:
						scontent.append(line.strip())
		if stitle in docBy["title"]:
				docBy["title"][stitle].append(sid)
		else:
				docBy["title"][stitle]=[sid]
		if ssource in docBy["source"]:
				docBy["source"][ssource].append(sid)
		else:
				docBy["source"][ssource]=[sid]
		if stype in docBy["type"]:
				docBy["type"][stype].append(sid)
		else:
				docBy["type"][stype]=[sid]
		for tag in stags:
				if tag in docBy["tag"]:
						docBy["tag"][tag].append(sid)
				else:
						docBy["tag"][tag]=[sid]
		snippetdb[sid]={"type":stype, "source":ssource, "title":stitle, "content":scontent, "tags":stags, "keywords":[]}
		return snippetdb[sid]

def snippetTermFreqs():
		global snippetdb, docBy, wc
		sids=snippetdb.keys()
		sids.sort()
		wordRe=re.compile("([a-z0-9][a-z0-9]*)")
		avg_df=0
		for sid in sids:
				stf={}
				snippet=snippetdb[sid]
				i=0
				for line in snippet["content"]+snippet["tags"]+[snippet["source"], snippet["title"]]:
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
				wc+=i
				snippet["tf"]=stf
				# Calculate average frequency for terms in this document
				df=0
				for w in stf:
						df+=stf[w]
				df=(1.0*df)/i
				avg_df+=df
		avg_df=avg_df/len(snippetdb) # global average frequency within a document

		ax=0
		for word in tf.keys():
				if tf[word]==1:
						del tf[word]
				else:
						ax+=tf[word]
		avg_tf=(1.0*ax)/len(tf) # average frequency between documents
		threshhold=avg_tf/avg_df
		dprint(str(("words", wc, "unique words", len(tf), "snippets", len(snippetdb), "avg_df", avg_df, "avg_tf", avg_tf, "threshhold", threshhold)), lnl=True, tnl=True)
		for sid in sids:
				snippet=snippetdb[sid]
				stfidf=[]
				stf=snippet["tf"]
				for word in stf:
						if word in tf:
								score=(1.0*tf[word])/stf[word]
								if(score>threshhold):
										stfidf.append( (score, word) )
				snippet["tfidf"]={}
				if len(stfidf):
						stfidf.sort()
						kw=[]
						if len(stfidf)>5:
								kw=stfidf[:5]
						else:
								kw=stfidf
						for item in kw:
								(score, word)=item
								snippet["keywords"].append(word)
								snippet["tfidf"][word]=score
								if word in docBy["keyword"]:
										docBy["keyword"][word][sid]=score
								else:
										docBy["keyword"][word]={sid:score}
				else:
						snippet["keywords"]=[]
		for kw in docBy["keyword"]:
				k=docBy["keyword"][kw]
				temp=[(k[w], w) for w in k]
				temp.sort()
				docBy["keyword"][kw]=[x[1] for x in temp]
		dprint(str(("total keywords:", len(docBy["keyword"]))), tnl=True)


def escape(s):
		return '"'+s.replace('"', '\\"')+'"'
def wln(f, line="", tabPos=0):
		f.write((tabPos*tab)+line+"\n")
def wmheader(f, q="Navigate to:", tabs=1, nvl_mode=True):
		wln(f, "nvl clear", tabs)
		menu="menu"
		if nvl_mode:
				menu="menu (nvl=True)"
		wln(f, menu+":", tabs)
		wln(f, "menuTitle "+escape(q), tabs+1)
def wmitem(f, title="[no title]", target="index", sfx="", tabs=1):
		if sfx:
				sfx=" "+sfx
		wln(f, escape(title)+sfx+":", tabs+1)
		wln(f, "jump "+target, tabs+2)

def sid2label(s):
			return "s"+s
tab="    "
audiotypes=["video", "audio"]
texttypes=["text", "audio"]
imagetypes=["video", "image"]
menuRedoAction={"video":"watch", "audio":"listen", "text":"read"}
hyperRe=re.compile("\[([^\] ]*)\]")
def snippet2rpy(sid):
		global snippetdb, docBy

		snippet=snippetdb[sid]
		stype=snippet["type"]
		stitle=snippet["title"]
		ssource=snippet["source"]
		tags=snippet["tags"]
		keywords=snippet["keywords"]
		content=snippet["content"]
		def fmt(l):
				lines=[]
				if l and len(l)>80 and l.find(" ")>0 and l.find(" ")<80:
						while len(l)>80 and l.find(" ")>0 and l.find(" ")<80:
							idx=l.rfind(" ")
							while idx>80:
									idx=l[:idx].rfind(" ")
							lines.append(l[:idx]+"\\n{nw}")
							l=l[idx+1:]
				lines.append(l)
				return lines
		def replaceHyperLinks(l):
			return hyperRe.sub("{a=jump:s\\1}\\1{/a}",l)	
		def sid2char(s):
				return "c"+s
		def wjmp(f, s, tabs=3):
				wln(f, "jump "+sid2label(s), tabs)
		def wsay(f, l, s=sid, tabs=1):
				wln(f, " ".join([sid2char(s), escape(l)]), tabs)
		def writeHeader(f):
				wln(f, "# This renpy script was generated by snippets2rpy")
				wln(f, "# "+tab+"sid: "+sid)
				for item in snippet:
						wln(f, "# "+tab+item+": "+escape(str(snippet[item])))
				wln(f)
		def writeTop(f):
				if stype in audiotypes:
						wln(f, "stop sound")
						wln(f, "stop music")
						wln(f)
				wln(f, "define "+sid2char(sid)+" = Character("+escape(stitle)+", kind=nvl, voice_tag="+escape(sid)+")")
				if stype=="audio":
						wln(f, "$ SetVoiceMute("+escape(sid)+", False)")
				else:
						wln(f, "$ SetVoiceMute("+escape(sid)+", True)")
				wln(f)
		def writeMenu(f, items, by):
				if items:
						lookup=docBy[by]
						header=by.upper()
						for item in items:
								if item in lookup and len(lookup[item]) >1:
										suffix=":"
										tsuffix=" ("+stype+")"
										if lookup[item][-1]==sid:
												suffix=" if False:"
												tsuffix+=" (trailhead)"
										ss=lookup[item]
										s=ss[(ss.index(sid)+1)%len(ss)]
										title=snippetdb[s]["title"]
										wln(f, escape(header+': '+item+'-> '+title+tsuffix)+suffix, 2)
										wjmp(f, s)
								else:
										wln(f, escape(header+": "+item+'-> '+stitle+' (no more matches found)')+" if False:", 2)
										wjmp(f, sid)
		def writeMenus(f):
				wmheader(f)
				wln(f, escape(menuRedoAction.get(stype, "view").capitalize()+" again")+":", 2)
				wjmp(f, sid)
				writeMenu(f, tags, "tag")
				writeMenu(f, keywords, "keyword")
				writeMenu(f, [ssource], "source")
				writeMenu(f, [stype], "type")
				wln(f, escape("Return to index")+":", 2)
				wln(f, "jump index", 3)
		def writeLabel(f):
				wln(f, "label "+sid2label(sid)+":")
				wln(f, "nvl clear", 1)
				i=0
				if stype=="video":
						wln(f, "nvl "+escape(snippet["title"] + " (video) ("+str(len(snippet["content"]))+" clips)"), 1)
				for l in content:
						if l:
								if stype in texttypes:
										l=replaceHyperLinks(l)
										fmtl=fmt(l)
										wsay(f, fmtl.pop(0))
										while fmtl:
												wln(f, "extend "+escape(fmtl.pop(0)), 1)
								elif stype=="video":
										if(len(snippet["content"])>1):
												i+=1
												wln(f, "nvl "+escape(snippet["title"] + " (clip "+str(i)+"/"+str(len(snippet["content"]))+")"), 1)
										wln(f, "renpy.movie_cutscene("+escape(l)+")", 1)
								i+=1
				if stype=="audio":
						wln(f, "$ SetVoiceMute("+escape(sid)+", True)", 1)
				if tags:
							wsay(f, "Tags: "+(", ".join(tags)))
				if keywords:
							wsay(f, "Keywords: "+(", ".join(keywords)))
				writeMenus(f)
				wln(f)


		rf=open("snippet_"+sid+".rpy", "w")
		writeHeader(rf)
		writeTop(rf)
		writeLabel(rf)
		rf.close()

def generateIndex(sids):
		f=open("index.rpy", "w")
		wln(f, "label index:")
		wln(f, "nvl clear", 1)
		wmheader(f, "Index")
		for by in docByCategories:
				wmitem(f, "By "+by, by+"_index")
		wmitem(f, "By ID", "sid_index")
		wln(f)
		def sortHelper(by, fn=None):
				if not fn:
						fn=lambda x: len(docBy[by][x])
				temp=[(fn(x), x, docBy[by][x][0])
								for x in docBy[by].keys()]
				temp.sort()
				return [(x[1], x[2]) for x in temp]
		lookup={
				"sid": [(x, x) for x in sids],
				"title":sortHelper("title", lambda x: x),
				"keyword":sortHelper("keyword", lambda x: snippetdb[docBy["keyword"][x][0]]["tfidf"][x]),
				"tag":sortHelper("tag"),
				"source":sortHelper("source"),
				"type":sortHelper("type")
				}
		def generateIndex_r(by, allOptions, offset=0):
				print(by)
				wln(f, "label "+by+"_index"+str(offset)+":")
				wln(f, "nvl clear", 1)
				wmheader(f, "Index by "+by)
				options=allOptions[offset:]
				if len(options)>maxMenuItems:
						options=options[:maxMenuItems]
				for option in options:
						wmitem(f, option[0], sid2label(option[1]))
				wmitem(f, "Return to index", "index")
				if (len(allOptions)-offset)>maxMenuItems:
						wmitem(f, "Next Page", by+"_index"+str(offset+1))
						wln(f)
						generateIndex_r(by, allOptions, offset+maxMenuItems)
				wln(f)

		for by in docByCategories+["sid"]:
				wln(f, "label "+by+"_index:")
				wln(f, "jump "+by+"_index0", 1)
				wln(f)
				generateIndex_r(by, lookup[by])
		f.close()


def processSnippets(sids):
		dprint("Processing snippets...")
		for sid in sids:
				snippetIngest(sid)
				progress()
		dprint("\tDONE\nCalculating term frequencies...")
		snippetTermFreqs()
		dprint("\tDONE\nGenerating rpy files...")
		for sid in sids:
				snippet2rpy(sid)
				progress()
		dprint("\tDONE\nGenerating index...")
		generateIndex(sids)
		dprint("\tDONE", tnl=True)



def main():
		global silent, sids
		sids=[]
		if "-s" in sys.argv:
				silent=True
				sys.argv.remove("-s")
		if len(sys.argv)>1:
				sids=sys.argv[1:]
		sids.sort()
		print(sids)
		processSnippets(sids)

main()
