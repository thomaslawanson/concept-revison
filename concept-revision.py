import random  # random


def list_generator(list_size):
    empty_lst = []

    for i in range(list_size):
        rand = random.randint(1, 7)  # 7 is odd
        empty_lst.append(rand)

    return empty_lst


opt = list_generator(440)

print(opt)
print(len(opt))

# if we're removing lots of items in a list, using a loop,
# we need to iterate over a copy of the list instead of the list itself
# then remove the item from the original list

for i in opt.copy():
    if i == 3:
        opt.remove(i)

print(opt)
print(len(opt))

