# -*- coding: utf-8 -*-
"""
Created on Sun May 24 00:04:11 2020

@author: 45242
"""

crews =  [['00000027','Shakespeare in Love',1998,'Costume Design'],

            ['00000209','The Matrix',1999,'Sound Effects Editing'],

            ['00000205','The Matrix',1999,'Visual Effects'],

            ['00000206','The Matrix',1999,'Visual Effects'],

            ['00000207','The Matrix',1999,'Visual Effects'],

            ['00000208','The Matrix',1999,'Visual Effects'],

            ['00001140','The Piano',1993,'Cinematography'],

            ['00000306','The Piano',1993,'Costume Design'],

            ['00000307','The Piano',1993,'Production Design'],

            ['00000325','Mad Max',1979,'Music'],

            ['00000349','Strictly Ballroom',1992,'Costume Design'],

            ['00000348','Strictly Ballroom',1992,'Production Design'],

            ['00000347','Strictly Ballroom',1992,'Editing'],

            ['00000545','Alien',1979,'Music'],

            ['00000546','Alien',1979,'Production Design'],

            ['00000547','Alien',1979,'Special Effects'],

            ['00000562','Aliens',1986,'Sound Editor'],

            ['00000563','Aliens',1986,'Visual Effects'],

            ['00000564','Aliens',1986,'Visual Effects'],

            ['00000006','Titanic',1997,'Set Decorator'],

            ['00000007','Titanic',1997,'Cinematography'],

            ['00000008','Titanic',1997,'Costume Design'],

            ['00000009','Titanic',1997,'Visual Effects'],

            ['00000010','Titanic',1997,'Sound Effects'],

            ['00000011','Titanic',1997,'Editing'],

            ['00000012','Titanic',1997,'Music'],

            ['00000013','Titanic',1997,'Song Lyric'],

            ['00001009','Bullets Over Broadway',1994,'producer'],

            ['00001010','Bullets Over Broadway',1994,'cinematography'],

            ['00001011','Bullets Over Broadway',1994,'film editing'],

            ['00001012','Bullets Over Broadway',1994,'casting'],

            ['00001013','Bullets Over Broadway',1994,'costume design'],

            ['00001019','Tombstone',1993,'producer'],

            ['00001020','Tombstone',1993,'cinematography'],

            ['00001021','Tombstone',1993,'film editing'],

            ['00001022','Tombstone',1993,'casting'],

            ['00001023','Tombstone',1993,'costume design'],

            ['00001009','Alice',1990,'producer'],

            ['00001010','Alice',1990,'cinematography'],

            ['00001011','Alice',1990,'film editing'],

            ['00001012','Alice',1990,'casting'],

            ['00001013','Alice',1990,'costume design'],

            ['00001032','Mermaids',1990,'producer'],

            ['00001033','Mermaids',1990,'cinematography'],

            ['00001034','Mermaids',1990,'film editing'],

            ['00001035','Mermaids',1990,'casting'],

            ['00001036','Mermaids',1990,'costume design'],

            ['00001041','Exotica',1994,'producer'],

            ['00001042','Exotica',1994,'cinematography'],

            ['00001043','Exotica',1994,'film editing'],

            ['00001047','Red Rock West',1992,'producer'],

            ['00001048','Red Rock West',1992,'cinematography'],

            ['00001049','Red Rock West',1992,'film editing'],

            ['00001050','Red Rock West',1992,'costume design'],

            ['00001056','Chaplin',1992,'cinematography'],

            ['00001057','Chaplin',1992,'film editing'],

            ['00001058','Chaplin',1992,'casting'],

            ['00001059','Chaplin',1992,'costume design'],

            ['00001065','Fearless',1993,'producer'],

            ['00001066','Fearless',1993,'cinematography'],

            ['00001067','Fearless',1993,'film editing'],

            ['00001068','Fearless',1993,'casting'],

            ['00001069','Fearless',1993,'costume design'],

            ['00001074','Threesome',1994,'producer'],

            ['00001075','Threesome',1994,'cinematography'],

            ['00001076','Threesome',1994,'film editing'],

            ['00001077','Threesome',1994,'casting'],

            ['00001078','Threesome',1994,'costume design'],

            ['00001079','Jungle Fever',1991,'producer'],

            ['00001082','Jungle Fever',1991,'cinematography'],

            ['00001083','Jungle Fever',1991,'film editing'],

            ['00001084','Jungle Fever',1991,'casting'],

            ['00001085','Jungle Fever',1991,'costume design'],

            ['00001091','Internal Affairs',1990,'producer'],

            ['00001092','Internal Affairs',1990,'cinematography'],

            ['00001093','Internal Affairs',1990,'film editing'],

            ['00001094','Internal Affairs',1990,'casting'],

            ['00001095','Internal Affairs',1990,'costume design'],

            ['00001096','Single White Female',1992,'producer'],

            ['00001101','Single White Female',1992,'cinematography'],

            ['00001102','Single White Female',1992,'film editing'],

            ['00001103','Single White Female',1992,'costume design'],

            ['00001104','Trust',1990,'producer'],

            ['00001107','Trust',1990,'cinematography'],

            ['00001108','Trust',1990,'film editing'],

            ['00001109','Trust',1990,'costume design'],

            ['00001114','Ju Dou',1990,'producer'],

            ['00001115','Ju Dou',1990,'cinematography'],

            ['00001116','Ju Dou',1990,'film editing'],

            ['00001117','Ju Dou',1990,'costume design'],

            ['00001121','Dahong Denglong Gaogao Gua',1991,'producer'],

            ['00001122','Dahong Denglong Gaogao Gua',1991,'cinematography'],

            ['00001123','Dahong Denglong Gaogao Gua',1991,'film editing'],

            ['00001127','Cyrano de Bergerac',1990,'producer'],

            ['00001128','Cyrano de Bergerac',1990,'cinematography'],

            ['00001129','Cyrano de Bergerac',1990,'film editing'],

            ['00001130','Cyrano de Bergerac',1990,'costume design'],

            ['00001010','Manhattan Murder Mystery',1993,'cinematography'],

            ['00001011','Manhattan Murder Mystery',1993,'film editing'],

            ['00001012','Manhattan Murder Mystery',1993,'casting'],

            ['00001013','Manhattan Murder Mystery',1993,'costume design'],

            ['00001132','El Mariachi',1992,'producer'],

            ['00001139','Once Were Warriors',1994,'producer'],

            ['00001140','Once Were Warriors',1994,'cinematography'],

            ['00001141','Once Were Warriors',1994,'film editing'],

            ['00001142','Once Were Warriors',1994,'casting'],

            ['00001147','Priest',1994,'producer'],

            ['00001148','Priest',1994,'cinematography'],

            ['00001149','Priest',1994,'film editing'],

            ['00001150','Priest',1994,'casting'],

            ['00001154','Pump Up the Volum',1990,'producer'],

            ['00001155','Pump Up the Volum',1990,'cinematography'],

            ['00001156','Pump Up the Volum',1990,'film editing'],

            ['00001157','Pump Up the Volum',1990,'casting'],

            ['00001162','Benny and Joon',1993,'cinematography'],

            ['00001163','Benny and Joon',1993,'film editing'],

            ['00001164','Benny and Joon',1993,'casting'],

            ['00001165','Six Degrees of Separation',1993,'producer'],

            ['00001170','Six Degrees of Separation',1993,'cinematography'],

            ['00001171','Six Degrees of Separation',1993,'film editing'],

            ['00001172','Six Degrees of Separation',1993,'casting'],

            ['00001177','Bawang Bie Ji',1993,'producer'],

            ['00001178','Bawang Bie Ji',1993,'film editing'],

            ['00001179','In the Line of Fire',1993,'producer'],

            ['00001184','In the Line of Fire',1993,'cinematography'],

            ['00001185','In the Line of Fire',1993,'casting'],

            ['00001186','Heavenly Creatures',1994,'producer'],

            ['00001189','Heavenly Creatures',1994,'cinematography'],

            ['00001190','Heavenly Creatures',1994,'film editing'],

            ['00001194','Hoop Dreams',1994,'producer'],

            ['00001199','Seven',1995,'cinematography'],

            ['00001200','Seven',1995,'film editing'],

            ['00001201','Seven',1995,'casting'],

            ['00001207','Shallow Grave',1994,'producer'],

            ['00001208','Shallow Grave',1994,'cinematography'],

            ['00001209','Shallow Grave',1994,'film editing'],

            ['00001212','French Kiss',1995,'producer'],

            ['00001215','French Kiss',1995,'cinematography'],

            ['00001216','French Kiss',1995,'film editing'],

            ['00001190','Braindead',1992,'producer'],

            ['00001220','Braindead',1992,'cinematography'],

            ['00001221','Clerks',1994,'producer'],

            ['00001224','Clerks',1994,'cinematography'],

            ['00001185','Apollo 13',1995,'casting'],

            ['00001230','Apollo 13',1995,'producer'],

            ['00001231','Apollo 13',1995,'cinematography'],

            ['00001232','Reservoir Dogs',1992,'producer'],

            ['00001236','Reservoir Dogs',1992,'film editing'],

            ['00001237','Reservoir Dogs',1992,'casting'],

            ['00001240','Pulp Fiction',1994,'producer'],

            ['00001236','Pulp Fiction',1994,'film editing'],

            ['00001245','Yinshi Nan Nu',1994,'producer'],

            ['00001246','Yinshi Nan Nu',1994,'cinematography'],

            ['00001247','Yinshi Nan Nu',1994,'film editing'],

            ['00001252','Short Cuts',1993,'producer'],

            ['00001255','Short Cuts',1993,'cinematography'],

            ['00001253','Short Cuts',1993,'film editing'],

            ['00001258','Legends of the Fall',1994,'cinematography'],

            ['00001259','Legends of the Fall',1994,'film editing'],

            ['00001260','Legends of the Fall',1994,'casting'],

            ['00001265','Natural Born Killers',1994,'film editing'],

            ['00001266','Natural Born Killers',1994,'costume design'],

            ['00001268','In the Mouth of Madness',1995,'producer'],

            ['00001272','In the Mouth of Madness',1995,'cinematography'],

            ['00001273','In the Mouth of Madness',1995,'film editing'],

            ['00001278','Forrest Gump',1994,'producer'],

            ['00001279','Forrest Gump',1994,'cinematography'],

            ['00001280','Forrest Gump',1994,'casting'],

            ['00001082','Malcolm X',1992,'cinematography'],

            ['00001084','Malcolm X',1992,'casting'],

            ['00001283','Malcolm X',1992,'film editing'],

            ['00001287','Dead Again',1991,'producer'],

            ['00001288','Dead Again',1991,'cinematography'],

            ['00001289','Dead Again',1991,'film editing'],

            ['00001290','Dead Again',1991,'casting'],

            ['00001295','Jurassic Park',1993,'producer'],

            ['00001296','Jurassic Park',1993,'film editing'],

            ['00001185','Jurassic Park',1993,'casting'],

            ['00001301','Clueless',1995,'producer'],

            ['00001302','Clueless',1995,'cinematography'],

            ['00001303','Clueless',1995,'film editing'],

            ['00001304','Clueless',1995,'casting'],

            ['00001305','Shadowlands',1993,'producer'],

            ['00001309','Shadowlands',1993,'cinematography'],

            ['00001310','Shadowlands',1993,'film editing'],

            ['00001311','Shadowlands',1993,'casting'],

            ['00001104','Amateur',1994,'producer'],

            ['00001314','Amateur',1994,'film editing'],

            ['00001315','Amateur',1994,'casting'],

            ['00001316','Amateur',1994,'costume design'],

            ['00001321','GoodFellas',1990,'producer'],

            ['00001322','GoodFellas',1990,'cinematography'],

            ['00001323','GoodFellas',1990,'film editing'],

            ['00001328','Little Women',1994,'producer'],

            ['00001329','Little Women',1994,'cinematography'],

            ['00001330','Little Women',1994,'film editing'],

            ['00001335','While You Were Sleeping',1995,'producer'],

            ['00001336','While You Were Sleeping',1995,'film editing'],

            ['00001337','While You Were Sleeping',1995,'casting']]
