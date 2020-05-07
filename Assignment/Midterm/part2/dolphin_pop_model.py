import numpy as np
import string
from numpy.random import randn
import random
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import networkx as nx


'''
get male names from website
'''
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

'''
get male names from website
'''
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

'''
generate the next name by sex
'''
def generate_names(sex) :
    if (sex == "M") :
        male_file = open("males.dat", "r")
        for m in male_file:
            yield m
        # if ran out names, add middle name
        male_file = open("males.dat", "r")
        for m in male_file:
            letters = string.ascii_lowercase
            middle_name = ''.join(random.choice(letters) for i in range(10))
            yield m + ' ' + middle_name  
    else :
        female_file = open("females.dat", "r")
        for f in female_file:
            yield f
        # if ran out names, add middle name
        female_file = open("females.dat", "r")
        for f in female_file:
            letters = string.ascii_lowercase
            middle_name = ''.join(random.choice(letters) for i in range(10))
            yield f + ' ' + middle_name

'''
define a class Dolphin
'''
class Dolphin:
    def __init__(self, name, sex, mother, father):
        self.name = name
        self.sex = sex
        self.age = 0
        self.years_since_procreation = 0
        self.mother = mother
        self.father = father
        self.death = int(random.gauss(35, 5))
        self.status = "alive"

    def __str__(self):
        return ("Dolphin's name is {:s}, age is {:d}, gap is {:d}, death is {:d}\n".format(self.name, self.age, self.years_since_procreation, self.death))
    
    def age_record(self):
        self.age += 1
        if self.age > self.death:
            self.status = "died"

        self.years_since_procreation += 1

    def request_procreation(self, another):
        if self.status == "died" or another.status == "died":
            return False
        if (self.sex == another.sex) :
            return False
        if (self.age <= 6) :
            return False
        if (abs(self.age - another.age) > 10) :
            return False
        if (self.years_since_procreation < 5) :
            return False
        if (self.mother == another.name) :
            return False
        if (self.father == another.name) :
            return False
        if (self.father == another.father and self.mother == another.mother) :
            return False
        return True

    def can_breeding(self) :
        return self.status == "alive" and self.age > 6 and self.years_since_procreation >= 5

'''
breeding
'''
def procreate():
    total = np.zeros(shape=(10,150))
    for i in range(1, 11):
        print("Trial No. {:d}".format(i))
        birth = 0
        male_names = generate_names("M")
        female_names = generate_names("F")
        females = []
        males = []
        for year in range(150):
            breeding_num = 0
            if year == 0:
                females.append(Dolphin(next(female_names), "F", next(female_names), next(male_names)))
                females.append(Dolphin(next(female_names), "F", next(female_names), next(male_names)))
                males.append(Dolphin(next(male_names), "M", next(female_names), next(male_names)))
                males.append(Dolphin(next(male_names), "M", next(female_names), next(male_names)))
            population = len(females) + len(males)

            male_breeding_num = 0
            for d in males:
                if d.can_breeding():
                    male_breeding_num += 1
            female_breeding_num = 0
            for d in females:
                if d.can_breeding():
                    female_breeding_num += 1
            breeding_num = male_breeding_num + female_breeding_num
            
            for y in males:
                if (len(females) == 0):
                    continue
                x = (random.sample(females, 1))[0] 
                if (y.request_procreation(x)):
                    gender = ["F", "M"]
                    sex = random.choice(gender)
                    if (sex == "F"):
                        birth += 1
                        new_born = Dolphin(next(female_names), "F", x.name, y.name)
                        females.append(new_born)
                    else :
                        birth += 1
                        new_born = Dolphin(next(male_names), "M", x.name, y.name)
                        males.append(new_born)
                    y.years_since_procreation = 0
                    x.years_since_procreation = 0
                    continue
                
            for dolphin in males:
                dolphin.age_record()
                if dolphin.status == "died":
                    males.remove(dolphin)
            for dolphin in females:
                dolphin.age_record()
                if dolphin.status == "died":
                    females.remove(dolphin)
            living_population = len(females) + len(males)
            total[i-1][year] = living_population

            if (year % 25 == 0) :
                print("##################################################")
                print("entering year {:d} with {:d} dolphins, with {:d} breeding.".format(year, population, breeding_num))
            if (year == 100):
                print("at year 100, there are {:d} living dolphins, there have been {:d} births, in total".format(living_population, birth))
            if (year == 149):
                print("at year 149, there are {:d} living dolphins".format(living_population))
        
        print("**************************************************")
    return total

    
'''
draw the picture
'''
def draw():
    x = np.arange(0, 150)
    total = np.zeros(shape=(10,150))
    total = procreate()
    mean_array = np.mean(total, axis=0)
    std_array = np.std(total, axis=0)
    fig, ax = plt.subplots(figsize = (10, 10))
    ax.plot(x, mean_array, '-')
    ax.plot(x, mean_array-std_array, '-', color='blue', alpha=0.4)
    ax.plot(x, mean_array+std_array, '-', color='blue', alpha=0.4)
    ax.fill_between(x, mean_array-std_array, mean_array+std_array, color='blue', alpha=0.2)
    plt.xlabel('Years')
    plt.ylabel('Number of Living Dolphins')
    plt.title('Average Population and Standard Deviation from 10 Trials')
    plt.savefig('population_growth.pdf')
    plt.show()

