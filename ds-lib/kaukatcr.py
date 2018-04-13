#!/usr/bin/env python
from ZZCell import *

def str2num(s):
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            return s

builtins={}
# Stack manipulation builtins
def Kdup(intepreterHead, currCell):
    item=rankPop(interpreterHead, "d.stack")
    rankPush(interpreterHead, "d.stack", item)
    rankPush(interpreterHead, "d.stack", item)
    return currCell.getNext("d.exec")
builtins["dup"]=Kdup
def Kswap(interpreterHead, currCell):
    item1=rankPop(interpreterHead, "d.stack")
    item2=rankPop(interpreterHead, "d.stack")
    rankPush(interpreterHead, "d.stack", item1)
    rankPush(interpreterHead, "d.stack", item2)
    return currCell.getNext("d.exec")
builtins["swap"]=Kswap
def Krot(interpreterHead, currCell):
    item1=rankPop(interpreterHead, "d.stack")
    item2=rankPop(interpreterHead, "d.stack")
    item3=rankPop(interpreterHead, "d.stack")
    rankPush(interpreterHead, "d.stack", item1)
    rankPush(interpreterHead, "d.stack", item3)
    rankPush(interpreterHead, "d.stack", item2)
    return currCell.getNext("d.exec")
builtins["rot"]=Krot 
def Kpop(interpreterHead, currCell):
    rankPop(interpreterHead, "d.stack")
    return currCell.getNext("d.exec")
builtins["pop"]=Kpop
# Control flow builtins
def Kdef(interpreterHead, currCell):
    n=currCell.getNext("d.exec")
    remote=n.clone()
    interpreterHead.rankHead("d.funcs", True).setNext("d.funcs", remote)
    n=n.getNext("d.exec")
    while n!=None and n!="end" and n!=";;":
        remote=rankPush(remote, "d.exec", n.clone())
        n=n.getNext("d.exec")
    if(n):
        return n.getNext("d.exec")
    return n
builtins["def"]=Kdef
builtins[":"]=Kdef
def Kif(interpreterHead, currCell):
    if(rankPop(interpreterHead, "d.stack").getValue()):
        return currCell.getNext("d.branch")
    return currCell.getNext("d.exec")
builtins["if"]=Kif
def Kret(interpreterHead, currCell):
    return rankPop(interpreterHead, "d.call")
builtins["ret"]=Kret
# Arithmetic builtins
def Kadd(interpreterHead, currCell):
    rankPush(interpreterHead, "d.stack", 
        ZZCell(str2num(rankPop(interpreterHead, "d.stack").getValue())+
        str2num(rankPop(interpreterHead, "d.stack").getValue()))
        )
    return currCell.getNext("d.exec")
builtins["+"]=Kadd
def Ksub(interpreterHead, currCell):
    rankPush(interpreterHead, "d.stack", 
        ZZCell(str2num(rankPop(interpreterHead, "d.stack").getValue())-
        str2num(rankPop(interpreterHead, "d.stack").getValue()))
        )
    return currCell.getNext("d.exec")
builtins["-"]=Ksub
def Kmul(interpreterHead, currCell):
    rankPush(interpreterHead, "d.stack", 
        ZZCell(str2num(rankPop(interpreterHead, "d.stack").getValue())*
        str2num(rankPop(interpreterHead, "d.stack").getValue()))
        )
    return currCell.getNext("d.exec")
builtins["*"]=Kmul
def Kdiv(interpreterHead, currCell):
    rankPush(interpreterHead, "d.stack", 
        ZZCell(str2num(rankPop(interpreterHead, "d.stack").getValue())/
        str2num(rankPop(interpreterHead, "d.stack").getValue()))
        )
    return currCell.getNext("d.exec")
builtins["/"]=Kdiv
def Kmod(interpreterHead, currCell):
    rankPush(interpreterHead, "d.stack", 
        ZZCell(str2num(rankPop(interpreterHead, "d.stack").getValue())%
        str2num(rankPop(interpreterHead, "d.stack").getValue()))
        )
    return currCell.getNext("d.exec")
builtins["%"]=Kmod
# IO builtins
def Kdot(intepreterHead, currCell):
    item=rankPop(interpreterHead, "d.stack")
    print(item.getValue())
    return currCell.getNext("d.exec")
builtins["."]=Kdot
def Kreadline(interpreterHead, currCell):
    rankPush(interpreterHead, "d.stack", sys.stdin.readline())
    return currCell.getNext("d.exec")
builtins["readline"]=Kreadline
def Kreadcell(interpreterHead, currCell):
    cid=int(rankPop(interpreterHead, "d.stack"))
    rankPush(interpreterHead, "d.stack", cells[cid].clone())
    return currCell.getNext("d.exec")
builtins["readcell"]=Kreadcell
def Kwritecell(interpreterHead, currCell):
    cid=int(rankPop(interpreterHead, "d.stack"))
    content=rankPop(interpreterHead, "d.stack")
    cells[cid].cloneHead().value=content.getValue()
    return currCell.getNext("d.exec")
builtins["writecell"]=Kwritecell
def Knext(interpreterHead, currCell):
    cid=int(rankPop(interpreterHead, "d.stack"))
    dim=rankPop(interpreterHead, "d.stack").getValue()
    rankPush(interpreterHead, "d.stack", ZZCell(cells[cid].getNext(dim).cid))
    return currCell.getNext("d.exec")
builtins["next"]=Knext
def Kprev(interpreterHead, currCell):
    cid=int(rankPop(interpreterHead, "d.stack"))
    dim=rankPop(interpreterHead, "d.stack").getValue()
    rankPush(interpreterHead, "d.stack", ZZCell(cells[cid].getNext(dim, false).cid))
    return currCell.getNext("d.exec")
builtins["prev"]=Kprev

def getRank(currCell, dim):
    rank=[currCell]
    n=currCell.getNext(dim)
    while n!=None and n!=currCell:
        rank.append(n)
        n=currCell.getNext(dim)
    return rank
def rankPush(currCell, dim, item):
    currCell.insert(dim, item)
    return item
def rankPop(currCell, dim):
    ret=currCell.getNext(dim)
    if(ret):
        ret.elide(dim)
    return ret
def step(interpreterHead, currCell):
    val=currCell.getValue()
    if val in builtins:
        return builtins[val](interpreterHead, currCell)
    else:
        funcs=getRank(interpreterHead, "d.funcs")
        if val in map(lambda x: x.getValue(), funcs):
            rankPush(interpreterHead, "d.call", currCell.getNext("d.exec"))
            for func in funcs:
                if(func.getValue()==val):
                    return func
        else:
            rankPush(interpreterHead, "d.stack", currCell.clone())
    return currCell.getNext("d.exec")
def execute(interpreterHead):
    n=step(interpreterHead, interpreterHead)
    while(n):
        n=step(interpreterHead, n)
