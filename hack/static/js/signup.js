(function($) {
  $(document).ready(function(){
    $( "#id_username" ).addClass('form-control');
    $( "#id_username" ).attr('placeholder', 'Username');
    $( "#id_username" ).prop('required', true);
    $( "#id_password1" ).addClass('form-control');
    $( "#id_password1" ).attr('placeholder', 'Password');
    $( "#id_password1" ).prop('required', true);
    $( "#id_password2" ).addClass('form-control');
    $( "#id_password2" ).attr('placeholder', 'Re-enter Password');
    $( "#id_password2" ).prop('required', true);
    var check_user = function() {
      var v = $("#id_username").val();
      var error;
      if ((/^[a-zA-Z0-9\@\.\+\-\_]*$/.test(v)) &&
          (v.length < 31) &&
          (v.length > 0)) {
        error = false;
        $( "#usr-help" ).hide('fast');
      } else {
        error = true;
        $( "#usr-help" ).show('slow');
      }
      // cleaning up
      $( "#user" ).removeClass('has-success has-error');
      // adding status
      if (error) {
        $( "#user" ).addClass('has-error')
        return false;
      } else {
        $( "#user" ).addClass('has-success')
        return true;
      }
    };
    var check_pass = function() {
      var v = $("#id_password1").val();
      var error;
      if (0 < v.length) {
        error = false;
        $( "#pass-help" ).hide('fast');
      } else {
        error = true;
        $( "#pass-help" ).show('slow');
      };
      // cleaning up
      $( "#password" ).removeClass('has-success has-error');
      // adding status
      if (error) {
        $( "#password" ).addClass('has-error')
        return false;
      } else {
        $( "#password" ).addClass('has-success')
        return true;
      };
    };
    var check_cpass = function() {
      var v = $("#id_password1").val();
      var v2 = $("#id_password2").val();
      var error;
      if (v == v2) {
        error = false;
        $( "#cpass-help" ).hide('fast');
      } else {
        error = true;
        $( "#cpass-help" ).show('slow');
      };
      // cleaning up
      $( "#cpassword" ).removeClass('has-success has-error');
      // adding status
      if (error) {
        $( "#cpassword" ).addClass('has-error')
        return false;
      } else {
        $( "#cpassword" ).addClass('has-success')
        return true;
      };
    };
    $("#id_username").keyup(check_user);
    $("#id_password1").keyup(check_pass);
    $("#id_password1").keyup(check_cpass);
    $("#id_password2").keyup(check_cpass);
  });
})(jQuery);
