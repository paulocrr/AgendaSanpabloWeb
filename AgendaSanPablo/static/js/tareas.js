$(document).ready(function(){
  $('select').material_select();
  $('#textarea1').trigger('autoresize');
  $('.datepicker').pickadate({
  selectMonths: true, // Creates a dropdown to control month
  selectYears: 15, // Creates a dropdown of 15 years to control year
  monthsFull: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
  monthsShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec'],
  weekdaysFull: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
  weekdaysShort: ['Dom', 'Lun', 'Mar', 'Miér', 'Jue', 'Vie', 'Sab'],
  });

  $.ajax({
    url: '/inicio/getCursosPersonales/',
    dataType: 'json',
    success: function (json) {
      for(var i =0;i<json.length;i++){
        $("#curso").append("<option value='"+json[i][0]+"'>"+json[i][1]+"</option>");
      }
      $('select').material_select();
    }
  });
});
