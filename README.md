# potboiler
Minimal Flask+Docker Boilerplate

### Installation

```
docker build -t potboiler .
docker run -it --rm potboiler pytest
```

If tests run okay, start the Flask server (the default command).

```
docker run -it --rm -p 80:5000 potboiler
```
