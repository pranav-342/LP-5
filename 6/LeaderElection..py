

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.is_coordinator = False

    def initiate_election(self, nodes):
        for node in nodes:
            if node.id > self.id:
                print(f"Node {self.id} sends election message to Node {node.id}")
                node.start_election(nodes)
        self.is_coordinator = True
        print(f"Node {self.id} becomes the coordinator.")

    def start_election(self, nodes):
        for node in nodes:
            if node.id > self.id:
                print(f"Node {self.id} sends election message to Node {node.id}")
                node.start_election(nodes)
        self.is_coordinator = True
        print(f"Node {self.id} becomes the coordinator.")

if __name__ == "__main__":
    
    nodes = [Node(i) for i in range(1, 6)]

    print("Bully Algorithm:")

    nodes[-1].initiate_election(nodes)

    print("\nRing Algorithm:")

    nodes[0].start_election(nodes)



