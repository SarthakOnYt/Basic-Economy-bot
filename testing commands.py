import json
my_json = {
   "name" : "Kalyan",
   "age" : 25,
   "city" : 'Delhi'
}
a = json.dumps(my_json,indent = 4)
print(a)