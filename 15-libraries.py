#!/Users/neal/venv/python-test/bin/python
# coding: utf8

# 2023-09-18
#
# 15 Python Libraries You Should Know About in 2023
# https://www.youtube.com/watch?v=o06MyVhYte4&t=9s
#

# 1. BETTER DATETIME
# Pendulum: https://pendulum.eustace.io
# NOTES:
# found some issues with the objects in the site examples!
import pendulum

print("\nPython library: pendulum")
dur = pendulum.duration(days=15)
# More properties
dur.weeks
dur.hours
# Handy methods
dur.in_hours()
# 360
dur.in_words()
#'2 weeks 1 day'

dt = pendulum.now()
# A period is the difference between 2 instances
period = dt - dt.subtract(days=3)
period.in_days()


in_utc = pendulum.datetime(2013, 3, 31, 0, 59, 59)
tz = pendulum.timezone("Europe/Paris")
in_paris = tz.convert(in_utc)
print(in_utc)
print(in_paris)


# 2. pypdf
# https://pypdf.readthedocs.io/en/stable/
# NOTES:
# Doesn't export with proper linefeeds (none w/ text and added for emojis)
# In the docs, "extracting text is hard"
import pypdf

from pypdf import PdfReader

print("\nPython Library: pypdf")
reader = PdfReader("example.pdf")
page = reader.pages[0]
print(page.extract_text())

# 3. Make debugging easier: icecream
# https://github.com/gruns/icecream
# NOTES:
# syntax highlighed output - prints funcion name and args to func - amazing
# will do this for dictionaries
print ("\nPython module: icecream / ic")
import time
from icecream import ic
 
def unixTimestamp():
    return '%i |> ' % int(time.time())
ic.configureOutput(prefix=unixTimestamp)
ic('world')
# 1519185860 |> 'world': 'world'

# 4. stupidly simple python logging: loguru
# https://github.com/Delgan/loguru
# NOTES:
# better view of entire stack trace; colors
#
print("\nPython library: loguru")
from loguru import logger

logger.debug("That's it, beautiful and simple logging!")

# 5. rich text and beautiful formatting in the terminal.: rich
# https://github.com/Textualize/rich
# NOTES:
# display tables
# writes markdown

print("\nPython library: rich")
from rich.console import Console
from rich.markdown import Markdown

console = Console()
console.print("Hello", "World!", style="bold red")

with open("README.md") as readme:
    markdown = Markdown(readme.read())
console.print(markdown)

# 6. Easy Command Line Interface creation: argparse
# https://docs.python.org/3/library/argparse.html
# 

# 7. progress bars: tqdm
# https://github.com/tqdm/tqdm
# NOTES:
#

print("\nPython library: tqdm")
from tqdm import tqdm
from time import sleep

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    sleep(0.25)
    text = text + char
    
# 8. working with multi-dimensional data: xarray
# https://github.com/pydata/xarray
# indexing, attributes, computation, GroupBy, Plotting, pandas, datasets

# 9. DataFrame library written in rust: Polars
# https://github.com/pola-rs/polars
# good for REALLY LARGE datasets; better than pandas
# multi-threating
# SQL querying data

# 10. seaborn: statistical data vistualization
# https://seaborn.pydata.org/
# very easily create beautiful charts and graphs
# provide data and it will plot automatically using themes/colors

# 11. railroad oriented programming: result
# Result: https://pypi.org/project/result/
# alternative to handling errors/exceptions such as bad input
# better flow handling errors

print("\nPython library: result")
from result import Result, Ok, Err

def divide(a: int, b: int) -> Result[int, str]:
    if b == 0:
        return Err("Cannot divide by zero")
    return Ok(a // b)

values = [(10, 0), (10, 5)]
for a, b in values:
    divide_result = divide(a, b)
    match divide_result:
        case Ok(value):
            print(f"{a} // {b} == {value}")
        case Err(e):
            print(e)

# 12: data validation library: pydantic
# Pydantic: https://docs.pydantic.dev/latest/
# used by a lot of libraries in python ecosystem

# 13: FastAPI - build APIs fast, easy and ready for production
# FastAPI: https://fastapi.tiangolo.com

# 1. code in main.py
# 2. run the server using: uvicorn main:app --reload
# 3. curl http://127.0.0.1:8000/items/5?q=somequery

print("\nPython library: FastAPI")
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 14: SQLModel - interact with SQL databases from Python code w/ Python objects
# Sqlmodel: https://sqlmodel.tiangolo.com
# object relational mapping library
# connect your api to sql/sqlite using python types
print("\nPython library: sqlmodel\n")
from typing import Optional
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = -1

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

# itterate through the list of heros and use a ternary to print if a value exists
for hero in (hero_1, hero_2, hero_3):
    print("The hero", hero.name, "is really", hero.secret_name, 
          "aged " + str(hero.age) + "!" if hero.age > 0 else "\b!")


# 15. Httpx: https://github.com/encode/httpx
# dealing with async requests
print("\nPython library: httpx\n")
import httpx
r = httpx.get('http://checkip.amazonaws.com/')
print(r, '\n', r.status_code, '\n', r.headers, '\n', r.text)


# bonus: Python-dotenv: https://saurabh-kumar.com/python-dotenv/
# Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. 
# It helps in the development of applications following the 12-factor principles.
# NOTE: Not working in python@3.11
