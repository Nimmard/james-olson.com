$(document).ready(function() {
    $('#addimage').click(function(event){
        event.preventDefault();
        $('#dialog').dialog();
    });

    var thedialog = $('#albumdialog').dialog({ 
        autoOpen: false,
        resizabale: false,
        modal: true,
        width: 'auto', 
        show: 'fade',
        hide: 'drop'
    });
    var photodialog = $('#photodialog').dialog({
        autoOpen: false,
        resizable: true,
        modal: true,
        width: 'auto',
        show: 'fade',
        hide: 'drop'
    });
    function get_an_album(albumid){
        $.get("/images/album/" + albumid + "/", function(data) {
            $.each(data, function(index, value){
                $("#photos").append(index);
                $("#photos").append("<img src='/uploads/" + value.image + "' width=200 height=200>");
            });
        });
    }
    
    function get_albums(){
        $.get("/images/albums/", function(data) {
            $.each(data, function(index, value){
                $("#albums").append("<div class='albumchoices' id='album_" + index + "'>");
                $('#album_' + index).append("<a href='#' class='singlealbum'>Test</a><h1>" + value.album + "</h1><img src='/uploads/" + value.image + "' width=200 height=200></a>");
            });
        });
    }

    $('.album2').on("click", function(event) {
        event.preventDefault();
        var $this = this
        get_albums();
        thedialog.dialog('open');
    });

   $('#albumdialog').on("click", '.singlealbum', function(event) {
       event.preventDefault();
       get_an_album("001");
       thedialog.dialog("close");
       photodialog.dialog("open");
       
   });

});

