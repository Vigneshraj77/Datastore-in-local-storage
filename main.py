import json
import os
from json.decoder import JSONDecodeError

class Datastore:

    def __init__(self, path):
        self.path = path
        self.mutex = 0
    def Create(self):
        self.mutex=self.mutex + 1
        if(self.mutex > 1):
            print("DETECTED DEADLOCK")
            return None
        data = {}
        mode = 'a' if os.path.exists(self.path) else 'w'
        create = open(self.path, mode)
        create.close()
        key = input("ENTER THE KEY : ")
        with open(self.path, "r") as file:
            try:
                data = json.load(file)
                if(data[key] != None):
                    print("Key already exist")
                    return
            except json.decoder.JSONDecodeError:
                print("file is empty")
            except KeyError:
                print("go ahead")
        value = input("ENTER THE VALUE IN JSON FORMAT : ")
        data_new={}
        data_new[key] = value
        with open(self.path, 'a') as f:
            json.dump(data_new , f)
        # when finished, close the file
        f.close()
        print("successfully created a datastore")
        self.mutex = self.mutex - 1

    def Read(self):
        self.mutex=self.mutex + 1
        data={}
        if(self.mutex > 1):
            print("DETECTED DEADLOCK")
            return None
        key=input(" ENTER THE KEY : ")
        with open(self.path, "r+") as file:
            try:
                data = json.load(file)
                if(data[key] == None):
                    print("key not found")
                    return None
            except json.decoder.JSONDecodeError:
                print("file is empty")
                return None
            except KeyError:
                print("Key not found")
                return None
        print(data[key])
        self.mutex = self.mutex - 1
        
    def Delete(self):
        self.mutex=self.mutex + 1
        if(self.mutex > 1):
            print("DETECTED DEADLOCK")
            return None
        key=input(" ENTER THE KEY : ")
        with open(self.path, "r+") as file:
            try:
                data = json.load(file)
                if(data[key] == None):
                    print("key not found")
                    return None
            except json.decoder.JSONDecodeError:
                print("file is empty")
                return None
            except KeyError:
                print("Key not found")
                return None
        for element in data:
            element.pop(key, None)
        with open(self.path, 'w') as data_file:
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
    path ="D:\Mydatastore.json"
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
