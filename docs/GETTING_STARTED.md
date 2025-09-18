# Getting started

## Install (from source)

```bash
git clone https://github.com/yourname/hktoll.git
cd hktoll
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e ".[dev]"
```

## Fetch datasets

The first run will download and cache the official datasets into your user cache directory.
You can prefetch them:

```bash
hktoll refresh-data
```

## Try the CLI

```bash
hktoll route --coords "114.1582,22.2799;114.1721,22.2975"
```
