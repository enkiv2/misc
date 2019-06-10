/* Usage: swipl -s output.pl -g tracery_all */
:- set_prolog_flag(double_quotes, chars).
t_origin --> "A ", t_A, " ", t_B, " about a ", t_C, "'s ", t_D, " ", t_E, " to ", t_F, " their ", t_G, ".".
t_A --> "edge-of-your-seat".
t_A --> "keenly observed".
t_A --> "lyrical".
t_A --> "profound".
t_A --> "erotic".
t_A --> "inspiring".
t_A --> "razor-sharp".
t_A --> "heartrending".
t_A --> "dream-like".
t_A --> "darkly comic".
t_A --> "unflinching".
t_A --> "fiercely honest".
t_A --> "richly drawn".
t_A --> "unforgettable".
t_A --> "riveting".
t_A --> "high-voltage".
t_A --> "psycho-sexual".
t_A --> "riotously funny".
t_A --> "passionate".
t_A --> "surreal".
t_A --> "dystopian".
t_A --> "hysterical".
t_A --> "meditative".
t_C --> "depressed".
t_C --> "wealthy".
t_C --> "doomed".
t_C --> "exuberant".
t_C --> "agoraphobic".
t_C --> "maladjusted".
t_C --> "misanthropic".
t_C --> "alcoholic".
t_C --> "young".
t_C --> "philosophical".
t_C --> "hopelessly romantic".
t_C --> "hyper-sexual".
t_C --> "precocious".
t_C --> "unlucky".
t_C --> "quixotic".
t_C --> "desperate".
t_C --> "refugee".
t_C --> "dissatisfied".
t_C --> "bored".
t_C --> "morally compromised".
t_C --> "lovesick".
t_C --> "drug-addled".
t_C --> "jilted".
t_C --> "vengeful".
t_C --> "overbearing".
t_C --> "closeted".
t_B --> "thriller".
t_B --> "meditation".
t_B --> "coming of age story".
t_B --> "family drama".
t_B --> "war epic".
t_B --> "epistolary novel".
t_B --> "romance".
t_B --> "tragedy".
t_B --> "story".
t_B --> "tour de force".
t_B --> "comedy".
t_B --> "noir".
t_B --> "instant classic".
t_B --> "fairy tale".
t_B --> "autobiographical novel".
t_B --> "romp".
t_B --> "fictional memoir".
t_B --> "trilogy".
t_B --> "detective novel".
t_B --> "page-turner".
t_B --> "tragicomedy".
t_B --> "murder mystery".
t_B --> "novel in stories".
t_B --> "historical novel".
t_B --> "graphic novel".
t_B --> "saga".
t_E --> "adventure".
t_E --> "committment".
t_E --> "desire".
t_E --> "devotion".
t_E --> "dream".
t_E --> "effort".
t_E --> "strategy".
t_E --> "pains".
t_E --> "failure".
t_E --> "inability".
t_E --> "journey".
t_E --> "mission".
t_E --> "not-so-secret desire".
t_E --> "quest".
t_E --> "endevour".
t_E --> "secret longing".
t_E --> "struggle".
t_E --> "vacation".
t_E --> "wish".
t_E --> "expedition".
t_E --> "plan".
t_E --> "scheme".
t_E --> "resolve".
t_E --> "project".
t_E --> "promise".
t_E --> "battle".
t_D --> "man".
t_D --> "orphan".
t_D --> "daughter".
t_D --> "mother".
t_D --> "adolescent".
t_D --> "soldier".
t_D --> "student".
t_D --> "widow".
t_D --> "woman".
t_D --> "professor".
t_D --> "devorcee".
t_D --> "adventurer".
t_D --> "extended family".
t_D --> "child".
t_D --> "mistress".
t_D --> "dictator".
t_D --> "vampire".
t_D --> "ghost".
t_D --> "starship captain".
t_D --> "doctor".
t_D --> "writer".
t_D --> "private investigator".
t_D --> "couple".
t_D --> "coven".
t_D --> "murder detective".
t_D --> "octogenarian".
t_G --> "fear of spiders".
t_G --> "adoption".
t_G --> "traumatic childhood".
t_G --> "mother's death".
t_G --> "sexless marriage".
t_G --> "Oedipal complex".
t_G --> "feminism".
t_G --> "religious upbringing".
t_G --> "political apathy".
t_G --> "biological clock".
t_G --> "ugly divorce".
t_G --> "writer's block".
t_G --> "toxic friendships".
t_G --> "eating disorder".
t_G --> "own birth".
t_G --> "cancer".
t_G --> "23andMe results".
t_G --> "privilege".
t_G --> "untimely death".
t_G --> "social media addiction".
t_G --> "spiritual evolution".
t_G --> "secret second family".
t_G --> "sexual awakening".
t_G --> "Amazon reviews".
t_G --> "father's murder".
t_G --> "disinheritance".
t_F --> "re-awaken".
t_F --> "come to grips with".
t_F --> "grapple with".
t_F --> "understand".
t_F --> "explore".
t_F --> "accept".
t_F --> "overcome".
t_F --> "avenge".
t_F --> "persue".
t_F --> "defend".
t_F --> "undertake".
t_F --> "discover".
t_F --> "contemplate".
t_F --> "transcend".
t_F --> "withdraw from".
t_F --> "avoid".
t_F --> "betray".
t_F --> "circumvent".
t_F --> "confront".
t_F --> "expose".
t_F --> "give up".
t_F --> "investigate".
t_F --> "navigate".
t_F --> "reconnect with".
t_F --> "embrace".
t_F --> "reconcile to".

format_helper(X) :- format("~s\n", [X]).
tracery_print(Goal) :- phrase(Goal, X), format_helper(X).
tracery_helper(X) :- phrase(t_origin, X).
tracery_rand :- findnsols(100000, X, tracery_helper(X), Res), length(Res, N), ItemNum is random(N), nth0(ItemNum, Res, Item), format_helper(Item).
tracery :- tracery_print(t_origin).
tracery_all :- findall(_, tracery, _).
