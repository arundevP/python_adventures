import os

def list_to_dict(l):
    return dict(zip(map(str, range(len(l))), l))

def dd(d1, d2, ctx=""):
    print "Changes in " + ctx
    for k in d1:
        if k not in d2:
            print k + " removed from d2"
    for k in d2:
        if k not in d1:
            print k + " added in d2"
            continue
        if d2[k] != d1[k]:
            if type(d2[k]) not in (dict, list):
                print k + " changed in d2 to " + str(d2[k])
            else:
                if type(d1[k]) != type(d2[k]):
                    print k + " changed to " + str(d2[k])
                    continue
                else:
                    if type(d2[k]) == dict:
                        dd(d1[k], d2[k], k)
                        continue
                    elif type(d2[k]) == list:
                        dd(list_to_dict(d1[k]), list_to_dict(d2[k]), k)

    print "Done with changes in " + ctx
    return

a = {'icon_list': [{'weight': 60, 'height': 20}, {'iq': 200, 'age': 23}, {'hobbies': [1, 2, 3]}], 'name': 'arun'}
b = {'icon_list': [{'weight': 60, 'height': 20}, {'iq': 20, 'age': 53}, {'hobbies': [2, 3]}], 'name': 'tt'}
dd(a, b)