$( document ).ready(function() {

    function submitResume() {

        var selected_file = document.getElementById('resume').files[0];
        var client = new Dropbox.Client({key: "g3btzms68f42hmx", token:"dDNPNOsuMJ8AAAAAAAAABQv_5j_QnElpvPwwm9mqUlh3kR9HdAkHZ8MjdZQE6w-j"});
        // Try to finish OAuth authorization.
        client.authenticate({interactive: false}, function (error) {
            if (error) {
                console.error('Dropbox authentication error: ' + error);
            }
        });

        if (client.isAuthenticated()) {
            var name = String($('#firstName').val() + $('#lastName').val() + ".pdf");
            client.writeFile(name, selected_file, function() {
                console.log("Resume submitted");
            });
        }

    }

    $('#submit').click(function(e){
        submitResume();
    });

});
