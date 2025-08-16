start=int(input("enter a starting number"))
end=int(input("enter a ending number"))
square=[]
even_square=[]
odd_square=[]
for i in range(start,end+1):
    sq=i**2
    square.append(sq)
    if sq%2==0:
        even_square.append(sq)
    else:
        odd_square.append(sq)
print("square",square)
print("even square",even_square)
print("odd square",odd_square)