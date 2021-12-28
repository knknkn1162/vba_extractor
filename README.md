# README.md

```sh
# in directory with excel files
## extract .vba files
docker run -it -v $(pwd):/app/src --rm knknkn1162/olevba -- ./src/ex3.xlsm
```
