$(document).ready(function() {
    $(".entry:nth-child(odd)").addClass('alternate');
    $(".entry:first-of-type").addClass('first');
    $(".entry:first-of-type").removeClass('alternate');

    $('#contactsubmit').click(function(event){
        event.preventDefault();
        $.ajax({
            url: '/contact/',
            type: 'post',
            data: $('#contactform').serializeArray(),
            success: function(response) {
                console.log(response);
                $("#contactform").remove();
            },
            error: function(response) {
                console.log(response);
            }
        });
        });

});
