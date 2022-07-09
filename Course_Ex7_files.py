def add_block(b: list, cb: dict):
    dish = b[0]
    cb[dish] = []
    b.pop(0)
    b.pop(0)
    for s in b:
        d = ingredient_to_dict(s)
        cb[dish].append(d)


def ingredient_to_dict(s: str):
    d = {}
    arr = s.split(" | ")
    d["ingredient_name"] = arr[0]
    d["quantity"] = int(arr[1])
    d["measure"] = arr[2]
    return d


def get_dishes(cb: dict):
    d = []
    for key in cb.keys():
        for ingredient in cb[key]:
            s = ingredient["ingredient_name"]
            d.append(s)
    d = set(d)
    d = list(d)
    return d


def get_ingr_info(name: str, cb: dict):
    d = {}
    for key in cb.keys():
        for ingredient in cb[key]:
            s = ingredient["ingredient_name"]
            if s == name:
                q = ingredient["quantity"]
                m = ingredient["measure"]
                a = d.get("quantity")
                if a == None:
                    a = 0
                d["measure"] = m
                d["quantity"] = q + a

    return d


def get_shop_list_by_dishes(dishes: list, person_count: int):
    d = {}
    for dish in dishes:
        d[dish] = get_ingr_info(dish, cook_book)
    return d


"""Задача 2"""
cook_book = {}
block = []

f = open(r"recipes.txt", "r")
while True:
    s = f.readline()
    if s == "":
        add_block(block, cook_book)
        break
    s = s.strip()
    if s != "":
        block.append(s)
    else:
        add_block(block, cook_book)
        block.clear()
f.close()

"""Задача 2"""
dishes = get_dishes(cook_book)
shop_list = get_shop_list_by_dishes(dishes, 10)
print(shop_list)