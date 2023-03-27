from threading import Lock, Thread


class ChocolateBoiler:
    __uniqueInstance = None

    def __new__(cls):
        if not cls.__uniqueInstance:
            cls.__uniqueInstance = super().__new__(cls)

        return cls.__uniqueInstance


s1 = ChocolateBoiler()
s2 = ChocolateBoiler()
print(s1 is s2)


# thread-safe
class MultiChocolateBoiler:
    __uniqueInstance = None
    __lock = Lock()
    value = None

    def __new__(cls, value):
        if not cls.__uniqueInstance:
            with cls.__lock:
                if not cls.__uniqueInstance:
                    cls.__uniqueInstance = super().__new__(cls)
                    cls.__uniqueInstance.value = value

        return cls.__uniqueInstance


def test_singleton(value):
    s = MultiChocolateBoiler(value)
    print(s.value)


process1 = Thread(target=test_singleton, args=('toy',))
process2 = Thread(target=test_singleton, args=('store',))
process1.start()
process2.start()
