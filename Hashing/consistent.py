# REALLY high-level Consistent Hashing for use in horizontal scaling for DBs or Caches or whatever
# Mock object
import hashlib


class StorageNode:

    def __init__(self, name, host):
        self.name = name
        self.host = host

    def fetch_file(self, path):
        return f"{path}"

    def put_file(self, path):
        return f"{path}"


storage_nodes = [
        # Some named object/class
        StorageNode(name="A", host="10.22.101.34"),
        StorageNode(name="B", host="10.22.101.35"),
        StorageNode(name="C", host="10.22.101.36"),
        StorageNode(name="D", host="10.22.101.37"),
        StorageNode(name="E", host="10.22.101.38")
    ]


def hash_function(key: str, total_slots: int):
    hsh = hashlib.sha256()
    hsh.update(bytes(key.encode("utf-8")))
    return int(hsh.hexdigest(), 16) % total_slots


def _get_index(path):
    return hash_function(path, len(storage_nodes))


def _get_node(idx):
    return storage_nodes[idx]


def upload(path):
    index = _get_index(path)
    node = _get_node(index)
    return node.put_file(path)


def fetch(path):
    index = _get_index(path)
    node = _get_node(index)
    print(f"Here is our randomized index/node: {index, node.name}")
    return node.fetch_file(path)


if __name__ == "__main__":
    print(fetch("/home/foo.bar"))
