# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:43:22 2020

@author: 45242
"""


scenes = [['Rear Window',1954,1,'Jeffs appartment'],

    ['Rear Window',1954,2,'Private Dramas'],

    ['Rear Window',1954,3,'The Piano Player'],

    ['Rear Window',1954,4,'The Salesman'],

    ['Rear Window',1954,5,'Witness of a murder'],

    ['Rear Window',1954,6,'Lisa in danger'],

    ['Rear Window',1954,7,'Final battle'],

    ['Rear Window',1954,8,'One more broken leg'],

    ['The Birds',1963,1,'Love Birds'],

    ['The Birds',1963,2,'Dogs in front of a pet shop'],

    ['The Birds',1963,3,'Arriving at Bodega Bay'],

    ['The Birds',1963,4,'Gull attack'],

    ['The Birds',1963,5,'Birthday party'],

    ['The Birds',1963,6,'Bird meeting'],

    ['The Birds',1963,7,'At Brenners House'],

    ['The Birds',1963,8,'Open End'],

    ['Psycho',1960,1,'Fed up with life'],

    ['Psycho',1960,2,'40000 dollars for a new start'],

    ['Psycho',1960,3,'Coffee Break'],

    ['Psycho',1960,4,'The Bates Motel'],

    ['Psycho',1960,5,'Norman and Mother'],

    ['Psycho',1960,6,'Taking a shower'],

    ['Psycho',1960,7,'Norman takes over'],

    ['Psycho',1960,8,'Killing mother'],

    ['Traffic',2000,1,'Corruption at Mexican Border'],

    ['Traffic',2000,2,'A new anti-drug czar'],

    ['Traffic',2000,3,'Addicted to Drugs'],

    ['Traffic',2000,4,'Arresting a Baron'],

    ['Traffic',2000,5,'Temptations'],

    ['Traffic',2000,6,'Loosing Caroline'],

    ['Traffic',2000,7,'Taking over the Business'],

    ['Traffic',2000,8,'Untenable Situation'],

    ['Traffic',2000,9,'Assassains'],

    ['Traffic',2000,10,'New Family Values'],

    ['Traffic',2000,11,'The Fight goes on'],

    ['Bullets Over Broadway',1994,1,'gangster'],

    ['Bullets Over Broadway',1994,2,'playwright'],

    ['Bullets Over Broadway',1994,3,'theater'],

    ['Bullets Over Broadway',1994,4,'writing'],

    ['Bullets Over Broadway',1994,5,'murder'],

    ['Bullets Over Broadway',1994,6,'new-york'],

    ['Tombstone',1993,1,'settle down in Tombstone'],

    ['Tombstone',1993,2,'Wyatts brother'],

    ['Tombstone',1993,3,'The Cowboys band'],

    ['Tombstone',1993,4,'problems caused'],

    ['Tombstone',1993,5,'violence region'],

    ['Tombstone',1993,6,'shoot-out at the OK Corral'],

    ['Alice',1990,1,'bored-housewife'],

    ['Alice',1990,2,'infidelity'],

    ['Alice',1990,3,'human-relationship'],

    ['Alice',1990,4,'socialite'],

    ['Alice',1990,5,'christmas'],

    ['Alice',1990,6,'gossip'],

    ['Alice',1990,7,'invisible-man'],

    ['Alice',1990,8,'invisible'],

    ['Mermaids',1990,1,'failed relationship'],

    ['Mermaids',1990,2,'move to east coast'],

    ['Mermaids',1990,3,'Charlottes life'],

    ['Mermaids',1990,4,'the church employee'],

    ['Mermaids',1990,5,'mother-daughter relationship'],

    ['Exotica',1994,1,'bay-sitting'],

    ['Exotica',1994,2,'flashback-sequence'],

    ['Exotica',1994,3,'homesexual'],

    ['Exotica',1994,4,'audit'],

    ['Exotica',1994,5,'ticket-scalping'],

    ['Exotica',1994,6,'psychological-drama'],

    ['Exotica',1994,7,'lesbian-scene'],

    ['Exotica',1994,8,'smuggling'],

    ['Red Rock West',1992,1,'money'],

    ['Red Rock West',1992,2,'neo-noir'],

    ['Red Rock West',1992,3,'hitman'],

    ['Red Rock West',1992,4,'sheriff'],

    ['Red Rock West',1992,5,'murder'],

    ['Red Rock West',1992,6,'small-town'],

    ['Red Rock West',1992,7,'railway'],

    ['Red Rock West',1992,8,'train'],

    ['Chaplin',1992,1,'charlie-chaplin'],

    ['Chaplin',1992,2,'hollywood'],

    ['Chaplin',1992,3,'silent-film-maker'],

    ['Chaplin',1992,4,'political-persecution'],

    ['Chaplin',1992,5,'film-making'],

    ['Chaplin',1992,6,'based-on-multiple-works'],

    ['Fearless',1993,1,'car-crash'],

    ['Fearless',1993,2,'isolation'],

    ['Fearless',1993,3,'recovery'],

    ['Fearless',1993,4,'law'],

    ['Fearless',1993,5,'self-confidence'],

    ['Fearless',1993,6,'disaster'],

    ['Fearless',1993,7,'video-game'],

    ['Fearless',1993,8,'airplane-accident'],

    ['Fearless',1993,9,'flashback-sequence'],

    ['Fearless',1993,10,'allergy'],

    ['Fearless',1993,11,'strawberry'],

    ['Threesome',1994,1,'midget'],

    ['Threesome',1994,2,'dormitory'],

    ['Threesome',1994,3,'best-friend'],

    ['Threesome',1994,4,'college'],

    ['Threesome',1994,5,'homosexual'],

    ['Threesome',1994,6,'roommate'],

    ['Threesome',1994,7,'shower-scene'],

    ['Threesome',1994,8,'adult-humor'],

    ['Jungle Fever',1991,1,'racial'],

    ['Jungle Fever',1991,2,'affair'],

    ['Jungle Fever',1991,3,'deception'],

    ['Jungle Fever',1991,4,'interracial-love'],

    ['Jungle Fever',1991,5,'crack-den'],

    ['Jungle Fever',1991,6,'drugs'],

    ['Jungle Fever',1991,7,'new-york'],

    ['Jungle Fever',1991,8,'racism'],

    ['Internal Affairs',1990,1,'corrupt-cop'],

    ['Internal Affairs',1990,2,'internal-affairs'],

    ['Internal Affairs',1990,3,'investigation'],

    ['Internal Affairs',1990,4,'unfaithfulness'],

    ['Internal Affairs',1990,5,'lesbian-cop'],

    ['Internal Affairs',1990,6,'police'],

    ['Single White Female',1992,1,'apartment'],

    ['Single White Female',1992,2,'software'],

    ['Single White Female',1992,3,'notebook'],

    ['Single White Female',1992,4,'personals-column'],

    ['Single White Female',1992,5,'murder'],

    ['Single White Female',1992,6,'psychopath'],

    ['Single White Female',1992,7,'puppy'],

    ['Single White Female',1992,8,'roommate'],

    ['Single White Female',1992,9,'female scene'],

    ['Trust',1990,1,'Marias pregnancy'],

    ['Trust',1990,2,'homeless'],

    ['Trust',1990,3,'Matthew Slaughter'],

    ['Trust',1990,4,'Matthews job'],

    ['Trust',1990,5,'being together'],

    ['Trust',1990,6,'changes'],

    ['Ju Dou',1990,1,'1920s'],

    ['Ju Dou',1990,2,'crippling-accident'],

    ['Ju Dou',1990,3,'factory-owner'],

    ['Ju Dou',1990,4,'feudal-society'],

    ['Ju Dou',1990,5,'impotence'],

    ['Ju Dou',1990,6,'push-cart'],

    ['Ju Dou',1990,7,'sadism'],

    ['Dahong Denglong Gaogao Gua',1991,1,'marriage'],

    ['Dahong Denglong Gaogao Gua',1991,2,'Chens castle'],

    ['Dahong Denglong Gaogao Gua',1991,3,'competition between the wives'],

    ['Dahong Denglong Gaogao Gua',1991,4,'the red lantern'],

    ['Dahong Denglong Gaogao Gua',1991,5,'haircut'],

    ['Dahong Denglong Gaogao Gua',1991,6,'doctor'],

    ['Cyrano de Bergerac',1990,1,'fall in love with Roxane'],

    ['Cyrano de Bergerac',1990,2,'the large nose'],

    ['Cyrano de Bergerac',1990,3,'the letter'],

    ['Cyrano de Bergerac',1990,4,'Christian in love'],

    ['Cyrano de Bergerac',1990,5,'the mistake'],

    ['Manhattan Murder Mystery',1993,1,'blackmail'],

    ['Manhattan Murder Mystery',1993,2,'neighbor'],

    ['Manhattan Murder Mystery',1993,3,'heart-attack'],

    ['Manhattan Murder Mystery',1993,4,'husband-wife-relationship'],

    ['Manhattan Murder Mystery',1993,5,'new-york'],

    ['Manhattan Murder Mystery',1993,6,'publisher'],

    ['Manhattan Murder Mystery',1993,7,'amateur-detective'],

    ['Manhattan Murder Mystery',1993,8,'murder'],

    ['El Mariachi',1992,1,'motorcycle'],

    ['El Mariachi',1992,2,'paper-knife'],

    ['El Mariachi',1992,3,'singer'],

    ['El Mariachi',1992,4,'low-budget'],

    ['El Mariachi',1992,5,'bathtub'],

    ['El Mariachi',1992,6,'guitar'],

    ['El Mariachi',1992,7,'mistaken-identity'],

    ['El Mariachi',1992,8,'dream'],

    ['El Mariachi',1992,9,'guitar-case'],

    ['El Mariachi',1992,10,'hotel'],

    ['Once Were Warriors',1994,1,'marriage'],

    ['Once Were Warriors',1994,2,'rape'],

    ['Once Were Warriors',1994,3,'suicide'],

    ['Once Were Warriors',1994,4,'vulgarity'],

    ['Once Were Warriors',1994,5,'alcohol'],

    ['Once Were Warriors',1994,6,'suicide-by-hanging'],

    ['Priest',1994,1,'Love Birds'],

    ['Priest',1994,2,'Dogs in front of a pet shop'],

    ['Priest',1994,3,'Arriving at Bodega Bay'],

    ['Priest',1994,4,'Gull attack'],

    ['Priest',1994,5,'Birthday party'],

    ['Priest',1994,6,'Bird meeting'],

    ['Priest',1994,7,'At Brenners House'],

    ['Priest',1994,8,'Open End'],

    ['Pump Up the Volum',1990,1,'catholic'],

    ['Pump Up the Volum',1990,2,'controversial'],

    ['Pump Up the Volum',1990,3,'homosexual'],

    ['Pump Up the Volum',1990,4,'incest'],

    ['Pump Up the Volum',1990,5,'priest'],

    ['Pump Up the Volum',1990,6,'religion'],

    ['Benny and Joon',1993,1,'mechanic'],

    ['Benny and Joon',1993,2,'psychiatrist'],

    ['Benny and Joon',1993,3,'mental-illness'],

    ['Benny and Joon',1993,4,'psychoanalysis'],

    ['Benny and Joon',1993,5,'schizophrenia'],

    ['Six Degrees of Separation',1993,1,'bisexual'],

    ['Six Degrees of Separation',1993,2,'homosexual'],

    ['Six Degrees of Separation',1993,3,'impostor'],

    ['Six Degrees of Separation',1993,4,'suicide'],

    ['Six Degrees of Separation',1993,5,'nudity'],

    ['Bawang Bie Ji',1993,1,'peking-opera'],

    ['Bawang Bie Ji',1993,2,'training'],

    ['Bawang Bie Ji',1993,3,'become famous'],

    ['Bawang Bie Ji',1993,4,'prostitution'],

    ['Bawang Bie Ji',1993,5,'japanese-occupation'],

    ['Bawang Bie Ji',1993,6,'communism'],

    ['Bawang Bie Ji',1993,7,'drugs'],

    ['Bawang Bie Ji',1993,8,'culture revolution'],

    ['In the Line of Fire',1993,1,'assassination'],

    ['In the Line of Fire',1993,2,'master-of-disguise'],

    ['In the Line of Fire',1993,3,'president'],

    ['In the Line of Fire',1993,4,'neck-breaking-scene'],

    ['In the Line of Fire',1993,5,'secret-service'],

    ['Heavenly Creatures',1994,1,'schoolgirl'],

    ['Heavenly Creatures',1994,2,'bathtub'],

    ['Heavenly Creatures',1994,3,'make-believe'],

    ['Heavenly Creatures',1994,4,'parent'],

    ['Heavenly Creatures',1994,5,'surreal'],

    ['Heavenly Creatures',1994,6,'murder'],

    ['Hoop Dreams',1994,1,'college'],

    ['Hoop Dreams',1994,2,'ghetto'],

    ['Hoop Dreams',1994,3,'high-school'],

    ['Hoop Dreams',1994,4,'narrated'],

    ['Hoop Dreams',1994,5,'school'],

    ['Seven',1995,1,'detective'],

    ['Seven',1995,2,'seven-deadly-sins'],

    ['Seven',1995,3,'violence'],

    ['Seven',1995,4,'overweight'],

    ['Seven',1995,5,'partner'],

    ['Seven',1995,6,'serial-killer'],

    ['Seven',1995,7,'disturbing'],

    ['Shallow Grave',1994,1,'apartment'],

    ['Shallow Grave',1994,2,'corpse'],

    ['Shallow Grave',1994,3,'death'],

    ['Shallow Grave',1994,4,'friend'],

    ['Shallow Grave',1994,5,'greed'],

    ['Shallow Grave',1994,6,'betrayal'],

    ['French Kiss',1995,1,'wine'],

    ['French Kiss',1995,2,'american-in-paris'],

    ['French Kiss',1995,3,'france'],

    ['French Kiss',1995,4,'human-relaionship'],

    ['French Kiss',1995,5,'paris-france'],

    ['French Kiss',1995,6,'toronto'],

    ['Braindead',1992,1,'1950s'],

    ['Braindead',1992,2,'splatter'],

    ['Braindead',1992,3,'dominatnt-mother'],

    ['Braindead',1992,4,'zombie'],

    ['Braindead',1992,5,'gore'],

    ['Braindead',1992,6,'disturbing'],

    ['Braindead',1992,7,'mutant-baby'],

    ['Braindead',1992,8,'reanimation'],

    ['Braindead',1992,9,'zoo'],

    ['Clerks',1994,1,'necrophilia'],

    ['Clerks',1994,2,'new-jersey'],

    ['Clerks',1994,3,'russian-rock'],

    ['Clerks',1994,4,'snowball'],

    ['Clerks',1994,5,'funeral'],

    ['Clerks',1994,6,'generation-X'],

    ['Clerks',1994,7,'disgruntled-worker'],

    ['Clerks',1994,8,'accidental-necrophilia'],

    ['Apollo 13',1995,1,'astronaut'],

    ['Apollo 13',1995,2,'husband and wife'],

    ['Apollo 13',1995,3,'launch'],

    ['Apollo 13',1995,4,'nasa'],

    ['Apollo 13',1995,5,'lunar-mission'],

    ['Apollo 13',1995,6,'survival'],

    ['Apollo 13',1995,7,'explosion'],

    ['Apollo 13',1995,8,'space-travel'],

    ['Apollo 13',1995,9,'spacecraft'],

    ['Apollo 13',1995,10,'return'],

    ['Reservoir Dogs',1992,1,'car-jacking'],

    ['Reservoir Dogs',1992,2,'hit-and-run'],

    ['Reservoir Dogs',1992,3,'severed-ear'],

    ['Reservoir Dogs',1992,4,'cop-killer'],

    ['Reservoir Dogs',1992,5,'chase'],

    ['Reservoir Dogs',1992,6,'undercover'],

    ['Pulp Fiction',1994,1,'injection'],

    ['Pulp Fiction',1994,2,'dance-contest'],

    ['Pulp Fiction',1994,3,'ganster'],

    ['Pulp Fiction',1994,4,'full-circle'],

    ['Pulp Fiction',1994,5,'boxing'],

    ['Pulp Fiction',1994,6,'taxicab'],

    ['Pulp Fiction',1994,7,'foot-massage'],

    ['Pulp Fiction',1994,8,'hamburger'],

    ['Pulp Fiction',1994,9,'corpse'],

    ['Yinshi Nan Nu',1994,1,'father and daughter'],

    ['Yinshi Nan Nu',1994,2,'dinner'],

    ['Yinshi Nan Nu',1994,3,'life of Jia-Chien'],

    ['Yinshi Nan Nu',1994,4,'in fast food restaurant'],

    ['Yinshi Nan Nu',1994,5,'pregnant'],

    ['Yinshi Nan Nu',1994,6,'family discussion'],

    ['Short Cuts',1993,1,'fishing'],

    ['Short Cuts',1993,2,'helicopter'],

    ['Short Cuts',1993,3,'unfaithfulness'],

    ['Short Cuts',1993,4,'suicide'],

    ['Short Cuts',1993,5,'telepone-sex'],

    ['Short Cuts',1993,6,'chainsaw'],

    ['Short Cuts',1993,7,'earthquake'],

    ['Short Cuts',1993,8,'hospital'],

    ['Legends of the Fall',1994,1,'bear'],

    ['Legends of the Fall',1994,2,'brothers'],

    ['Legends of the Fall',1994,3,'racism'],

    ['Legends of the Fall',1994,4,'the war'],

    ['Legends of the Fall',1994,5,'passion'],

    ['Legends of the Fall',1994,6,'corruption'],

    ['Legends of the Fall',1994,7,'marriage'],

    ['Legends of the Fall',1994,8,'father and son'],

    ['Natural Born Killers',1994,1,'escape'],

    ['Natural Born Killers',1994,2,'snake-bite'],

    ['Natural Born Killers',1994,3,'serial-killer'],

    ['Natural Born Killers',1994,4,'desert'],

    ['Natural Born Killers',1994,5,'prison'],

    ['Natural Born Killers',1994,6,'revenge'],

    ['Natural Born Killers',1994,7,'wedding-ring'],

    ['In the Mouth of Madness',1995,1,'axe'],

    ['In the Mouth of Madness',1995,2,'horro-writer'],

    ['In the Mouth of Madness',1995,3,'lovecraft'],

    ['In the Mouth of Madness',1995,4,'author'],

    ['In the Mouth of Madness',1995,5,'publisher'],

    ['In the Mouth of Madness',1995,6,'asylum'],

    ['In the Mouth of Madness',1995,7,'monster'],

    ['Forrest Gump',1994,1,'running'],

    ['Forrest Gump',1994,2,'folk-singer'],

    ['Forrest Gump',1994,3,'vietnam war'],

    ['Forrest Gump',1994,4,'table-tennis'],

    ['Forrest Gump',1994,5,'hero'],

    ['Forrest Gump',1994,6,'strom'],

    ['Forrest Gump',1994,7,'shrimping'],

    ['Forrest Gump',1994,8,'marathon'],

    ['Forrest Gump',1994,9,'wedding'],

    ['Forrest Gump',1994,10,'cancer'],

    ['Forrest Gump',1994,11,'son'],

    ['Malcolm X',1992,1,'penitentiary'],

    ['Malcolm X',1992,2,'hustler'],

    ['Malcolm X',1992,3,'beach'],

    ['Malcolm X',1992,4,'harlem'],

    ['Malcolm X',1992,5,'streetcar'],

    ['Malcolm X',1992,6,'police-brutality'],

    ['Malcolm X',1992,7,'streetcar'],

    ['Malcolm X',1992,8,'surveillance'],

    ['Malcolm X',1992,9,'train'],

    ['Malcolm X',1992,10,'urban-decay'],

    ['Dead Again',1991,1,'reporter'],

    ['Dead Again',1991,2,'reincarnation'],

    ['Dead Again',1991,3,'scandal'],

    ['Dead Again',1991,4,'opera'],

    ['Dead Again',1991,5,'private-detective'],

    ['Dead Again',1991,6,'wedding'],

    ['Dead Again',1991,7,'amnesia'],

    ['Dead Again',1991,8,'jewelry'],

    ['Jurassic Park',1993,1,'amusement-park'],

    ['Jurassic Park',1993,2,'tropical-island'],

    ['Jurassic Park',1993,3,'tyrannosaurus'],

    ['Jurassic Park',1993,4,'child'],

    ['Jurassic Park',1993,5,'gene-manipulation'],

    ['Jurassic Park',1993,6,'raptor'],

    ['Jurassic Park',1993,7,'computer-cracker'],

    ['Jurassic Park',1993,8,'disaster'],

    ['Jurassic Park',1993,9,'product-placement'],

    ['Clueless',1995,1,'beverly-hills'],

    ['Clueless',1995,2,'high-school'],

    ['Clueless',1995,3,'popularity'],

    ['Clueless',1995,4,'teen'],

    ['Clueless',1995,5,'makeover'],

    ['Clueless',1995,6,'driving test'],

    ['Clueless',1995,7,'wedding'],

    ['Shadowlands',1993,1,'author'],

    ['Shadowlands',1993,2,'the Narnia books'],

    ['Shadowlands',1993,3,'teacher of Oxford'],

    ['Shadowlands',1993,4,'Joy Gresham'],

    ['Shadowlands',1993,5,'love affair'],

    ['Shadowlands',1993,6,'Joy is unwell'],

    ['Shadowlands',1993,7,'life became complicated'],

    ['Amateur',1994,1,'amnesia'],

    ['Amateur',1994,2,'blackmail'],

    ['Amateur',1994,3,'nun'],

    ['Amateur',1994,4,'torture'],

    ['Amateur',1994,5,'pornographer'],

    ['GoodFellas',1990,1,'gangster'],

    ['GoodFellas',1990,2,'prison'],

    ['GoodFellas',1990,3,'heist'],

    ['GoodFellas',1990,4,'paranoia'],

    ['GoodFellas',1990,5,'contraband'],

    ['GoodFellas',1990,6,'mafia'],

    ['GoodFellas',1990,7,'nightclub'],

    ['GoodFellas',1990,8,'cheat-on-wife'],

    ['GoodFellas',1990,9,'organized-crime'],

    ['GoodFellas',1990,10,'witness-protection'],

    ['GoodFellas',1990,11,'christmas'],

    ['Little Women',1994,1,'1860s'],

    ['Little Women',1994,2,'american-civil-war'],

    ['Little Women',1994,3,'neighbor'],

    ['Little Women',1994,4,'sisters'],

    ['Little Women',1994,5,'secret meetings'],

    ['Little Women',1994,6,'party'],

    ['Little Women',1994,7,'father'],

    ['Little Women',1994,8,'piano'],

    ['While You Were Sleeping',1995,1,'family'],

    ['While You Were Sleeping',1995,2,'christmas'],

    ['While You Were Sleeping',1995,3,'winter'],

    ['While You Were Sleeping',1995,4,'coma'],

    ['While You Were Sleeping',1995,5,'financee'],

    ['While You Were Sleeping',1995,6,'loneliness'],

    ['While You Were Sleeping',1995,7,'infatuation'],

    ['While You Were Sleeping',1995,8,'subway'],

    ['While You Were Sleeping',1995,9,'new-year-eve']]