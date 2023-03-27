class ChocolateBoiler:
    __uniqueInstance = None

    # 創建類實例的靜態方法
    def __new__(cls):
        if not cls.__uniqueInstance:
            cls.__uniqueInstance = super().__new__(cls)

        return cls.__uniqueInstance


s1 = ChocolateBoiler()
s2 = ChocolateBoiler()
print(s1 is s2)
