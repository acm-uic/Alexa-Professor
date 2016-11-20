import json 
with open('mydatafile') as f:
	a=json.load(f)

input_dump = raw_input()

data=json.loads(input_dump)


