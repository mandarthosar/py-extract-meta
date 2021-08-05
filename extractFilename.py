import ntpath
# ntpath.basename("a/b/c")

def name(path):
    head, tail = ntpath.split(path)
    # or ntpath.basename(head)
    return tail

# print(name(path))
