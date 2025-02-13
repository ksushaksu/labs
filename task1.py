from abc import ABC, abstractmethod


class Device(ABC):
    """
    Базовый класс для всех электронных устройств.
    """

    def __init__(self, brand: str, model: str, price: float):
        """
        Конструктор базового класса Device.
        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param price: Цена устройства.
        """
        self._brand = brand  # Инкапсуляция бренда, так как он неизменяемый
        self.model = model
        self.price = price

    def __str__(self) -> str:
        return f"Устройство {self._brand} {self.model}, цена {self.price} USD"

    def __repr__(self) -> str:
        return f"Device(brand={self._brand}, model={self.model}, price={self.price})"

    @abstractmethod
    def turn_on(self) -> str:
        """
        Абстрактный метод, который должен быть реализован в дочерних классах.
        """
        pass


class Smartphone(Device):
    """
    Дочерний класс, представляющий смартфон.
    """

    def __init__(self, brand: str, model: str, price: float, os: str):
        """
        Конструктор класса Smartphone. Расширяет базовый класс Device.
        :param brand: Бренд смартфона.
        :param model: Модель смартфона.
        :param price: Цена смартфона.
        :param os: Операционная система смартфона.
        """
        super().__init__(brand, model, price)
        self.os = os

    def __str__(self) -> str:
        return f"Смартфон {self._brand} {self.model}, ОС {self.os}, цена {self.price} USD"

    def __repr__(self) -> str:
        return f"Smartphone(brand={self._brand}, model={self.model}, price={self.price}, os={self.os})"

    def turn_on(self) -> str:
        return f"{self._brand} {self.model} включается..."

    def install_app(self, app_name: str) -> str:
        """
        Метод, который демонстрирует установку приложения на смартфон.
        """
        return f"Приложение {app_name} установлено на {self._brand} {self.model}!"


class Laptop(Device):
    """
    Дочерний класс, представляющий ноутбук.
    """

    def __init__(self, brand: str, model: str, price: float, ram: int):
        """
        Конструктор класса Laptop. Расширяет базовый класс Device.
        :param brand: Бренд ноутбука.
        :param model: Модель ноутбука.
        :param price: Цена ноутбука.
        :param ram: Объем оперативной памяти ноутбука (в ГБ).
        """
        super().__init__(brand, model, price)
        self.ram = ram

    def __str__(self) -> str:
        return f"Ноутбук {self._brand} {self.model}, RAM {self.ram}GB, цена {self.price} USD"

    def __repr__(self) -> str:
        return f"Laptop(brand={self._brand}, model={self.model}, price={self.price}, ram={self.ram})"

    def turn_on(self) -> str:
        return f"{self._brand} {self.model} загружается..."

    def upgrade_ram(self, additional_ram: int) -> str:
        """
        Метод, демонстрирующий возможность увеличения оперативной памяти ноутбука.
        """
        self.ram += additional_ram
        return f"ОЗУ ноутбука {self._brand} {self.model} увеличено до {self.ram}GB!"


if __name__ == "__main__":
    smartphone = Smartphone("Apple", "iPhone 15", 999, "iOS")
    laptop = Laptop("Dell", "XPS 15", 1500, 16)

    print(smartphone)
    print(laptop)

    print(smartphone.turn_on())
    print(laptop.turn_on())

    print(smartphone.install_app("WhatsApp"))
    print(laptop.upgrade_ram(8))
