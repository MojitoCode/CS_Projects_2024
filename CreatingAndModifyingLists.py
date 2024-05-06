# Your code below:
#create a toppings list
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
#create a prices list
prices = [2,6,1,3,2,7,2]
#find the number of $2 slices in the prices list
num_two_dollar_slices = prices.count(2)
#find the number of pizza types sold
num_pizzas = len(toppings)
#display a banner message with the number of pizza types sold
print(f"We sell {num_pizzas} different kinds of pizza!")

#create a 2D list of pizza and their prices
pizza_and_prices = [[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)
pizza_and_prices.sort()
#print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza[1])
pizza_and_prices.pop()
#print(pizza_and_prices)
