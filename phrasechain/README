= PHRASE CHAIN =

Phrasechain takes text input from stdin & produces new text based on configurable rearrangement of phrases.

phrasechain.py takes one phrase per line; phrasechain.sh is a front-end that takes formatted text and breaks it into one phrase per 'sentence' (where sentences end with a period), producing output that renders nicely as markdown.


== HOW IT WORKS ==

Phrasechain is a variant on a markov chain. Rather than having a token-size of word, it treats each phrase as a token; a word from each phrase is chosen as a representative of that phrase, and so each phrase is classified based on the representative of the previous phrase.

The method by which representative words are chosen is configurable by a 'mode' setting, which can be passed as the first argument to either script. The modes are:

* first: Pick the first word in the phrase as a representative. (This is the default, and is the fastest)
* last: Pick the last word in the phrase as a representative. (This is the second-fastest)
* min: Of all words in the phrase, choose the one that occurs least frequently in the entire input text. (This often produces paragraphs that are very similar to the original input.)
* max: Of all words in the phrase, choose the one that occurs most frequently in the entire input text. (Because we do not eliminate stopwords, this produces very loose associations.)
* avg: For each word in the phrase, find its frequency in the entire input text. Take the average of these values, and then choose the word whose frequency is closest to this average value. (This produces the second-best results but is also the second-slowest.)
* avg2: Choose the word in the phrase that is closest to the global average frequency. (This produces the best results but is also the slowest.)

Each script can also take an optional 'seed' -- the representative for the imaginary phrase immediately preceeding the first output phrase. If the first arg passed to the script is a valid mode, then this seed can be the second arg; otherwise, it may be the first arg. If the seed happens to also be a valid mode name, a mode must be specified as the first arg to disambiguate the behavior. If no seed is supplied or the seed that is supplied does not occur as a representative, the special seed "" (empty string), representing the imaginary phrase prior to the first phrase of input, is used.

