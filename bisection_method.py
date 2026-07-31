x = int(input("Enter the lower bound: "))
y = int(input("Enter the upper bound: "))
#now we cannnot take an equation as input 
# so we will solve an equation created by us inside the program 
# the user input equation solving - will be the future work for this problem

# so let's keep it simple like the algorithm suggests -

f_a = 2*pow(x,2) - 5*x - 18
f_b = 2*pow(y,2) - 5*y - 18

if (f_a*f_b < 0):
    for i in range(5):
        c = float((x+y))/2
        f_c = 2*pow(c,2) - 5*c + 18
        if(f_c*f_a < 0):
             a = c
             f_a = f_c
        if(f_c*f_b < 0):
             b = c
             f_b = f_c
print(c)    
    

