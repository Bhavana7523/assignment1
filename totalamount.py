#Description -
# Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 

#Book - Introduction to Python Programming : Rs 499.00

#Book - Python Libraries Cookbook : Rs. 855.00

#Book - Data Science in Python : Rs. 645.00
#Taxes and additional charges are described as details - 
#GST : 12%
#Delivery Charges : Rs. 250.00
           
         #code
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

#output:
#Testcase1:
#Enter the number of books of type14
#Enter the number of books of type22
#Enter the number of books of type 33
# 6567.92
#Testcase2:
#Enter the number of books of type140
#Enter the number of books of type239
#Enter the number of books of type 320
#74399.6
