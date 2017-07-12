function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function getCursosxDia(idDia){
	var csrftoken = getCookie('csrftoken');
	$.ajax({
		url: '/inicio/getCursosPorDia/',
		type:"POST",
		data:"id_dia="+idDia,
		dataType: 'json',
		beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
		success: function (json) {
			$("#inp_curso").html("");
			if(json.length==0){
				$("#dia_"+idDia).append("<li class='collection-item'><div>Genial Tienes el Dia Libre</div></li>");
			}else{
				for(var i =0;i<json.length;i++){
					$("#dia_"+idDia).append("<li class='collection-item'><div>Curso: "+json[i][1]+" - De "+json[i][3]+" A "+json[i][4]+"<a href='#!' class='secondary-content'><i class='material-icons blue-text'>edit</i></a></div></li>");
				}
			}
		}
	});
}
$(document).ready(function(){
	$.ajax({
		url: '/inicio/getDias/',
		dataType: 'json',
		success: function (json) {
			$("#inp_curso").html("");
			for(var i =0;i<json.length;i++){
				$("#dias").append("<div class='col s12 m3 l3'><ul class='collection with-header' id='dia_"+json[i][0]+"'><li class='collection-header'><h4>"+json[i][1]+"</h4></li></ul></div>");
				getCursosxDia(json[i][0]);
			}
		}
	});
});