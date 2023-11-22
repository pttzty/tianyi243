'''
Use a generator generating 0 with probability p, and 1 with probability 1-p
Generate a number from [0,6] with uniform probability
'''

import random

class RandGenerator():
    def zero_one_choice(self, p=0.4):
        return random.choices([0,1],[p,1-p])[0]

    def coin_flip(self, p=0.4):
        res1 = self.zero_one_choice(p)
        res2 = self.zero_one_choice(p)
        res = "{}{}".format(res1,res2)
        if res == '01':
            return "H"
        elif res == '10':
            return "T"
        else:
            return self.coin_flip(p)
    
    def generate_06(self, p=0.4):
        res = "".join([self.coin_flip(p) for _ in range(3)])
        if res == "HHH":
            return 0
        elif res == "HHT":
            return 1
        elif res == "HTH":
            return 2
        elif res == "THH":
            return 3
        elif res == "TTH":
            return 4
        elif res == "THT":
            return 5
        elif res == "HTT":
            return 6
        else:
            return self.generate_06(p)

C = RandGenerator()

print(C.generate_06(p=0.3))

uniform_vector = [C.generate_06(p=0.3) for _ in range(7000)]

print("Total 7000 elements")

for i in range(7):
    print("{} elements for number {} in uniform vector".format(sum([k == i for k in uniform_vector]),i))