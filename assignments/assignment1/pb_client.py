import socket
import json


host = socket.gethostname()
port = 5000
client_socket = socket.socket()
client_socket.connect((host, port))

def sort():
    client_socket.send(json.dumps({'fun': 'list'}).encode())
    response = json.loads(json.loads(client_socket.recv(1024).decode()))
    if response['status'] == "ok":
        for name, number in response["contacts"].items():
            print(f'Name : {name}')
            print(f'Number : {number}')
    else:
        print(response['message'])

def add():
    name = input("Enter contact name:")
    no = input("Enter contact no.:")
    client_socket.send(json.dumps({'fun': 'add', 'name' : name, 'number' : no}).encode())
    response = json.loads(json.loads(client_socket.recv(1024).decode()))
    print(response['message'])
    

def searchName():
    name = input("Enter contact name:")
    client_socket.send(json.dumps({'fun': 'searchName', 'name' : name}).encode())
    response = json.loads(json.loads(client_socket.recv(1024).decode()))
    if response['status'] == 'ok':
        name = response['contact']['name']
        number = response['contact']['number']
        print(f'Name: {name}')
        print(f'Number: {number}\n')
    else:
        print(response["message"])

def searchNo():
    no = input("Enter contact no.:")
    client_socket.send(json.dumps({'fun': 'searchNo', 'number' : no}).encode())
    response = json.loads(json.loads(client_socket.recv(1024).decode()))
    if response['status'] == 'ok':
        name = response['contact']['name']
        number = response['contact']['number']
        print(f'Name: {name}')
        print(f'Number: {number}\n')
    else:
        print(response["message"])

def delete():
    name = input("Enter contact name:")
    client_socket.send(json.dumps({'fun': 'delete', 'name' : name}).encode())
    response = json.loads(json.loads(client_socket.recv(1024).decode()))
    print(response['message'])



while True:
    print("\nYellow Pages\n")
    print("1. List all contacts \n2. Add a new contact \n3. Search by name \n4. Search by number \n5. Delete a contact \n6. Exit")
    opt = int(input("\nEnter your choice:"))
    match opt:
        case 1: sort()
        case 2: add()
        case 3: searchName()
        case 4: searchNo()
        case 5: delete()
        case 6: break
        case _: print("\nInvalid choice!\n")

client_socket.close()

