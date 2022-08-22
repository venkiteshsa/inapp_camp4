var params = {
    "id": 8,
    "email": "testuser8@gmail.com",
    "password": "testpassword8",
    "first_name": "FirstName 8",
    "last_name": "LastName 8",
    "mobile_no": "88888888888",
    "date_of_joining": "08-08-2021"
}

fetch("https://localhost:3001/staff", {
    method: 'post',
    headers: {
        'Accept' : 'application/json, text/plain, */*',
        'Content-Type' : 'application/json'
    },
    body: JSON.stringify(params)
})
.then((response) => response.json())
.then((data) => console.log(data)) // printing data to console
.catch((error) => console.log(error))

