from split_sim import my_split

# MY SPLIT TESTS:
#1
print("\n TEST 1")
print("My split: ", my_split("Ser o no ser, esa es la pregunta"))
print("Py split: ", "Ser o no ser, esa es la pregunta".split() )
#2
print("\n TEST 2")
print("My split: ", my_split("Ser o no ser,esa es la pregunta"))
print("Py split: ", "Ser o no ser,esa es la pregunta".split() )
#3
print("\n TEST 3")
print("My split: ", my_split("   "))
print("Py split: ", "   ".split() )
#4
print("\n TEST 4")
print("My split: ", my_split(" abc "))
print("Py split: ", " abc ".split() )
#5
print("\n TEST 5")
print("My split: ",my_split(""))
print("Py split: ", "".split() )