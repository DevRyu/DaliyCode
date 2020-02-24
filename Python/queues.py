# 큐의 정의
# FIFO
# 데이터 순차적으로 처리
# 운영체제에서 멀티테스킹 프로세스 스케줄링을 위해서 사ㅛㅇ

# 큐의 종류 

# 일반 큐 :FIFO
# LIFO 큐 : 스텍과 같은형태의 큐를 설정
# Priority Queue : 우선순위를 가지는 큐
import queue

normal_queue = queue.Queue()

normal_queue.put(1)
normal_queue.put(2)
normal_queue.put(3)
normal_queue.put(4)
print(normal_queue.qsize()) # 4 
print(normal_queue.get()) # 1
print(normal_queue.get()) # 2
print(normal_queue.get()) # 3

lifo_queue = queue.LifoQueue()
lifo_queue.put(1)
lifo_queue.put(2)
lifo_queue.put(3)
lifo_queue.put(4)
print(lifo_queue.qsize()) # 4 
print(lifo_queue.get()) # 4
print(lifo_queue.get()) # 3
print(lifo_queue.get()) # 2

priority_queue = queue.PriorityQueue()
priority_queue.put((1, "first"))
priority_queue.put((10, "last"))
priority_queue.put((4, "third"))
priority_queue.put((3, "second"))
print(priority_queue.qsize()) # 4 
print(priority_queue.get())
# (1, 'first')
print(priority_queue.get()) 
# (3, 'second')
print(priority_queue.get()) 
# (4, 'third')
print(priority_queue.get())
# (10, 'last') 


# 리스트로 enq, deq구현

queue_list = []

def enq(data):
    queue_list.append(data)

def deq():
    # 첫번째 들어온 인덱스 삭제
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enq(index)
print(deq()) # 0
print(queue_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]