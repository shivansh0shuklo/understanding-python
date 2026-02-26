import json 

with open('output.json','r') as r:
    data = json.load(r)

print("hunting for score less than 100")


for  file in data['files']:
    path = file['path']
    licenses = file.get('licenses',[])
    for lic in licenses:
        score = lic.get('score',0)
        if(score <100):
            print(f"target found!: {path}")
            print(f"  --> license key: {lic.get('key')}")
            print(f"  --> score: {score}")
            print("-"*40)
            