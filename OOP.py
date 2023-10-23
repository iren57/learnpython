# class-Is a blueprint of an object
# object-Is an instance of that class
# method-a function that is being associated with an object
# constructor-this is a must to have.
#Every class should have a constructor

class fruits:     #fruits is a class
    def __init__(self,type,price,color):  #def init is a constructor
        self.type=type
        self.price=price
        self.color=color

    def onyesha(self):   #This is a method
        print(f"I like eating {self.type} and it costs {self.price}, color being {self.color}")

#Creating an object
myobj1=fruits("bananas","Kshs.20", "Yellow")
myobj2=fruits("mangoes","Kshs.40","green")

myobj1.onyesha()
myobj2.onyesha()