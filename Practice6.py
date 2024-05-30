
def outer():
    print("i am outer function")

    def inner():
        print ("i am inner function") 

outer() 

def outer():
    print('im outer function') 

    def inner():
        print('im inner function') 
    inner() 

outer() 

def profile():

    def registration():
        print ("Jane", "12", "data science and python") 

    registration() 
profile()     
        

def  profile():

    def registration():
        print ("name","age","course") 
    return registration 
    

data=profile()
data()   


def registration():
    y= "ram", "12", "python usage"

    def profile(): 
        print("y:", y) 
    return profile()
registration()