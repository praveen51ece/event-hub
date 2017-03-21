      function UserLogin() { 
        var formData = new FormData();          
        var username = $('#username').val();
        var password = $('#password').val();
        formData.append("password", password);
        formData.append("username", username);
        url = '/login/'
            $.ajax({
                type: 'POST',
                url: url,
                async: false,
                data: formData,
                cache: false,
                contentType: false,
                processData: false,
                success: function(data) {
                    if(data.status=='success'){
                        $('#loginModal').hide();
                        window.location.replace('/event_insert/')
                    }
                    else{
                        $("#login_error").css('display','block')
                    }

                },
                error: function(e) {
                    alert(e.message);
                }
            });    
    }


