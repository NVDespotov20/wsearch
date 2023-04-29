
# wsearch

wsearch is a Windows CLI web browser


## Installation

### Installing from releases:

Go to the [latest release]("https://github.com/NVDespotov20/wsearch/releases/latest")
and download it.

Extract the contents of the zip folder.

Navigate to the installation directory and run
wsearch.exe from your terminal:

```bash
  .\wsearch.exe "your query goes here"
```

### Building from source:

Clone the repository:
```bash
  git clone https://github.com/NVDespotov20/wsearch.git
```
Navigate the installation directory and install the dependencies:

```bash
  pip install -r requirements.txt
```

Either run main.py or install pyinstaller:

```bash
  pip install pyinstaller
```

And build the executable:

```bash
  pyinstaller --distpath .\ -F main.py -n wsearch
```
## Usage
```bash
usage: wsearch.exe [-h] [-e {neeva,bing,google,duckduckgo}] query [query ...]

Browse the web from the command line

positional arguments:
  query                 Search query

options:
  -h, --help            show this help message and exit
  -e {neeva,bing,google,duckduckgo}, --engine {neeva,bing,google,duckduckgo}
                        Search engine to use
```
## Authors

- [NVDespotov20](https://github.com/NVDespotov20)
- [GGGeorgiev](https://github.com/GGGeorgiev20)

