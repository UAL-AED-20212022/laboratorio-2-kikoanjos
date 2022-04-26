#Inserir país no início
def insert_at_start(self, data):
    new_node = Node(data)
    new_node.ref = self.start_node
    self.start_node = new_node

#Inserir país no fim
def insert_at_end(self, data):
    new_node = Node(data)

    if self.start_node is None:
        self.start_node = new_node
        return
    n = self.start_node
    while n.ref is not None:
        n = n.ref
    n.ref = new_node

#Inserir país depois de outro
def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

#Inserir país antes de outro
def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return
        
        if x == self.start_node.item:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item is not None:
                if n.ref.item == x:
                    break 
                n = n.ref

        if n.ref is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

#Registar país num determinado índice
def insert_at_index(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i + 1
        if n is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

#Verificar número de elementos
def get_count(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0

        while n is not None:
            count += 1
            n = n.ref
        return count

#Verificar se o país se encontra na lista
def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.ref
        print("item bot found")
        return False

#Eliminar o primeiro país
def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        self.start_node = self.start_node.ref

#Eliminar o ultimo país
def delete_at_end(self):
        if self.start_node is None:
            print("The list has no elemnet to delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

#Eliminar um determinado país
def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")

        else:
            n.ref = n.ref.ref