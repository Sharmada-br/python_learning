def get_argument(*args):
    print("type:",type(args))
    print("first argument:",args[0])
    print("second argument:",args[1])
    print("all the arguments:",args)
get_argument("abc","bcd","dfg")