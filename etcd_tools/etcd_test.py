import etcd

etcd_config = (
    ('127.0.0.1', 2379),
    ('127.0.0.1', 22379),
    ('127.0.0.1', 32379),
)

class Etcd_Tools(object):
    def __init__(self, etcd_cfg: etcd_config):
        self.__client = etcd.Client(host=etcd_cfg, allow_reconnect=True)


    def put(self, key, value, ttl=0) -> etcd.EtcdResult:
        return self.__client.write(key, value, ttl)


    def get(self, key) -> etcd.EtcdResult:
        return self.__client.get(key)

if __name__ == '__main__':
    e = Etcd_Tools(etcd_config)
    print( e.put('lalala', 12345) )
    print( e.get('lalala') )