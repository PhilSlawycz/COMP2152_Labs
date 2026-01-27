print("=" * 50)
print("Question 2: Shopping Cart")
print("=" * 50)

cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

apple_count = cart.count("apple")
print("Number of Apples: ", apple_count)

milk_position = cart.index("milk")
print("Position of milk:", milk_position)

cart.remove("apple")
#Pop an item
Removed_item = cart.pop()
print("Removed item using pop: ", Removed_item)

print("Is banana in the cart", "banana" in cart)
print("Final cart: ", cart)