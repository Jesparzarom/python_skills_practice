# EXAMPLE

class Stack:    # define la clase Stack
    def __init__(self):    # define la función del constructor
        self.__list_stack = []
    
    def Push(self, element):
        self.__list_stack.append(element)
        
    def Pop(self):
        element = self.__list_stack[-1]
        del self.__list_stack[-1]
        return element
      
    def ShowStack(self):
        print(self.__list_stack)


# Subclass
class StackSum(Stack): # Suma o resta los números de la pila
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
    
    def Push(self, element):
        self.__sum += element
        Stack.Push(self, element)
    
    def Pop(self):
        element = Stack.Pop(self)
        self.__sum -= element
        return element
    
    def GetSum(self):
        print(self.__sum)
        return self.__sum
    

        
# =================Test==================
stack = StackSum()    # instanciando el objeto

for number in range(5):
    stack.Push(number)    
stack.GetSum()

print("================")

for element in range(5):
    pop_element = stack.Pop()
    print(pop_element)
