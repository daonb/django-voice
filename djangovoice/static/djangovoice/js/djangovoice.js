var dv_data = {
    div: {
        widget: document.getElementById('djangovoice-widget'),
        dialogbox: document.getElementById('djangovoice-dialogbox')
    }
};

var dv_connectSignals = function() {
    dv_data.div.widget.onclick = function() {
        if (dv_data.div.dialogbox.style.display === 'block') {
            dv_data.div.dialogbox.style.display = 'none';
            console.log("hide");
        } else {
            dv_data.div.dialogbox.style.display = 'block';
            console.log("show");
        }
    };
};

dv_connectSignals();