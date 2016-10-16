import time
import random

print "inspirational quote generator"
print "by paul bell and sam moore"

time.sleep(1)

prt_1 = ["believe ", "it's what's on the inside ", "be ", "the most important thing is ", "life is what happens when " "live, laugh, ", "you have to look through the rain to ", "sing like ", "keep calm and ", "shoot for the moon. even if you miss, ", "when life gives you lemons, ", ""]
prt_2 = ["in yourself", "that counts", "yourself", "to never stop questioning", "you're busy making other plans", "love", "see the rainbow", "nobody's listening", "carry on", "you'll land among the stars", "make lemonade", ""]

prnt_prt1 = random.choice(prt_1)
prnt_prt2 = random.choice(prt_2)

fin = prnt_prt1 + prnt_prt2

print fin
