from encodings import undefined

people:int = int(input("How many people? "))
quantity:int = int(input("How many products? "))
peoples = {}
for i in range(people):
  peoples[i] = i
while peoples[0] != undefined and quantity > 0:
  for i in range(people):
    print(peoples[i])
  del peoples[0]
  quantity -= 1
if peoples[0] == undefined:
  print("No one queues")
if quantity == 0:
  print("Sold out!")