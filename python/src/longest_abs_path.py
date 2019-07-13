def is_dir(dirent):
    return dirent.rfind('.') == -1

def next_dirent(path):
    dirent = ''

    for ch in path:
        if ch == '\n':
            yield dirent
            dirent = ''
        else:
            dirent += ch
    yield dirent

def next_file(path):
    abs_path = []
    
    for dirent in next_dirent(path):
        tab_count = dirent.count('\t')
        while len(abs_path) != tab_count:
            abs_path.pop()

        if is_dir(dirent):
            abs_path.append(dirent[tab_count:])
        else:
            yield "/".join(abs_path + [dirent[tab_count:]])

def longest_abs_path(path):
    longest = 0

    for file in next_file(path):
        n = len(file)
        if n > longest:
            longest = n
    return longest

fs = 'dir\n\tsubdir\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
print(longest_abs_path(fs))
