# PageDownloader
## ITALIANO 
Scarica tutto il contenuto disponibile su una pagina web (no video di solito)

Se avete Windows tutto apposto vi basta un versione recente di python installata (io avevo la 3.10.0rc2).

Se avete un Mac dovete fare da terminale :
- " pip3 install tkmacosx " ed usare la versione dell'interprete sul quale avete installato il pacchetto ( se non avete scaricato più versioni di python tutto apposto)

Se avete Linux (generico) vi potrebbe mancare la libreria di tkinter quindi:
- sudo apt-get install python3-tk 

La grafica è molto intuitiva :
- Scegliete una cartella dove salvare i file (ad esempio Uni->esami->EsameX).
- Dategli l'url della pagina interessata nella riga sotto
- Alcuni per scaricare i file chiedono username e password ma sono opzionali
- In ultimo dovete scegliere se scaricare la singola pagina o tutto. Io vi consiglio tutto perchè l'altra potrebbe non funzionare correttamente per alcuni siti ma fate delle prove.

Per eseguire:
- Da terminale andate nella cartella del progetto e scrivete "python3 main.py"

Potete anche lanciare direttamente l'eseguibile "main" se avete Mac o linux ma dovete prima dare i permessi :
- Sempre da terminale andate nella cartella del progetto
- chmod +x main
 Et voilà, la grafica se lo lanciate da terminale forse è un po' peggio. Fate come preferite.

P.S. : Non ho fantasia di riorganizzare le cartelle, so che fa schifo così ma capitemi.


## ENG
Downloads all available files on web page

Sorry for all the chaos in project folder but I'm too lazy, by the way if someone will join the project I ensure you I will organize it better :)

Requirements:
- Recent version of Python3 installed (I used 3.10.0rc2 but it's optional)

Additional step for Linux users ->
MacOS and Windows python versions have Tkinter embedded, you probably not so :
- sudo apt-get install python3-tk (since u're using linux you already know )

Only MacOS users :
- pip3 install tkmacosx (Dark mode can break Tkinter library, this extension will fix)

This program will download all avaible files on a web page inside your desired folder.

Usage:
- Pick-A-Folder using button or writing 
- Copy-paste the URL of the desired web page (web page with all pdf files)
- Username and password optionals (sometimes are needed)
- Pick "single page" or "All pages" on your needs (sometimes "single page" can be lazy so
  if you don't find what you're looking for in your folder try with "All pages"
 
 That's it, have fun!
