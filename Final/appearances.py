# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:44:10 2020

@author: 45242
"""


appearances = [['Psycho',1960,'Lila Crane',1],

    ['Psycho',1960,'Marion Crane',1],

    ['Psycho',1960,'Sam Loomis',1],

    ['Psycho',1960,'Lila Crane',2],

    ['Psycho',1960,'Lila Crane',3],

    ['Psycho',1960,'Marion Crane',3],

    ['Psycho',1960,'Man in hat',3],

    ['Psycho',1960,'Norman Bates',4],

    ['Psycho',1960,'Lila Crane',4],

    ['Psycho',1960,'Norman Bates',5],

    ['Psycho',1960,'Mother',5],

    ['Psycho',1960,'Norman Bates',6],

    ['Psycho',1960,'Lila Crane',6],

    ['Psycho',1960,'Norman Bates',7],

    ['Psycho',1960,'Sam Loomis',7],

    ['Psycho',1960,'Marion Crane',7],

    ['Psycho',1960,'Lila Crane',7],

    ['Psycho',1960,'Norman Bates',8],

    ['Psycho',1960,'Mother',8],

    ['The Birds',1963,'Mitch Brenner',1],

    ['The Birds',1963,'Melanie Daniels',1],

    ['The Birds',1963,'Mitch Brenner',2],

    ['The Birds',1963,'Man in pet shop',2],

    ['The Birds',1963,'Annie Hayworth',3],

    ['The Birds',1963,'Melanie Daniels',3],

    ['The Birds',1963,'Mitch Brenner',4],

    ['The Birds',1963,'Lydia Brenner',4],

    ['The Birds',1963,'Melanie Daniels',4],

    ['The Birds',1963,'Mitch Brenner',5],

    ['The Birds',1963,'Annie Hayworth',5],

    ['The Birds',1963,'Melanie Daniels',5],

    ['The Birds',1963,'Mitch Brenner',6],

    ['The Birds',1963,'Annie Hayworth',6],

    ['The Birds',1963,'Melanie Daniels',6],

    ['The Birds',1963,'Lydia Brenner',6],

    ['The Birds',1963,'Mitch Brenner',7],

    ['The Birds',1963,'Melanie Daniels',7],

    ['The Birds',1963,'Lydia Brenner',7],

    ['The Birds',1963,'Mitch Brenner',8],

    ['The Birds',1963,'Melanie Daniels',8],

    ['The Birds',1963,'Lydia Brenner',8],

    ['Rear Window',1954,'L.B. Jeff Jefferies',1],

    ['Rear Window',1954,'L.B. Jeff Jefferies',2],

    ['Rear Window',1954,'Lisa Carol Fremont',2],

    ['Rear Window',1954,'Lisa Carol Fremont',3],

    ['Rear Window',1954,'Clock-Winding Man',3],

    ['Rear Window',1954,'Lisa Carol Fremont',4],

    ['Rear Window',1954,'Lars Thorwald',4],

    ['Rear Window',1954,'L.B. Jeff Jefferies',4],

    ['Rear Window',1954,'L.B. Jeff Jefferies',5],

    ['Rear Window',1954,'Lars Thorwald',5],

    ['Rear Window',1954,'Lisa Carol Fremont',6],

    ['Rear Window',1954,'Lars Thorwald',6],

    ['Rear Window',1954,'L.B. Jeff Jefferies',7],

    ['Rear Window',1954,'Lars Thorwald',7],

    ['Rear Window',1954,'L.B. Jeff Jefferies',8],

    ['Rear Window',1954,'Lisa Carol Fremont',8],

    ['Traffic',2000,'Javier Rodriguez',1],

    ['Traffic',2000,'Manolo Sanchez',1],

    ['Traffic',2000,'Robert Wakefield',2],

    ['Traffic',2000,'Barbara Wakefield',2],

    ['Traffic',2000,'Caroline Wakefield',3],

    ['Traffic',2000,'Montel Gordon',4],

    ['Traffic',2000,'Ray Castro',4],

    ['Traffic',2000,'Carlos Ayala',4],

    ['Traffic',2000,'Helena Ayala',4],

    ['Traffic',2000,'Manolo Sanchez',5],

    ['Traffic',2000,'Ray Castro',5],

    ['Traffic',2000,'Javier Rodriguez',5],

    ['Traffic',2000,'Montel Gordon',5],

    ['Traffic',2000,'Robert Wakefield',6],

    ['Traffic',2000,'Barbara Wakefield',6],

    ['Traffic',2000,'Caroline Wakefield',6],

    ['Traffic',2000,'Francisco Flores',6],

    ['Traffic',2000,'Montel Gordon',6],

    ['Traffic',2000,'Helena Ayala',7],

    ['Traffic',2000,'Javier Rodriguez',7],

    ['Traffic',2000,'Manolo Sanchez',7],

    ['Traffic',2000,'Francisco Flores',7],

    ['Traffic',2000,'Javier Rodriguez',8],

    ['Traffic',2000,'Manolo Sanchez',8],

    ['Traffic',2000,'Robert Wakefield',8],

    ['Traffic',2000,'Barbara Wakefield',8],

    ['Traffic',2000,'Francisco Flores',9],

    ['Traffic',2000,'Robert Wakefield',9],

    ['Traffic',2000,'Montel Gordon',9],

    ['Traffic',2000,'Carlos Ayala',9],

    ['Traffic',2000,'Robert Wakefield',10],

    ['Traffic',2000,'Barbara Wakefield',10],

    ['Traffic',2000,'Caroline Wakefield',10],

    ['Traffic',2000,'Carlos Ayala',10],

    ['Traffic',2000,'Montel Gordon',10],

    ['Traffic',2000,'Manolo Sanchez',10],

    ['Traffic',2000,'Francisco Flores',10],

    ['Traffic',2000,'Carlos Ayala',11],

    ['Traffic',2000,'Helena Ayala',11],

    ['Traffic',2000,'Montel Gordon',11],

    ['Bullets Over Broadway',1994,'David Shayne',1],

    ['Bullets Over Broadway',1994,'Julian Marx',1],

    ['Bullets Over Broadway',1994,'Rocco',1],

    ['Bullets Over Broadway',1994,'David Shayne',2],

    ['Bullets Over Broadway',1994,'David Shayne',3],

    ['Bullets Over Broadway',1994,'Julian Marx',3],

    ['Bullets Over Broadway',1994,'Rocco',3],

    ['Bullets Over Broadway',1994,'Rocco',4],

    ['Bullets Over Broadway',1994,'Julian Marx',4],

    ['Bullets Over Broadway',1994,'Rocco',5],

    ['Bullets Over Broadway',1994,'David Shayne',6],

    ['Bullets Over Broadway',1994,'Julian Marx',6],

    ['Tombstone',1993,'Kurt Russell',1],

    ['Tombstone',1993,'Val Kilmer',1],

    ['Tombstone',1993,'Kurt Russell',2],

    ['Tombstone',1993,'Kurt Russell',3],

    ['Tombstone',1993,'Val Kilmer',3],

    ['Tombstone',1993,'Sam Elliott',3],

    ['Tombstone',1993,'Val Kilmer',4],

    ['Tombstone',1993,'Sam Elliott',5],

    ['Tombstone',1993,'Kurt Russell',5],

    ['Tombstone',1993,'Kurt Russell',6],

    ['Tombstone',1993,'Sam Elliott',6],

    ['Alice',1990,'Joe',1],

    ['Alice',1990,'Alice Tate',2],

    ['Alice',1990,'Doug Tate',2],

    ['Alice',1990,'Joe',3],

    ['Alice',1990,'Alice Tate',3],

    ['Alice',1990,'Joe',4],

    ['Alice',1990,'Doug Tate',4],

    ['Alice',1990,'Alice Tate',5],

    ['Alice',1990,'Doug Tate',5],

    ['Alice',1990,'Joe',6],

    ['Alice',1990,'Alice Tate',7],

    ['Alice',1990,'Joe',8],

    ['Mermaids',1990,'Rachel Flax',1],

    ['Mermaids',1990,'Lou Landsky',1],

    ['Mermaids',1990,'Lou Landsky',2],

    ['Mermaids',1990,'Charlotte Flax',2],

    ['Mermaids',1990,'Rachel Flax',3],

    ['Mermaids',1990,'Lou Landsky',3],

    ['Mermaids',1990,'Charlotte Flax',3],

    ['Mermaids',1990,'Rachel Flax',4],

    ['Mermaids',1990,'Lou Landsky',4],

    ['Mermaids',1990,'Rachel Flax',5],

    ['Exotica',1994,'Inspector',1],

    ['Exotica',1994,'Thomas Pinto',1],

    ['Exotica',1994,'Inspector',2],

    ['Exotica',1994,'Inspector',3],

    ['Exotica',1994,'Thomas Pinto',3],

    ['Exotica',1994,'Christina',3],

    ['Exotica',1994,'Thomas Pinto',4],

    ['Exotica',1994,'Inspector',5],

    ['Exotica',1994,'Christina',5],

    ['Exotica',1994,'Christina',6],

    ['Exotica',1994,'Inspector',7],

    ['Exotica',1994,'Thomas Pinto',8],

    ['Red Rock West',1992,'Michael Williams',1],

    ['Red Rock West',1992,'Michael Williams',2],

    ['Red Rock West',1992,'Jim',2],

    ['Red Rock West',1992,'Michael Williams',3],

    ['Red Rock West',1992,'Jim',3],

    ['Red Rock West',1992,'Jim',4],

    ['Red Rock West',1992,'Michael Williams',5],

    ['Red Rock West',1992,'Jim',5],

    ['Red Rock West',1992,'Jim',6],

    ['Red Rock West',1992,'Michael Williams',7],

    ['Red Rock West',1992,'Michael Williams',8],

    ['Red Rock West',1992,'Jim',8],

    ['Chaplin',1992,'Charlie Chaplin',1],

    ['Chaplin',1992,'Hannah Chaplin',1],

    ['Chaplin',1992,'Sydney Chaplin',1],

    ['Chaplin',1992,'Hannah Chaplin',2],

    ['Chaplin',1992,'Charlie Chaplin',3],

    ['Chaplin',1992,'Sydney Chaplin',3],

    ['Chaplin',1992,'Charlie Chaplin',4],

    ['Chaplin',1992,'Hannah Chaplin',4],

    ['Chaplin',1992,'Sydney Chaplin',5],

    ['Chaplin',1992,'Charlie Chaplin',6],

    ['Chaplin',1992,'Hannah Chaplin',6],

    ['Fearless',1993,'Max Klein',1],

    ['Fearless',1993,'Laura Klein',2],

    ['Fearless',1993,'Max Klein',3],

    ['Fearless',1993,'Max Klein',4],

    ['Fearless',1993,'Laura Klein',4],

    ['Fearless',1993,'Laura Klein',5],

    ['Fearless',1993,'Carla Rodrigo',5],

    ['Fearless',1993,'Max Klein',6],

    ['Fearless',1993,'Laura Klein',7],

    ['Fearless',1993,'Carla Rodrigo',8],

    ['Fearless',1993,'Max Klein',9],

    ['Fearless',1993,'Laura Klein',10],

    ['Fearless',1993,'Max Klein',11],

    ['Threesome',1994,'Alex',1],

    ['Threesome',1994,'Stuart',1],

    ['Threesome',1994,'Stuart',2],

    ['Threesome',1994,'Eddy',2],

    ['Threesome',1994,'Alex',3],

    ['Threesome',1994,'Stuart',3],

    ['Threesome',1994,'Alex',4],

    ['Threesome',1994,'Stuart',5],

    ['Threesome',1994,'Eddy',5],

    ['Threesome',1994,'Alex',6],

    ['Threesome',1994,'Stuart',7],

    ['Threesome',1994,'Alex',8],

    ['Jungle Fever',1991,'Flipper Purify',1],

    ['Jungle Fever',1991,'Flipper Purify',2],

    ['Jungle Fever',1991,'Angie Tucci',2],

    ['Jungle Fever',1991,'Flipper Purify',3],

    ['Jungle Fever',1991,'Angie Tucci',3],

    ['Jungle Fever',1991,'Flipper Purify',4],

    ['Jungle Fever',1991,'Angie Tucci',4],

    ['Jungle Fever',1991,'Flipper Purify',5],

    ['Jungle Fever',1991,'Angie Tucci',6],

    ['Jungle Fever',1991,'Flipper Purify',7],

    ['Jungle Fever',1991,'Angie Tucci',8],

    ['Internal Affairs',1990,'Dennis Peck',1],

    ['Internal Affairs',1990,'Raymond Avila',1],

    ['Internal Affairs',1990,'Kathleen Avila',1],

    ['Internal Affairs',1990,'Dennis Peck',2],

    ['Internal Affairs',1990,'Raymond Avila',2],

    ['Internal Affairs',1990,'Raymond Avila',3],

    ['Internal Affairs',1990,'Kathleen Avila',3],

    ['Internal Affairs',1990,'Dennis Peck',4],

    ['Internal Affairs',1990,'Raymond Avila',5],

    ['Internal Affairs',1990,'Kathleen Avila',5],

    ['Internal Affairs',1990,'Dennis Peck',6],

    ['Internal Affairs',1990,'Kathleen Avila',6],

    ['Single White Female',1992,'Allison Jones',1],

    ['Single White Female',1992,'Hedra Carlson',2],

    ['Single White Female',1992,'Allison Jones',3],

    ['Single White Female',1992,'Allison Jones',4],

    ['Single White Female',1992,'Hedra Carlson',4],

    ['Single White Female',1992,'Sam Rawson',5],

    ['Single White Female',1992,'Allison Jones',6],

    ['Single White Female',1992,'Sam Rawson',6],

    ['Single White Female',1992,'Sam Rawson',7],

    ['Single White Female',1992,'Allison Jones',8],

    ['Single White Female',1992,'Hedra Carlson',8],

    ['Single White Female',1992,'Allison Jones',9],

    ['Trust',1990,'Maria Coughlin',1],

    ['Trust',1990,'Matthew Slaughter',1],

    ['Trust',1990,'Maria Coughlin',2],

    ['Trust',1990,'Matthew Slaughter',2],

    ['Trust',1990,'Maria Coughlin',3],

    ['Trust',1990,'Matthew Slaughter',3],

    ['Trust',1990,'Matthew Slaughter',4],

    ['Trust',1990,'Maria Coughlin',5],

    ['Trust',1990,'Matthew Slaughter',5],

    ['Trust',1990,'Maria Coughlin',6],

    ['Ju Dou',1990,'Ju Dou',1],

    ['Ju Dou',1990,'Yang Tian-qing',1],

    ['Ju Dou',1990,'Ju Dou',2],

    ['Ju Dou',1990,'Yang Tian-qing',2],

    ['Ju Dou',1990,'Ju Dou',3],

    ['Ju Dou',1990,'Yang Tian-qing',3],

    ['Ju Dou',1990,'Ju Dou',4],

    ['Ju Dou',1990,'Yang Tian-qing',4],

    ['Ju Dou',1990,'Ju Dou',5],

    ['Ju Dou',1990,'Yang Tian-qing',5],

    ['Ju Dou',1990,'Ju Dou',6],

    ['Ju Dou',1990,'Yang Tian-qing',7],

    ['Dahong Denglong Gaogao Gua',1991,'Songlian',1],

    ['Dahong Denglong Gaogao Gua',1991,'The Master',1],

    ['Dahong Denglong Gaogao Gua',1991,'The Third Concubine',2],

    ['Dahong Denglong Gaogao Gua',1991,'The Master',2],

    ['Dahong Denglong Gaogao Gua',1991,'Songlian',3],

    ['Dahong Denglong Gaogao Gua',1991,'The Third Concubine',3],

    ['Dahong Denglong Gaogao Gua',1991,'Songlian',4],

    ['Dahong Denglong Gaogao Gua',1991,'Songlian',5],

    ['Dahong Denglong Gaogao Gua',1991,'The Third Concubine',5],

    ['Dahong Denglong Gaogao Gua',1991,'Songlian',6],

    ['Dahong Denglong Gaogao Gua',1991,'The Master',6],

    ['Cyrano de Bergerac',1990,'Cyrano De Bergerac',1],

    ['Cyrano de Bergerac',1990,'Roxane',1],

    ['Cyrano de Bergerac',1990,'Cyrano De Bergerac',2],

    ['Cyrano de Bergerac',1990,'Roxane',2],

    ['Cyrano de Bergerac',1990,'Cyrano De Bergerac',3],

    ['Cyrano de Bergerac',1990,'Cyrano De Bergerac',4],

    ['Cyrano de Bergerac',1990,'Roxane',4],

    ['Cyrano de Bergerac',1990,'Cyrano De Bergerac',5],

    ['Cyrano de Bergerac',1990,'Roxane',5],

    ['Manhattan Murder Mystery',1993,'Larry Lipton',1],

    ['Manhattan Murder Mystery',1993,'Larry Lipton',2],

    ['Manhattan Murder Mystery',1993,'Carol Lipton',2],

    ['Manhattan Murder Mystery',1993,'Larry Lipton',3],

    ['Manhattan Murder Mystery',1993,'Carol Lipton',3],

    ['Manhattan Murder Mystery',1993,'Larry Lipton',4],

    ['Manhattan Murder Mystery',1993,'Carol Lipton',4],

    ['Manhattan Murder Mystery',1993,'Larry Lipton',5],

    ['Manhattan Murder Mystery',1993,'Carol Lipton',6],

    ['Manhattan Murder Mystery',1993,'Larry Lipton',7],

    ['Manhattan Murder Mystery',1993,'Larry Lipton',8],

    ['Manhattan Murder Mystery',1993,'Carol Lipton',8],

    ['El Mariachi',1992,'El Mariachi',1],

    ['El Mariachi',1992,'Domino',1],

    ['El Mariachi',1992,'El Mariachi',2],

    ['El Mariachi',1992,'El Mariachi',3],

    ['El Mariachi',1992,'Domino',3],

    ['El Mariachi',1992,'Domino',4],

    ['El Mariachi',1992,'El Mariachi',5],

    ['El Mariachi',1992,'El Mariachi',6],

    ['El Mariachi',1992,'Domino',6],

    ['El Mariachi',1992,'Domino',7],

    ['El Mariachi',1992,'El Mariachi',8],

    ['El Mariachi',1992,'Domino',9],

    ['El Mariachi',1992,'El Mariachi',10],

    ['El Mariachi',1992,'Domino',10],

    ['Once Were Warriors',1994,'Beth Heke',1],

    ['Once Were Warriors',1994,'Jake Heke',1],

    ['Once Were Warriors',1994,'Beth Heke',2],

    ['Once Were Warriors',1994,'Jake Heke',2],

    ['Once Were Warriors',1994,'Beth Heke',3],

    ['Once Were Warriors',1994,'Jake Heke',3],

    ['Once Were Warriors',1994,'Jake Heke',4],

    ['Once Were Warriors',1994,'Beth Heke',5],

    ['Once Were Warriors',1994,'Jake Heke',5],

    ['Once Were Warriors',1994,'Beth Heke',6],

    ['Once Were Warriors',1994,'Jake Heke',6],

    ['Priest',1994,'Father Greg Pilkington',1],

    ['Priest',1994,'Father Matthew Thomas',2],

    ['Priest',1994,'Father Greg Pilkington',3],

    ['Priest',1994,'Father Matthew Thomas',3],

    ['Priest',1994,'Father Greg Pilkington',4],

    ['Priest',1994,'Father Greg Pilkington',5],

    ['Priest',1994,'Father Matthew Thomas',5],

    ['Priest',1994,'Father Matthew Thomas',6],

    ['Priest',1994,'Father Greg Pilkington',7],

    ['Priest',1994,'Father Matthew Thomas',7],

    ['Priest',1994,'Father Greg Pilkington',8],

    ['Pump Up the Volum',1990,'Mark Hunter',1],

    ['Pump Up the Volum',1990,'Nora Diniro',1],

    ['Pump Up the Volum',1990,'Mark Hunter',2],

    ['Pump Up the Volum',1990,'Nora Diniro',2],

    ['Pump Up the Volum',1990,'Mark Hunter',3],

    ['Pump Up the Volum',1990,'Nora Diniro',3],

    ['Pump Up the Volum',1990,'Mark Hunter',4],

    ['Pump Up the Volum',1990,'Nora Diniro',4],

    ['Pump Up the Volum',1990,'Mark Hunter',5],

    ['Pump Up the Volum',1990,'Nora Diniro',5],

    ['Pump Up the Volum',1990,'Mark Hunter',6],

    ['Benny and Joon',1993,'Sam',1],

    ['Benny and Joon',1993,'Juniper Pearl',1],

    ['Benny and Joon',1993,'Sam',2],

    ['Benny and Joon',1993,'Juniper Pearl',2],

    ['Benny and Joon',1993,'Sam',3],

    ['Benny and Joon',1993,'Juniper Pearl',3],

    ['Benny and Joon',1993,'Sam',4],

    ['Benny and Joon',1993,'Juniper Pearl',4],

    ['Benny and Joon',1993,'Sam',5],

    ['Benny and Joon',1993,'Juniper Pearl',5],

    ['Six Degrees of Separation',1993,'Ouisa Kittredge',1],

    ['Six Degrees of Separation',1993,'Paul',1],

    ['Six Degrees of Separation',1993,'John Flanders',2],

    ['Six Degrees of Separation',1993,'Ouisa Kittredge',3],

    ['Six Degrees of Separation',1993,'Paul',3],

    ['Six Degrees of Separation',1993,'John Flanders',3],

    ['Six Degrees of Separation',1993,'Ouisa Kittredge',4],

    ['Six Degrees of Separation',1993,'Paul',4],

    ['Six Degrees of Separation',1993,'John Flanders',4],

    ['Six Degrees of Separation',1993,'Ouisa Kittredge',5],

    ['Six Degrees of Separation',1993,'Paul',5],

    ['Bawang Bie Ji',1993,'Cheng Dieyi',1],

    ['Bawang Bie Ji',1993,'Duan Xiaolou',2],

    ['Bawang Bie Ji',1993,'Cheng Dieyi',3],

    ['Bawang Bie Ji',1993,'Duan Xiaolou',3],

    ['Bawang Bie Ji',1993,'Cheng Dieyi',4],

    ['Bawang Bie Ji',1993,'Juxian',4],

    ['Bawang Bie Ji',1993,'Duan Xiaolou',5],

    ['Bawang Bie Ji',1993,'Juxian',5],

    ['Bawang Bie Ji',1993,'Cheng Dieyi',6],

    ['Bawang Bie Ji',1993,'Duan Xiaolou',6],

    ['Bawang Bie Ji',1993,'Juxian',7],

    ['Bawang Bie Ji',1993,'Cheng Dieyi',8],

    ['In the Line of Fire',1993,'Secret Service Agent Frank Horrigan',1],

    ['In the Line of Fire',1993,'Mitch Leary',1],

    ['In the Line of Fire',1993,'Secret Service Agent Lilly Raines',1],

    ['In the Line of Fire',1993,'Secret Service Agent Frank Horrigan',2],

    ['In the Line of Fire',1993,'Secret Service Agent Lilly Raines',2],

    ['In the Line of Fire',1993,'Mitch Leary',3],

    ['In the Line of Fire',1993,'Secret Service Agent Frank Horrigan',4],

    ['In the Line of Fire',1993,'Secret Service Agent Lilly Raines',4],

    ['In the Line of Fire',1993,'Secret Service Agent Frank Horrigan',5],

    ['In the Line of Fire',1993,'Mitch Leary',5],

    ['In the Line of Fire',1993,'Secret Service Agent Lilly Raines',5],

    ['Heavenly Creatures',1994,'Pauline Yvonne Rieper',1],

    ['Heavenly Creatures',1994,'Juliet Marion Hulme',1],

    ['Heavenly Creatures',1994,'Pauline Yvonne Rieper',2],

    ['Heavenly Creatures',1994,'Juliet Marion Hulme',2],

    ['Heavenly Creatures',1994,'Pauline Yvonne Rieper',3],

    ['Heavenly Creatures',1994,'Juliet Marion Hulme',3],

    ['Heavenly Creatures',1994,'Pauline Yvonne Rieper',4],

    ['Heavenly Creatures',1994,'Juliet Marion Hulme',4],

    ['Heavenly Creatures',1994,'Pauline Yvonne Rieper',5],

    ['Heavenly Creatures',1994,'Pauline Yvonne Rieper',6],

    ['Heavenly Creatures',1994,'Juliet Marion Hulme',6],

    ['Hoop Dreams',1994,'Himself',1],

    ['Hoop Dreams',1994,'Himself',2],

    ['Hoop Dreams',1994,'Himself',3],

    ['Hoop Dreams',1994,'Himself',4],

    ['Hoop Dreams',1994,'Himself',5],

    ['Seven',1995,'Detective William Somerset',1],

    ['Seven',1995,'Detective William Somerset',2],

    ['Seven',1995,'Detective David Mills',2],

    ['Seven',1995,'Detective William Somerset',3],

    ['Seven',1995,'Detective David Mills',3],

    ['Seven',1995,'Detective William Somerset',4],

    ['Seven',1995,'Detective David Mills',4],

    ['Seven',1995,'Detective William Somerset',5],

    ['Seven',1995,'Detective David Mills',5],

    ['Seven',1995,'Detective David Mills',6],

    ['Seven',1995,'Detective William Somerset',7],

    ['Seven',1995,'Detective David Mills',7],

    ['Shallow Grave',1994,'Juliet Miller',1],

    ['Shallow Grave',1994,'David Stephens',1],

    ['Shallow Grave',1994,'Alex Law',1],

    ['Shallow Grave',1994,'Juliet Miller',2],

    ['Shallow Grave',1994,'David Stephens',2],

    ['Shallow Grave',1994,'Alex Law',2],

    ['Shallow Grave',1994,'David Stephens',3],

    ['Shallow Grave',1994,'Juliet Miller',4],

    ['Shallow Grave',1994,'David Stephens',5],

    ['Shallow Grave',1994,'Alex Law',5],

    ['Shallow Grave',1994,'Juliet Miller',6],

    ['Shallow Grave',1994,'David Stephens',6],

    ['French Kiss',1995,'Kate',1],

    ['French Kiss',1995,'Luc Teyssier',1],

    ['French Kiss',1995,'Kate',2],

    ['French Kiss',1995,'Luc Teyssier',2],

    ['French Kiss',1995,'Luc Teyssier',3],

    ['French Kiss',1995,'Charlie',3],

    ['French Kiss',1995,'Kate',4],

    ['French Kiss',1995,'Luc Teyssier',4],

    ['French Kiss',1995,'Charlie',5],

    ['French Kiss',1995,'Kate',6],

    ['French Kiss',1995,'Luc Teyssier',6],

    ['Braindead',1992,'Lionel Cosgrove',1],

    ['Braindead',1992,'Paquita Maria Sanchez',2],

    ['Braindead',1992,'Mum',2],

    ['Braindead',1992,'Lionel Cosgrove',3],

    ['Braindead',1992,'Paquita Maria Sanchez',4],

    ['Braindead',1992,'Mum',4],

    ['Braindead',1992,'Undertaker Assistant',5],

    ['Braindead',1992,'Lionel Cosgrove',6],

    ['Braindead',1992,'Paquita Maria Sanchez',6],

    ['Braindead',1992,'Undertaker Assistant',7],

    ['Braindead',1992,'Undertaker Assistant',8],

    ['Braindead',1992,'Mum',9],

    ['Clerks',1994,'Veronica Loughran',1],

    ['Clerks',1994,'Caitlin Bree',1],

    ['Clerks',1994,'Veronica Loughran',2],

    ['Clerks',1994,'Veronica Loughran',3],

    ['Clerks',1994,'Caitlin Bree',3],

    ['Clerks',1994,'Veronica Loughran',4],

    ['Clerks',1994,'Caitlin Bree',4],

    ['Clerks',1994,'Veronica Loughran',5],

    ['Clerks',1994,'Caitlin Bree',5],

    ['Clerks',1994,'Caitlin Bree',6],

    ['Clerks',1994,'Veronica Loughran',7],

    ['Clerks',1994,'Caitlin Bree',8],

    ['Apollo 13',1995,'Jim Lovell',1],

    ['Apollo 13',1995,'Fred Haise',2],

    ['Apollo 13',1995,'Jack Swigert',2],

    ['Apollo 13',1995,'Jim Lovell',3],

    ['Apollo 13',1995,'Fred Haise',4],

    ['Apollo 13',1995,'Jack Swigert',4],

    ['Apollo 13',1995,'Jim Lovell',5],

    ['Apollo 13',1995,'Fred Haise',6],

    ['Apollo 13',1995,'Jim Lovell',7],

    ['Apollo 13',1995,'Jack Swigert',8],

    ['Apollo 13',1995,'Jim Lovell',9],

    ['Apollo 13',1995,'Fred Haise',9],

    ['Apollo 13',1995,'Jack Swigert',10],

    ['Reservoir Dogs',1992,'Larry',1],

    ['Reservoir Dogs',1992,'Freddy',2],

    ['Reservoir Dogs',1992,'Larry',3],

    ['Reservoir Dogs',1992,'Vic',3],

    ['Reservoir Dogs',1992,'Freddy',4],

    ['Reservoir Dogs',1992,'Vic',4],

    ['Reservoir Dogs',1992,'Larry',5],

    ['Reservoir Dogs',1992,'Freddy',6],

    ['Reservoir Dogs',1992,'Vic',6],

    ['Pulp Fiction',1994,'Vincent Vega',1],

    ['Pulp Fiction',1994,'Jules Winnfield',1],

    ['Pulp Fiction',1994,'Vincent Vega',2],

    ['Pulp Fiction',1994,'Jules Winnfield',3],

    ['Pulp Fiction',1994,'Winston Wolf',3],

    ['Pulp Fiction',1994,'Vincent Vega',4],

    ['Pulp Fiction',1994,'Jules Winnfield',5],

    ['Pulp Fiction',1994,'Vincent Vega',6],

    ['Pulp Fiction',1994,'Vincent Vega',7],

    ['Pulp Fiction',1994,'Winston Wolf',7],

    ['Pulp Fiction',1994,'Winston Wolf',8],

    ['Pulp Fiction',1994,'Jules Winnfield',9],

    ['Yinshi Nan Nu',1994,'Chu',1],

    ['Yinshi Nan Nu',1994,'Jia-Ning',2],

    ['Yinshi Nan Nu',1994,'Jia-Chien',2],

    ['Yinshi Nan Nu',1994,'Chu',3],

    ['Yinshi Nan Nu',1994,'Jia-Chien',3],

    ['Yinshi Nan Nu',1994,'Chu',4],

    ['Yinshi Nan Nu',1994,'Jia-Chien',4],

    ['Yinshi Nan Nu',1994,'Chu',5],

    ['Yinshi Nan Nu',1994,'Jia-Ning',5],

    ['Yinshi Nan Nu',1994,'Jia-Chien',5],

    ['Yinshi Nan Nu',1994,'Chu',6],

    ['Yinshi Nan Nu',1994,'Jia-Chien',6],

    ['Short Cuts',1993,'Ann Finnigan',1],

    ['Short Cuts',1993,'Howard Finnigan',2],

    ['Short Cuts',1993,'Ann Finnigan',3],

    ['Short Cuts',1993,'Paul Finnigan',3],

    ['Short Cuts',1993,'Howard Finnigan',4],

    ['Short Cuts',1993,'Ann Finnigan',5],

    ['Short Cuts',1993,'Paul Finnigan',5],

    ['Short Cuts',1993,'Paul Finnigan',6],

    ['Short Cuts',1993,'Howard Finnigan',7],

    ['Short Cuts',1993,'Paul Finnigan',7],

    ['Short Cuts',1993,'Ann Finnigan',8],

    ['Short Cuts',1993,'Paul Finnigan',8],

    ['Legends of the Fall',1994,'Tristan Ludlow',1],

    ['Legends of the Fall',1994,'Colonel William Ludlow',1],

    ['Legends of the Fall',1994,'Tristan Ludlow',2],

    ['Legends of the Fall',1994,'Alfred Ludlow',2],

    ['Legends of the Fall',1994,'Colonel William Ludlow',3],

    ['Legends of the Fall',1994,'Tristan Ludlow',4],

    ['Legends of the Fall',1994,'Colonel William Ludlow',5],

    ['Legends of the Fall',1994,'Alfred Ludlow',5],

    ['Legends of the Fall',1994,'Tristan Ludlow',6],

    ['Legends of the Fall',1994,'Alfred Ludlow',7],

    ['Legends of the Fall',1994,'Tristan Ludlow',8],

    ['Legends of the Fall',1994,'Colonel William Ludlow',8],

    ['Natural Born Killers',1994,'Mickey Knox',1],

    ['Natural Born Killers',1994,'Mallory Wilson Knox',1],

    ['Natural Born Killers',1994,'Wayne Gale',2],

    ['Natural Born Killers',1994,'Mickey Knox',3],

    ['Natural Born Killers',1994,'Mallory Wilson Knox',3],

    ['Natural Born Killers',1994,'Mickey Knox',4],

    ['Natural Born Killers',1994,'Mallory Wilson Knox',5],

    ['Natural Born Killers',1994,'Wayne Gale',5],

    ['Natural Born Killers',1994,'Mickey Knox',6],

    ['Natural Born Killers',1994,'Wayne Gale',6],

    ['Natural Born Killers',1994,'Mickey Knox',7],

    ['Natural Born Killers',1994,'Mallory Wilson Knox',7],

    ['In the Mouth of Madness',1995,'John Trent',1],

    ['In the Mouth of Madness',1995,'Sutter Cane',1],

    ['In the Mouth of Madness',1995,'Sutter Cane',2],

    ['In the Mouth of Madness',1995,'John Trent',3],

    ['In the Mouth of Madness',1995,'Linda Styles',3],

    ['In the Mouth of Madness',1995,'Sutter Cane',4],

    ['In the Mouth of Madness',1995,'Linda Styles',4],

    ['In the Mouth of Madness',1995,'John Trent',5],

    ['In the Mouth of Madness',1995,'Linda Styles',5],

    ['In the Mouth of Madness',1995,'Sutter Cane',6],

    ['In the Mouth of Madness',1995,'John Trent',7],

    ['Forrest Gump',1994,'Forrest Gump',1],

    ['Forrest Gump',1994,'Forrest Gump',2],

    ['Forrest Gump',1994,'Forrest Gump',3],

    ['Forrest Gump',1994,'Jenny Curran',3],

    ['Forrest Gump',1994,'Lieutenant Daniel Taylor',4],

    ['Forrest Gump',1994,'Forrest Gump',5],

    ['Forrest Gump',1994,'Jenny Curran',5],

    ['Forrest Gump',1994,'Lieutenant Daniel Taylor',6],

    ['Forrest Gump',1994,'Forrest Gump',7],

    ['Forrest Gump',1994,'Lieutenant Daniel Taylor',7],

    ['Forrest Gump',1994,'Forrest Gump',8],

    ['Forrest Gump',1994,'Lieutenant Daniel Taylor',9],

    ['Forrest Gump',1994,'Forrest Gump',10],

    ['Forrest Gump',1994,'Jenny Curran',11],

    ['Malcolm X',1992,'Malcolm X',1],

    ['Malcolm X',1992,'Betty Shabazz',1],

    ['Malcolm X',1992,'Shorty',2],

    ['Malcolm X',1992,'Malcolm X',3],

    ['Malcolm X',1992,'Betty Shabazz',3],

    ['Malcolm X',1992,'Shorty',4],

    ['Malcolm X',1992,'Malcolm X',5],

    ['Malcolm X',1992,'Betty Shabazz',6],

    ['Malcolm X',1992,'Malcolm X',7],

    ['Malcolm X',1992,'Shorty',7],

    ['Malcolm X',1992,'Shorty',8],

    ['Malcolm X',1992,'Malcolm X',9],

    ['Malcolm X',1992,'Malcolm X',10],

    ['Malcolm X',1992,'Betty Shabazz',10],

    ['Dead Again',1991,'Mike Church',1],

    ['Dead Again',1991,'Gray Baker',2],

    ['Dead Again',1991,'Margaret Strauss',2],

    ['Dead Again',1991,'Mike Church',3],

    ['Dead Again',1991,'Gray Baker',3],

    ['Dead Again',1991,'Margaret Strauss',4],

    ['Dead Again',1991,'Mike Church',5],

    ['Dead Again',1991,'Margaret Strauss',5],

    ['Dead Again',1991,'Gray Baker',6],

    ['Dead Again',1991,'Mike Church',7],

    ['Dead Again',1991,'Margaret Strauss',7],

    ['Dead Again',1991,'Gray Baker',8],

    ['Jurassic Park',1993,'Alan Grant',1],

    ['Jurassic Park',1993,'Ellie Sattler',1],

    ['Jurassic Park',1993,'Ian Malcolm',2],

    ['Jurassic Park',1993,'Ellie Sattler',3],

    ['Jurassic Park',1993,'Alan Grant',4],

    ['Jurassic Park',1993,'Ian Malcolm',5],

    ['Jurassic Park',1993,'John Parker Hammond',5],

    ['Jurassic Park',1993,'Ian Malcolm',6],

    ['Jurassic Park',1993,'Alan Grant',7],

    ['Jurassic Park',1993,'John Parker Hammond',8],

    ['Jurassic Park',1993,'Ellie Sattler',8],

    ['Jurassic Park',1993,'John Parker Hammond',9],

    ['Clueless',1995,'Cher Horowitz',1],

    ['Clueless',1995,'Dionne',2],

    ['Clueless',1995,'Tai Fraiser',2],

    ['Clueless',1995,'Cher Horowitz',3],

    ['Clueless',1995,'Cher Horowitz',4],

    ['Clueless',1995,'Dionne',4],

    ['Clueless',1995,'Tai Fraiser',4],

    ['Clueless',1995,'Dionne',5],

    ['Clueless',1995,'Tai Fraiser',5],

    ['Clueless',1995,'Cher Horowitz',6],

    ['Clueless',1995,'Dionne',7],

    ['Clueless',1995,'Tai Fraiser',7],

    ['Shadowlands',1993,'Lewis',1],

    ['Shadowlands',1993,'Joy Gresham',1],

    ['Shadowlands',1993,'Lewis',2],

    ['Shadowlands',1993,'Arnold Dopliss',2],

    ['Shadowlands',1993,'Joy Gresham',3],

    ['Shadowlands',1993,'Lewis',4],

    ['Shadowlands',1993,'Arnold Dopliss',5],

    ['Shadowlands',1993,'Lewis',6],

    ['Shadowlands',1993,'Arnold Dopliss',6],

    ['Shadowlands',1993,'Joy Gresham',7],

    ['Shadowlands',1993,'Arnold Dopliss',7],

    ['Amateur',1994,'Isabelle',1],

    ['Amateur',1994,'Thomas Ludens',1],

    ['Amateur',1994,'Sofia Ludens',1],

    ['Amateur',1994,'Isabelle',2],

    ['Amateur',1994,'Thomas Ludens',2],

    ['Amateur',1994,'Thomas Ludens',3],

    ['Amateur',1994,'Sofia Ludens',3],

    ['Amateur',1994,'Isabelle',4],

    ['Amateur',1994,'Sofia Ludens',4],

    ['Amateur',1994,'Isabelle',5],

    ['Amateur',1994,'Thomas Ludens',5],

    ['GoodFellas',1990,'James',1],

    ['GoodFellas',1990,'Henry Hill',2],

    ['GoodFellas',1990,'Tommy DeVito',2],

    ['GoodFellas',1990,'James',3],

    ['GoodFellas',1990,'Henry Hill',3],

    ['GoodFellas',1990,'Tommy DeVito',4],

    ['GoodFellas',1990,'James',5],

    ['GoodFellas',1990,'Henry Hill',6],

    ['GoodFellas',1990,'James',7],

    ['GoodFellas',1990,'Tommy DeVito',8],

    ['GoodFellas',1990,'James',9],

    ['GoodFellas',1990,'Tommy DeVito',9],

    ['GoodFellas',1990,'James',10],

    ['GoodFellas',1990,'Henry Hill',11],

    ['Little Women',1994,'Josephine',1],

    ['Little Women',1994,'Friedrich',2],

    ['Little Women',1994,'Josephine',3],

    ['Little Women',1994,'Margaret',3],

    ['Little Women',1994,'Josephine',4],

    ['Little Women',1994,'Older Amy March',4],

    ['Little Women',1994,'Margaret',5],

    ['Little Women',1994,'Josephine',6],

    ['Little Women',1994,'Friedrich',6],

    ['Little Women',1994,'Older Amy March',7],

    ['Little Women',1994,'Josephine',8],

    ['Little Women',1994,'Older Amy March',8],

    ['While You Were Sleeping',1995,'Narrator',1],

    ['While You Were Sleeping',1995,'Jack Callaghan',1],

    ['While You Were Sleeping',1995,'Narrator',2],

    ['While You Were Sleeping',1995,'Saul',3],

    ['While You Were Sleeping',1995,'Jack Callaghan',4],

    ['While You Were Sleeping',1995,'Saul',4],

    ['While You Were Sleeping',1995,'Narrator',5],

    ['While You Were Sleeping',1995,'Saul',6],

    ['While You Were Sleeping',1995,'Narrator',7],

    ['While You Were Sleeping',1995,'Saul',7],

    ['While You Were Sleeping',1995,'Jack Callaghan',8],

    ['While You Were Sleeping',1995,'Narrator',9]]
