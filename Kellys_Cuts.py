#PRICING MODEL
total_price = 0
#list of styles offered
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

#current price list
prices = [30, 25, 40, 20, 20, 35, 50, 35]

#frequency of purchased haircuts - last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#get total prices
for p in prices:
  total_price += p

#get average price and display it to the screen
average_price = total_price / len(prices)
print(f"Average Haircut Price: {average_price}")

#build new price list using list comprehension (take each current price, subtract $5, and then add the new price to the list)
new_prices = [np - 5 for np in prices]
print(new_prices)

#REVENUE
total_revenue = 0

#find the weekly revenue
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(f"Total Revenue: {total_revenue}")

#find the daily revenue avg.
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#create list of cuts under $30 and display it
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
