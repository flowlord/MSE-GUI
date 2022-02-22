from random import shuffle

t = "UI0299Siqy_@@@"
t = list(t)


for _ in range(3):
	shuffle(t)


t = ''.join(t)
print(t)



