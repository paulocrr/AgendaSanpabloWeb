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
function getCosasPorHacer(){
	var csrftoken = getCookie('csrftoken');
	$.ajax({
		url: '/inicio/getTareas/',
		type:"POST",
		dataType: 'json',
		beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    },
		success: function (json) {

			for(var i =0;i<json.length;i++){
				$("#pendientes").append("<li id = '"+ json[i][0]+"'> <div class='collapsible-header'> <i class='material-icons'>assignment</i>"+ json[i][3]+" <p class='right'>"+json[i][2]+"</p></div><div class='collapsible-body'><p>"+json[i][1]+"</p><a href='/inicio/borrarTarea/"+ json[i][0]+"' class='right'>borrar</a></div></li>");
			}

		}
	});
}
$(document).ready(function(){
  getCosasPorHacer();
});
