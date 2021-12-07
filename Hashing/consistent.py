# REALLY high-level Consistent Hashing for use in horizontal scaling for DBs or Caches or whatever
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
    return hash_function(path)


def _get_node(idx):
    return storage_nodes[idx]


def upload(path):
    index = _get_index(path)
    node = _get_node(index)
    return node.put_file(path)


def fetch(path):
    index = _get_index(path)
    node = _get_node(index)
    return node.fetch_file(path)
