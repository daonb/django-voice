$(function() {
    var dv_data = {
        div: {
            widget: $('#djangovoice-widget'),
            dialogbox: $('#djangovoice-dialogbox')
        }
    };

    var dv_connectSignals = function() {
        dv_data.div.widget.bind('click', function() {
             dv_data.div.dialogbox.toggle();
        });
    };

    var dv_initialize = function() {
        dv_connectSignals();
    };

    dv_initialize();
});