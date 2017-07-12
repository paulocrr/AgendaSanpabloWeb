
$(document).ready(function(){
	$('.timepicker').pickatime({
	    autoclose: false,
	    twelvehour: false,
	    default: '14:20:00'
	  });
	$.ajax({
		url: '/inicio/getCursos/',
		dataType: 'json',
		success: function (json) {
			//$("#inp_curso").html("");
			for(var i =0;i<json.length;i++){
				$("#inp_curso").append("<option value='"+json[i][0]+"'>"+json[i][1]+"</option>");
			}
			$.ajax({
				url: '/inicio/getDias/',
				dataType: 'json',
				success: function (json) {
					$("#inp_dia").html("");
					for(var i =0;i<json.length;i++){
						$("#inp_dia").append("<option value='"+json[i][0]+"'>"+json[i][1]+"</option>");
					}
					$('select').material_select();
				}
			});
		}
	});
	

});
