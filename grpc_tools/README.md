# package install 

```bash
pip3 install grpcio
pip3 install grpcio-tools
```

# create py file

```bash

protoc -I ../../protos --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_python_plugin` ../../protos/route_guide.proto
```

```bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto 
```

# speedy command

```bash
python3 create_pb_py.py `pwd`/test/hello.proto
```