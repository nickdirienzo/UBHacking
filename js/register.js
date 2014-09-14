$(function() {
  $("form[name='registration']").submit(
    function(e) {
      alert("stahp!!");
      resume = $("input[name='resume']");
      return false;
      var request = $.post('/submit', inputs, function(){
        alert('success!');
      });
      e.preventDefault();
    });
});