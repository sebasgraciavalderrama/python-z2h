def lesser_of_two_evens(a,b):
   if (a%2==0) and (b%2==0):
       return min(a,b)
   else:
       return max(a,b)

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

def master_yoda(text):
    split_text = text.split()
    first_word = split_text[0]
    last_word = split_text[-1]
    split_text[0] = last_word
    split_text[-1] = first_word
    return ' '.join(split_text)

def almost_there(n):
    if (n>= 90 and n<=110) or (n>= 190 and n<=210):
        return True
    return False

def has_33(nums):
    for i, num in enumerate(nums):
        if num[i] == 3 and num [i+1]==3:
            return True
    return False

def paper_doll(text):
    letters = list(text)
    new_string = []
    for letter in letters:
        new_string.append(letter)
        new_string.append(letter)
        new_string.append(letter)
    return ''.join(new_string)

def blackjack(a,b,c):
    total = a+b+c
    if total <= 21:
        return total
    elif total >= 21 and 11 in (a,b,c):
        return total-10
    else:
        return 'BUST'

def summer_69(arr):
    total = 0
    flag = True
    for number in arr:
        if number == 6 or number == 9:
            flag = nine_or_six(number)
        if flag:
            total += number
    return total

def nine_or_six(num):
    if num == 6 :
        return False
    if num == 9:
        return True

def summer_69_actual_solution(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

def summer_69_powered(arr):
    s = set(arr)
    if 6 in s and 9 in s:
        where_is_six = arr.index(6)
        where_is_nine = arr.index(9)
        how_many_times_to_pop = 0
        for i in range(where_is_six, where_is_nine+1):
            how_many_times_to_pop = how_many_times_to_pop + 1
        for index in range (how_many_times_to_pop):
            arr.pop()
        return (sum(arr))
    else:
        return 0

def spy_game(nums):
    my_strings= ''
    for i in nums:
        my_strings += str(i)
    if '007' in my_strings:
        return True
    return False
#This can be done in one line of code: return '007' in ''.join(str(i) for i in arr)

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    return len(primes)

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

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

print(count_primes(100))

print('##############################')

#print(summer_69_powered([1, 3, 5]))
print(summer_69_powered([1, 6, 3, 5]))
#print(summer_69_powered([4, 5, 6, 7, 8, 9]))
#print(summer_69_powered([2, 1, 6, 9, 11]))