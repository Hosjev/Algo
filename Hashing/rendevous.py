storage_nodes = [
        # Some named object/class
        StorageNode(name="A", host="10.22.101.34"),
        StorageNode(name="B", host="10.22.101.35"),
        StorageNode(name="C", host="10.22.101.36"),
        StorageNode(name="D", host="10.22.101.37"),
        StorageNode(name="E", host="10.22.101.38")
    ]


class StorageNode:

    def __init__(self, name, host):
        self.name = name
        self.host = host

    def fetch_file(self, path):
        return f"{path}"

    def put_file(self, path):
        return f"{path}"


class Hash:

    def __init__(self):
        self.maxScore = None
        self.maxServer = None

    def pickServer(self, node):
        for node in storage_nodes:
            score = compute_score(username or hostname, node)
            if not self.maxScore and score > self.maxScore:
                self.maxScore = score
                self.maxServer = node
        return self.maxServer



def hash_string(string):
    hash_i = int()
    if len(string) == 0: return hash_i
    for char in string:
        char_code = ord(char)
        hash_i = (hash_i << 5) - hash_i + char_code
        hash_i |= 0
    return hash_i

def compute_score(username or hostname, node):
    unique_thing_to_hash = hash_string(...)
    node_hash = hash_string(node)
    return (unique_thing * 13 + node_hash * 11) % 67
