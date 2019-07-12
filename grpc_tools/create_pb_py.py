import sys
import os

target_dir = ''
target_file = ''
abs_proto_file = ''

cmd = 'python3 -m grpc_tools.protoc -I{2} --python_out={0} --grpc_python_out={0} {1}'

def create_pb_py_file():
    pass




if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        print("parameter number is err!\n")

    abs_proto_file = argv[1] if len(argv) == 2 else './'

    target_dir =  os.path.dirname(abs_proto_file)
    if not target_dir:
        print("file path is not absolute path!")
        os._exit(0)

    target_file = os.path.basename(abs_proto_file)
    # print( os.path.abspath(abs_proto_file) )
    # print( os.path.dirname(abs_proto_file) )

    # dir_list = os.listdir(work_dir)
    # proto_file = list(filter(lambda x: True if '.proto' in x else False, dir_list))
    # if proto_file:
    #     proto_file = proto_file[0]
    # os._exit(0)




    genetate_dir = os.path.join(target_dir, 'proto')
    # print(cmd.format(genetate_dir, abs_proto_file))
    # os._exit(1)
    if not os.path.isdir(genetate_dir):
        print("mkdir", genetate_dir)
        os.mkdir(genetate_dir)

    run_cmd = cmd.format(genetate_dir, target_file, target_dir)
    print("run cmd", run_cmd)
    os.system( run_cmd )

