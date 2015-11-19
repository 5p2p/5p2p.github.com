---
title: Guida pratica per gli autori del matrimoniofrancescano.it
permalink: guida-pratica/
type: page
---

Di seguito alcune regole pratiche per scrivere un articolo su questo sito.

## Va bene se scrivo gli articoli in Word?

No. Ogni articolo deve essere un semplice file di testo formattato usando il linguaggio *markdown* (vedi sotto). Questo è il tipo di file più semplice e basilare e puo' essere generato con (quasi) qualsiasi programma: dall'email al notepad di Windows. Esistono anche interfaccie apposta sia per Windows che per Mac che facilitano la scrittura in markdown. La cosa più **semplice** in assoluto è usare un editor online come

- <https://stackedit.io>
- <http://dillinger.io>

 Su *Android* un'ottima app si chiama [Jotterpad](https://play.google.com/store/apps/details?id=com.jotterpad.x&hl=en). Tutti e tre questi editor possono anche essere sincronizzati con *Dropbox*.


## Come inizio un nuovo articolo?

Il sistema di pubblicazione consiste in tre stadi:

- draft
- preview
- published

Un articolo si trova nella categoria **draft** quando è ancora una bozza o solo un'idea (infatti si possono creare quanti draft si desiderano e possono anche rimanere incompleti). Ci sono diverse cartelle all'interno di *drafts*, una per ogni coppia che contribuisce al blog. Un draft è definito da una intestazione di questo tipo:

    ---
    title: Ho avuto un'idea geniale
    author: luca
    ---

Sia i tre trattini sopra e sotto che i due tag *title* e *author* sono necessari. Di seguito va scritto il testo dell'articolo. Quindi un tipico draft ha la seguente forma:

    ---
    title: Ho avuto un'idea geniale
    author: luca
    ---
    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 


Quando un articolo è finito di scrivere passa alla fase successiva **preview**. In questo stadio l'articolo viene pubblicato online in forma semi-privata in modo da poter essere letto e corretto. In questa fase l'articolo viene rimosso dalla cartella **drafts** e passa alla cartella **previews**. Qui gli articoli di tutti gli autori stanno insieme. Questi articoli possono essere visionati online su <http://matrimoniofrancescano.it/previews>. Ogni correzione deve essere apportata sul file nella cartella **previews**. La modifica sarà visualizzabile online in seguito. Un tipico articolo in questo stadio ha la forma:

    ---
    title: Ho avuto un'idea geniale
    author: luca
    preview: ok
    ---
    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 

Quindi aggiungendo il tag *preview* l'articolo passa da **drafts** a **previews**.

Quando tutte le correzione sono state apportate l'articolo può essere publicato e passa a **published**. Per poter passare a questa fase bisogna aggiungere delle tags:

    ---
    title: Ho avuto un'idea geniale
    author: luca
    publish: ok
    slug: un-idea-geniale
    date: 10-11-2015
    ---
    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 

- publish: da l'ok per la publicazione
- slug: è una variabile interna che contiene un titolo semplificato dove non ci sono caratteri accentati, maiuscole e gli spazi sono sostituiti da "-".
- date: questa è la data quando l'articolo verrà pubblicato.

Tutte e tre le tags sono necessarie per la pubblicazione. Quando queste sono presenti, l'articolo viene automaticamente rimosso dalla cartella **previews** e va nella cartella **published**. La cartella **published** funge solo da archivio locale, nessuna modifica all'interno di questa cartella andrà online.

Come **esempio** all'interno della cartella dropbox condivisa si trova una cartella chiamata *_templates* che contiene i tre modelli di base per scrivere un articolo.


## Ho scritto un nuovo articolo, come devo chiamare il file?

Ogni nuovo file deve essere chiamato con un nome che non contiene *spazi* e con estensione "md", che sta appunto per markdown

### Sbagliato

    il mio nuovo articolo.txt
    il mio nuovo articolo.doc

### Giusto

    il-mio-nuovo-articolo.md


## Dove devo mettere per le immagini?

Si può inserire al massimo una immagine per articolo. L'immagine va messa nella stessa cartella dell'articolo stesso e viene mossa automaticamente nei vari stadi di pubblicazione. Ad esempio per associare una immagine dal nome 'la-mia-foto.jpg' bisogna modificare l'articolo nel seguente modo:

    ---
    title: Ho avuto un'idea geniale
    author: luca
    preview: ok
    image: la-mia-foto.jpg
    ---
    Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy
    eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam
    voluptua. At vero eos et accusam et justo duo dolores et ea rebum. 


## Che cos'è il markdown?

Ogni articolo deve essere scirtto in *markdown*. Questo è un linguaggio di scrittura semplificato che permettere di formattare un testo senza la necessità di usare programmi come Word. Di seguito una serie esempi su come scrivere in markdown ed il risultato che si ottiene nell'articolo pubblicato.

### Testo in grassetto e corsivo

**Markdown**


    Questo testo ha una **piccola parte in grassetto** ed una seconda parte in *corsivo*


**Diventa**

Questo testo ha una **piccola parte in grassetto** ed una seconda parte in *corsivo*

### Citazioni

**Markdown**


Se invece vuoi scrivere una citazione:

    > Ciò che mi sembrava amaro, mi fu cambiato in dolcezza di anima e di corpo
    <cite>San Francesco</cite>


**Diventa**


> Ciò che mi sembrava amaro, mi fu cambiato in dolcezza di anima e di corpo
<cite>San Francesco</cite>

### Liste

**Markdown**

Ecco una semplice lista:

    - castità
    - povertà
    - obbedienza

Che può essere anche ordinata:

    1. castità
    2. povertà
    3. obbedienza


**Diventa**

Ecco una semplice lista:

- castità
- povertà
- obbedienza

Che può essere anche ordinata:

1. castità
2. povertà
3. obbedienza

### Titolo per una nuova sezione

**Markdown**

    ## Una nuova sezione

    Qui va il testo della nuova sezione bla bla bla


**Diventa**

## Una nuova sezione

Qui va il testo della nuova sezione bla bla bla


