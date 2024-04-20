'''testing flower'''
import timeit
from original_solution import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket
from memory_profiler import profile



class TestFlower:
    """Test class for Flower, Tulip, Rose, Chamomile, FlowerSet, and Bucket classes."""

    @staticmethod
    def test_flower():
        """Test method for Flower class."""
        flower = Flower('green', 7, 11)
        assert flower.color == 'green'
        assert flower.petals == 7
        assert flower.price == 11

    @staticmethod
    def test_color():
        """Test method for checking color type."""
        try:
            flower = Flower(11, 7, 11)
        except TypeError:
            pass

    @staticmethod
    def test_petals():
        """Test method for checking petals type and value."""
        try:
            flower = Flower('green', '7', 11)
        except TypeError:
            pass
        try:
            flower1 = Flower('green', -7, 11)
        except ValueError:
            pass

    @staticmethod
    def test_price():
        """Test method for checking price type and value."""
        try:
            flower = Flower('green', 7, '11')
        except TypeError:
            pass
        try:
            flower1 = Flower('green', 7, -11)
        except ValueError:
            pass

    @staticmethod
    def test_tulip():
        """Test method for Tulip class."""
        tulip = Tulip(10, 15)
        assert tulip.color == 'pink'
        assert tulip.petals == 10
        assert tulip.price == 15

    @staticmethod
    def test_rose():
        """Test method for Rose class."""
        rose = Rose(14, 2)
        assert rose.color == 'red'
        assert rose.petals == 14
        assert rose.price == 2

    @staticmethod
    def test_chamomile():
        """Test method for Chamomile class."""
        chamomile = Chamomile(2, 10)
        assert chamomile.color == 'white'
        assert chamomile.petals == 2
        assert chamomile.price == 10

    @staticmethod
    def test_add_flower():
        """Test method for adding flowers to FlowerSet."""
        flower_set = FlowerSet()
        flower = Flower('green', 7, 11)
        flower_set.add_flower(flower)
        assert len(flower_set.flowers) == 1
        flower1 = Flower('red', 3, 10)
        flower_set.add_flower(flower1)
        assert len(flower_set.flowers) == 2

    @staticmethod
    def test_add_not_flower():
        """Test method for adding non-flower objects to FlowerSet."""
        flower_set = FlowerSet()
        try:
            flower_set.add_flower('sunflower')
        except TypeError:
            pass

    @staticmethod
    def test_add_set():
        """Test method for adding FlowerSets to Bucket."""
        bucket = Bucket()
        flower_set = FlowerSet()
        bucket.add_set(flower_set)
        assert len(bucket.sets) == 1
        flower_set1 = FlowerSet()
        bucket.add_set(flower_set1)
        assert len(bucket.sets) == 2

    @staticmethod
    def test_add_not_set():
        """Test method for adding non-sets to Bucket."""
        bucket = Bucket()
        try:
            bucket.add_set(['flower1', 'flower2'])
        except TypeError:
            pass

    @staticmethod
    def test_total_price():
        """Test method for calculating the total price of flowers in a Bucket."""
        bucket = Bucket()
        flower_set = FlowerSet()
        flower = Flower('green', 7, 11)
        flower_set.add_flower(flower)
        bucket.add_set(flower_set)
        assert bucket.total_price() == 11
        flower1 = Flower('red', 3, 10)
        flower_set.add_flower(flower1)
        assert bucket.total_price() == 21

    @staticmethod
    def test_all():
        """Test all functionalities."""
        test_cases = TestFlower()
        test_cases.test_flower()
        test_cases.test_color()
        test_cases.test_petals()
        test_cases.test_price()
        test_cases.test_tulip()
        test_cases.test_rose()
        test_cases.test_chamomile()
        test_cases.test_add_flower()
        test_cases.test_add_not_flower()
        test_cases.test_add_set()
        test_cases.test_add_not_set()
        test_cases.test_total_price()


@profile
def main():
    '''testing'''
    TestFlower.test_all()


if __name__ == '__main__':
    # Measuring the time
    execution_time = timeit.timeit('main()', number=10)
    print(f'Execution time: {execution_time} seconds')

    # Measuring the memory usage
    main()
