# Adhesome.org

This project is a series of jinja templates designed to construct the static adhesome.org based on the database in `data/db.sqlite3`.

## Build

```bash
# install required dependencies
pip install -r requirements.txt
# build site, output is in build/
python build.py
```

## Publish to Github Pages

```bash
# TODO: configure config.py base to /adhesome if publishing to a /adhesome subdirectory
# fix issues with gh-pages in non-npm project
touch package.json
# fix any clone issues with lfs
git lfs install --skip-smudge
# actually publish build directory to gh-pages branch
npx gh-pages -d build
```

## Publish with Docker

```bash
docker build -t maayanlab/adhesome:1.0.0 .
docker push maayanlab/adhesome:1.0.0
```
