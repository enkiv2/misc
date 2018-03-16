// senketsu - a dialect of io with a persistent memory-mapped lobby & a MUMPS-style global persistent list-keyed database
struct object {
	typeName string
	name	string
	parent *object
	supportedMessages map[string]string
	mailbox chan message
}
struct message {
	messageName string
	args object[]
	response chan object
	expectsResponse bool
}

var Object object {"Object", "Object", nil, nil, make(chan message)}
var Future object {"Future", "Future", &Object, nil, make(chan message)}

func (self object) clone(newName string) {
	var ret=object{}
	if (newName==nil) {
		ret.typeName=self.typeName
		newName=self.typeName+&ret
	} else {
		if(newName[0]>=A && newName[0]<=Z) {
			ret.typeName=newName
		} else {
			ret.typeName=self.typeName
		}
	}
	ret.name=newName
	ret.parent=&self
	ret.run()
	return ret
}
func (self object) handle(m message) {
	// TODO implement error stack and error condition
	var impl string
	if(self.supportedMessages != nil) {
		impl=self.supportedMessages[m.messageName]
	} else {
		impl=nil
	}
	var ret object
	if(impl) {
		// TODO call out to parser/executor, set ret
	} else {
		if(self.parent!=nil) {
			ret=(*(self.parent).handle(m))
		} else {
			// TODO throw error
		}
	}
	if(m.expectsResponse) {
		ret -> m.response
	}
}
func (self object) run() {
	self.mailbox=make(chan message)
	go func() {
		select{
		case msg := <-self.mailbox:
			self.handle(msg)
		}
	}
}
func (self object) call(other object, msg message) object{
	msg -> other.mailbox
	var ret object
	if(msg.expectsResponse) {
		ret <- msg.response
		return ret
	}
	return nil // TODO: replace with nil object
}
func (self object) callAsync(other object, msg message) object {
	var ret=Future.clone(nil)
	go func() {
		ret=call(other, msg)
	}
	return ret
}
