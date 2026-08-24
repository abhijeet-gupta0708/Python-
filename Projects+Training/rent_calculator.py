# Total room rent , water bill , electricity unit , electric rate ,other expenses , total no of roomates

room_rent=int(input("Enter your room rent : "))
water_bill=int(input("Enter your Water bill : "))
electric_unit=int(input("Enter the unit of electricity consumed  : "))
electric_rate=int(input("Enter your electric rate per unit : "))
other_expenses=int(input("Enter other expenses : "))
roomates=int(input("Enter no of person living with you : "))


## Calculation 
## E_bill=rates*unit consume 
## WaterBill+other_expenses+roomrent

#individual _expense=total/no of people


e_bill=electric_rate*electric_unit
total_bill=e_bill+water_bill+other_expenses+room_rent

print("Your Total Monthly expense is ", +total_bill)

individual_bill=total_bill/roomates
print("Your Individual monthly expense is " ,+ individual_bill)

