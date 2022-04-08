class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

    def __str__(self) -> str:
        return self.dataval


class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        print("Printing Linked List : ")
        while printval is not None:
            print(f"{printval.dataval} ->", end=" ")
            printval = printval.nextval
        print("NULL(End of list)")
