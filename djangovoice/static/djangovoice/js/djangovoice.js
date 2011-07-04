var dv_initialize = function($) {
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

    dv_connectSignals();
};

try {
    var dv_$ = $;
} catch(err) {
    if(err.type === 'not_defined') {
        var jquery = document.createElement('script');
        jquery.type = 'text/javascript';
        jquery.src = window.dv_jqueryPath;
        jquery.onload = dv_initialize($);

        document.head.appendChild(jquery);
        console.log(jquery);

        dv_$ = $;
    }
}

dv_initialize(dv_$);