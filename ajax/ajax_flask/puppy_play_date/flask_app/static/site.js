function getUsers() {
	fetch("http://localhost:5000/users")
		.then((res) => res.json())
		.then((data) => {
			var users = document.getElementById("users");
			for (let i = 0; i < data.length; i++) {
				let row = document.createElement("tr");

				let name = document.createElement("td");
				name.innerHTML = data[i].user_name;
				row.appendChild(name);

				let email = document.createElement("td");
				email.innerHTML = data[i].email;
				row.appendChild(email);
				users.appendChild(row);
			}
		});
}
getUsers();

function createUser() {
	var myForm = document.getElementById("myForm");
	myForm.onsubmit = function (e) {
		// "e" is the js event happening when we submit the form.
		// e.preventDefault() is a method that stops the default nature of javascript.
		e.preventDefault();
		// create FormData object from javascript and send it through a fetch post request.
		var form = new FormData(myForm);
		// this how we set up a post request and send the form data.
		fetch("http://localhost:5000/create/user", {
			method: "POST",
			body: form,
		})
			.then((response) => response.json())
			.then((data) => console.log(data));
	};
}
createUser();
function search(e) {
	e.preventDefault();
	var searchForm = document.getElementById("searchForm");
	var form = new FormData(searchForm);
	fetch("http://localhost:5000/search", { method: "POST", body: form })
		.then((res) => res.json())
		.then((data) => console.log(data));
}
search();
// async function getAnimals(header) {

// 	var apiRequest = await fetch(header+"GET https://api.petfinder.com/v2/animals");
// 	var animalData = await apiRequest.json();
// 	console.log(animalData);
// }

// getAnimals();

// async function getAnimals() {
// 	await fetch("http://localhost:5000/users")
// 		.then((res) => res.json())
// 		.then((data) => {
// 		console.log(data);
// 			var pets = document.getElementById("pets");
// 			for (let i = 0; i < data.length; i++) {
// 				let row = document.createElement("tr");

// 				// let name = document.createElement("td");
// 				// name.innerHTML = data[i].user_name;
// 				// row.appendChild(name);

// 				// let email = document.createElement("td");
// 				// email.innerHTML = data[i].email;
// 				// row.appendChild(email);
// 				pets.appendChild(row);
// 			}
// 		});
// }
// getAnimals();
