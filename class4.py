class MemoryClass:

    def __init__(self, func):
        self.func = func
        print('Instance of MemoryClass was created!')

    def __call__(self, obj, list_of_items):
        print('Calling MemoryClass instance!')
        items_not_selected = [item for item in list_of_items if item not in obj.additives]
        self.func(obj, items_not_selected)


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def __str__(self):
        a = f'{self.kind} {self.name} {self.additives}'
        return a

    def __iadd__(self, other):
        if type(other) is str:
            self.additives.append(other)
            print(self.additives)
            return self
        elif type(other) is list:
            self.additives.extend(other)
            print(self.additives)
            return self
        else:
            raise Exception('This type of object is not implemented!', type(other))

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    def add_additives(self, additives):
        self.additives.extend(additives)

    @property
    def full_name(self):
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


class SpecialCake(Cake):
    def __init__(self, name, kind, taste, additives, filling, occasion, shape, ornaments, text):
        super().__init__(name, kind, taste, additives, filling)
        self.occasion = occasion
        self.shape = shape
        self.ornaments = ornaments
        self.text = text

    def show_info(self):
        super().show_info()
        print('Occasion:     {}'.format(self.occasion))
        print('Shape:        {}'.format(self.shape))
        print('Ornaments:    {}'.format(self.ornaments))
        print('Text:         {}\n'.format(self.text))


@MemoryClass
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolate', 'nuts'], 'cream')

birthday = SpecialCake('Chocolate Cake', 'cake', 'chocolate', ['chocolate', 'nuts'], 'cream', 'birthday', 'rectangle',
                       'MM & AK', 'Happy birthday! :)')
weeding = SpecialCake('Orange Cake', 'cake', 'orange', ['chocolate', 'nuts'], 'cream', 'wedding', 'rectangle',
                      'MM & AK', 'Happy weeding! :)')

birthday.show_info()
weeding.show_info()

for c in SpecialCake.bakery_offer:
    print(c.full_name)
    c.show_info()

cake01.show_info()
add_extra_additives(cake01, ['sugar', 'cherry', 'cream'])
cake01.show_info()

# print(hasattr(cake01, 'kind') and callable(Cake))
# cake01 += ['whipped cream', 'orange pieces']
# cake01.show_info()
# print(cake01)
