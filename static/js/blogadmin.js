$(document).ready(function() {
    var thedialog = $('#albumdialog').dialog({ 
        autoOpen: false,
        resizabale: false,
        modal: true,
        width: 600, 
        height: 400,
        show: 'fade',
        hide: 'drop'
    });
    function insert_image() {
        var textbox = $("#id_content");
        $(".highlightimage").each(function () {
            textbox.insertAtCursor("[![blah blah](" + $(this).attr('src') + ")](" + $(this).attr('src')+ ")");
        });
    }

    function get_an_album(albumid){
        var singlealbumdiv = $('<div id="singlealbum"></div>')
        $.get("/images/album/" + albumid + "/", function(data) {
            $.each(data, function(index, value){
                $(singlealbumdiv).append(value.name);
                $(singlealbumdiv).append("<br /><img src='/uploads/" + value.image + "' width=200 height=200>");
            });
            var olddialog= thedialog.html()
            thedialog.html(singlealbumdiv);
            thedialog.dialog({
                buttons: {
                    Back: function () {
                        thedialog.html(olddialog);
                        thedialog.dialog({buttons:{}});
                    },
                    "Insert Images": function () {
                        insert_image();
                }
                }
            });
        });
    }
    
    function get_albums(){
        var albumdiv = $('<div id="albums"></div>');
        $.get("/images/albums/", function(data) {
            $.each(data, function(index, value){
                $("#albums").append("<div class='albumchoices' id='album_" + index + "'>");
                $('#album_' + index).append("<a href='#' id='" + index + "'class='singlealbum'><h1>" + value.album + "</h1><img src='/uploads/" + value.image + "' width=200 height=200></a>");
            });
        });
        $('#albumdialog').html(albumdiv)
    }

    $('.album2').on("click", function(event) {
        if ($('#albums').length == 0) {
            get_albums();
            thedialog.dialog('open');
        } else {
            thedialog.dialog('open');
        }
        return false;
    });

    $('#albumdialog').on("click", '.singlealbum', function(event) {
        get_an_album(this.id);
        return false;
    });

    $('#albumdialog').on("click", "#singlealbum img", function(event) {
        if ($(this).hasClass("highlightimage")) {
            $(this).removeClass("highlightimage");
        } else {
            $(this).addClass("highlightimage");
        }
        return false;
    });
});

