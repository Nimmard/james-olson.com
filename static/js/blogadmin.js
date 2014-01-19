$(document).ready(function() {
    var newdialog = $('#dialog').dialog({ 
        autoOpen: false,
        resizabale: false,
        modal: true,
        width: 800, 
        height: 800,
        show: 'fade',
        hide: 'drop'
    });
    function insert_image() {
        var textbox = $("#id_content");
        $(".highlightimage").each(function () {
            textbox.insertAtCursor("<img src='" + $(this).attr('src') + "' />");
        });
    }

    function get_an_album(albumid){
        var singlealbumdiv = $('<div id="singlealbum"></div>')
        $(singlealbumdiv).append('<div class="options"><h3>Alignment:</h3><ul id="alignment"><li class="active">Align Left</li><li> | </li><li>Align Right</li></ul></div>');
        $(singlealbumdiv).append('<div class="options"><h3>Size</h3><ul id="size"><li class="active">Small | </li><li>Medium | </li><li>Large</li></div>')
        $.get("/images/album/" + albumid + "/", function(data) {
            $.each(data, function(index, value){
                imagesdiv = $('<div class="images"></div>');
                $(imagesdiv).append(value.name);
                $(imagesdiv).append("<br /><img src='/uploads/" + value.image + "' width=200 height=200>");
                $(singlealbumdiv).append(imagesdiv);
            });
            var olddialog= newdialog.html()
            newdialog.html(singlealbumdiv);
            newdialog.dialog({
                buttons: {
                    Back: function () {
                        newdialog.html(olddialog);
                        newdialog.dialog({buttons:{}});
                    },
                    "Insert Images": function () {
                        insert_image();
                }
                }
            });
        });
    }
    
    $('#addimage').on("click", function() {
        if ($('#albums').length == 0) {
            newdialog.dialog("open");
            console.log("destroy");
        } else {
            newdialog.dialog("open");
            console.log("Not destory");
        }
        return false;
    });

    $('#dialog').on("click", '#albums a', function(event) {
        console.log(this);
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

