
# reading and replacing data again writing into that file

with open('test.txt','r') as file:
	data = file.read()

data = data.replace('category','replaced')


with open('test.txt','w') as file:
	data = file.write(data)

print('done!')