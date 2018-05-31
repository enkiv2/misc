package senketsu
// senketsu - a dialect of io with a persistent memory-mapped lobby & a MUMPS-style global persistent list-keyed database

import (
//	"strconv"
	"fmt"
	"strings"
)

type object struct {
	typeName string
	name	string
	parent *object
	supportedMessages map[string]string
	mailbox chan message
	children map[string]object
}
type message struct {
	messageName string
	args []object
	response chan object
	expectsResponse bool
}

var Object object
var Future object
var Nil object
var String object

var Lobby map[string]*object

func initializeEnvironment() {
	/* TODO: 
		- Lobby object in Lobby, providing all objects as children
		- Function executor (requires looking up Io semantics in detail)
		- FFI of some kind (so we can implement builtins, at least)
		- Error handling
		- Memory mapped lobby
		- Versioned lobby (maybe just as journal to start out with)
	 */
	Object := object{"Object", "Object", nil, nil, make(chan message), nil}
	Future := object{"Future", "Future", &Object, nil, make(chan message), nil}
	String := object{"String", "String", &Object, nil, make(chan message), nil}
	Lobby["Object"]=&Object
	Lobby["Future"]=&Future
	Lobby["Nil"]=&Nil
	Lobby["String"]=&String

}
func nextChunk(s string, term string) (string, string) {
	var head string
	var tail string
	s=strings.TrimSpace(s)
	nextComma := strings.IndexAny(s, term)
	nextParen := strings.Index(s, "(")
	if(nextComma==-1) { nextComma=len(s) }
	if(nextParen==-1 || nextComma<nextParen) {
		head = s[0:nextComma-1]
		if(nextComma+1<len(s)-1) {
			tail = s[nextComma+1:len(s)-1]
		} else {
			tail = ""
		}
	} else if(nextParen!=0) {
		head = s[0:nextParen-1]
		if(nextParen<len(s)-1) {
			tail = s[nextParen:len(s)-1]
		} else {
			tail = ""
		}
	} else { // Our parenthetical expression begins the chunk
		depth := 1
		i:=0
		for i=0; i<len(s); i++ {
			if (s[i]=='(') {
				depth++
			} else if(s[i]==')') {
				depth--
				if(depth==0) {
					head = s[1:i-1]
					if(i+1<len(s)-1) {
						tail = s[i+1:len(s)-1]
					} else {
						tail = ""
					}
					return strings.TrimSpace(head), tail
				}
			}
		}
	}
	return strings.TrimSpace(head), tail
}
func nextPtFreeChunk(s string) (string, string) {
	return nextChunk(s, " \t\n");
}
func nextArgChunk(s string) (string, string) {
	return nextChunk(s, ",");
}

func vivifyObject(context object, name string) object {
	ret := context.handle(vivifyMsg(name))
	var ret2 *object
	var ok bool
	if(ret.name=="") {
		if ret2, ok=Lobby[name];ok{
			return *ret2
		} else {
			if(name[0]=='"') {
				return String.clone(name)
			} // TODO: parse numbers and turn them into Number objects
		}
	}
	return Nil
}
func vivifyMsg(head string) message {
	var msg message
	if(head[0]=='@') {
		msg.expectsResponse=false
		msg.messageName=head[1:len(head)-1]
	} else {
		msg.expectsResponse=true
		msg.messageName=head
	}
	msg.response=make(chan object)
	return msg
}

func execute_r(context object, head string, tail string) []object { // accumulates args of a message
	var ret []object
	if(head=="") { head, tail = nextArgChunk(tail) }
	for ;len(head)>0||len(tail)>0; head, tail = nextArgChunk(tail) {
		if(head[0]=='(') {
			head2, tail2 := nextArgChunk(head)
			ret=append(ret, execute(context, head2, tail2))
		} else {
			ret=append(ret, vivifyObject(context, head))
		}
	}
	return ret
}
func execute(context object, head string, tail string) object { // handles pointfree sequences of messages, given initial context
	if(head=="") { head, tail = nextPtFreeChunk(tail) }
	for ;len(head)>0 || len(tail)>0; head, tail = nextPtFreeChunk(tail) {
		if(head[0]=='(') {
			head2, tail2 := nextPtFreeChunk(head)
			context=execute(context, head2, tail2)
		} else {
			msg:=vivifyMsg(head)
			if(tail[0]=='(') {
				argList:=""
				argList, tail = nextPtFreeChunk(tail)
				msg.args=execute_r(context, "", argList)
			}
			context=context.handle(msg)
		}
	}
	return context

}

func (self object) clone(newName string) object {
	var ret=object{}
	if (newName=="") {
		if(self.typeName=="") { self.typeName="Object" }
		ret.typeName=self.typeName
		newName=self.typeName+fmt.Sprintf("_%x", &ret)
	} else {
		if(newName[0]>='A' && newName[0]<='Z') {
			ret.typeName=newName
		} else {
			ret.typeName=self.typeName
		}
	}
	ret.name=newName
	ret.parent=&self
	Lobby[ret.name]=&ret
	ret.run()
	return ret
}
func (self object) handle(m message) object {
	// TODO implement error stack and error condition
	var impl string
	var ret object
	var ok bool
	if impl, ok=self.supportedMessages[m.messageName]; ok {
		ret = execute(self, "", impl)
	} else {
		if ret, ok = self.children[m.messageName]; !ok {
			if(self.parent!=nil) {
				ret=self.parent.handle(m)
			} else {
				// TODO throw error
			}
		}
	}
	if(m.expectsResponse) {
		m.response<-ret
	}
	return ret
}
func (self object) run() {
	self.mailbox=make(chan message)
	go func() {
		select{
		case msg := <-self.mailbox:
			self.handle(msg)
		}
	}()
}
func (self object) call(other object, msg message) object{
	other.mailbox <- msg
	if(msg.expectsResponse) {
		ret := <-msg.response
		return ret
	}
	return Nil
}
func (self object) callAsync(other object, msg message) object {
	var ret=Future.clone("")
	go func() {
		ret=self.call(other, msg)
	}()
	return ret
}
