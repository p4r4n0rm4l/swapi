# swapi
## _A test project for the Star Wars API (SWAPI)_

The Star Wars API, or "swapi" (Swah-pee) is the world's first quantified and programmatically-accessible data source for all the data from the Star Wars canon universe!

## Features

- Search for a Star Wars Hero
- Take information about his name, height, mass, birth year and his homeworld
- Get information about his world in relation with Earth
- Cache already searched queries
- Clear the cache when you want to

## Installation

swapi requires python 3.9.0 to run.

To install follow the instructions

```sh
python3 -m venv name_of_your_venv
git clone https://github.com/p4r4n0rm4l/swapi.git
cd swapi
pip install -r requirements.txt
```

## Commands

For Help:
```sh
python main.py -h
```

Search for a Star Wars hero:
```sh
python main.py --search "SWHero"
```

Take more information about the hero`s Homeworld:
```sh
python main.py --search "SWHero" --world
```

Clear search cache:
```sh
python main.py --clear_cache
```

## Examples of input/output
Input:
```sh
python main.py --search "luke sky"
```
Output:
```sh
Name:  Luke Skywalker
Height:  172
Mass:  77
Birthday:  19BBY
```

Input:
```sh
python main.py --search "leia" -w
```
Output:
```sh
Name:  Leia Organa
Height:  150
Mass:  49
Birthday:  19BBY
On Alderaan 1 year on earth is 0.9972602739726028 and 1 day 1.0 days.
```

If the search is already cached then:
Output:
```sh
Name:  Leia Organa
Height:  150
Mass:  49
Birthday:  19BBY
On Alderaan 1 year on earth is 0.9972602739726028 and 1 day 1.0 days.
Cached: 2021-04-27 20:47:02.516888
```