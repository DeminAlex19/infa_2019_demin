from classes import *
import datetime


def read_level(level_name):
    objects = []

    with open(level_name + '.txt') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            object_type = line.split()[0].lower()
            if object_type == "block":
                block_one = Block()
                block_one.parse_parametrs(line)
                objects.append(block_one)
                del block_one
            if object_type == "body":
                body_one = Body()
                body_one.parse_parametrs(line)
                objects.append(body_one)
                del body_one
            if object_type == "item":
                item_one = Item()
                item_one.parse_parametrs(line)
                objects.append(item_one)
                del item_one
            del object_type

    return objects


def find_hero(objects, hero):
    for obj in objects:
        if obj.type == 'hero':
            hero = obj
    return hero


def write_scores(file, level_name, score):
    with open(file, 'w') as out_file:
        out_file.write("%s %s, score: %d" % (str(datetime.datetime.now()), level_name, score))


def view_scores(win):
    None
