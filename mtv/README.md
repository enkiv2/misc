    mtv - minimal transliterature viewer
    (c) 2017 John Ohno
    This software is not associated with Project Xanadu (tm)!

    Requirements: python, tkinter, ipfs command line tools



EDL format:

An EDL is an array of clips. Each clip is a json object containing the following attributes:

* "path" is a URL or IPFS hash
* "row" is the line that the quote begins on
* "col" is the character offset from the beginning of the line that the quote starts on
* "dRows" is the number of full lines the quote continues for
* "dCols" is the number of characters we continue for on the final line


ODL format:

An ODL is an array of links. Each link is an array of endpoints. Each endpoint has all of the attributes of a clip, but additionally includes:

* "type": an arbitrary string indicating the variety of link
* "attributes": an object corresponding to TK text widget tag attributes. It must exist if type = "format", and otherwise should not exist

