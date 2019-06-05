# Osiągnięcia 

- Ostateczny wybór środowiska pracy. Wybraliśmy program logisim-evolution. Jest to ulepszona wersja darmowego narzędzia logisim. Dodano do niej przede wszystkim najważniejsze dla naszego projektu wykresy czasowe układów. Dzięki temu bez problemów będziemy mogli debbugować nasz układ.
- Zapoznanie się z podstawami architektury prostych CPU, w szczególności Intelem 4004. Dzięki temu wyodrębniliśmy najważniejsze układy naszego przyszłego CPU to jest: ALU oraz jednostkę sterującą. Oprócz tego procesor będzie składał się jeszcze z pomniejszych elementów takich jak jego zegar, akumulator, rejestry do przechowywania tymczasowych danych oraz informacji odnośnie wykonywanych instrukcji.
- Skonstruowanie 8 bitowego ALU. Może ono wykonywać operacje dodawania oraz odejmowania liczb naturalnych, operacje logiczne na bitach tych liczb oraz ustawia ono 3 flagi: czy wynik jest zerem, flage przeniesienia, flage większości.

# Przemyślenia

- Program do procesora będzie dostarczany po przez pamięć RAM. Pierwsze komórki danych będą zawierały rozkazy dla procesora a następne dane dla niego. Procesor będzie mógł swobodnie zapisywać dane do RAMu a nawet, zgodnie z wolą programisty nadpisywać dane w pamięci. To na programiście będzie ciążyła odowiedzialność w wypadku kiedy przez źle napisany program procesor nadpisał potrzebne dane itp.
- Naszym pierwszym celem będzie zaprojektowanie procesora do wykonywania prostych operacji arytmetycznych na liczbach naturalnych. Następnie będziemy wprowadzać do jego ALU podjednostki odpowiedzialne za wykonywanie zadań na liczbach zespolonych.

# Plany

- Zaprojektowanie jednostki sterującej procesora, która będzie wykonywać trzy etapowy cykl procesora:
  1. pobranie kolejnej instrukcji z pamięci
  2. dekodowanie instrukcji
  3. wykonanie instrukcji
- Zdebbugowanie ewentualnych błędów oraz napisanie pierwszego prostego programu dla procesora.
- Pierwsze projekty podjednostki dla naszego ALU odpowiedzialnej za mnożenie dwóch liczb zespolonych.