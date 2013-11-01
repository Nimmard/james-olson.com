$(document).ready(function() {
    $(".entry:nth-child(odd)").addClass('alternate');
    $(".entry:first-of-type").addClass('first');
    $(".entry:first-of-type").removeClass('alternate');

    $('#contactform').validate({
        rules: {
            name: {
                required: true
            },
            email: {
                required: true,
                email: true
            },
            message: {
                required: true}
        },
        highlight: function(element) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function(element) {
            $(element).closest('.form-group').removeClass('has-error');
        }
    });
    $('#contactsubmit').click(function(event){
        event.preventDefault();
        var valid = $('#contactform').valid();
        if (valid) {
        $.ajax({
            url: '/contact/',
            type: 'post',
            data: $('#contactform').serializeArray(),
            success: function(response) {
                console.log(response);
                $("#contactform").fadeOut(500, function() {
                    var html = "<p style='text-align: center;'><strong>" + response + "</strong></p>";
                    $(html).appendTo(".contact").hide().fadeIn(500);
                });
            },
            error: function(response) {
                console.log(response);
            }
        });
        }
        });
});
