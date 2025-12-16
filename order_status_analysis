#sorting orders
# Import literal_eval to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
records = literal_eval(input())

# Write your code here
dic_inside_list={'delivered': 0, 'in transit': 0, 'cancelled': 0}
ord_id_of_cancelled_in_transit=[]
list_of_city=[]
for ord_id,city,status in records:
  dic_inside_list[status]=dic_inside_list.get(status,0)+1
  if status=='in transit' or status=='cancelled':
    ord_id_of_cancelled_in_transit.append(ord_id)
  elif status=='delivered':
    #ord_id_of_cancelled_in_transit.append(ord_id)
    list_of_city.append(city)
status_count=dic_inside_list
problematic_orders=sorted(ord_id_of_cancelled_in_transit)
delivered_cities=sorted(set(list_of_city))
# Print the output
print([status_count, problematic_orders, delivered_cities])
