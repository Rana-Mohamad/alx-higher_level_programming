#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp = 0
    for i in range(list_length):
        try:
            temp = my_list_1[i] / my_list_2[i]
            new_list.append(temp)
        except TypeError:
            new_list.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            new_list.append(0)
            print("out of range")
            continue
        finally:
            pass
    return new_list
