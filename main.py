from tkinter import *
def one():
    v = input(str("Какое вы хотите мороженое? (OnStick или Soft): ")).lower()

    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, location, time, flavors):
            self.name = restaurant_name
            self.type = cuisine_type
            self.flavors = flavors
            self.location = location
            self.time = time
        def open_restaurant(self):
            print("Ресторан открыт")
    class IceCreamStand(Restaurant):
        def ice(self):
            print(f"Название ресторана: {self.name}")
            print(f"Тип кухни: {self.type}")
            print(f"Локация: {self.location}")
            print(f"Время работы: {self.time}")
            print(f"Допинг: {self.doping}")


    class IceOnAStick(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, location, time, flavors, doping):
            super().__init__(restaurant_name, cuisine_type, location, time, flavors)
            self.doping = doping

    class pos(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, location, time, flavors):
            super().__init__(restaurant_name, cuisine_type, location, time, flavors)

    class SoftIce(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, location, time, flavors, doping):
            super().__init__(restaurant_name, cuisine_type, location, time, flavors)
            self.doping = doping

    if "onstick" in v:
        onstick = IceOnAStick("KFC", "Fastfood", "м.Спасская", "10:00-21:00", {"chocolate": "1", "strawberry": "2"},
                              "raspberry")
        onstick.ice()
        print("Мороженное:", onstick.flavors)
        onstick.open_restaurant()
        onstick.flavors[input("Введите новый вкус: ").lower()] = "3"
        p = input("Введите вкус который хотите удалить: ").lower()
        if p in onstick.flavors:
            del onstick.flavors[p]
        else:
            print("Такого вкуса нет")

        print("Мороженное:", onstick.flavors)

        a = input("Проверьте наличие мороженного: ")

        if a in onstick.flavors:
            print(a, "есть")
        else:
            print("Данного вкуса нет")

        window = Tk()
        window.title("Доступные вкусы:")
        o = 1
        for i in onstick.flavors:
            lbl = Label(window, text=i, font=("Arial Bold", 20))
            lbl.grid(row=o)
            o += 1
        window.geometry('400x250')
        window.mainloop()

    elif "soft" in v:
        soft = SoftIce("KFC", "Fastfood", "м.Спасская", "10:00-21:00", {"vanilla": "1",
                                                                        "raspberry": "2"}, "chocolate")
        soft.ice()
        print("Мороженное:", soft.flavors)
        soft.open_restaurant()
        soft.flavors[input("Введите новый вкус: ").lower()] = "3"

        pp = input("Введите вкус который хотите удалить: ").lower()
        if pp in soft.flavors:
            del soft.flavors[pp]
        else:
            print("Такого вкуса нет")
        print("Мороженное:", soft.flavors)

        b = input("Проверьте наличие мороженного: ")

        if b in soft.flavors:
            print(b, "есть")
        else:
            print("Данного вкуса нет")

        window = Tk()
        window.title("Доступные вкусы:")
        o = 1
        for i in soft.flavors:
            lbl = Label(window, text=i, font=("Arial Bold", 20))
            lbl.grid(row=o)
            o += 1
        window.geometry('400x250')
        window.mainloop()

    else:
        print("Такого мороженного в меню нет")

# one()