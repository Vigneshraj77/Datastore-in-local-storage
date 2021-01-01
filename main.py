import json

class Datastore:

    def __init__(self, path):
        self.path = path
        self.mutex = 0
    def Create(self):
        self.mutex=self.mutex + 1
        if(mutex > 1):
            print("DETECTED DEADLOCK")
            return None
        data = {}
        # add a team member
        key = input("ENTER THE KEY : ")
        file = open(self.path,)
        data = json.load(file)
        if(data[key] != None):
            print("the key already exist")
            return None
        value = input("ENTER THE VALUE IN JSON FORMAT : ")
        data[key] = value
        with open(self.path, 'a') as f:
            json.dump(data , f)
        # when finished, close the file
        f.close()
        print("successfully created a datastore")
        self.mutex = self.mutex - 1

    def Read(self):
        self.mutex=self.mutex + 1
        if(mutex > 1):
            print("DETECTED DEADLOCK")
            return None
        f = open(self.path,)
        key=input(" ENTER THE KEY : ")
        data = json.load(f)
        print(data[key])
        # Closing file 
        f.close()
        self.mutex = self.mutex - 1
        
    def Delete(self):
        self.mutex=self.mutex + 1
        if(mutex > 1):
            print("DETECTED DEADLOCK")
            return None
        with open(self.path, 'r') as data_file:
            data = json.load(data_file)
        key=input(" ENTER THE KEY : ")
        for element in data:
            element.pop(key, None)
        with open('data.json', 'w') as data_file:
            data = json.dump(data, data_file)
        data_file.close()
        self.mutex = self.mutex - 1
        print("successfully deleted the object from datastore")

print("1. Provide a path to file ")
print("2. Default location ")
opt = int(input("Choose from above option :"))
if(opt == 1):
      path = input("ENTER THE FILE LOCATION :")
      instance = Datastore(path)
elif(opt == 2):
    path ="C:\Mydatastore.json"
    instance = Datastore(path)
print("1. Create a datastore ")
print("2. Read from a datastore ")
print("3. Delete a value from datastore ")
print("CHOOSE FROM THE OPTION : ")
choice = int(input())
if(choice == 1):
    instance.Create()
elif(choice == 2):
    instance.Read()
elif(choice == 3):
    instance.Delete()
