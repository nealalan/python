#!/Users/neal/venv/python-test/bin/python
# coding: utf8

"""Code to demonstrate sqlmodel and a ternary in a print"""

# 2023-10-03
# 14: SQLModel - interact with SQL databases from Python code w/ Python objects
# Sqlmodel: https://sqlmodel.tiangolo.com
# object relational mapping library
# connect your api to sql/sqlite using python types

from typing import Optional
from sqlmodel import Field, SQLModel

print("\nPython library: sqlmodel\n")

class Hero(SQLModel, table=True):
    """class creating the Hero object"""
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

#OUTPUT:
#Python library: sqlmodel
#
#The hero Deadpond is really Dive Wilson!
#The hero Spider-Boy is really Pedro Parqueador!
#The hero Rusty-Man is really Tommy Sharp aged 48!
#
