class Stack:
    """ """

    def __init__(self):
        self.items = []

    def push(self, item):
        """

        Args:
          item:

        Returns:

        """
        self.items.append(item)

    def pop(self):
        """ """
        return self.items.pop() if self.items else None
