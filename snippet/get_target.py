def get_target(default_port):
    import sys
    host = sys.argv[1] if len(sys.argv) >= 2 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) >= 3 else default_port
    return host, port

# r = remote(*get_target(CHANGE_ME_TO_SERVICE_PORT))
