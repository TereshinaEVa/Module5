class Building:
    total = 0
    def __init__(self):
        Building.total += 1

obj = {}
for i in range(1,41):
   num = 'obj{}'.format(i)
   obj[num] = Building()
   print(f'измененный атрибут класса {Building.total}, ', f'атрибут экземпляра {obj[num].total}.')

