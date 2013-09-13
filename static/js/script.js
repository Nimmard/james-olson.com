$(document).ready(function() {
    $(".entry:nth-child(odd)").addClass('alternate');
    $(".entry:first-of-type").addClass('first');
    $(".entry:first-of-type").removeClass('alternate');

});
