import time
import random

print "pick up line generator 2016"
print "by paul bell and sam moore"

time.sleep(1)

prt1 = ["if i could rearrange the alphabet, ", "are you from tennessee, ", "did it hurt when you fell ", ""]

prt2 = ["i would you put 'u' and 'i' together", "because you're the only 10 i see", "from heaven", ""]

prnt_prt1 = random.choice(prt1)
prnt_prt2 = random.choice(prt2)

fin = prnt_prt1 + prnt_prt2

print fin