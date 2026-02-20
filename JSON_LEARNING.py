import json
people_string = '''
{
    "people": [
        {
            "name": "aftermeth",
            "phone": "730-72702-32",
            "emails": ["shivanshshukla2080@gmail.com"],
            "has_license": false
        },
        {
            "name":"shivansh",
            "phone":"678-7899-678",
            "emails": null,
            "has_license": true
        }

    ]

}

'''
#loading the jsn --> pyhton
data = json.loads(people_string)
print(type(data['people']))
# print(data)

# for person in data['people']:
#     print(person['name'])

#dumping pyhton --> json

for person in data['people']:
    del person['phone']

new_string = json.dumps(data)

print(new_string)

