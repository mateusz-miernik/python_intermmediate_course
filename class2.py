import pickle
import os
import glob
import types

base_path = os.getcwd()


def export_all_cakes_to_html(cls, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        for c in cls.bakery_offer:
            content = template.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)


def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair',
                   'christmas', 'pretzel', 'other']
    bakery_offer = []
    numberOfCakes = 0

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        Cake.numberOfCakes += 1
        self.numberOfCakes = Cake.numberOfCakes
        self.__gluten_free = gluten_free
        if self.kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('Sentence can not be written into instance')

    def __str__(self):
        sentence = 'This is object nr {} of class Cake'.format(self.numberOfCakes)
        return sentence

    def show_info(self):
        print('{}'.format(self.name).upper())
        print("Kind:    {}".format(self.kind))
        print('Taste: {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print('\t{}'.format(a))

        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('Gluten free: {}'.format(self.__gluten_free))
        print('-'*20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    # def __get_text(self):
    #     return self.__text
    @property
    def Text(self):
        return self.__text

    @Text.setter
    def Text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text

    @Text.deleter
    def Text(self):
        self.__text = None

    def save_to_file(self, path):
        with open(os.path.join(path, __class__.__name__ + '_' + str(self.numberOfCakes) + '.bakery'), 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    # Text = property(__get_text, __set_text, None, 'This is property of class')

    @staticmethod
    def get_bakery_files(folder):
        print([os.path.basename(item) for item in glob.glob(folder + '\\' + '*.bakery')])


print(dir(Cake))
print(vars(Cake))
cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'napis')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, 'hjahjaf')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, '')

Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html(os.path.join(base_path, 'bakery_offer_class.html'))

for obj in Cake.bakery_offer:
    obj.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, obj)
    # new_name = [x if x.find('_') == -1 else '_' for x in obj.name]
    obj.export_this_cake_to_html(os.path.join(base_path, obj.name.replace(' ', '_') + '.html'))

cake01.save_to_file(base_path)
print(cake01.Text)
# load_file = Cake.read_from_file(os.path.join(base_path, 'Cake_1.bakery'))
# # load_file.show_info()
Cake.get_bakery_files(base_path)
print(cake01)
print(cake02)
print(cake03)
print(cake04)
# bakery_offer = list()
# bakery_offer.append(cake01)
# bakery_offer.append(cake02)
# bakery_offer.append(cake03)
# bakery_offer.append(cake04)

cake02.set_filling('vanilia cream')
cake03.add_additives(['cocoa powder', 'coconuts'])

cake03._Cake__gluten_free = False
print(dir(cake03))
print('Today in our offer:\n')
for c in Cake.bakery_offer:
    c.show_info()

print(cake01.name)
print(cake02.name)
print(cake03.name)
"""
cake_01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7
}

cake_02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3
}


def show_cake_info(aCake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        aCake['taste'], aCake['glaze'], aCake['text'], aCake['weight']))


show_cake_info(cake_01)
show_cake_info(cake_02)

cakes = [cake_01, cake_02]

for c in cakes:
    show_cake_info(c)

# show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
# show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)
"""
