import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(self.__name) >= 10:
            return self.__name[:10]
        else:
            return self.__name

    @classmethod
    def instantiate_from_csv(cls, file_csv):
        with open(file_csv, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row["name"]
                price = int(row["price"])
                quantity = int(row["quantity"])
                cls(name, price, quantity)
        return len(Item.all)

    @staticmethod
    def string_to_number(num):
        num = int(num)
        return num
