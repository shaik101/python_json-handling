import json


# reading json file load() or loads()

with open("in.json","r") as file:
	data = file.read() # data is str 
	# data = json.load() --> data is dict



data = json.loads(data) # data is dict

print(type(data))
# print('json reading',data)


print("#"*50)

########################
# writing into json file dump() or dumps()
#########################
int = 0;
str = "some string"
list = ["name","shaik"]
dict = {"mydict":"some value"}

with open('out.json', mode='w', encoding='utf-8') as f:
    json.dump([], f)

all_data  =[]

with open('out.json', mode='w', encoding='utf-8') as file:
	all_data.append(int)
	all_data.append(str)
	all_data.append(list)
	all_data.append(dict)
	json.dump(all_data, file)

print("done!")