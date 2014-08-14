# vimtips-search

Fuzzy Search vim tips from http://zzapper.co.uk/vimtips.html

##Setup

```bash
$ git clone https://github.com/ninegene/vimtips-search.git
$ cd vimtips-search
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

##Testing
```bash
$ python build-json.py
$ python -m SimpleHTTPServer 8000
```
Navigate to [http://localhost:8000/](http://localhost:8000/)
