class NoDuplicates:
    def __init__(self):
        self.list = []

    def __call__(self, new_items):
        for item in new_items:
            if item not in self.list:
                self.list.append(item)


instance = NoDuplicates()
instance(['Ford', 'Porsche', 'Ferrari'])
print(instance.list)
instance(['Opel', 'Ford', 'Lambo'])
print(instance.list)
