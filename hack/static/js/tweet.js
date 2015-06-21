(function($) {
  $(document).ready(function(){
    $("#id_data").keyup(function(event) {
      $("#info").text($("#id_data").val().length + '/140');
    });
  });
})(jQuery);
