print("This is a multiplication Math Game!")
print()
multiples = int(input("Name your multiples: "))
print(type(multiples))
OurRange = range(1,11)
counter = 0
for i in OurRange:
  answer = (i * multiples)
  print (i,"x", multiples)
  results = int(input("= "))
  if results == answer:
    print()
    print("Great job you're Correct!")
    print()
    counter += 1
  else:
    print()
    print("Nope, The answer was", answer)
    print()
print("You scored", counter,"out of 10.")
