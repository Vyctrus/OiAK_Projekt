Program logisim-evolution uruchamiamy z terminala komendą:
java -jar logisim-evolution.jar

Przed przystąpieniem do otwarcia projektu upewniamy się że pliki:
CPUCOmplexGajewskiGierlak.circ i alu3_5v2.circ znajdują się w tym samym katalogu

Aby wczytać projekt wybieramy: File->Open->CPUCOmplexGajewskiGierlak.circ
Jeśli program zapyta o brakującą bibliotekę alu3_5v2.circ, wybieramy w oknie
dialogowym plik alu3_5v2.circ(problem może wystąpić przy pierwszym uruchomieniu projektu)

Aby wczytać program do pamięci RAM znajdującej się po prawej stronie sekcji sterującej
klikamy na niego prawym przyciskiem myszki, wybieram Load image i następnie w oknie dialogowym
otwieramy program do wczytania

Aby wybrać częstotliwość zegara procesora wybieramy zakładkę Simulate->Tick Frequancy,
domyślna częstotliwość to 16 Hz

Symulacje działania procesora włączamy/zatrzymujemy wciśnięciem kombinacji Ctrl-K lub klikając
w zakładce Simulate->Ticks Enabled

Symulacje resetujemy klikając w zakładce Simulate->Reset Simulation

W przypadku złego działania procesora należy sprawdzić w sekcji kontrolnej
czy pamięć ROM nie została wyzerowana. Jeśli tak należy ją wczytać z załączonego
pliku ROM. Robi się to w analogiczny sposób jak w przypadku pamięci ROM

Aby przejść do "wnętrza" któregoś z elementów procesora robimy to kilkając
na wybrany element prawym przyciskiem myszki i wybieramy View 'nazwa elemenut' lub
wybieramy go z panelu obwodów po lewj stronie okna programu.

Głównym obwodem projektu jest CPU otwierający się domyślnie przy starcie programy.
Pod nim znajduje się obwód ControlSection zawierający sekcje sterującą.
W folderze alu3_5v2 znajdują się obwody tworzące ALU procesora.
Główny obwód ALU to ALU_v2


Używanie skryptu do tłumaczenia kodu:
możemy w oparciu o dokumentację napisać program:
082 069 083 044 100 004
Działanie tego programu to: Użyj intrukcji DATA z określonym rejestrem (010) zeby wczytac 069, następnie znowu DATA do rejestru (011) wczytac 044.
Zawieszenie programu JUMP do miejsca gdzie jest JUMP.

W skrypcie, w main, możemy napisać to po prostu:
DATA("010","069")
DATA("011","044")
JUMP("004")
Zostanie wygenerowany plik *.txt w którym będzie zpaisany program w postaci 3digitHex, który przyjmuje procesor.
Należy uważać na JUMP, gdyż nie wiemy, w które miejsce chcemy dokonać skoku, bez podglądu na RAM, zalecane jest zawieszanie programu w stary sposób.

Obecna forma pisania programu na dodanie 2ch liczb:
DATA_INT(regC, 105)
DATA_INT(regD, 68)
ADD(regC, regD)
STORE_RESULTS(regE,regE)
KEEP_IN_PLACE()

w can create simple FOR Loop:
DATA_INT(regC,0)            #2
DATA_INT(regD,1)            #2
DATA_INT(regE,8)            #2
RESET_FLG()                 #1

ADD(regC,regD)              #1
STORE_RESULTS(regC,regC)    #1

COMPARE(regC,regE)          #1
JMP_IF_3("020")             #2
JUMP("007")                 #2
** JUMP("020") **
cell_update_after_jump("020")
KEEP_IN_PLACE()
i dont know how to update ... eureka? ** JUMP("020")** should update CURRENT_CELL corectly and is placed in unreachable section of code, but anyway: u need to play carefullly with jumps if u wish to use CURRENT_CELL variable or KEEP_IN_PLACE, to support calculations i wrote size of each command next to itself.
Todo: convert this into high level function FOR(int i=?, max= ?, step=?) i- start value, max value 4 comparation, step- size of single step (should be 1 in standard loop)

