Filip Gajewski 236597, Andrzej Gierlak 236411											23.05.2019

Raport z projektu z Organizacji i Architektury Komputerów
Temat: Projekt i implementacja procesora liczącego na liczbach zespolonych

# Osiągnięcia

- Poszerzenie słowa procesora z 8 do 11 bitów dzięki czemu liczba rejestrów swobodnego dostępu zwiększyła się z 4 do 8 oraz kody operacji dla ALU i pamięci zostały poszerzone z 3 do 4 bitów.
- Przeprojektowanie dotychczasowego zegara procesora. Poprzednio składał się on z 3 pod zegarów, których taktowanie zależało od jednego zegara nadrzędnego. 3 zegary podrzędne wysyłały swoje sygnały do sekcji kontrolnej, która samodzielnie sterowała dostępami do wszystkich rejestrów w procesorze i pamięci RAM.
  Obecnie cały procesor jest taktowany jednym zegarem. Są do niego podłączone wszystkie znajdujące się w CPU rejestry, pamięć RAM oraz sekcja kontrolna.
- Przeprojektowanie steppera zarządzającego jednostką sterującą. Tak jak w przypadku całego procesora cały stepper, jego wewnętrzna budowa, został uzależniony wyłącznie od jednego zegara procesora. 
- Zaprojektowanie i implementacja ALU wykonującego operacje na liczbach zespolonych. Liczby są dostarczane w postaci czterech rejestrów 11 bitowych A,B,C i D. Pierwsze dwa przechowują częścią rzeczywiste liczb a pozostałe urojone. ALU wykonuje 4 działania arytmetyczne, zespolone(dodawanie, odejmowanie, dzielenie, mnożenie) oraz porównanie rejestrów A i B. ALU wyznacza też kwadrat modułu liczby zespolonej.
- Procesor po wykonaniu całego programu "zawiesza się" do momentu zresetowania całego układu. Realizowane jest to jako skok w to samo miejsce w pamięci gdzie znajduję się instrukcja skoku, kodowana 0x100.
-  Obecnie ALU nie zostało jeszcze w pełni połączone z jednostką sterującą.

# Plany

- Pełne podłączenie ALU do jednostki sterującej.
- Napisanie próbnych programów testujących działanie CPU.
- Oszacowanie złożoności czasowej i obszarowej CPU (badanie użytych elementów programu Logisim-evolution)