def find_min_prob_male():
    probabilities = np.arange(0., 0.501, 0.01)
    p_array = np.zeros(5)
    for i in range(0, 5):
        for p in probabilities:
            male_names = generate_names("M")
            female_names = generate_names("F")
            females = []
            males = []
            living_population = 0
            for year in range(150):
                if year == 0:
                    females.append(Dolphin(next(female_names), "F", next(female_names), next(male_names)))
                    females.append(Dolphin(next(female_names), "F", next(female_names), next(male_names)))
                    males.append(Dolphin(next(male_names), "M", next(female_names), next(male_names)))
                    males.append(Dolphin(next(male_names), "M", next(female_names), next(male_names)))
                for y in males:
                    if (len(females) == 0):
                        continue
                    x = (random.sample(females, 1))[0]
                    if (y.request_procreation(x)):
                        gender = ["F", "M"]
                        sex = (random.choices(gender, k=1, weights=[1-p, p]))[0]
                        if (sex == "F"):
                            new_born = Dolphin(next(female_names), "F", x.name, y.name)
                            females.append(new_born)
                        else :
                            new_born = Dolphin(next(male_names), "M", x.name, y.name)
                            males.append(new_born)
                        y.years_since_procreation = 0
                        x.years_since_procreation = 0
                        continue
                
                for dolphin in males:
                    dolphin.age_record()
                    if dolphin.status == "died":
                        males.remove(dolphin)
                for dolphin in females:
                    dolphin.age_record()
                    if dolphin.status == "died":
                        females.remove(dolphin)
                living_population = len(females) + len(males)
            if living_population > 0:
                p_array[i] = p
                break
    print("The average minimum probability for P(male) is {:0.001f}".format(np.mean(p_array)))
    return np.mean(p_array)


    import networkx as nx

def draw_pic():
    male_names = generate_names("M")
    female_names = generate_names("F")
    females = []
    males = []
    for year in range(71):
        if year == 0:
            females.append(Dolphin(next(female_names), "F", next(female_names), next(male_names)))
            females.append(Dolphin(next(female_names), "F", next(female_names), next(male_names)))
            males.append(Dolphin(next(male_names), "M", next(female_names), next(male_names)))
            males.append(Dolphin(next(male_names), "M", next(female_names), next(male_names)))
            
        for y in males:
            if (len(females) == 0):
                continue
            x = (random.sample(females, 1))[0]
            if (y.request_procreation(x)):
                gender = ["F", "M"]
                sex = random.choice(gender)
                if (sex == "F"):
                    new_born = Dolphin(next(female_names), "F", x.name, y.name)
                    females.append(new_born)
                else :
                    new_born = Dolphin(next(male_names), "M", x.name, y.name)
                    males.append(new_born)
                y.years_since_procreation = 0
                x.years_since_procreation = 0
                continue

        for dolphin in males:
            dolphin.age_record()
            if dolphin.status == "died":
                males.remove(dolphin)
        for dolphin in females:
            dolphin.age_record()
            if dolphin.status == "died":
                females.remove(dolphin)

    # draw the graph
    dol = random.choice(females)
    parents = [dol.mother, dol.father]
    siblings = []
    full_siblings = []
    half_siblings = []
    for x in females:
        if x.name == dol.name:
            continue
        if x.name == dol.mother:
            continue
        if x.mother == dol.mother and x.father == dol.father:
            full_siblings.append(x)
            continue
        if x.mother == dol.mother or x.father == dol.father:
            half_siblings.append(x)
            continue
    for x in males:
        if x.name == dol.name:
            continue
        if x.name == dol.father:
            continue
        if x.mother == dol.mother and x.father == dol.father:
            full_siblings.append(x)
            continue
        if x.mother == dol.mother or x.father == dol.father:
            half_siblings.append(x)
            continue
    
    G = nx.Graph()
    G.add_edge(dol.name, parents[0])
    G.add_edge(dol.name, parents[1])
    pos = {parents[0]:(0,0), parents[1]:(1,0), dol.name:(0, -1)}
    for i, d in enumerate(full_siblings):
        G.add_edge(d.name, parents[0])
        G.add_edge(d.name, parents[1])
        pos[d.name] = (i+2, -1)
    for j, d in enumerate(half_siblings):
        if d.mother == parents[0]:
            G.add_edge(d.name, parents[0])
            pos[d.name] = (j+1, -2)
        if d.father == parents[1]:
            G.add_edge(d.name, parents[1])
            pos[d.name] = (j+1, -2)

    nx.draw(G, pos = pos, with_labels=True)
    plt.savefig("genealogy.pdf")
    # display
    plt.show() 

if __name__ == "__main__":
    draw()
    find_min_prob_male()
    draw_pic()

'''
I didn't find the plot file
you should save it as and pdf file    -5
'''