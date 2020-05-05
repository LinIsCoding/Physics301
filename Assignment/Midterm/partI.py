import numpy as np
from numpy.random import randn
from math import abs
import random
from bs4 import BeautifulSoup
import requests


def get_male_names():
    file_path= "males.dat"
    file = open(file_path,"w")
    for i in range(1, 76):
        url = "http://www.prokerala.com/kids/baby-names/boy/page-{:d}.html".format(i)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        list = soup.select('span a')
        names = [item.text for item in list[:100]]
        for name in names:
            file.write(name + '\n') 
    file.close()    

def get_female_names():
    file_path= "females.dat"
    file = open(file_path,"w")
    for i in range(1, 76):
        url = "http://www.prokerala.com/kids/baby-names/girl/page-{:d}.html".format(i)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        list = soup.select('span a')
        names = [item.text for item in list[:100]]
        for name in names:
            file.write(name + '\n')
    file.close()

def generate_names(sex) :
    if (sex == "M") :
        male_file = open("males.dat", "r")
        for m in male_file:
            yield m
        # if ran out names, add middle name
        for m in male_file:
            letters = string.ascii_lowercase
            middle_name = ''.join(random.choice(letters) for i in range(10))
            yield m + ' ' + middle_name
    
    else :
        female_file = open("females.dat", "r")
        for f in female_file:
            yield f
        # if ran out names, add middle name
        for f in female_file:
            letters = string.ascii_lowercase
            middle_name = ''.join(random.choice(letters) for i in range(10))
            yield f + ' ' + middle_name
      

class Dolphins:
    def __init__(self, name, sex, mother, father):
        self.name = name
        self.sex = sex
        self.age = 0
        self.years_since_procreation = 0
        self.mother = mother
        self.father = father
        self.death = int(randn()*5 + 35) # gausian distribution
        self.status = "alive"

    def age_record(self):
        self.age += 1
        if self.age > self.death:
            self.status = "died"

        self.years_since_procreation += 1
        self.years_since_procreation %= 6

    def request_procreation(self, another):
        if (self.sex == another.sex) :
            return false
        if (self.age < 6) :
            return false
        if (abs(self.age - another.age) > 10) :
            return false
        if (self.years_since_procreation < 5) :
            return false
        if (self.mother.name == another.name) :
            return false
        if (self.father.name == another.name) :
            return false
        if (self.father.name == another.father.name && self.mother.name == another.mother.name) :
            return false
        return true

        '''
        dolpthins' death should follow gausian distribution     -5
        '''