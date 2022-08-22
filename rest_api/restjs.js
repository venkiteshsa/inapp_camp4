var params = {
    "id": 7,
    "email": "testuser7@gmail.com",
    "password": "testpassword7",
    "first_name": "FirstName 7",
    "last_name": "LastName 7",
    "mobile_no": "7777777777",
    "date_of_joining": "07-07-2021"
}

var request = new XMLHttpRequest()
request.open('POST', 'http://localhost:3001/staff')
request.setRequestHeader('Content-type', 'application/json')
request.send(JSON.stringify(params))

request.onload = loadData

function loadData() {
    // create a new XMLHttpRequest
    var request = new XMLHttpRequest()
    // open the API end point url using the open() method
    request.open('GET', 'http://localhost:3001/staff')
    // sending the request
    request.send();
    // after completing the request process, check the status
    request.onload = () => {
        // checking if success
        if(request.status === 200){
            const users = JSON.parse(request.response);
            tbody = document.getElementById('users')
            users.forEach(user => {
                const row = document.createElement('tr')
                const id = document.createElement('td');
                const fname = document.createElement('td');
                const lname = document.createElement('td');
                const email = document.createElement('td');
                id.innerText = user.id;
                fname.innerText = user.first_name;
                lname.innerText = user.last_name;
                email.innerText = user.email;
                row.appendChild(id)
                row.appendChild(fname)
                row.appendChild(lname)
                row.appendChild(email)
                tbody.appendChild(row)
            });
        }else{
            console.log('Cannot contact server');
        }
    }
}
