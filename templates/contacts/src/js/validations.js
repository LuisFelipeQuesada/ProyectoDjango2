function validateForm() {
	var name = document.getElementById("id_name").defaultValue;
	var lastName = document.getElementById("id_lastName").defaultValue;
	var age = document.getElementById("id_age").defaultValue;
	var phone = document.getElementById("id_phone").defaultValue;
	var email = document.getElementById("id_email").defaultValue;
	var business = document.getElementById("id_business").defaultValue;
	var lat = document.getElementById("id_latitud").defaultValue;
	var lng = document.getElementById("id_longitud").defaultValue;
	if (name == null || name =="" || lastName == null || lastName =="" || age == null || age =="" || phone == null || phone =="" || email == null || email =="" || business == null || business =="" || lat == null || lat =="")
	{
		document.getElementById("id_button").disabled = true;
	}
	else {
		document.getElementById("id_button").disabled = false;
	}
}

//function validateName() {
//	if(document.getElementById("id_name").defaultValue == null || document.getElementById("id_name").defaultValue == "") {
//		document.getElementById("id_button").disabled = true;
//	}
//	else {
//		document.getElementById("id_button").disabled = false;
//	}
//}




