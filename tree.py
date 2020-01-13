class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"**value** : {self.value} |||| [{self.left}]<-left |||| right->[{self.right}]"

class NodeMgmt:
    # 위의 Node 를 여기 넣음 
    def __init__(self, head):
        # head는 루트노드
        self.head = head
    
    def insert(self, value):
        #순회 기준의 노드
        self.current_node = self.head
        while True:
            # 왼쪽(작은 경우)
            # 삽입된 노드가 순회 기준의 노드가 작으면
            if value < self.current_node.value:
                # 순회 기준의 노드의 왼쪽값이 있다면
                if self.current_node.left != None:
                    # 순회기준의 왼쪽값을  순회 기준 노드로 두고 다시 while문 반복
                    self.current_node = self.current_node.left
                else:
                    # 순회 기준의 노드의 왼쪽값이 없다면 현재 루트노드에 추가
                    self.current_node.left = Node(value)
                    break
            # 오른쪽(큰 경우)
            # 삽입된 노드가 순회 기준의 노드가 크다면
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        # 루트노드를 기준으로 잡고 값이 None이면 멈춤
        # 마지막 leaf노드의 경우 왼쪽 오른쪽이 None이니
        while self.current_node:
            # 값이 있으면 True
            if value == self.current_node.value:
                return True
            # 기준값보다 작으면
            elif value < self.current_node.value:
                # 왼쪽의 노드 인스턴스를 준다.
                self.current_node = self.current_node.left
            # 기준값 보다 크면(value > self.current_node.value)
            else :
                # 왼쪽의 노드 인스턴스를 준다.
                self.current_node = self.current_node.right
        # while문이 끝나도 없으면 False
        return False
    def delete(self, value):
        # 삭제할 노드 탐색
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False    


            
head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(4)


print(head) 
#**value** : 1 |||| [None]<-left |||| right->
#[**value** : 2 |||| [None]<-left |||| right->
#[**value** : 3 |||| [None]<-left |||| right->
#[**value** : 4 |||| [None]<-left |||| right->[None]]]]
print(BST.search(3)) # true
print(BST.search(5)) # false