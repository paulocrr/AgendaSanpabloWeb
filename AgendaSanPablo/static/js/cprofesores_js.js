$(document).ready(function(){
	$.ajax({
		url: '/calProfesores/getProfesores/',
		dataType: 'json',
		success: function (json) {
			for(var i =0;i<json.length;i++){
				$("#listProfes").append("<div class='col s12 m3 l3'><div class='card light-blue darken-4'><div class='card-content white-text'><span class='card-title'>Profesor: "+json[i][0]+" "+json[i][1]+"</span><p>Promedio actual es: "+json[i][2]+" y su Numero de votos es: "+json[i][3]+"</p></div><div class='card-action'><a href='/calProfesores/CalificarProfesor/?id="+json[i][4]+"&&nom="+json[i][0]+"&&ap="+json[i][1]+"'>Calificar</a></div></div></div>")
			}
	}
	});


});