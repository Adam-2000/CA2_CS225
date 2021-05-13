# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:03:30 2020

@author: 45242
"""
"""NO 00000163""" 
roles =[['00000002','Titanic',1997,'Jack Dawson',''],
 
            ['00001188','Titanic',1997,'Rose DeWitt Bukater','Heavenly Creatures'],
 
            ['00000004','Titanic',1997,'Cal Hockley',''],
 
            ['00000005','Titanic',1997,'Molly Brown',''],
 
            ['00000023','Shakespeare in Love',1998,'Philip Henslowe',''],
 
            ['00001146','Shakespeare in Love',1998,'Hugh Fennyman','Priest'],
 
            ['00000025','Shakespeare in Love',1998,'Lambert',''],
 
            ['00000026','Shakespeare in Love',1998,'Queen Elizabeth',''],
 
            ['00000043','The Cider House Rules',1999,'Olive Worthington',''],
 
            ['00000044','The Cider House Rules',1999,'Homer Wells',''],
 
            ['00000045','The Cider House Rules',1999,'Candy Kendall',''],
 
            ['00000046','The Cider House Rules',1999,'Mr.Rose',''],
 
            ['00000047','The Cider House Rules',1999,'Dr Wilbur Larch',''],
 
            ['00000063','Gandhi',1982,'Mahatma Gandhi',''],
 
            ['00000064','Gandhi',1982,'Margaret Bourke',''],
 
            ['00000065','Gandhi',1982,'Pandit Nehru',''],
 
            ['00000066','Gandhi',1982,'General Dyer',''],
 
            ['00000083','American Beauty',1999,'Lester Burnham',''],
 
            ['00000084','American Beauty',1999,'Carolyn Burnham',''],
 
            ['00000085','American Beauty',1999,'Jane Burnham',''],
 
            ['00000086','American Beauty',1999,'Ricky Fitts',''],
 
            ['00000103','Affliction',1997,'Wade Whitehouse',''],
 
            ['00000104','Affliction',1997,'Jill',''],
 
            ['00000105','Affliction',1997,'Gordon LaRiviere',''],
 
            ['00000106','Affliction',1997,'Jack Hewitt',''],
 
            ['00000107','Affliction',1997,'Glen Whitehouse',''],
 
            ['00000121','Life is Beautiful',1997,'Guido Orefice',''],
 
            ['00000123','Life is Beautiful',1997,'Dora',''],
 
            ['00000143','Boys Dont Cry',1999,'Brandon Teena',''],
 
            ['00000144','Boys Dont Cry',1999,'Lana Tisdel',''],
 
            ['00000145','Boys Dont Cry',1999,'John Lotter',''],
 
            ['00000146','Boys Dont Cry',1999,'Marvin Thomas',''],
 
            ['00001227','Saving Private Ryan',1998,'Captain John','Toy Story'],
 
            ['00000164','Saving Private Ryan',1998,'Sergeant Michael',''],
 
            ['00000165','Saving Private Ryan',1998,'Richard Reiben',''],
 
            ['00000166','Saving Private Ryan',1998,'Jackson',''],
 
            ['00000181','The Birds',1963,'Man in pet shop',''],
 
            ['00000184','The Birds',1963,'Mitch Brenner',''],
 
            ['00000185','The Birds',1963,'Lydia Brenner',''],
 
            ['00000186','The Birds',1963,'Annie Hayworth',''],

            ['00000187','The Birds',1963,'Melanie Daniels',''],

            ['00001001','Rear Window',1954,'L.B. Jeff Jefferies',''],

            ['00001002','Rear Window',1954,'Lisa Carol Fremont',''],

            ['00001003','Rear Window',1954,'Lars Thorwald',''],

            ['00000181','Rear Window',1954,'Clock-Winding Man','Psycho, Birds'],
 
            ['00000203','The Matrix',1999,'Thomas',''],
 
            ['00000204','The Matrix',1999,'Morpheus',''],
 
            ['00001227','Toy Story',1995,'Woody','Saving Private Ryan'],
 
            ['00000942','Toy Story',1995,'Buzz Lightyear',''],
 
            ['00000943','Toy Story',1995,'Bo Peep',''],
 
            ['00001212','Proof of Life',2000,'Alice Bowman','Hanging Up'],
 
            ['00000622','Proof of Life',2000,'Terry Thorne','Gladiator'],
 
            ['00000963','Proof of Life',2000,'Peter Bowman',''],
 
            ['00001212','Hanging Up',2000,'Eve','Proof of Life'],
 
            ['00001131','Hanging Up',2000,'Georgia','Manhattan Murder Mystery'],
 
            ['00000983','Hanging Up',2000,'Maddy',''], 
 
            ['00000223','You have Got Mail',1998,'Patricia Eden',''],


 
            ['00001212','You have Got Mail',1998,'Kathleen Kelly','Hanging Up'],
 
            ['00000242','The Price of Milk',2000,'Lucinda','Topless Women Talk About Their Lives'], 
 
            ['00000243','The Price of Milk',2000,'Rob',''], 
 
            ['00000244','The Price of Milk',2000,'Drosophila','Topless Women Talk About Their Lives'],
 
            ['00000262','The Footstep Man',1992,'Sam',''], 
 
            ['00000263','The Footstep Man',1992,'Mirielle',''], 
 
            ['00000264','The Footstep Man',1992,'Henri de Toulouse',''], 
 
            ['00000242','Topless Women Talk About Their Lives',1997,'Liz','The Price of Milk'], 
 
            ['00000281','Topless Women Talk About Their Lives',1997,'Neil',''],
 
            ['00000282','Topless Women Talk About Their Lives',1997,'Ant',''],  
 
            ['00000244','Topless Women Talk About Their Lives',1997,'Prue','The Price of Milk'],
 
            ['00000302','The Piano',1993,'Ada McGrath',''],
 
            ['00001233','The Piano',1993,'George Baines','Reservoir Dogs'],
 
            ['00000304','The Piano',1993,'Flora McGrath',''],
 
            ['00000323','Mad Max',1979,'Max Rockatansky','Lethal Weapon 4'],
 
            ['00000324','Mad Max',1979,'Jessie Rockatansky',''],
 
            ['00000343','Strictly Ballroom',1992,'Scott Hastings',''],
 
            ['00000344','Strictly Ballroom',1992,'Fran',''],
 
            ['00000345','Strictly Ballroom',1992,'Shirley Hastings',''],
 
            ['00000346','Strictly Ballroom',1992,'Doug Hastings',''],
 
            ['00000362','My Mother Frank',2000,'Mike',''],
 
            ['00000363','My Mother Frank',2000,'Jenny',''],
 
            ['00000364','My Mother Frank',2000,'Frank',''],
 
            ['00000383','American Psycho',2000,'Patrick Bateman ',''],
 
            ['00000384','American Psycho',2000,'Donald Kimball',''],
 
            ['00000385','American Psycho',2000,'Paul Allen',''],
 
            ['00001153','American Psycho',2000,'Courtney Rawlinson','Pump Up the Volume'],
 
            ['00000403','Scream 2',1997,'Dwight Dewey Riley',''],
 
            ['00000404','Scream 2',1997,'Sidney Prescott',''],
 
            ['00000405','Scream 2',1997,'Gale Weathers',''],
 
            ['00000485','Scream 2',1997,'Casey','I Know What You Did Last Summer'],
 
            ['00000421','Scream 3',2000,'Cotton Weary',''],
 
            ['00000422','Scream 3',2000,'Female Caller',''],
 
            ['00000423','Scream 3',2000,'The Voice',''],
 
            ['00000424','Scream 3',2000,'Christine',''],
 
            ['00000404','Scream 3',2000,'Sidney Prescott','Scream 2'],
 
            ['00000405','Scream 3',2000,'Gale Weathers','Scream 2'],
 
            ['00000443','Traffic',2000,'Robert Wakefield',''],
 
            ['00000444','Traffic',2000,'Javier Rodriguez',''],
 
            ['00000445','Traffic',2000,'Helena Ayala','Entrapment'],
 
            ['00000446','Traffic',2000,'Carlos Ayala',''],
 
            ['00000447','Traffic',2000,'Ray Castro',''],
 
            ['00000448','Traffic',2000,'Barbara Wakefield',''],
 
            ['00000449','Traffic',2000,'Caroline Wakefield',''],
 
            ['00000450','Traffic',2000,'Montel Gordon',''],
 
            ['00000451','Traffic',2000,'Manolo Sanchez',''],
 
            ['00000452','Traffic',2000,'Francisco Flores',''],
 
            ['00000462','Psycho',1960,'Norman Bates',''],
 
            ['00000463','Psycho',1960,'Lila Crane',''],
 
            ['00000464','Psycho',1960,'Marion Crane',''],
 
            ['00000181','Psycho',1960,'Man in hat',''],
            ['00000465','Psycho',1960,'Sam Loomis',''],
            ['00000466','Psycho',1960,'Mother',''],
 
            ['00000483','I Know What You Did Last Summer',1997,'Julie James',''],
 
            ['00000485','I Know What You Did Last Summer',1997,'Helen Shivers','Scream 2'],
 
            ['00000484','I Know What You Did Last Summer',1997,'Barry Cox','Cruel Intentions'],
 
            ['00000484','Cruel Intentions',1999,'Sebastian Valmont','I Know What You Did Last Summer'],
 
            ['00000485','Cruel Intentions',1999,'Kathryn Merteuil','Scream 2'],
 
            ['00000503','Cruel Intentions',1999,'Annette Hargrove',''],
 
            ['00000504','Cruel Intentions',1999,'Cecile Caldwell',''],
 
            ['00001229','Wild Things',1998,'Ray Duquette','Apollo 13'],
 
            ['00000524','Wild Things',1998,'Sam Lombardo',''],
 
            ['00000404','Wild Things',1998,'Suzie Toller','Scream 2'],
 
            ['00000543','Alien',1979,'Captain',''],
 
            ['00000544','Alien',1979,'Warrent Officer','Aliens'],
 
            ['00000544','Aliens',1986,'Lieutenant','Alien'],
 
            ['00000561','Aliens',1986,'Rebecca',''],
 
            ['00000544','Alien 3',1992,'Ellen Ripley','Aliens'],
 
            ['00000583','Alien 3',1992,'Dillon',''],
 
            ['00000584','Alien 3',1992,'Clemens',''],
 
            ['00000544','Alien: Resurrection',1997,'Lieutenant Ellen','Aliens'],
 
            ['00001031','Alien: Resurrection',1997,'Betty Mechanic','Mermaids'],
 
            ['00000604','Alien: Resurrection',1997,'Betty Chief Mechanic',''],
 
            ['00000622','Gladiator',2000,'Maximus','The Insider'],
 
            ['00000623','Gladiator',2000,'Commodus',''],
 
            ['00000624','Gladiator',2000,'Lucilla',''],
 
            ['00000643','The World Is Not Enough',1999,'James Bond',''],
 
            ['00000644','The World Is Not Enough',1999,'CEO Elektra',''],
 
            ['00000645','The World Is Not Enough',1999,'Christmas',''],
 
            ['00000662','Heat',1995,'Vincent Hanna','The Insider'],
 
            ['00000663','Heat',1995,'Neil McCauley',''],
 
            ['00001017','Heat',1995,'Chris Shiherlis','Tombstone'],
 
            ['00000683','American History X',1998,'Derek Vinyard',''],
 
            ['00000684','American History X',1998,'Daniel Vinyard',''],
 
            ['00000685','American History X',1998,'Doris Vinyard',''],
 
            ['00000683','Fight Club',1999,'Narrator',''],
 
            ['00001198','Fight Club',1999,'Tyler Durden','Twelve Monkeys'],
 
            ['00000703','Fight Club',1999,'Robert Paulsen',''],
 
            ['00000722','Out of Sight',1998,'Jack Foley',''],
 
            ['00000723','Out of Sight',1998,'Bank Employee',''],
 
            ['00000724','Out of Sight',1998,'Karen Sisco',''],
 
            ['00000445','Entrapment',1999,'Virginia Baker','Traffic'],
 
            ['00000743','Entrapment',1999,'Robert Mac',''],
 
            ['00000744','Entrapment',1999,'Aaron Thibadeaux',''],
 
            ['00000762','The Insider',1999,'Liane Wigand',''],
 
            ['00000622','The Insider',1999,'Jeffrey Wigand','Gladiator'],
 
            ['00000662','The Insider',1999,'Lowell Bergman','Heat'],
 
            ['00000782','The Blair Witch Project',1999,'Heather Donahue',''],
 
            ['00000783','The Blair Witch Project',1999,'Josh',''],
 
            ['00000784','The Blair Witch Project',1999,'Mike',''],
 
            ['00000803','Lethal Weapon 4',1998,'Roger Murtaugh',''],
 
            ['00001183','Lethal Weapon 4',1998,'Lorna Cole','In the Line of Fire'],
 
            ['00000323','Lethal Weapon 4',1998,'Martin Riggs','Mad Max'],
 
            ['00000822','The Fifth Element',1997,'Korben Dallas','The Sixth Sense'],
 
            ['00000823','The Fifth Element',1997,'Zorg',''],
 
            ['00000824','The Fifth Element',1997,'Leeloo',''],
 
            ['00000822','The Sixth Sense',1999,'Dr.Malcolm Crowe','The Fifth Element'],
 
            ['00000842','The Sixth Sense',1999,'Cole Sear',''],
 
            ['00000843','The Sixth Sense',1999,'Lynn Sear',''],
 
            ['00000822','Unbreakable',2000,'David Dunn','The Sixth Sense'],
 
            ['00001276','Unbreakable',2000,'Audrey Dunn','Forrest Gump'],
 
            ['00000862','Unbreakable',2000,'Joseph Dunn',''],
 
            ['00000822','Armageddon',1998,'Harry S.Stamper','The Fifth Element'],
 
            ['00000883','Armageddon',1998,'Dan Truman',''],
 
            ['00000884','Armageddon',1998,'Grace Stamper',''],
 
            ['00000822','The Kid',2000,'Russ Duritz','Armageddon'],
 
            ['00000903','The Kid',2000,'Rusty Duritz',''],
 
            ['00000904','The Kid',2000,'Amy',''],
 
            ['00000822','Twelve Monkeys',1995,'James Cole','The Fifth Element'],
 
            ['00000923','Twelve Monkeys',1995,'Young Cole',''],
 
            ['00001198','Twelve Monkeys',1995,'Jeffrey Goines','Fight Club'],
 
            ['00001006','Bullets Over Broadway',1994,'David Shayne',''],
 
            ['00001007','Bullets Over Broadway',1994,'Julian Marx','While You Were Sleeping'],
 
            ['00001008','Bullets Over Broadway',1994,'Rocco',''],
 
            ['00001016','Tombstone',1993,'Kurt Russell',''],
 
            ['00001017','Tombstone',1993,'Val Kilmer','Heat'],
 
            ['00001018','Tombstone',1993,'Sam Elliott',''],
 
            ['00001024','Alice',1990,'Joe',''],
 
            ['00001025','Alice',1990,'Alice Tate',''],
 
            ['00001026','Alice',1990,'Doug Tate',''],
 
            ['00001029','Mermaids',1990,'Rachel Flax',''],
 
            ['00001030','Mermaids',1990,'Lou Landsky',''],
 
            ['00001031','Mermaids',1990,'Charlotte Flax','Little Women'],
 
            ['00001038','Exotica',1994,'Inspector',''],
 
            ['00001039','Exotica',1994,'Thomas Pinto',''],
 
            ['00001040','Exotica',1994,'Christina',''],
 
            ['00001045','Red Rock West',1992,'Michael Williams',''],
 
            ['00001046','Red Rock West',1992,'Jim',''],
 
            ['00001053','Chaplin',1992,'Charlie Chaplin',''],
 
            ['00001054','Chaplin',1992,'Hannah Chaplin',''],
 
            ['00001055','Chaplin',1992,'Sydney Chaplin',''],
 
            ['00001062','Fearless',1993,'Max Klein',''],
 
            ['00001063','Fearless',1993,'Laura Klein',''],
 
            ['00001064','Fearless',1993,'Carla Rodrigo',''],
 
            ['00001071','Threesome',1994,'Alex',''],
 
            ['00001072','Threesome',1994,'Stuart',''],
 
            ['00001073','Threesome',1994,'Eddy',''],
 
            ['00001080','Jungle Fever',1991,'Flipper Purify',''],
 
            ['00001081','Jungle Fever',1991,'Angie Tucci',''],
 
            ['00001088','Internal Affairs',1990,'Dennis Peck',''],
 
            ['00001089','Internal Affairs',1990,'Raymond Avila','Dead Again'],
 
            ['00001090','Internal Affairs',1990,'Kathleen Avila',''],
 
            ['00001098','Single White Female',1992,'Allison Jones',''],
 
            ['00001099','Single White Female',1992,'Hedra Carlson',''],
 
            ['00001100','Single White Female',1992,'Sam Rawson',''],
 
            ['00001105','Trust',1990,'Maria Coughlin',''],
 
            ['00001106','Trust',1990,'Matthew Slaughter','Amateur'],
 
            ['00001112','Ju Dou',1990,'Ju Dou','Daohong Denglong Gaogao Gua'],
 
            ['00001113','Ju Dou',1990,'Yang Tian-qing',''],
 
            ['00001112','Dahong Denglong Gaogao Gua',1991,'Songlian','Ju Dou'],
 
            ['00001120','Dahong Denglong Gaogao Gua',1991,'The Third Concubine',''],
 
            ['00001119','Dahong Denglong Gaogao Gua',1991,'The Master',''],
 
            ['00001125','Cyrano de Bergerac',1990,'Cyrano De Bergerac',''],
 
            ['00001126','Cyrano de Bergerac',1990,'Roxane',''],
 
            ['00001005','Manhattan Murder Mystery',1993,'Larry Lipton',''],
 
            ['00001131','Manhattan Murder Mystery',1993,'Carol Lipton','Hanging Up'],
 
            ['00001133','El Mariachi',1992,'El Mariachi',''],
 
            ['00001134','El Mariachi',1992,'Domino',''],
 
            ['00001137','Once Were Warriors',1994,'Beth Heke',''],
 
            ['00001138','Once Were Warriors',1994,'Jake Heke',''],
 
            ['00001145','Priest',1994,'Father Greg Pilkington',''],
 
            ['00001146','Priest',1994,'Father Matthew Thomas','Shakespeare in Love'],
 
            ['00001152','Pump Up the Volum',1990,'Mark Hunter',''],
 
            ['00001153','Pump Up the Volum',1990,'Nora Diniro','Little Women'],
 
            ['00001160','Benny and Joon',1993,'Sam',''],
 
            ['00001161','Benny and Joon',1993,'Juniper Pearl',''],
 
            ['00001167','Six Degrees of Separation',1993,'Ouisa Kittredge',''],
 
            ['00001168','Six Degrees of Separation',1993,'Paul',''],
 
            ['00001169','Six Degrees of Separation',1993,'John Flanders',''],
 
            ['00001175','Bawang Bie Ji',1993,'Cheng Dieyi',''],
 
            ['00001176','Bawang Bie Ji',1993,'Duan Xiaolou',''],
 
            ['00001112','Bawang Bie Ji',1993,'Juxian',''],
 
            ['00001181','In the Line of Fire',1993,'Secret Service Agent Frank Horrigan',''],
 
            ['00001182','In the Line of Fire',1993,'Mitch Leary',''],
 
            ['00001183','In the Line of Fire',1993,'Secret Service Agent Lilly Raines','Lethal Weapon 4'],
 
            ['00001187','Heavenly Creatures',1994,'Pauline Yvonne Rieper',''],
 
            ['00001188','Heavenly Creatures',1994,'Juliet Marion Hulme','Titanic'],
 
            ['00001192','Hoop Dreams',1994,'Himself',''],
 
            ['00001193','Hoop Dreams',1994,'Arthur',''],
 
            ['00001197','Seven',1995,'Detective William Somerset',''],
 
            ['00001198','Seven',1995,'Detective David Mills','Legends of the Fall'],
 
            ['00001204','Shallow Grave',1994,'Juliet Miller',''],
 
            ['00001205','Shallow Grave',1994,'David Stephens',''],
 
            ['00001206','Shallow Grave',1994,'Alex Law',''],
 
            ['00001212','French Kiss',1995,'Kate','You have Got Mail'],
 
            ['00001213','French Kiss',1995,'Luc Teyssier',''],
 
            ['00001214','French Kiss',1995,'Charlie',''],
 
            ['00001217','Braindead',1992,'Lionel Cosgrove',''],
 
            ['00001218','Braindead',1992,'Paquita Maria Sanchez',''],
 
            ['00001219','Braindead',1992,'Mum',''],
 
            ['00001186','Braindead',1992,'Undertaker Assistant',''],
 
            ['00001222','Clerks',1994,'Veronica Loughran',''],
 
            ['00001223','Clerks',1994,'Caitlin Bree',''],
 
            ['00001227','Apollo 13',1995,'Jim Lovell','Forrest Gump'],
 
            ['00001228','Apollo 13',1995,'Fred Haise',''],
 
            ['00001229','Apollo 13',1995,'Jack Swigert','Wild Things'],
 
            ['00001233','Reservoir Dogs',1992,'Larry','Pulp Fiction'],
 
            ['00001234','Reservoir Dogs',1992,'Freddy',''],
 
            ['00001235','Reservoir Dogs',1992,'Vic',''],
 
            ['00001238','Pulp Fiction',1994,'Vincent Vega',''],
 
            ['00001239','Pulp Fiction',1994,'Jules Winnfield',''],
 
            ['00001233','Pulp Fiction',1994,'Winston Wolf','Reservoir Dogs'],
 
            ['00001242','Yinshi Nan Nu',1994,'Chu',''],
 
            ['00001243','Yinshi Nan Nu',1994,'Jia-Ning',''],
 
            ['00001244','Yinshi Nan Nu',1994,'Jia-Chien',''],
 
            ['00001249','Short Cuts',1993,'Ann Finnigan',''],
 
            ['00001250','Short Cuts',1993,'Howard Finnigan',''],
 
            ['00001251','Short Cuts',1993,'Paul Finnigan',''],
 
            ['00001198','Legends of the Fall',1994,'Tristan Ludlow','Seven'],
 
            ['00001256','Legends of the Fall',1994,'Colonel William Ludlow','Shadowlands'],
 
            ['00001257','Legends of the Fall',1994,'Alfred Ludlow',''],
 
            ['00001262','Natural Born Killers',1994,'Mickey Knox',''],
 
            ['00001263','Natural Born Killers',1994,'Mallory Wilson Knox',''],
 
            ['00001264','Natural Born Killers',1994,'Wayne Gale',''],
 
            ['00001269','In the Mouth of Madness',1995,'John Trent','Jurassic Park'],
 
            ['00001270','In the Mouth of Madness',1995,'Sutter Cane',''],
 
            ['00001271','In the Mouth of Madness',1995,'Linda Styles',''],
 
            ['00001227','Forrest Gump',1994,'Forrest Gump','Apollo 13'],
 
            ['00001276','Forrest Gump',1994,'Jenny Curran','Unbreakable'],
 
            ['00001277','Forrest Gump',1994,'Lieutenant Daniel Taylor',''],
 
            ['00001281','Malcolm X',1992,'Malcolm X',''],
 
            ['00001282','Malcolm X',1992,'Betty Shabazz',''],
 
            ['00001079','Malcolm X',1992,'Shorty',''],
 
            ['00001284','Dead Again',1991,'Mike Church',''],
 
            ['00001089','Dead Again',1991,'Gray Baker','Internal Affaris'],
 
            ['00001286','Dead Again',1991,'Margaret Strauss',''],
 
            ['00001269','Jurassic Park',1993,'Alan Grant','In the Mouth of Madness'],
 
            ['00001293','Jurassic Park',1993,'Ellie Sattler',''],
 
            ['00001294','Jurassic Park',1993,'Ian Malcolm',''],
 
            ['00001051','Jurassic Park',1993,'John Parker Hammond',''],
 
            ['00001298','Clueless',1995,'Cher Horowitz',''],
 
            ['00001299','Clueless',1995,'Dionne',''],
 
            ['00001300','Clueless',1995,'Tai Fraiser',''],
 
            ['00001256','Shadowlands',1993,'Lewis','Legends of the Fall'],
 
            ['00001307','Shadowlands',1993,'Joy Gresham',''],
 
            ['00001308','Shadowlands',1993,'Arnold Dopliss',''],
 
            ['00001312','Amateur',1994,'Isabelle',''],
 
            ['00001106','Amateur',1994,'Thomas Ludens','Trust'],
 
            ['00001313','Amateur',1994,'Sofia Ludens',''],
 
            ['00001318','GoodFellas',1990,'James',''],
 
            ['00001319','GoodFellas',1990,'Henry Hill',''],
 
            ['00001320','GoodFellas',1990,'Tommy DeVito',''],
 
            ['00001031','Little Women',1994,'Josephine','Mermaids'],
 
            ['00001326','Little Women',1994,'Friedrich',''],
 
            ['00001327','Little Women',1994,'Margaret',''],
 
            ['00001153','Little Women',1994,'Older Amy March','Pump Up the Volum'],
 
            ['00001333','While You Were Sleeping',1995,'Narrator',''],
 
            ['00001334','While You Were Sleeping',1995,'Jack Callaghan',''],
 
            ['00001007','While You Were Sleeping',1995,'Saul','Bullets Over Broadway']]