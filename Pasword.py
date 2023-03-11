import random

lower = "abcçdefgğhiıjklmnoöprsştuüvyz"
upper = "ABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ"
numbers = "0123456789"
sembols = "[]{}()*;/,._-"

all = lower+upper+numbers+sembols
Length = 16  #sets password length
password = "".join(random.sample(all,Length))
print(password)