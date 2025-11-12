# crypto_tracker
App that is meant to be run on your desktop and gives you updates on crypto currency prices. At the moment only works on coingecko
## Installation
Just run the app using python
### Prequisites
Requries a coingecko API key
### Installation and Running Program
Base program is run from the CLI. Looks for a file called "CONFIG" that has details of the coins you track. API key must be in a file called keyfile.
.
├── CONFIG     <--create this
├── crypto_tracker.py
├── keyfile    <--create this
├── LICENSE
└── README.md

CONFIG file sample format:
api_key_file=keyfile
symbols=btc,eth
currency=usd
## Credits
Ruwan Samaranayake
## License
Refer to license file in repository
