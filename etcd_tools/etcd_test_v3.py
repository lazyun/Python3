import etcd3

etcd_config = (
    ('127.0.0.1', 2379),
    ('127.0.0.1', 22379),
    ('127.0.0.1', 32379),
)

class Etcd_Tools(object):
    def __init__(self, etcd_cfg: etcd_config):
        self.__client = etcd3.Client(max_retries=3)


    def get_client_version(self):
        self.__client.version()

    def put(self, key, value, ttl=0):
        return self.__client.put(key, value, ttl)


    def get(self, key):
        return self.__client.range(key)

if __name__ == '__main__':
    e = Etcd_Tools(etcd_config)
    print( e.put('lalala', 12345) )
    print( e.get('lalala') )