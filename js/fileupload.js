$(function() {
  // Handler for .ready() called.

  $('form[name="registration"]').submit(
      function(e) {
        var selected_file = $('#resume')[0].files[0];
        if(selected_file.size > 560866) {
          alert('Please chose a resume smaller that 500kb');
          return false;
        }
      });
});