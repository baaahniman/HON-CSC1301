import random

def encode(n,s):
    result = ''
    for item in s:
        if (item.islower()):
            result += chr((ord(item) - ord('a')+ n) % 26 + ord('a'))
        else:
            result += item
    return result

#print(encode(21,"hello, how are you"))

def table_from_corpus():
  return [8.1, 1.5, 2.8, 4.2, 12.7, 2.2, 2.0, 6.1, 7.0,
          0.2, 0.8, 4.0, 2.4, 6.7,  7.5, 1.9, 0.1, 6.0,
          6.3, 9.0, 2.8, 1.0, 2.4,  0.2, 2.0, 0.1]

def count(c,s):
    result = 0
    for item in s:
        if item == c:
            result += 1
    return result

#print(count('o','How are you'))

def num_lower_case(s):
    result = 0
    for item in s:
        if item.islower():
            result += 1
    return result

#print(num_lower_case("How are you bro"))

def frequencies(s):
    result = []
    for item in "abcdefghijklmnopqrstuvwxyz":
        m = count(item,s)
        n = num_lower_case(s)
        result.append((m/n) * 100)
    return result

#print(frequencies("hello, how are you"))

def chisqr(os,es):
    result = 0
    for set in zip(os,es):
        equation = (set[0] - set[1])**2/set[1]
        result += equation
    return result

#print(chisqr(frequencies("czggj, cjr vmz tjp"),table_from_corpus()))
#print(chisqr(frequencies("hello, how are you"),table_from_corpus()))

def rotate(list, shift):
    list = list[shift:] + list[:shift]
    return list

#print(rotate([7, 5, 3, 2],2))    

def chisquare_statistic(os,es):
    result = []
    for item in range(0,26):
        result.append(chisqr(rotate(os,item),es))
    return result

#print(chisquare_statistic(frequencies("czggj, cjr vmz tjp"),table_from_corpus()))


def crack(s):
    chi_list = (chisquare_statistic(frequencies(s),table_from_corpus()))
    minimum = min(chisquare_statistic(frequencies(s),table_from_corpus()))
    negative_index_of_minimum = 0 - chi_list.index(minimum)
    cracked = encode(negative_index_of_minimum,s)
    return cracked

#print(crack("czggj, cjr vmz tjp"))

def main():
  while True:
    plain = input("\nEnter plain text: ")
    if plain == "exit":
      break
    shift = random.randint(2,25)
    cipher = encode(shift,plain)
    print("Coded text: ",cipher)
    recovered = crack(cipher)
    print("Cracked text: ",recovered)

main() 



