Cards Against Blockchain
==========================

Cards Against Blockchain is a fork of [Cards Against Cryptography](https://github.com/CardsAgainstCryptography/CAC), and based on Cards Against Humanity.  Cards Against Humanity describes itself as "a party game for horrible people", and Cards Against Blockchain strives to be equally mean.  If you don't like crude or offensive humor, this game may not be for you.  We hope this game is played in a spirit of fun, and even played on-chain.

Basic Rules
-----------

See [RULES.md](https://github.com/CardsAgainstBlockchain/CardsAgainstBlockchain/blob/master/RULES.md) for the rules.

License
-------

<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/2.0/88x31.png" />

Cards Against Blochchain was based on Cards Against Humanity, which was released under a Creative Commons BY-NC-SA 2.0 license (https://creativecommons.org/licenses/by-nc-sa/2.0/).  All files in this repository are covered by this license, except the actual Cards Against Blockchain card files.  You can threfore use, remix, and share this repository for free, but cannot sell it.

<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" />

The Cards Against Blockchain card files in src/*.txt are both released under the more permissive <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

Contributing
------------

You can submit pull requests to propose new cards; see `src/black.txt` and `src/white.txt`.

Please check out the original Cards Against Humanity decks, either by purchase of free download at https://www.cardsagainsthumanity.com/, or download from another source like http://mdsc.info/dropbox/cah/ 

You might gleen ideas from news archives like web3isgoinggreat.com or rekt.news too.

Building
--------

Install the required dependencies:

    `pacman -S texlive-core texlive-latexextra texlive-fontsextra texlive-pictures`
    `pacman -S ttf-dejavu ttf-liberation`

The top-level Makefile can be used to recompile printable PDF and PNG versions of the cards:

    `make PDFs PNGs`

You can build specific releases of the cards using environment variables, e.g.

    `make PDFs PNGs WHITE=white-ec19-expansion BLACK=black-ec19-expansion`

Printed copies
--------------

Since Cards Against Humanity was released under a BY-NC-SA 2.0 license, the "non-commercial" aspect of that license implies that we cannot sell you a copy of this game.  You can make your own printed copy in three ways.  

1. **Print at home.**  Under the `PDFs-to-print` folder, there are printable PDFs of all the cards, formatted for 2-sided printing on either A4 or letter paper.  You'll use up all the toner if print pages and pages of all-black backgrounds, so you should probably use the gray background.  
2. **Print at a local printshop.** You could also take the PDFs to your local print shop and have them print it on cardstock (80-pound or higher).  Use a paper cutter to cut out the cards.
3. **Print via a commercial custom card manufacturer.**  We printed our version of Cards Against Blockchain using MakePlayingCards.com.  The folder `PNGs-to-print` contains the PNG images required to print a deck of cards at MakePlayingCards.com's [US Game Deck Size](https://www.makeplayingcards.com/design/custom-us-game-deck-size-cards.html), along with a [bi-fold (4 side) instruction booklet](https://www.makeplayingcards.com/pops/booklet-guide.html).  At the time we wrote this, 1 set of cards, along with a booklet and plain white box, is $34.35 (US dollars), plus shipping (approximately $10 for standard shipping to most countries).  Uploading the images and configure the project takes about 10 minutes.
