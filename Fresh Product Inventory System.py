class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None        
        self.size = 0
        
    def enqueue(self, item):
        self.size += 1
        node = Node(item)
        
        if self.rear == None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node   # rear가 참조하고 있는 노드의 next를 새로 추가한 node로 변경
            node.prev = self.rear
            self.rear = node    # rear가 새로 추가한 노드를 가르키도록 변경
            
    def dequeue(self):  # 제일 앞 node를 반환하고 제거
        if self.front is None:  # is : 같은 위치를 참조하고 있는지 확인
            raise IndexError("-1") 
        self.size -= 1
        temp = self.front   # 제거될 node
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        return temp.data
    
    def dequeue_rear(self):
        if self.rear is None:
            raise IndexError("-1")
        self.size -= 1
        temp = self.rear
        if self.rear.prev is None:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            temp.prev = None
            self.rear.next = None
        return temp.data
    
    
    
    
    
    
    
    '''
    연결이 끊긴 temp = node 의 node -> 자동으로 삭제
    
    temp는 메서드 내부의 변수임으로 메서드 실행 종류 후 삭제됨. node의 참조 갯수가 0개로
    
    Python에서 객체(이 경우 링크드 리스트의 노드)는 참조 카운팅(reference counting) 방식으로 메모리 관리가 이루어집니다. 
    객체에 대한 참조가 더 이상 없을 때, 즉 참조 카운트가 0이 되면, 
    Python의 가비지 컬렉터(garbage collector)가 자동으로 해당 객체를 메모리에서 해제합니다.
    
    '''
    
    def get_size(self):
        return self.size
        
        


# Fresh Product Inventory System Problem

# input : id, production_timestamp, expiration_timestamp

# add ProductInventory class
# function : add_product(id, production_timestamp, expiration_timestamp) 물건 추가
# function : sell_product() 제일 최근에 추가된 물건 판매
# function : remove_expired_products(current_timestamp) 현재 시간 기준으로 유통기한이 지난 물건 제거
# function : get_inventory() 최근에 추가된 물건 순서부터 목록 출력


class Product:
    def __init__(self, id, production_timestamp, expiration_timestamp):
        self.id = id
        self.production_timestamp = production_timestamp
        self.expiration_timestamp = expiration_timestamp



class ProductInventory:
    def __init__(self):
        self.products = Queue() # 컴포지션(Composition)
                                # self 객체의 products 성분이 Queue로 구성됨
        
    
    def add_product(self, id, production_timestamp, expiration_timestamp):
        product = Product(id, production_timestamp, expiration_timestamp)
        self.products.enqueue(product)   # product를 data로 하는 node 생성
    
    
    def sell_product(self):
        if self.products.get_size() == 0:
            return "-1"
        else:
            sold_product = self.products.dequeue_rear()
        return sold_product.id
        

    def remove_expired_products(self, current_timestamp):
        current = self.products.front
        previous = None
        while current:
            if current.data.expiration_timestamp < current_timestamp:   # 유통기한 지난 상품 제거하는 파트
                if previous:    # 이전 노드가 존재하는 경우, 이전 노드가 None이 아닌 경우
                      previous.next = current.next  # current 노드의 참조를 끊어 논리적 연결에서 제거됨
                else:           # 이전 노드가 없는 경우 == 제일 앞 front인 경우
                    self.products.front = current.next  
                if current == self.products.rear:   # 만약 current가 마지막 노드(rear)였으면 privious.next가 None을 가르킴
                    self.products.rear = previous   # rear를 previous 수정해야 함
                self.products.size -= 1
                # 여기까지가 삭제 시퀀스
                # 이제부터 current 위치를 이동시킴
                if not previous: # previous가 false일 때 true. 맨 앞의 front 노드일 때
                    current = self.products.front # 이미 current는 이동했음
                else:           # 2번 이후의 노드일 때
                    current = previous.next
                            
            else:
                previous = current  # 탐색하는 노드 다음으로 이동
                current = current.next
                
                
    def get_inventory(self):
        current = self.products.front
        inventory_list = []
        
        while current:
            inventory_list.append(current.data.id)
            current = current.next
            
        return inventory_list[::-1]    


## input을 어떻게 할지 도저히 모르겠어서 GPT 사용했
class ProductInventorySystem:
    def __init__(self):
        self.inventory = ProductInventory()

    def process_command(self, command):
        parts = command.split()
        if parts[0] == "add_product":
            id, production_timestamp, expiration_timestamp = map(int, parts[1:])
            self.inventory.add_product(id, production_timestamp, expiration_timestamp)
        elif parts[0] == "sell_product":
            result = self.inventory.sell_product()
            if result != -1:
                print(result)
        elif parts[0] == "remove_expired_products":
            current_timestamp = int(parts[1])
            self.inventory.remove_expired_products(current_timestamp)
        elif parts[0] == "get_inventory":
            inventory_list = self.inventory.get_inventory()
            print(inventory_list)

def main():
    system = ProductInventorySystem()
    try:
        while True:
            command = input()
            system.process_command(command)
    except EOFError:
        pass  # 입력이 끝나면 반복 종료

if __name__ == "__main__":
    main()


