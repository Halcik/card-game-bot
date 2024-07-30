# <p style="text-align: center; color: Wheat">Card Game Bot</p>

Jest to bot, którego docelową funkcją będzie rozegranie całej gry w karty. Przed ostateczną wersją ma skupić się na analizie posiadanych w grze kart i proponować, które użyć w trwającej rundzie, by z największym prawdopodobieństwem pokonać przeciwnika.
>Obecnie projekt jest na etapie tworzenia samego obiektu karty na podstawie testowych screenów.

***
## <p style="text-align: center; color: Wheat">Klasa Card</p>

 Tworzy <span style="color: green">obiekt karty</span>, która posiada:

- przekształcone zdjęcie do odczytu danych <span style="color: green">**[image_read]**</span>,

- ilość gwiazdek do ulepszeń karty **<span style="color: green">[n_stars]**</span>,

- wartości mocy w kolejności: fioletowa (dowództwo), zielona (zręczność), niebieska (inteligencja), czerwona (siła), suma <span style="color: green">**[powers]**</span>,

- ilość energii <span style="color: green">**[energy]**</span>,

- numer karty w grze <span style="color: green">**[n_card]**</span>,

- pozycja karty <span style="color: green">**[position]**</span>,

- level karty - ustalany przy pierwszym rozpoznaniu <span style="color: green">**[level]**</span> ***chwilowo nie wiem, czy będzie jednak potrzebna***.

#####

  Oprócz tego posiada <span style="color: LightSkyBlue">metody</span>:

- <span style="color: LightSkyBlue">**take_screenshoot**</span> - robiąca screena tworzonej lub aktualizowanej karty,

- <span style="color: LightSkyBlue">**change_image**</span> - zmieniającą screena karty w postać do odczytu danych,

- <span style="color: LightSkyBlue">**set_level**</span> - ustalającą level karty - ***chwilowo nie wiem, czy będzie potrzebna, patrząc na to, że pozycję zaczęłam ustawiać względem sumy mocy***,

- <span style="color: LightSkyBlue">**get_stars**</span> - ustala ilość gwiazdek do ulepszenia,

- <span style="color: LightSkyBlue">**set_position**</span> - ustalenie pozycji karty i zwrócenie jej numeru,

- <span style="color: LightSkyBlue">**get_powers**</span> - pobranie mocy z karty,

- <span style="color: LightSkyBlue">**use**</span> - oznacza użycie karty i aktualizuje jej energię (zmniejsza ją o 1),

- <span style="color: LightSkyBlue">**update_stars**</span> - aktualizuje dostępną liczbę ulepszeń,

- <span style="color: LightSkyBlue">**get**</span> - metoda tworząca kartę - dostępna za pomocą odwołania się do nazwy klasy (Card.get()) ze sprawdzaniem, czy nowa karta nie przekroczy maksymalnej ilości kart,

- <span style="color: LightSkyBlue">**sum_of_powers**</span> - metoda klasy, która zlicza moc wszystkich kart. Bez podania argumentu - sumę wszystkich, gdy natomiast podamy, to odpowiedniej mocy.

#####

...oraz <span style="color: Orange">statyczne pola</span>:

- <span style="color: Orange">**star**</span> - przechowuje odczytaną gwiazdkę,

- <span style="color: Orange">**n_cards**</span> - liczba kart istniejących w danej grze (niekoniecznie już aktywnych). Istotne przy ustalaniu kolejności kart - nowsza karta=wyższa pozycja,

- <span style="color: Orange">**positions**</span> - lista z kartami (ich słabymi referencjami do obiektu), na której operujemy zmianą kolejności.

***
## <p style="text-align: center; color: Wheat">Zasady gry</p>

Wspinaczka - karty

- składa się z czterech etapów
- na start dostajemy 3 losowe karty
- możemy mieć max 6 kart
- każda karta ma swoje moce oraz energię
- jedna karta może mieć max 4 punkty energii
- moce:
 	- fioletowa - dowództwo
 	- zielona - zręczność
 	- niebieska - inteligencja
 	- czerwona - siła
- boss ma wszystkich mocy po 18 pkt.
- dostępne premie po poziomach:
 	- boska karta
 	- zwiększenie poziomu
 	- odzyskanie energii
 	- dopalacze (teoretycznie najmniej opłacalne)
- etap pierwszy
 	- rozpoznanie kart i zliczenie ich początkowej mocy, by ułatwić dalsze dobieranie
 	- idziemy prawą ścieżką zawsze
 	- priorytety na ten etap:
  		- wymaksowanie niebieskich
  		- zdobycie dużej ilości koni
  		- utrzymanie energii

***
## <p style="text-align: center; color: Wheat">Określanie pozycji kart - notatka na przyszłość</p>

- Wyjaśnienie oznaczeń:
  - <span style="color: Plum">F</span> - karta fioletowa (najwyższy level)
  - <span style="color: Gold">G</span> - karta złota
  - <span style="color: Turquoise">N</span> - karta niebieska
  - <span style="color: Silver">SZ</span> - karta szara (najniższy level)
  - liczba za skrótem oznacza ilość gwiazdek (ulepszeń) w grze
- Jest ona zależna od:
  - sumy mocy kart
  - kolejności dodania do gry (nowsza karta = wyższe miejsce, gdy suma jest taka sama)
- Sumy mocy kart w zależności od poziomu i ilości gwiazdek:
  - <span style="color: Plum">F5</span> (**27**)
  - <span style="color: Plum">F4</span> (**23**)
  - <span style="color: Gold">G4</span> (**21**)
  - <span style="color: Plum">F3</span> (**19**)
  - <span style="color: Gold">G3</span> (**17**)
  - <span style="color: Plum">F2</span> i <span style="color: Turquoise">N3</span> (**15**)
  - <span style="color: Gold">G2</span> (**13**)
  - <span style="color: Plum">F1</span> i <span style="color: Turquoise">N2</span> (**11**)
  - <span style="color: Gold">G1</span> i <span style="color: Silver">SZ2</span> (**9**)
  - <span style="color: Turquoise">N1</span> (**7**)
  - <span style="color: Silver">SZ1</span> (**5**)
