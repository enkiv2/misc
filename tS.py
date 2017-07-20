#!/usr/bin/env python
import json
import re
import sys

# A vaguely sed-like stream processing tool for tracery

# commands:
# g -> grep
# s -> replace
# modifiers:
# g -> all (default)
# r -> rule only
# o -> option only
# grep-only modifiers:
# b -> require both rule and option to match
# v -> invert selection

def merge(world, results, rule):
	if not (rule in results):
		results[rule]=world[rule]
	else:
		if(results[rule]!=world[rule]):
			for option in world[rule]:
				if not option in results[rule]:
					results[rule].append(option)
	return results

def cmpI(expr, v):
	if(v):
		return (not expr)
	return expr

def grep(world, expr, modifiers):
	ec=re.compile(expr)
	v=(modifiers.find("v")>=0)
	results={}
	for rule in world.keys():
		if(modifiers.find("o")==-1 and modifiers.find("b")==-1):
			if(cmpI(re.match(ec, rule)!=None, v)):
				results=merge(world, results, rule)
		if(modifiers.find("r")==-1 and modifiers.find("b")==-1):
			for option in world[rule]:
				if(cmpI(re.match(ec, option)!=None, v)):
					if not (rule in results):
						results[rule]=[option]
					else:
						if not (option in results[rule]):
							results[rule].append(option)
		if(modifiers.find("b")!=-1):
			if(cmpI(re.match(ec, rule)!=None, v)):
				for option in world[rule]:
					if(cmpI(re.match(ec, option)!=None, v)):	
						if not (rule in results):
							results[rule]=[option]
						else:
							if not (option in results[rule]):
								results[rule].append(option)
	return results
def incMatches(m):
	g=int(m.group(0))
	if(g>0):
		g+=2
	return "\\"+str(g)
def replace(world, expr, expr2, modifiers):
	ex=re.compile(expr)
	ex2=re.compile("\(#[^#]*\)"+expr+"\([^#]*#\)")
	results={}
	for rule in world.keys():
		rulename=rule
		if(modifiers.find("o")==-1):
			rulename=re.sub(ex, expr2, rule)
		if not (rulename in results):
			results[rulename]=[]
		for option in world[rule]:
			if(modifiers.find("r")==-1):
				opt=re.sub(ex, expr2, option)
			else:
				opt=re.sub(ex2, "\1"+re.sub("\\\\\([0-9]+\)", incMatches, expr2)+"\2", option)
			results[rulename].append(opt)
	return results
def mergeEscaped(items, sep):
	res=[]
	curr=""
	for item in items:
		if(len(item)>0):
			curr+=item
			if(curr[-1]=="\\"):
				curr+=sep
			else:
				res.append(curr)
				curr=""
	res.append(curr)
	return res
def parseScriptLine(line):
	sep=line[1]
	components=mergeEscaped(line.split(sep), sep)
	obj={}
	obj["cmd"]=components[0]
	if not (obj["cmd"] in ["g", "s"]):
		raise Exception("Parse error: command \""+obj["cmd"]+"\" invalid.")
	obj["modifiers"]=""
	obj["expr"]=""
	obj["expr2"]=""
	if(len(components)<2):
		raise Exception("Parse error: expected expression after \""+obj["cmd"]+sep+"\".")
	obj["expr"]=components[1]
	if(obj["cmd"]=="g"):
		if(len(components)>2):
			obj["modifiers"]=components[2]
	else:
		if(len(components)<3):
			raise Exception("Parse error: expected replacement string after \""+sep.join([obj["cmd"], obj["expr"]])+sep+"\".")
		obj["expr2"]=components[2]
		if(len(components)>3):
			obj["modifiers"]=components[3]
	return obj
		
def parseScript(script):
	ast=[]
	lines=script.split(";")
	lines=mergeEscaped(lines, ";")
	for line in lines:
		if(len(line)>0):
			ast.append(parseScriptLine(line))
	return ast
def execute(ast, world):
	res=world
	for line in ast:
		cmd=line["cmd"]
		expr=line["expr"]
		expr2=line["expr2"]
		modifiers=line["modifiers"]
		if(cmd=="g"):
			res=grep(res, expr, modifiers)
		elif(cmd=="s"):
			res=replace(res, expr, expr2, modifiers)
		else:
			raise Exception("Runtime error: command \""+cmd+"\" not found.")
	return res
def executeScript(script, world):
	return execute(parseScript(script), world)

def main():
	if(len(sys.argv)<2):
		sys.stderr.write("Usage: "+sys.argv[0]+" script [file]\n")
	script=sys.argv[1]
	if(len(sys.argv)>2):
		with open(sys.argv[2], 'r') as f:
			print(json.dumps(executeScript(script, json.load(f))))
	else:
		print(json.dumps(executeScript(script, json.load(sys.stdin))))

if(__name__=="__main__"):
	main()

