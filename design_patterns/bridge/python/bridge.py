class Abstraction(object):
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")

def ExtendedAbstraction(Abstraction):
    def operation(self):
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")

class Implementation(object):
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on the platform A."

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Here's the result on the platform B."

def client_code(abstraction):
    print(abstraction.operation())