from livereload import Server
server = Server()
server.watch('kmd_tehingupaevik_ver2.html')
server.serve(root='.', port=5500, host='0.0.0.0', open_url_delay=None)
