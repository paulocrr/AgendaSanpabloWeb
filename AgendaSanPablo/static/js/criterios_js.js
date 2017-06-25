$(document).ready(function(){
	$('select').material_select();
	$.ajax({
		url: '/calProfesores/getCriterios/',
		dataType: 'json',
		success: function (json) {
			for(var i =0;i<json.length;i++){
				$("#textcriterios").append("<div class='row'><div class='input-field col s12'><select name='"+i+"'><option value='1'>1</option><option value='2'>2</option><option value='3'>3</option><option value='4'>4</option><option value='5'>5</option></select><label>Criterio: "+json[i][1]+"</label></div></div>");
				$('select').material_select();
			}
	}
	});

});