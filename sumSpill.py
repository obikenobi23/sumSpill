import random
def restart():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def inTput(string):
    return int(input(string))

sum = 0

for i in range(6):
    tall = random.randrange(20,101)
    print(tall)
    sum += tall
    fortsett = input("")
    restart()

svar = inTput("Hva er totalen?\n")
diff = svar - sum

if diff == 0:
    print("Riktig!")
    print(sum)
elif diff > 0:
    print("Du gjettet for høyt! Du bommet med", diff)
    print("Riktig svar er", sum)
elif diff < 0:
    print("Du undergjettet med", -diff)
    print("Riktig svar er", sum)
