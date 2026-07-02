import tkinter as tk 

rent=int(input("Enter the Room Rent :"))
electric_unit=int(input("Enter the Electric Unit Consumed :"))
electric_rate=int(input("Enter the Electric Rate  :"))
roomates=int(input("How many Roomates are there :"))
water_bill=int(input("Enter the water bill :"))

electric_bill=electric_rate*electric_unit 
total_bill=electric_bill+water_bill+rent
individual_bill=total_bill/3

print("\nYour Total Bill is : ",total_bill)
print("\n Individual  Bill is : ",individual_bill)

# Designing the Rent Calculator 

label=tk.Label(total_bill)

print(label)