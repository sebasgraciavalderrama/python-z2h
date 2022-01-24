def lesser_of_two_evens(a,b):
   if (a%2==0) and (b%2==0):
        if (a<b):
            return a
        else:
            return b
   else:
       if (a>b):
            return a
       else:
            return b

def animal_crackes(text):
    split_text = text.split()
    first_word_char = split_text[0][0]
    first_word2_char = split_text[1][0]
    if first_word_char == first_word2_char:
        return True
    return False

def makes_twenty (n1, n2):
    if (n1 == 20 or n2 == 20) or (n1+n2 == 20):
        return True
    return False


def old_macdonald(name):
    firstLetterCapitalized = name
    firstLetterCapitalized = firstLetterCapitalized[:3].capitalize()
    fourthLetterCapitalized = name[3:].capitalize()
    return (firstLetterCapitalized+fourthLetterCapitalized)

string1 = 'Levelheaded Llama'
string2 = 'Crazy Kangaroo'

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

print(animal_crackes(string1))
print(animal_crackes(string2))

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

print(old_macdonald('macdonald'))




