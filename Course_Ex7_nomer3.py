def get_line_count(file_name: str):
    counter = 0
    f = open(file_name, "r")
    while True:
        s = f.readline()
        if s == "":
            break
        counter += 1
    f.close()
    return counter


def get_file_by_count(count: int, d: dict):
    res = ""
    for file_name, v in d.items():
        if v == count:
            res = file_name
            break
    return res


def add_lines_to_file(source_file: str, receiver_file: str, last_file: bool):
    sf = open(source_file, "r")
    rf = open(receiver_file, "a")
    rf.write(source_file + "\n")
    c = str(get_line_count(source_file))
    rf.write(c + "\n")
    while True:
        s = sf.readline()
        if s == "":
            if not last_file:
                rf.write("\n")
            break
        rf.write(s)
    sf.close()
    rf.close()


def del_info(file_name: str, d: dict):
    del d[file_name]


# Основной алгоритм
f_list = ["1.txt", "2.txt", "3.txt"]
c_list = []
d = {}
for s in f_list:
    a = get_line_count(s)
    c_list.append(a)
    d[s] = a
c_list.sort()

receiver_file = "result.txt"
for count in c_list:
    # Проверка на последний файл
    c = len(d)
    if c == 1:
        last_file = True
    else:
        last_file = False
    # Добавление в файл
    file_name = get_file_by_count(count, d)
    add_lines_to_file(file_name, receiver_file, last_file)
    del_info(file_name, d)
