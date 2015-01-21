var geocoder;
var map;
var json;

function initialize() {
	geocoder = new google.maps.Geocoder();
	var myOptions = {
		zoom: 8,
		center: new google.maps.LatLng(9.75, -84),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
	
	for (var i = 0, len = json.length; i < len; i++) {
		var name = json[i]['fields'].name;
		var business = json[i]['fields'].business;
		var lastName = json[i]['fields'].lastName;
		var age = json[i]['fields'].age;
		var phone = json[i]['fields'].phone;
		var email = json[i]['fields'].email;
		var latitud = json[i]['fields'].latitud;
		var longitud = json[i]['fields'].longitud;
		
		var location = new google.maps.LatLng(latitud, longitud);
		
		var marker = new google.maps.Marker({
			position: location,
			map: map
		});
		showInfo(marker, name, lastName, business, phone);
	}
}

function codeAddress() {
	var address = document.getElementById("address").value;
		geocoder.geocode( { 'address': address}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			map.setCenter(results[0].geometry.location);
			var marker = new google.maps.Marker({
				map: map,
				position: results[0].geometry.location
			});
		}
		else {
			alert("Geocode was not successful for the following reason: " + status);
		}
	});
}

function getData(parsed_json) {
	json = parsed_json;
}

function showInfo(marker, name, lastName, business, phone) {
	var infowindow = new google.maps.InfoWindow( {
		content: name + " " + lastName + "\n" + business + "\n" + phone,
		size: new google.maps.Size(50,50)
	});
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.open(map,marker);
	});
}






