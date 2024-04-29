#Variable definitions
weight = 41.5
#flat fee + weight based rate:
ground_shipping_fee = 0
#drone shipping - no flat fee:
drone_shipping_fee = 0
#premium flat fee - no additional rate
prem_shipping = 125.00

#------------------GROUND SHIPPING----------------------

"""
> FLAT FEE: 20.00
> ADD. RATE BASED ON WEIGHT:
  ~ 2 lbs or less: 1.50/lb 
  ~ 2-6 lbs: 3.00/lb
  ~ 6-10 lbs: 4.00/lb
  ~ over 10 lbs: 4.75/lb
""" 

#small flat charge 
ground_shipping_flat_fee = 20.00
#ground shipping rates
grnd_t1 = 1.50
grnd_t2 = 3.00
grnd_t3 = 4.00
grnd_t4 = 4.75

#Determine Cost of Ground Shipping
if weight > 10:
  ground_shipping_fee = ground_shipping_flat_fee + (grnd_t4 * weight) 
elif weight > 6 and weight <= 10:
  ground_shipping_fee = ground_shipping_flat_fee + (grnd_t3 * weight)
elif weight > 2 and weight <= 6:
  ground_shipping_fee = ground_shipping_flat_fee + (grnd_t2 * weight)
elif weight <= 2:
  ground_shipping_fee = ground_shipping_flat_fee + (grnd_t1 * weight)

#display the cost to ship via ground
print(f"Ground Shipping Fee: ${ground_shipping_fee}")

"""
TEST - ground shipping fee: 
  ~ set weight to = 8.4lbs
  ~ result should be: $53.60
  ~ print(shipping_fee)
"""

#------------------DRONE SHIPPING----------------------

"""
> DRONE RATE BASED ON WEIGHT:
  ~ 2 lbs or less: 4.50/lb 
  ~ 2-6 lbs: 9.00/lb
  ~ 6-10 lbs: 12.00/lb
  ~ over 10 lbs: 14.25/lb
""" 
#drone shipping rates
drone_t1 = 4.50
drone_t2 = 9.00
drone_t3 = 12.00
drone_t4 = 14.25

#Determine Cost of Drone Shipping
if weight > 10:
  drone_shipping_fee = drone_t4 * weight
elif weight > 6 and weight <= 10:
  drone_shipping_fee = drone_t3 * weight
elif weight > 2 and weight <= 6:
  drone_shipping_fee = drone_t2 * weight
elif weight <= 2:
  drone_shipping_fee = drone_t1 * weight

#display the cost to ship via drone
print(f"Drone Shipping Fee: ${drone_shipping_fee}")

"""
TEST - drone shipping fee: 
  ~ set weight to = 1.5lbs
  ~ result should be: 6.75
  ~ print(drone_shipping_fee)
"""

#------------------PREMIUM SHIPPING---------------------
print(f"Premium Shipping Fee: ${prem_shipping}0")


