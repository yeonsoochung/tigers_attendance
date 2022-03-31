"""
Starting Pitchers
"""
starters_by_team = \
{2013: {'ARZ': {6: 'Patrick Corbin', 5: 'Wade Miley', 4: 'Trevor Cahill', \
                3: 'Brandon McCarthy', 2: 'Ian Kennedy'}, \
        'ATL': {6: 'Mike Minor', 5: 'Kris Medlen', 4: 'Julio Teheran', \
                3: 'Paul Maholm', 2: 'Tim Hudson'}, \
        'BAL': {6: 'Chris Tillman', 5: 'Miguel Gonzalez', 4: 'Wei-Yin Chen', \
                3: 'Jason Hammel', 2: 'Scott Feldman'}, \
        'BOS': {6: 'Jon Lester', 5: 'John Lackey', 4: 'Ryan Dempster', \
                3: 'Felix Doubront', 2: 'Clay Buchholz'}, \
        'CHC': {6: 'Jeff Samardzija', 5: 'Travis Wood', 4: 'Edwin Jackson', \
                3: 'Scott Feldman', 2: 'Carlos Villanueva'}, \
        'CWS': {6: 'Chris Sale', 5: 'Jose Quintana', 4: 'Hector Santiago', \
                3: 'John Danks', 2: 'Dylan Axelrod'}, \
        'CIN': {6: 'Mat Latos', 5: 'Homer Bailey', 4: 'Bronson Arroyo', \
                3: 'Mike Leake', 2: 'Tony Cingrani'}, \
        'CLE': {6: 'Justin Masterson', 5: 'Ubaldo Jimenez', 4: 'Corey Kluber', \
                3: 'Zach McAllister', 2: 'Scott Kazmir'}, \
        'COL': {6: 'Jhoulys Chacin', 5: 'Jorge De La Rosa', 4: 'Juan Nicasio', \
                3: 'Tyler Chatwood', 2: 'Jeff Francis'}, \
        'DET': {6: 'Justin Verlander', 5: 'Max Scherzer', 4: 'Doug Fister', \
                3: 'Anibal Sanchez', 2: 'Rick Porcello'}, \
        'HOU': {6: 'Bud Norris', 5: 'Lucas Harrell', 4: 'Dallas Keuchel', \
                3: 'Erik Bedard', 2: 'Jordan Lyles'}, \
        'KCR': {6: 'James Shields', 5: 'Ervin Santana', 4: 'Jeremy Guthrie', \
                3: 'Wade Davis', 2: 'Luis Mendoza'}, \
        'LAA': {6: 'Jered Weaver', 5: 'C.J. Wilson', 4: 'Jason Vargas', \
                3: 'Jerome Williams', 2: 'Joe Blanton'}, \
        'LAD': {6: 'Clayton Kershaw', 5: 'Zack Greinke', 4: 'Hyun Jin Ryu', \
                3: 'Chris Capuano', 2: 'Ricky Nolasco'}, \
        'MIA': {6: 'Jose Fernandez', 5: 'Nathan Eovaldi', 4: 'Jacob Turner', \
                3: 'Ricky Nolasco', 2: 'Tom Koehler'}, \
        'MIL': {6: 'Kyle Lohse', 5: 'Yovani Gallardo', 4: 'Wily Peralta', \
                3: 'Marco Estrada', 2: 'Tom Gorzelanny'}, \
        'MIN': {6: 'Kevin Correia', 5: 'Sam Deduno', 4: 'Mike Pelfrey', \
                3: 'Scott Diamond', 2: 'Pedro Hernandez'}, \
        'NYM': {6: 'Matt Harvey', 5: 'Dillon Gee', 4: 'Jon Niese', \
                3: 'Zack Wheeler', 2: 'Jeremy Hefner'}, \
        'NYY': {6: 'CC Sabathia', 5: 'Andy Pettitte', 4: 'Hiroki Kuroda', \
                3: 'Ivan Nova', 2: 'Phil Hughes'}, \
        'OAK': {6: 'Bartolo Colon', 5: 'A.J. Griffin', 4: 'Jarrod Parker', \
                3: 'Dan Straily', 2: 'Tommy Milone'}, \
        'PHI': {6: 'Cliff Lee', 5: 'Cole Hamels', 4: 'Kyle Kendrick', \
                3: 'Jonathan Pettibone', 2: 'John Lannan'}, \
        'PIT': {6: 'A.J. Burnett', 5: 'Francisco Liriano', 4: 'Jeff Locke', \
                3: 'Gerrit Cole', 2: 'Charlie Morton'}, \
        'SDP': {6: 'Andrew Cashner', 5: 'Eric Stults', 4: 'Jason Marquis', \
                3: 'Edinson Volquez', 2: 'Clayton Richards'}, \
        'SFG': {6: 'Madison Bumgarner', 5: 'Matt Cain', 4: 'Tim Lincecum', \
                3: 'Barry Zito', 2: 'Ryan Vogelsong'}, \
        'SEA': {6: 'Hisashi Iwakuma', 5: 'Felix Hernandez', 4: 'Joe Saunders', \
                3: 'Aaron Harang', 2: 'Brandon Maurer'}, \
        'STL': {6: 'Adam Wainwright', 5: 'Shelby Miller', 4: 'Lance Lynn', \
                3: 'Joe Kelly', 2: 'Jake Westbrook'}, \
        'TBR': {6: 'David Price', 5: 'Matt Moore', 4: 'Alex Cobb', \
                3: 'Chris Archer', 2: 'Jeremy Hellickson'}, \
        'TEX': {6: 'Yu Darvish', 5: 'Derek Holland', 4: 'Martin Perez', \
                3: 'Alexi Ogando', 2: 'Nick Tepesch'}, \
        'TOR': {6: 'R.A. Dickey', 5: 'Mark Buehrle', 4: 'J.A. Happ', \
                3: 'Todd Redmond', 2: 'Esmil Rogers'}, \
        'WAS': {6: 'Jordan Zimmermann', 5: 'Gio Gonzalez', 4: 'Stephen Strasburg', \
                3: 'Dan Haren', 2: 'Ross Detwiler'} } , \
 2014: {'ARZ': {6: 'Josh Collmenter', 5: 'Wade Miley', 4: 'Chase Anderson', \
                3: 'Brandon McCarthy', 2: 'Bronson Arroyo'}, \
        'ATL': {6: 'Julio Teheran', 5: 'Aaron Harang', 4: 'Ervin Santana', \
               3: 'Alex Wood', 2: 'Mike Minor'}, \
        'BAL': {6: 'Chris Tillman', 5: 'Miguel Gonzalez', 4: 'Wei-Yin Chen', \
                3: 'Bud Norris', 2: 'Ubaldo Jimenez'}, \
        'BOS': {6: 'Jon Lester', 5: 'John Lackey', 4: 'Clay Buchholz', \
                3: 'Rubby De La Rosa', 2: 'Jake Peavy'}, \
        'CHC': {6: 'Jake Arrieta', 5: 'Jeff Samardzija', 4: 'Jason Hammel', \
                3: 'Kyle Hendricks', 2: 'Travis Wood'}, \
        'CWS': {6: 'Chris Sale', 5: 'Jose Quintana', 4: 'John Danks', \
                3: 'Hector Noesi', 2: 'Scott Carroll'}, \
        'CIN': {6: 'Johnny Cueto', 5: 'Mike Leake', 4: 'Alfredo Simon', \
                3: 'Homer Bailey', 2: 'Mat Latos'}, \
        'CLE': {6: 'Corey Kluber', 5: 'Trevor Bauer', 4: 'Danny Salazar', \
                3: 'T.J. House', 2: 'Josh Tomlin'}, \
        'COL': {6: 'Jorge De La Rosa', 5: 'Jordan Lyles', 4: 'Tyler Matzek', \
                3: 'Franklin Morales', 2: 'Jhoulys Chacin'}, \
        'DET': {6: 'Max Scherzer', 5: 'Justin Verlander', 4: 'Rick Porcello', \
                3: 'Anibal Sanchez', 2: 'David Price'}, \
        'HOU': {6: 'Dallas Keuchel', 5: 'Collin McHugh', 4: 'Scott Feldman', \
                3: 'Brett Oberholtzer', 2: 'Jarred Cosart'}, \
        'KCR': {6: 'James Shields', 5: 'Yordano Ventura', 4: 'Danny Duffy', \
                3: 'Jason Vargas', 2: 'Jeremy Guthrie'}, \
        'LAA': {6: 'Jered Weaver', 5: 'Garrett Richards', 4: 'Matt Shoemaker', \
                3: 'C.J. Wilson', 2: 'Hector Santiago'}, \
        'LAD': {6: 'Clayton Kershaw', 5: 'Zack Greinke', 4: 'Josh Beckett', \
                3: 'Hyun Jin Ryu', 2: 'Dan Haren'}, \
        'MIA': {6: 'Henderson Alvarez III', 5: 'Tom Koehler', 4: 'Nathan Eovaldi', \
                3: 'Brad Hand', 2: 'Jacob Turner'}, \
        'MIL': {6: 'Wily Peralta', 5: 'Kyle Lohse', 4: 'Yovani Gallardo', \
                3: 'Matt Garza', 2: 'Jimmy Nelson'}, \
        'MIN': {6: 'Phil Hughes', 5: 'Kyle Gibson', 4: 'Ricky Nolasco', \
                3: 'Kevin Correia', 2: 'Yohan Pino'}, \
        'NYM': {6: 'Jon Niese', 5: 'Zack Wheeler', 4: 'Bartolo Colon', \
                3: 'Jacob deGrom', 2: 'Dillon Gee'}, \
        'NYY': {6: 'Masahiro Tanaka', 5: 'Hiroki Kuroda', 4: 'Brandon McCarthy', \
                3: 'Shane Greene', 2: 'David Phelps'}, \
        'OAK': {6: 'Sonny Gray', 5: 'Scott Kazmir', 4: 'Jesse Chavez', \
                3: 'Jeff Samardzija', 2: 'Tommy Milone'}, \
        'PHI': {6: 'Cole Hamels', 5: 'A.J. Burnett', 4: 'Kyle Kendrick', \
                3: 'Roberto Hernandez', 2: 'David Buchanan'}, \
        'PIT': {6: 'Edinson Volquez', 5: 'Francisco Liriano', 4: 'Gerrit Cole', \
                3: 'Charlie Morton', 2: 'Vance Worley'}, \
        'SDP': {6: 'Tyson Ross', 5: 'Andrew Cashner', 4: 'Ian Kennedy', \
                3: 'Odrisamer Despaigne', 2: 'Eric Stults'}, \
        'SFG': {6: 'Madison Bumgarner', 5: 'Tim Hudson', 4: 'Ryan Vogelsong', \
                3: 'Matt Cain', 2: 'Jake Peavy'}, \
        'SEA': {6: 'Felix Hernandez', 5: 'Hisashi Iwakuma', 4: 'Chris Young', \
                3: 'Roenis Elias', 2: 'James Paxton'}, \
        'STL': {6: 'Adam Wainwright', 5: 'Lance Lynn', 4: 'Shelby Miller',\
                3: 'Michael Wacha', 2: 'John Lackey'}, \
        'TBR': {6: 'David Price', 5: 'Alex Cobb', 4: 'Chris Archer', \
                3: 'Jake Odorizzi', 2: 'Erik Bedard'}, \
        'TEX': {6: 'Yu Darvish', 5: 'Colby Lewis', 4: 'Nick Tepesch', \
                3: 'Nick Martinez', 2: 'Scott Baker'}, \
        'TOR': {6: 'R.A. Dickey', 5: 'Mark Buehrle', 4: 'J.A. Happ', \
                3: 'Marcus Stroman', 2: 'Drew Hutchinson'}, \
        'WAS': {6: 'Jordan Zimmermann', 5: 'Doug Fister', 4: 'Stephen Strasburg', \
                3: 'Tanner Roark', 2: 'Gio Gonzalez'} } , \
 2015: {'ARZ': {6: 'Rubby De La Rosa', 5: 'Chase Anderson', 4: 'Jeremy Hellickson', \
                3: 'Robbie Ray', 2: 'Patrick Corbin'}, \
        'ATL': {6: 'Julio Teheran', 5: 'Shelby Miller', 4: 'Alex Wood', \
                3: 'Williams Perez', 2: 'Matt Wisler'}, \
        'BAL': {6: 'Wei-Yin Chen', 5: 'Ubaldo Jimenez', 4: 'Chris Tillman', \
                3: 'Miguel Gonzalez', 2: 'Kevin Gausman'}, \
        'BOS': {6: 'Clay Buchholz', 5: 'Eduardo Rodriguez', 4: 'Wade Miley', \
                3: 'Joe Kelly', 2: 'Rick Porcello'}, \
        'CHC': {6: 'Jake Arrieta', 5: 'Jon Lester', 4: 'Kyle Hendricks', \
                3: 'Jason Hammel', 2: 'Dan Haren'}, \
        'CWS': {6: 'Chris Sale', 5: 'Jose Quintana', 4: 'Carlos Rodon', \
                3: 'Jeff Samardzija', 2: 'John Danks'}, \
        'CIN': {6: 'Johnny Cueto', 5: 'Mike Leake', 4: 'Anthony DeSclafani', \
                3: 'Raisel Iglesias', 2: 'Michael Lorenzen'}, \
        'CLE': {6: 'Corey Kluber', 5: 'Danny Salazar', 4: 'Carlos Carrasco', \
                3: 'Trevor Bauer', 2: 'Cody Anderson'}, \
        'COL': {6: 'Jorge De La Rosa', 5: 'Chad Bettis', 4: 'Chris Rusin', \
                3: 'Kyle Kendrick', 2: 'Eddie Butler'}, \
        'DET': {6: 'David Price', 5: 'Justin Verlander', 4: 'Anibal Sanchez', \
                3: 'Alfredo Simon', 2: 'Shane Greene'}, \
        'HOU': {6: 'Dallas Keuchel', 5: 'Collin McHugh', 4: 'Lance McCullers Jr.', \
                3: 'Scott Feldman', 2: 'Scott Kazmir'}, \
        'KCR': {6: 'Edinson Volquez', 5: 'Chris Young', 4: 'Yordano Ventura', \
                3: 'Danny Duffy', 2: 'Jeremy Guthrie'}, \
        'LAA': {6: 'Garrett Richards', 5: 'Hector Santiago', 4: 'C.J. Wilson', \
                3: 'Jered Weaver', 2: 'Matt Shoemaker'}, \
        'LAD': {6: 'Zack Greinke', 5: 'Clayton Kershaw', 4: 'Brett Anderson', \
                3: 'Mike Bolsinger', 2: 'Carlos Frias'}, \
        'MIA': {6: 'Dan Haren', 5: 'Tom Koehler', 4: 'David Phelps', \
                3: 'Mat Latos', 2: 'Justin Nicolino'}, \
        'MIL': {6: 'Jimmy Nelson', 5: 'Mike Fiers', 4: 'Taylor Jungmann', \
                3: 'Matt Garza', 2: 'Kyle Lohse'}, \
        'MIN': {6: 'Kyle Gibson', 5: 'Mike Pelfrey', 4: 'Tommy Milone', \
                3: 'Phil Hughes', 2: 'Ervin Santana'}, \
        'NYM': {6: 'Jacob deGrom', 5: 'Matt Harvey', 4: 'Bartolo Colon', \
                3: 'Jon Niese', 2: 'Noah Syndergaard'}, \
        'NYY': {6: 'Masahiro Tanaka', 5: 'Nathan Eolvaldi', 4: 'Michael Pineda', \
                3: 'CC Sabathia', 2: 'Ivan Nova'}, \
        'OAK': {6: 'Sonny Gray', 5: 'Scott Kazmir', 4: 'Jesse Chavez', \
                3: 'Kendall Graveman', 2: 'Jesse Hahn'}, \
        'PHI': {6: 'Cole Hamels', 5: 'Aaron Harang', 4: 'Jerome Williams', \
                3: 'Aaron Nola', 2: 'Adam Morgan'}, \
        'PIT': {6: 'Gerrit Cole', 5: 'Francisco Liriano', 4: 'A.J. Burnett', \
                3: 'Jeff Locke', 2: 'Charlie Morton'}, \
        'SDP': {6: 'Tyson Ross', 5: 'James Shields', 4: 'Ian Kennedy', \
                3: 'Andrew Cashner', 2: 'Odrisamer Despaigne'}, \
        'SFG': {6: 'Madison Bumgarner', 5: 'Jake Peavy', 4: 'Chris Heston', \
                3: 'Tim Hudson', 2: 'Ryan Vogelsong'}, \
        'SEA': {6: 'Felix Hernandez', 5: 'Hisashi Iwakuma', 4: 'Roenis Elias', \
                3: 'Taijuan Walker', 2: 'J.A. Happ'}, \
        'STL': {6: 'John Lackey', 5: 'Michael Wacha', 4: 'Lance Lynn',\
                3: 'Carlos Martinez', 2: 'Jaime Garcia'}, \
        'TBR': {6: 'Chris Archer', 5: 'Joke Odorizzi', 4: 'Erasmo Ramirez', \
                3: 'Nate Karns', 2: 'Drew Smyly'}, \
        'TEX': {6: 'Yovani Gallardo', 5: 'Cole Hamels', 4: 'Nick Martinez', \
                3: 'Colby Lewis', 2: 'Wandy Rodriguez'}, \
        'TOR': {6: 'David Price', 5: 'Mark Buehrle', 4: 'R.A. Dickey', \
                3: 'Marco Estrada', 2: 'Drew Huthinson'}, \
        'WAS': {6: 'Max Scherzer', 5: 'Jordan Zimmermann', 4: 'Stephen Strasburg', \
                3: 'Gio Gonzalez', 2: 'Doug Fister'} } , \
 2016: {'ARZ': {6: 'Zack Greinke', 5: 'Robbie Ray', 4: 'Archie Bradley', \
                3: 'Patrick Corbin', 2: 'Shelby Miller'}, \
        'ATL': {6: 'Julio Teheran', 5: 'Mike Foltynewicz', 4: 'Matt Wisler', \
                3: 'Aaron Blair', 2: 'Williams Perez'}, \
        'BAL': {6: 'Chris Tillman', 5: 'Kevin Gausman', 4: 'Ubaldo Jimenez', \
                3: 'Yovani Gallardo', 2: 'Tyler Wilson'}, \
        'BOS': {6: 'Rick Porcello', 5: 'David Price', 4: 'Steven Wright', \
                3: 'Clay Buchholz', 2: 'Eduardo Rodriguez'}, \
        'CHC': {6: 'Jon Lester', 5: 'Kyle Hendricks', 4: 'Jake Arrieta', \
                3: 'John Lackey', 2: 'Jason Hammel'}, \
        'CWS': {6: 'Chris Sale', 5: 'Jose Quintana', 4: 'Carlos Rodon', \
                3: 'Miguel Gonzalez', 2: 'Mat Latos'}, \
        'CIN': {6: 'Anthony DeSclafani', 5: 'Dan Straily', 4: 'Brandon Finnegan', \
                3: 'Tim Adleman', 2: 'John Lamb'}, \
        'CLE': {6: 'Corey Kluber', 5: 'Carlos Carrasco', 4: 'Danny Salazar', \
                3: 'Trevor Bauer', 2: 'Josh Tomlin'}, \
        'COL': {6: 'Chad Bettis', 5: 'Jon Gray', 4: 'Tyler Chatwood', \
                3: 'Tyler Anderson', 2: 'Jorge De La Rosa'}, \
        'DET': {6: 'Justin Verlander', 5: 'Michael Fulmer', 4: 'Jordan Zimmermann', \
                3: 'Anibal Sanchez', 2: 'Mike Pelfrey'}, \
        'HOU': {6: 'Collin McHugh', 5: 'Mike Fiers', 4: 'Doug Fister', \
                3: 'Dallas Keuchel', 2: 'Lance McCullers Jr.'}, \
        'KCR': {6: 'Ian Kennedy', 5: 'Danny Duffy', 4: 'Yordano Ventura', \
                3: 'Edinson Volquez', 2: 'Dillon Gee'}, \
        'LAA': {6: 'Matt Shoemaker', 5: 'Hector Santiago', 4: 'Jered Weaver', \
                3: 'Jhoulys Chacin', 2: 'Ricky Nolasco'}, \
        'LAD': {6: 'Clayton Kershaw', 5: 'Kenta Maeda', 4: 'Scott Kazmir', \
                3: 'Julio Urias', 2: 'Ross Stripling'}, \
        'MIA': {6: 'Jose Fernandez', 5: 'Adam Conley', 4: 'Tom Koehler', \
                3: 'Wei-Yin Chen', 2: 'Justin Nicolino'}, \
        'MIL': {6: 'Zach Davies', 5: 'Jimmy Nelson', 4: 'Chase Anderson', \
                3: 'Wily Peralta', 2: 'Junior Guerra'}, \
        'MIN': {6: 'Ervin Santana', 5: 'Kyle Gibson', 4: 'Ricky Nolasco', \
                3: 'Tyler Duffey', 2: 'Tommy Milone'}, \
        'NYM': {6: 'Noah Syndergaard', 5: 'Bartolo Colon', 4: 'Jacob deGrom', \
                3: 'Steven Matz', 2: 'Matt Harvey'}, \
        'NYY': {6: 'Masahiro Tanaka', 5: 'CC Sabathia', 4: 'Nathan Eovaldi', \
                3: 'Michael Pineda', 2: 'Ivan Nova'}, \
        'OAK': {6: 'Sean Manaea', 5: 'Kendall Graveman', 4: 'Rich Hill', \
                3: 'Sonny Gray', 2: 'Daniel Mengden'}, \
        'PHI': {6: 'Jerad Eickhoff', 5: 'Jeremy Hellickson', 4: 'Vince Velasquez', \
                3: 'Aaron Nola', 2: 'Adam Morgan'}, \
        'PIT': {6: 'Gerrit Cole', 5: 'Jon Niese', 4: 'Jameson Taillon', \
                3: 'Jeff Locke', 2: 'Francisco Liriano'}, \
        'SDP': {6: 'Drew Pomeranz', 5: 'Christian Friedrich', 4: 'Andrew Cashner', \
                3: 'Colin Rea', 2: 'Luis Perdomo'}, \
        'SFG': {6: 'Madison Bumgarner', 5: 'Johnny Cueto', 4: 'Jeff Samardzija', \
                3: 'Jake Peavy', 2: 'Matt Cain'}, \
        'SEA': {6: 'Felix Hernandez', 5: 'Hisashi Iwakuma', 4: 'James Paxton', \
                3: 'Taijuan Walker', 2: 'Wade Miley'}, \
        'STL': {6: 'Carlos Martinez', 5: 'Adam Wainwright', 4: 'Jaime Garcia',\
                3: 'Mike Leake', 2: 'Michael Wacha'}, \
        'TBR': {6: 'Jake Odorizzi', 5: 'Chris Archer', 4: 'Matt Moore', \
                3: 'Matt Andriese', 2: 'Drew Smyly'}, \
        'TEX': {6: 'Cole Hamels', 5: 'Yu Darvish', 4: 'Colby Lewis', \
                3: 'Mrtin Perez', 2: 'A.J. Griffin'}, \
        'TOR': {6: 'J.A. Happ', 5: 'Aaron Sanchez', 4: 'Marco Estrada', \
                3: 'Marcus Stroman', 2: 'R.A. Dickey'}, \
        'WAS': {6: 'Max Scherzer', 5: 'Tanner Roark', 4: 'Stephen Strasburg', \
                3: 'Gio Gonzalez', 2: 'Joe Ross'} } , \
 2017: {'ARZ': {6: 'Zack Greinke', 5: 'Robbie Ray', 4: 'Patrick Corbin', \
                3: 'Taijuan Walker', 2: 'Zack Godley'}, \
        'ATL': {6: 'R.A. Dickey', 5: 'Julio Teheran', 4: 'Mike Foltynewicz', \
                3: 'Jaime Garcia', 2: 'Sean Newcomb'}, \
        'BAL': {6: 'Kevin Gausman', 5: 'Dylan Bundy', 4: 'Wade Miley', \
                3: 'Ubaldo Jimenez', 2: 'Chris Tillman'}, \
        'BOS': {6: 'Chris Sale', 5: 'Drew Pomeranz', 4: 'Rick Porcello', \
               3: 'David Price', 2: 'Eduardo Rodriguez'}, \
        'CHC': {6: 'Jon Lester', 5: 'Kyle Hendricks', 4: 'Jake Arrieta', \
                3: 'John Lackey', 2: 'Jose Quintana'}, \
        'CWS': {6: 'Miguel Gonzalez', 5: 'Jose Quintana', 4: 'James Shields', \
                3: 'Mike Pelfrey', 2: 'Derek Holland'}, \
        'CIN': {6: 'Scott Feldman', 5: 'Tim Adleman', 4: 'Luis Castillo', \
                3: 'Sal Romano', 2: 'Homer Bailey'}, \
        'CLE': {6: 'Corey Kluber', 5: 'Carlos Carrasco', 4: 'Mike Clevinger', \
                3: 'Trevor Bauer', 2: 'Danny Salazar'}, \
        'COL': {6: 'German Marquez', 5: 'Kyle Freeland', 4: 'Tyler Chatwood', \
                3: 'Jon Gray', 2: 'Antonio Senzatela'}, \
        'DET': {6: 'Justin Verlander', 5: 'Michael Fulmer', 4: 'Matthew Boyd', \
                3: 'Jordan Zimmermann', 2: 'Anibal Sanchez'}, \
        'HOU': {6: 'Dallas Keuchel', 5: 'Charlie Morton', 4: 'Brad Peacock', \
                3: 'Lance McCullers Jr.', 2: 'Mike Fiers'}, \
        'KCR': {6: 'Jason Vargas', 5: 'Danny Duffy', 4: 'Jakob Junis', \
                3: 'Jason Hammel', 2: 'Ian Kennedy'}, \
        'LAA': {6: 'JC Ramirez', 5: 'Parker Bridwell', 4: 'Matt Shoemaker', \
                3: 'Ricky Nolasco', 2: 'Jesse Chavez'}, \
        'LAD': {6: 'Clayton Kershaw', 5: 'Alex Wood', 4: 'Rich Hill', \
                3: 'Hyun Jin Ryu', 2: 'Kenta Maeda'}, \
        'MIA': {6: 'Jose Urena', 5: 'Dan Straily', 4: 'Edinson Volquez', \
                3: 'Adam Conley', 2: 'Tom Koehler'}, \
        'MIL': {6: 'Chase Anderson', 5: 'Jimmy Nelson', 4: 'Zach Davies', \
                3: 'Brent Suter', 2: 'Matt Garza'}, \
        'MIN': {6: 'Ervin Santana', 5: 'Jose Berrios', 4: 'Kyle Gibson', \
                3: 'Adalberto Mejia', 2: 'Bartolo Colon'}, \
        'NYM': {6: 'Jacob deGrom', 5: 'Seth Lugo', 4: 'Robert Gsellman', \
                3: 'Rafael Montero', 2: 'Zack Wheeler'}, \
        'NYY': {6: 'Luis Severino', 5: 'CC Sabathia', 4: 'Jordan Montgomery', \
                3: 'Masahiro Tanaka', 2: 'Michael Pineda'}, \
        'OAK': {6: 'Sean Manaea', 5: 'Sonny Gray', 4: 'Kendall Graveman', \
                3: 'Jharel Cotton', 2: 'Jesse Hahn'}, \
        'PHI': {6: 'Aaron Nola', 5: 'Jerad Eickhoff', 4: 'Jeremy Hellickson', \
                3: 'Ben Lively', 2: 'Vince Velasquez'}, \
        'PIT': {6: 'Gerrit Cole', 5: 'Ivan Nova', 4: 'Trevor Williams', \
                3: 'Chad Kuhl', 2: 'Jameson Taillon'}, \
        'SDP': {6: 'Jhoulys Chacin', 5: 'Trevor Cahill', 4: 'Dinelson Lamet', \
                3: 'Luis Perdomo', 2: 'Clayton Richard'}, \
        'SFG': {6: 'Madison Bumgarner', 5: 'Jess Samardzija', 4: 'Johnny Cueto', \
                3: 'Ty Blach', 2: 'Matt Moore'}, \
        'SEA': {6: 'James Paxton', 5: 'Felix Hernandez', 4: 'Ariel Miranda', \
                3: 'Erasmo Ramirez', 2: 'Yovani Gallardo'}, \
        'STL': {6: 'Carlos Martinez', 5: 'Lance Lynn', 4: 'Michael Wacha', \
                3: 'Mike Leake', 2: 'Adam Wainwright'}, \
        'TBR': {6: 'Alex Cobb', 5: 'Chris Archer', 4: 'Jake Odorizzi', \
                3: 'Blake Snell', 2: 'Jake Faria'}, \
        'TEX': {6: 'Andrew Cashner', 5: 'Yu Darvish', 4: 'Cole Hamels', \
                3: 'Martin Perez', 2: 'Nick Martinez'}, \
        'TOR': {6: 'Marcus Stroman', 5: 'J.A. Happ', 4: 'Marco Estrada', \
                3: 'Francisco Liriano', 2: 'Joe Biagini'}, \
        'WAS': {6: 'Max Scherzer', 5: 'Stephen Strasburg', 4: 'Gio Gonzalez', \
                3: 'Tanner Roark', 2: 'Joe Ross'} } , \
 2018: {'ARZ': {6: 'Zack Greinke', 5: 'Patrick Corbin', 4: 'Zack Godley', \
                3: 'Robbie Ray', 2: 'Clay Buchholz'}, \
        'ATL': {6: 'Mike Foltynewicz', 5: 'Julio Teheran', 4: 'Sean Newcomb', \
                3: 'Anibal Sanchez', 2: 'Brandon McCarthy'}, \
        'BAL': {6: 'Dylan Bundy', 5: 'Kevin Gausman', 4: 'Alex Cobb', \
                3: 'David Hess', 2: 'Andrew Cashner'}, \
        'BOS': {6: 'Chris Sale', 5: 'David Price', 4: 'Rick Porcello', \
                3: 'Eduardo Rodriguez', 2: 'Nathan Eovaldi'}, \
        'CHC': {6: 'Jon Lester', 5: 'Kyle Hendricks', 4: 'Jose Quintana', \
                3: 'Cole Hamels', 2: 'Tyler Chatwood'}, \
        'CWS': {6: 'Reynaldo Lopez', 5: 'James Shields', 4: 'Carlos Rodon', \
                3: 'Lucas Giolito', 2: 'Dylan Covey'}, \
        'CIN': {6: 'Luis Castillo', 5: 'Sal Romano', 4: 'Matt Harvey', \
                3: 'Anthony DeSclafani', 2: 'Tyler Mahle'}, \
        'CLE': {6: 'Corey Kluber', 5: 'Carlos Carrasco', 4: 'Mike Clevinger', \
                3: 'Trevor Bauer', 2: 'Shane Bieber'}, \
        'COL': {6: 'Kyle Freeland', 5: 'German Marquez', 4: 'Tyler Anderson', \
                3: 'Jon Gray', 2: 'Chad Bettis'}, \
        'DET': {6: 'Matthew Boyd', 5: 'Francisco Liriano', 4: 'Jordan Zimmermann', \
                3: 'Mike Fiers', 2: 'Michael Fulmer'}, \
        'HOU': {6: 'Justin Verlander', 5: 'Gerrit Cole', 4: 'Charlie Morton', \
                3: 'Dallas Keuchel', 2: 'Lance McCullers Jr.'}, \
        'KCR': {6: 'Jakob Junis', 5: 'Danny Duffy', 4: 'Ian Kennedy', \
                3: 'Heath Fillmyer', 2: 'Eric Skoglund'}, \
        'LAA': {6: 'Jaime Barria', 5: 'Shohei Ohtani', 4: 'Andrew Heaney', \
                3: 'Tyler Skaggs', 2: 'Garrett Richards'}, \
        'LAD': {6: 'Clayton Kershaw', 5: 'Walker Buehler', 4: 'Rich Hill', \
                3: 'Alex Wood', 2: 'Ross Stripling'}, \
        'MIA': {6: 'Jose Urena', 5: 'Dan Straily', 4: 'Trevor Richards', \
                3: 'Wei-Yin Chen', 2: 'Caleb Smith'}, \
        'MIL': {6: 'Jhoulys Chacin', 5: 'Chase Anderson', 4: 'Junior Guerra', \
                3: 'Brent Suter', 2: 'Wade Miley'}, \
        'MIN': {6: 'Kyle Gibson', 5: 'Jose Berrios', 4: 'Jake Odorizzi', \
                3: 'Lance Lynn', 2: 'Fernando Romero'}, \
        'NYM': {6: 'Jacob deGrom', 5: 'Noah Syndergaard', 4: 'Zack Wheeler', \
                3: 'Steven Matz', 2: 'Jason Vargas'}, \
        'NYY': {6: 'Luis Severino', 5: 'Masahiro Tanaka', 4: 'CC Sabathia', \
                3: 'Sonny Gray', 2: 'Domingo German'}, \
        'OAK': {6: 'Sean Manaea', 5: 'Edwin Jackson', 4: 'Trevor Cahill', \
                3: 'Daniel Mengden', 2: 'Brett Anderson'}, \
        'PHI': {6: 'Aaron Nola', 5: 'Jake Arrieta', 4: 'Nick Pivetta', \
                3: 'Vince Velasquez', 2: 'Zach Eflin'}, \
        'PIT': {6: 'Jameson Taillon', 5: 'Trevor Williams', 4: 'Ivan Nova', \
                3: 'Joe Musgrove', 2: 'Chad Kuhl'}, \
        'SDP': {6: 'Joey Lucchesi', 5: 'Eric Lauer', 4: 'Clayton Richard', \
                3: 'Tyson Ross', 2: 'Bryan Mitchell'}, \
        'SFG': {6: 'Derek Holland', 5: 'Madison Bumgarner', 4: 'Dereck Rodriguez', \
                3: 'Andrew Suarez', 2: 'Chris Stratton'}, \
        'SEA': {6: 'James Paxton', 5: 'Mike Leake', 4: 'Wade LeBlanc', \
                3: 'Marco Gonzalez', 2: 'Felix Hernandez'}, \
        'STL': {6: 'Miles Mikolas', 5: 'Carlos Martinez', 4: 'Jack Flaherty',\
                3: 'Michael Wacha', 2: 'John Gant'}, \
        'TBR': {6: 'Blake Snell', 5: 'Chris Archer', 4: 'Nathan Eovaldi', \
                3: 'Tyler Glasnow', 2: 'Jake Faria'}, \
        'TEX': {6: 'Mike Minor', 5: 'Cole Hamels', 4: 'Yovani Gallardo', \
                3: 'Bartolo Colon', 2: 'Doug Fister'}, \
        'TOR': {6: 'J.A. Happ', 5: 'Aaron Sanchez', 4: 'Marco Estrada', \
                3: 'Sam Gaviglio', 2: 'Marcus Stroman'}, \
        'WAS': {6: 'Max Scherzer', 5: 'Stephen Strasburg', 4: 'Tanner Roark', \
                3: 'Gio Gonzalez', 2: 'Jeremy Hellickson'} } ,
 2019: {'ARZ': {6: 'Zack Greinke', 5: 'Robbie Ray', 4: 'Merrill Kelly', \
                3: 'Alex Young', 2: 'Taylor Clarke'}, \
        'ATL': {6: 'Mike Soroka', 5: 'Julio Teheran', 4: 'Max Fried', \
                3: 'Dallas Keuchel', 2: 'Mike Foltynewicz'}, \
        'BAL': {6: 'John Means', 5: 'Andrew Cashner', 4: 'Dylan Bundy', \
                3: 'Asher Wojciechowski', 2: 'David Hess'}, \
        'BOS': {6: 'Eduardo Rodriguez', 5: 'David Price', 4: 'Chris Sale', \
                3: 'Rick Porcello', 2: 'Nathan Eovaldi'}, \
        'CHC': {6: 'Kyle Hendricks', 5: 'Jon Lester', 4: 'Cole Hamels', \
                3: 'Yu Darvish', 2: 'Jose Quintana'}, \
        'CWS': {6: 'Lucas Giolito', 5: 'Ivan Nova', 4: 'Reynaldo Lopez', \
                3: 'Dylan Cease', 2: 'Ross Detwiler'}, \
        'CIN': {6: 'Sonny Gray', 5: 'Luis Castillo', 4: 'Anthony DeSclafani', \
                3: 'Tanner Roark', 2: 'Tyler Mahle'}, \
        'CLE': {6: 'Mike Clevinger', 5: 'Shane Bieber', 4: 'Trevor Bauer', \
                3: 'Zach Plesac', 2: 'Adam Plutko'}, \
        'COL': {6: 'German Marquez', 5: 'Jon Gray', 4: 'Antonio Senzatela', \
                3: 'Kyle Freeland', 2: 'Peter Lambert'}, \
        'DET': {6: 'Matthew Boyd', 5: 'Daniel Norris', 4: 'Spencer Turnbull', \
                3: 'Jordan Zimmermann', 2: 'Tyler Alexander'}, \
        'HOU': {6: 'Justin Verlander', 5: 'Gerrit Cole', 4: 'Wade Miley', \
                3: 'Brad Peacock', 2: 'Zack Greinke'}, \
        'KCR': {6: 'Brad Keller', 5: 'Danny Duffy', 4: 'Jakob Junis', \
                3: 'Homer Bailey', 2: 'Glenn Sparkman'}, \
        'LAA': {6: 'Tyler Skaggs', 5: 'Griffin Canning', 4: 'Andrew Heaney', \
                3: 'Dillon Peters', 2: 'Jaime Barria'}, \
        'LAD': {6: 'Hyun Jin Ryu', 5: 'Clayton Kershaw', 4: 'Walker Buehler', \
                3: 'Rich Hill', 2: 'Kenta Maeda'}, \
        'MIA': {6: 'Sandy Alcantara', 5: 'Caleb Smith', 4: 'Trevor Richards', \
                3: 'Pablo Lopez', 2: 'Jordan Yamamoto'}, \
        'MIL': {6: 'Zach Davies', 5: 'Brandon Woodruff', 4: 'Chase Anderson', \
                3: 'Adrian Houser', 2: 'Jhoulys Chacin'}, \
        'MIN': {6: 'Jose Berrios', 5: 'Jake Odorizzi', 4: 'Michael Pineda', \
                3: 'Kyle Gibson', 2: 'Martin Perez'}, \
        'NYM': {6: 'Jason deGrom', 5: 'Zack Wheeler', 4: 'Noah Syndergaard', \
                3: 'Steven Matz', 2: 'Jason Vargas'}, \
        'NYY': {6: 'James Paxton', 5: 'Domingo German', 4: 'Masahiro Tanaka', \
                3: 'J.A. Happ', 2: 'CC Sabathia'}, \
        'OAK': {6: 'Mike Fiers', 5: 'Chris Bassitt', 4: 'Brett Anderson', \
                3: 'Frankie Montas', 2: 'Homer Bailey'}, \
        'PHI': {6: 'Aaron Nola', 5: 'Zach Eflin', 4: 'Jake Arrieta', \
                3: 'Vince Velasquez', 2: 'Drew Smyly'}, \
        'PIT': {6: 'Joe Musgrove', 5: 'Trevor Williams', 4: 'Chris Archer', \
                3: 'Steven Brault', 2: 'Jordan Lyles'}, \
        'SDP': {6: 'Chris Paddack', 5: 'Joey Lucchesi', 4: 'Eric Lauer', \
                3: 'Dinelson Lamet', 2: 'Cal Quantrill'}, \
        'SFG': {6: 'Madison Bumgarner', 5: 'Jeff Samardzija', 4: 'Tyler Beede', \
                3: 'Dereck Rodriguez', 2: 'Shaun Anderson'}, \
        'SEA': {6: 'Marco Gonzalez', 5: 'Mike Leake', 4: 'Yusei Kikuchi', \
                3: 'Felix Hernandez', 2: 'Wade LeBlanc'}, \
        'STL': {6: 'Jack Flaherty', 5: 'Dakota Hudson', 4: 'Miles Mikolas',\
                3: 'Adam Wainwright', 2: 'Michael Wacha'}, \
        'TBR': {6: 'Charlie Morton', 5: 'Yonny Chirinos', 4: 'Blake Snell', \
                3: 'Tyler Glasnow', 2: 'Ryne Stanek'}, \
        'TEX': {6: 'Mike Minor', 5: 'Lance Lynn', 4: 'Ariel Jurado', \
                3: 'Jesse Chavez', 2: 'Adrian Sampson'}, \
        'TOR': {6: 'Marcus Stroman', 5: 'Trent Thornton', 4: 'Jacob Waguespack', \
                3: 'Aaron Sanchez', 2: 'Clay Buchholz'}, \
        'WAS': {6: 'Max Scherzer', 5: 'Stephen Strasburg', 4: 'Patrick Corbin', \
                3: 'Anibal Sanchez', 2: 'Erick Fedde'} } }

