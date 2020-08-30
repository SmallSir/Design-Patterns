# code: utf-8


from abc import ABC, abstractmethod, abstractproperty


class Builder(ABC):
    @abstractmethod
    def Part1(self):
        pass

    @abstractmethod
    def Part2(self):
        pass

    @abstractmethod
    def Part3(self):
        pass


class Director(object):
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def construct(self):
        self._builder.product()


class Product():
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print("Product parts: ", self.parts)


def ConcreteBuilder1(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def Part1(self):
        self._product.add("Part1")

    def Part2(self):
        self._product.add("Part2")

    def Part3(self):
        self._product.add("Part3")


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard full featured product: ")
    director.construct()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.Part1()
    builder.Part2()
    builder.product.list_parts()

