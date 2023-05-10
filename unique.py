#Description: Write a program in Python to print the number of unique letters in a string. Only new letters from the string should be counted and not duplicates.
  
  string=input("Enter string")
  string1=string.lower()
  unique=set(string1)
  l=[]
  for i in string:
    if i in unique:
      l.append(i)
      unique.remove(i)
  print(",".join(l))
  
  #output:
  #Test case 1:
  #Enter string:Bhavana
  #h,a,v,n
  #Test case 2:
  #Enter string:India
  #n,d,i,a
  
