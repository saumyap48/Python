rent=int(input("Enter your hostel/flat rent ="))
food=int(input("Entre the amount of food ordered="))
electricity_spend=int(input("Entre the total of electricity spend="))
charge_per_unit=int(input("Entre the charge pet unit ="))
persons=int(input("Entre the number of person living in room/flat ="))
total_bill=electricity_spend*charge_per_unit
output=(food + rent + total_bill)
print("Each person will pay =",output)

 