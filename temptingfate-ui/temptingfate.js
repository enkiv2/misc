function shuffle(a) {
    var j, x, i;
    for (i = a.length; i; i--) {
        j = Math.floor(Math.random() * i);
        x = a[i - 1];
        a[i - 1] = a[j];
        a[j] = x;
    }
}

querent_deck=[]
fate_deck=[]

paths=[]
path_tokens=[]
discard=[]

querent_hand=[]
fate_hand=[]
function initialize_decks() {
	for(i=0; i<78; i++) {
		querent_deck.push(i)
	}
	for(i=0; i<20; i++) {
		for(j=0; j<5; j++) {
			fate_deck.push(j)
		}
	}

	shuffle(querent_deck)
	shuffle(fate_deck)
}

function draw_fate() {
	fate_hand.push(fate_deck.pop())
}
function draw_querent() {
	querent_hand.push(querent_deck.pop())
}

function initialize_game(){
	querent_deck=[]
	fate_deck=[]
	querent_hand=[]
	fate_hand=[]
	paths=[]
	path_tokens=[]
	discard=[]
	initialize_decks()
	for (i=0; i<5; i++) {
		draw_fate()
		draw_querent()
	}
}
initialize_game()
console.log("Querent deck:")
console.log(querent_deck)
console.log("Fate deck:")
console.log(fate_deck)
console.log("Querent hand:")
console.log(querent_hand)
console.log("Fate hand:")
console.log(fate_hand)
console.log("Paths:")
console.log(paths)
