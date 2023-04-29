b1=int(input("Enter the number of books of type1"))
b2=int(input("Enter the number of books of type2"))
b3=int(input("Enter the number of books of type 3"))
cb1=499.00
cb2=855.00
cb3=645.00
gst=0.12
dc=250.00
total=b1*cb1+b2*cb2+b3*cb3
tax=total*gst
total_invoice=total+tax+dc
print(total_invoice)
