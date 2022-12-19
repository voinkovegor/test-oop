class Tomato:

    stage = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index=1):
        self._index = index
        self._state = self.stage[self._index]

    def grow(self):
        if self._index != 3:
            self._index += 1
            return self._index
        print(f'Состояние помидора стало: {self.stage[self._index]}')

    def is_ripe(self):
        if self._index == 3:
            return True


class TomatoBush():

    def __init__(self, count):
        self.tomatoes = [Tomato()] * count

    def grow_all(self):
        self.tomatoes[0].grow()
        print('Куст растет')

    def all_are_ripe(self):
        temp = all(i.is_ripe() for i in self.tomatoes)
        print('Все созрело, все помидоры красные') if temp else print(f'Состояние помидоров: {self.tomatoes[0].stage[self.tomatoes[0]._index]}')
        return temp


    def give_away_all(self):
        self.tomatoes.clear()
        print('Снимаю весь урожай')
        self._index = 0


class Gardener():

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()
        print('Ухаживаю за кустом')

    def harvest(self):
        if self._plant.all_are_ripe():
            print('Собираю урожай')
            self._plant.give_away_all()
        else:
            print('Еще не все помидоры спелые')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству')

tom = TomatoBush(4)
gar = Gardener('Mark', tom)
gar.harvest()
gar.work()
gar.harvest()
gar.work()
gar.harvest()
