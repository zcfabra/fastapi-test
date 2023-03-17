import requests
import json

valid_data = {
    "id": "asdnaiosudn",
    "name": "bob",
    "age": 20,
}

# should be invalid b/c id is an int not a str 


# ok so this actually works which is weird. There's no validation error, 
# but it does interpret id as a string on the other side 
# it might be ok, but something nice to be aware of since it won't be caught in validation
invalid_data_a = {
    "name": "bob",
    "id": 10,
    "age": 20,
    "posts": []
}
# should be invalid b/c diff. property names

# ok so this doesn't pass validation b/c of diff property names
invalid_data_b = {
    "userName": "bob",
    "user_id": "asdnaiosudn",
    "age": 20,
    "posts": []
}
payload = json.dumps(valid_data)
print(payload)

res = requests.post("http://localhost:8000/create",json=invalid_data_a, headers={"Content-Type":"application/json", "accept": "application/json"})
print(res.json())