starters_by_int = { 2013: { 6: [] , 5: [] , 4: [] , 3: [] , 2: [] }, \
                    2014: { 6: [] , 5: [] , 4: [] , 3: [] , 2: [] }, \
                    2015: { 6: [] , 5: [] , 4: [] , 3: [] , 2: [] }, \
                    2016: { 6: [] , 5: [] , 4: [] , 3: [] , 2: [] }, \
                    2017: { 6: [] , 5: [] , 4: [] , 3: [] , 2: [] }, \
                    2018: { 6: [] , 5: [] , 4: [] , 3: [] , 2: [] }, \
                    2019: { 6: [] , 5: [] , 4: [] , 3: [] , 2: [] } }

for team in starters_by_team[2013]:
    starters_by_int[2013][6].append(starters_by_team[2013][team][6])
    starters_by_int[2013][5].append(starters_by_team[2013][team][5])
    starters_by_int[2013][4].append(starters_by_team[2013][team][4])
    starters_by_int[2013][3].append(starters_by_team[2013][team][3])
    starters_by_int[2013][2].append(starters_by_team[2013][team][2])

for team in starters_by_team[2014]:
    starters_by_int[2014][6].append(starters_by_team[2014][team][6])
    starters_by_int[2014][5].append(starters_by_team[2014][team][5])
    starters_by_int[2014][4].append(starters_by_team[2014][team][4])
    starters_by_int[2014][3].append(starters_by_team[2014][team][3])
    starters_by_int[2014][2].append(starters_by_team[2014][team][2])

