import json
import socket
import re

contacts = dict()

def sort():
    if len(contacts) > 0:
       return json.dumps({
        'status': 'ok',
        'message': '',
        'contacts': contacts
       })
    else:
        return json.dumps({
        'status': 'error',
        'message': 'No contacts',
        'contacts': ''
       })
            

def add(data):
    contacts[data['name']] = data['number']
    return json.dumps({
        'status': 'ok',
        'message': 'Contact added'
    })


def searchName(data):
    for name, no in contacts.items():
        if name == data['name']:
            return json.dumps({
                'status': 'ok',
                'message': '',
                'contact': {
                    'name': name,
                    'number': no
                }
            })
    return json.dumps({'status': "error", "message": f"{data['name']} does not exist", 'contact': {}})


def searchNo(data):
    for name, no in contacts.items():
        if no == data['number']:
            return json.dumps({
                'status': 'ok',
                'message': '',
                'contact': {
                    'name': name,
                    'number': no
                }
            })
    return json.dumps({'status': "error", "message": f"{data['number']} does not exist", 'contact': {}})

def delete(data):
    if contacts.get(data["name"]):
        del contacts[data["name"]]
        return json.dumps({"status": "ok", "message": "Deleted"})
    else:
        return json.dumps({"status": "error", "message": f"{data['name']} does not exist"})


def server_program():
    host = socket.gethostname() 
    port = 5000 

    server_socket = socket.socket()

    server_socket.bind((host, port))
   
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        d = json.loads(str(data))
        match d['fun']:
            case 'add': response = json.dumps(add(d))
            case 'delete': response = json.dumps(delete(d))
            case 'searchName': response = json.dumps(searchName(d))
            case 'searchNo': response = json.dumps(searchNo(d))
            case 'list': response = json.dumps(sort())
            case _: response = json.dumps({'status': 'error', 'message': 'Invalid option'})
        conn.send(response.encode()) 
    conn.close() 

if __name__ == "__main__":
    while True:
        server_program()

