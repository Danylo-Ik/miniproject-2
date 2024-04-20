'''flower'''
class Flower:
    '''flower'''
    def __init__(self, color, petals, price) -> None:
        if all([isinstance(color, str),
                isinstance(petals, int),
                isinstance(price, int)]):
            self.color = color
            if petals >= 0 and price >= 0:
                self.petals = petals
                self.price = price
            else:
                raise ValueError
        else:
            raise TypeError

class Tulip(Flower):
    '''tulip'''
    def __init__(self, petals, price) -> None:
        super().__init__('pink', petals, price)

class Rose(Flower):
    '''rose'''
    def __init__(self, petals, price) -> None:
        super().__init__('red', petals, price)

class Chamomile (Flower):
    '''chamomile'''
    def __init__(self, petals, price) -> None:
        super().__init__('white', petals, price)

class FlowerSet:
    '''flower set'''
    def __init__(self) -> None:
        self.flowers = []

    def add_flower(self, flower):
        '''add flower'''
        if isinstance(flower, Flower):
            self.flowers.append(flower)
        else:
            raise TypeError

class Bucket:
    '''bucket'''
    def __init__(self) -> None:
        self.sets = []

    def add_set(self, flowers_set):
        '''add set'''
        if isinstance(flowers_set, FlowerSet):
            self.sets.append(flowers_set.flowers)
        else:
            raise TypeError

    def total_price(self):
        '''total price'''
        price = 0
        for flowers_set in self.sets:
            for flower in flowers_set:
                price += flower.price
        return price
