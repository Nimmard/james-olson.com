$(document).ready(function() {
    $('#addimage').click(function(event){
        event.preventDefault();
        $('#dialog').dialog();
    });

    $('.album').click(function(event) {
        event.preventDefault();
        var $this = this
        $('#dialog').dialog('close');
        $('#' + $this.id).dialog({
                buttons: {
                    "Back to Album Selection": function(){
                        $(this).dialog('destroy');
                        $('#dialog').dialog('open');
                    }
                }
            });
    });
});

