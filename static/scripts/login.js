$(document).ready(function() {
    $('#username').on('focus', function() {
      $('#usernameIcon').hide();
    }).on('blur', function() {
      if ($('#username').val() === '') {
        $('#usernameIcon').show();
      }
    });
  
    $('#password').on('focus', function() {
      $('#passwordIcon').hide();
    }).on('blur', function() {
      if ($('#password').val() === '') {
        $('#passwordIcon').show();
      }
    });
  })