#!/usr/bin/env python

import re

def process_info(value):
    field_value = value.replace(" ","").replace("-","")

    field_name_str = ""
    stage_lst = []
    stage_lst2 = []
    pre = ""
    aux = ""
    count = 1

    for b in field_value:
        count += 1
        # if b.isdigit():
        if re.match("[0-9]",b):
            # print("Digit: {}".format(b))
            aux = b
        if re.match("[A-Z]",b):
            # print("Letter: {}".format(b))
            aux = b
        
        if (pre == ""):
            pre = aux
        else:
            if re.match("[0-9]",pre) and re.match("[0-9]",aux) and (re.match("[0-9]",pre) is not None):
                pre += aux
                if aux == field_value[len(field_value)-2] and count == len(field_value):
                    stage_lst.append(pre)
            elif re.match("[A-Z]",pre) and re.match("[A-Z]",aux) and (re.match("[A-Z]",pre) is not None):
                pre += aux
                if aux == field_value[len(field_value)-2] and count == len(field_value):
                    stage_lst.append(pre)
            else:
                stage_lst.append(pre)
                pre = aux

    # print("here")

    size_last_field = len(stage_lst[3])
    class_field = stage_lst[3][:size_last_field - 2]
    state = stage_lst[3][-2:]

    stage_lst2.append(stage_lst[0])
    stage_lst2.append(stage_lst[1])
    stage_lst2.append(stage_lst[2])
    stage_lst2.append(class_field)
    stage_lst2.append(state)

    # Adding space to the field name, if the same is not complete
    if len(stage_lst2[1]) == 0:
        stage_lst2[1] = "   "
    if len(stage_lst2[1]) == 1:
        stage_lst2[1] = stage_lst2[1] + "  "
    if len(stage_lst2[1]) == 2:
        stage_lst2[1] = stage_lst2[1] + " "

    # Adding space to the field number, if the same is not complete
    if len(stage_lst2[2]) == 0:
        stage_lst2[2] = "0000"
    if len(stage_lst2[2]) == 1:
        stage_lst2[2] = "000" + stage_lst2[2]
    if len(stage_lst2[2]) == 2:
        stage_lst2[2] = "00" + stage_lst2[2]
    if len(stage_lst2[2]) == 3:
        stage_lst2[2] = "0" + stage_lst2[2]

    # Adding space to the field well classification, if the same is not complete
    if len(stage_lst2[3]) == 0:
        stage_lst2[3] = "  "
    if len(stage_lst2[3]) == 1:
        stage_lst2[3] = stage_lst2[3] + " "

    stage_lst2.insert(2," ")

    return stage_lst2
    print("here")


def main():
    # print("hello")
    with open("pocos_exemplo","r") as fp:
        data = fp.read().split("\n")
        # print(data)
        for row in data:
            if len(row) > 0:
                final_value = ""
                first_field = row.split(",")[0]
                second_field = row.split(",")[1]
                third_field = row.split(",")[2]

                aux = process_info(third_field)
                final_value = final_value.join(aux)
                print("{},{},{}".format(first_field, second_field, final_value))
                pass




if __name__ == "__main__":
    main()