import json
from difflib import get_close_matches

# step:1
# data = json.loads(open("/home/prime/work_space/surya/python/project/interactive_dict/ data.json"))
with open("/home/prime/work_space/surya/python/project/interactive_dict/ data.json") as file:
    data = json.load(file)

# step:4---w == word
def translate(w):
    # check the key in data
    if w in data:
        return data[w]
    # check close matches
    elif len(get_close_matches(w, data.keys())) > 0:
        que = raw_input("Did you mean {} instead of {}, y/n :".format(get_close_matches(w,data.keys())[0],w))
        if que == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        elif que == 'n':
            return 'Word does not exist..! please double check.1'
        else:
            return "We can't understand your entry.."
    else:
        return 'Word does not exist..! please double check.'
# step:2
word = raw_input("Enter a Word: ").lower()

# step:3
output = translate(word)

# step:5
if type(output) == list:
    for i in output:
        print i
else:
    print output