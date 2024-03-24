class Node:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode

node1=Node(2)
node2=Node(4)
node3=Node(5)

node1.nextNode=node2
node2.nextNode=node3

currentNode=node1
while True:
    print(currentNode.value,'->')
    if currentNode.nextNode is None:
        print('none')
        break
    currentNode=currentNode.nextNode