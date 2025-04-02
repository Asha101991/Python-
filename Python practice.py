
# Pthyon Syntax

print("Hello,World!")

if 5 > 2:
    print("Five is greater than two!")
    if 5 > 2:
        print("Five is greater than two!")
        
        x = 5
        y = "Hello, World!"
        
        print(x)
        print(y)
        
    #Python Comments 
        
        #This is a comment.
        print("Hello,World!")
        
        #This is a comment 
        print("Hello,World!")
        
        #print("Hello,World!")
        print("Cheers,Mate!")
        
        #This is a comment 
        #written in
        #more than just one line
        print("Hello,World!")
        
        """
        This is a comment
        written in
        more than just one line
        """
        print("Hello,World!")
        

        # Python Variables
        
        x = 5
        y = "John"
        print(x)
        print(y)
        
        x = 4        # x is of type int
        x = "Sally"  # x is now of type str 
        print(x)
        
        
        x = str(3)    # x will be '3'
        y = int(3)    # y will be 3
        z = float(3)  # z will be 3.0
        
        
        x = 5
        y = "John"
        print(type(x))
        print(type(y))
        
        x = "John"
        # is the same as 
        x = 'John'
        
        a = 4
        A = "Sally"
        #A will not overwrite a
        
        
        #Python - Variable Names
        
        myvar = "John"
        my_var = "John"
        _my_var = "John"
        myVar = "John"
        MYVAR = "John"
        myvar2 = "John"
        
        x, y, z = "Orange" , "Banana" , "Cherry" 
        print(x)
        print(y)
        print(z)
        
        
        x = y = z = "Orange"
        print(x)
        print(y)
        print(z)
        
        fruits = ["apple" , "banana" , "cherry"]
        x , y , z = fruits
        print(x)
        print(y)
        print(z) 
        
        x = "Python is awesome"
        print(x)
        
        x = "Python"
        y = "is"
        z = "awesome"
        print(x , y, z)
        
        x = "Python"
        y = "is"
        z = "awesome"
        print(x + y + z)
        
        x = 5 
        y = 10
        print(x + y)
        
        x = 5
        y ="John"
        print(x , y)
        
        
        #Global Variables
        
        x = "awesome"
        
        def myfunc():
            print("Print is " + x)
            
        myfunc()
            
    
    x = "awesome"
    
    def myfunc():
        x = "Fantastic"
        print("Python is" + x)
        
        myfunc()
        
        print("Python is" + x)
        
        
def myfunc():
      global x
      x = "fantasic"


myfunc()

print("Python is " + x)


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)