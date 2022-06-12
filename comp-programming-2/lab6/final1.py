def append(self, data):

  new_myNode = Node(data)

  if self.isEmpty():

       self.__head = new_myNode
       self.__tail = new_myNode
  else:

        current = self.__head

        while current.getNext() != None:

                 current = current.getNext()

         // at the end

        self.__tail = new_myNode 
        current.setNext(new_myNode)

