import datetime
import numpy as np

class Whale:
    # constructor 
    def __init__(self, name, sex):
        self.name = name
        if sex == "M":
            self.sex = "male"
        else :
            self.sex = "female"
        
        self.birth = datetime.datetime.now()
        print('A {:s} whale named {:s} is born!'.format(self.sex, self.name))

    # determine the printing format  
    def __str__(self):
        return 'A whale named {:s} (age {:s})'.format(self.name, str(self.age))
    
    @property
    def age(self):
        return datetime.datetime.now() - self.birth
    
    def sing(self):
        print('\a')
        print('\a')
        print('\a')
        print('\a')
        print('\a')

if __name__ == "__main__":
    names = ["Ashley","Jake","Amanda","Lily","Sarah","Sam","Emily","Steve","Elizabeth","James",\
    "Megan","Mike","Chris","Matthew","Joe","Andrew","Brandon","Daniel", "Tyler","Mary"]
    ran = np.random.randint(0, 2, 20)
    convert = lambda s : "M" if s == 1 else "F"
    sex_list = [convert(s) for s in ran]
    whales = [Whale(w[0], w[1]) for w in zip(names, sex_list)]

    w = whales[0]
    print(w)
    print(w.name)
    print(w.sex)
    print(w.age)
    w.sing()

    