for team in starters_by_team[2015]:
    starters_by_int[2015][6].append(starters_by_team[2015][team][6])
    starters_by_int[2015][5].append(starters_by_team[2015][team][5])
    starters_by_int[2015][4].append(starters_by_team[2015][team][4])
    starters_by_int[2015][3].append(starters_by_team[2015][team][3])
    starters_by_int[2015][2].append(starters_by_team[2015][team][2])
    
for team in starters_by_team[2016]:
    starters_by_int[2016][6].append(starters_by_team[2016][team][6])
    starters_by_int[2016][5].append(starters_by_team[2016][team][5])
    starters_by_int[2016][4].append(starters_by_team[2016][team][4])
    starters_by_int[2016][3].append(starters_by_team[2016][team][3])
    starters_by_int[2016][2].append(starters_by_team[2016][team][2])
    
for team in starters_by_team[2017]:
    starters_by_int[2017][6].append(starters_by_team[2017][team][6])
    starters_by_int[2017][5].append(starters_by_team[2017][team][5])
    starters_by_int[2017][4].append(starters_by_team[2017][team][4])
    starters_by_int[2017][3].append(starters_by_team[2017][team][3])
    starters_by_int[2017][2].append(starters_by_team[2017][team][2])

for team in starters_by_team[2018]:
    starters_by_int[2018][6].append(starters_by_team[2018][team][6])
    starters_by_int[2018][5].append(starters_by_team[2018][team][5])
    starters_by_int[2018][4].append(starters_by_team[2018][team][4])
    starters_by_int[2018][3].append(starters_by_team[2018][team][3])
    starters_by_int[2018][2].append(starters_by_team[2018][team][2])
    
for team in starters_by_team[2019]:
    starters_by_int[2019][6].append(starters_by_team[2019][team][6])    
    starters_by_int[2019][5].append(starters_by_team[2019][team][5])
    starters_by_int[2019][4].append(starters_by_team[2019][team][4])
    starters_by_int[2019][3].append(starters_by_team[2019][team][3])
    starters_by_int[2019][2].append(starters_by_team[2019][team][2])

# print(starters_by_int)
