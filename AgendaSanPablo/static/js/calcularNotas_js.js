var ultimo = 1;
var res =0;
function calcularNotas(){

}
function agregar(){
	$("#contenido").append("<div id='inp_"+ultimo+"' class='row'><div class='input-field col s4 push-s1'><input id='not_"+ultimo+"' type='number'><label for='not_"+ultimo+"'>Nota</label></div><div class='input-field col s4 push-s2'><input id='pes_"+ultimo+"' type='number'><label for='pes_"+ultimo+"'>Peso</label></div></div>");
	ultimo++;
}
function borrar(){
	$("inp_"+ultimo).remove();
	ultimo--;
}
function suma(){
	for (var i = 0; i < ultimo; i++) {
		a = $("#not_"+i).val();
		b = $("#pes_"+i).val();
		res+=a*b;
	}
	$("#contenido").html("");
	$("#contenido").append("<div id='inp_0' class='row'><div class='input-field col s4 push-s1'><input id='not_0' type='number'><label for='not_0'>Nota</label></div><div class='input-field col s4 push-s2'><input id='pes_0' type='number'><label for='pes_0'>Peso</label></div></div>");
	ultimo = 1;
	res = parseFloat(res).toFixed(2);
	$("#resultado").html("<h5 style='margin-top:3em; margin-left: 2em;' > Tu Acumulado hasta la fecha es "+res+"</h5>");
	res=0;

}
$(document).ready(function(){
	$("#add_inputs").click(function(){
		agregar();
	});

	$("#delete_inputs").click(function(){
		console.log("borrar");
		borrar();
	});

	$("#sumar").click(function(){
		suma();
	})
});
