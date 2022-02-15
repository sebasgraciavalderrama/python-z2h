from collections import Counter
from collections import defaultdict
from collections import namedtuple

mylist = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3]
mylist1 = [1,1,1,1,1,'a','a','a',2,3,3,3,3,3,3]
print(Counter(mylist))
print(Counter(mylist1))
print(Counter('aaaabbbjjjjhsgygyhbbdbd'))
sentence = "How many times does each word show up in this sentence with a word"
print(Counter(sentence.lower().split()))
letters = 'aaaaabbbbbccccccccdddddd'
c = Counter(letters)
print(c.most_common())
print(list(c))

# Default dictionary ----------------
d = {'a':10}
print(d['a'])

#print(d['WRONG'])

d = defaultdict(lambda: 0)

d['correct'] = 100

print(d['WRONG KEY'])
print(d)

# Named tuple ----------------
mytuple = (10,20,30)
mytuple[0] # 10

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
print(Dog)
sammy = Dog(age=5, breed='Beagle', name='Sammy')
type(sammy)
print(sammy)
print(sammy.age)
print(sammy.breed)
print(sammy[0])
print(sammy[1])
