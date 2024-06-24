class Building:
    total = 0
    def __init__(self, i):
        self.number = Building.total + i

obj = {}
for i in range(1,41):
   num = 'obj{}'.format(i)
   obj[num] = Building(i)
   Building.total = obj[num].number
   obj[num].total = obj[num].number
   print(f'измененный атрибут класса {Building.total}, ', f'атрибут экземпляра {obj[num].total}.')

