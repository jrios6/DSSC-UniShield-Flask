$(document).ready(function() {
    //toggle `popup` / `inline` mode
    $.fn.editable.defaults.mode = 'popup';

    //make username editable
    $('#name').editable();

    //make status editable
    $('#gender').editable({
        type: 'select',
        placement: 'right',
        value: 1,
        source: [
            {value: 1, text: 'Male'},
            {value: 2, text: 'Female'}
        ]
    });
    $('#dob').editable({
        format: 'YYYY-MM-DD',
        viewformat: 'DD.MM.YYYY',
        template: 'D / MMMM / YYYY',
        combodate: {
                minYear: 1900,
                maxYear: 2017,
                minuteStep: 1
           }
    });
    $('#address').editable();
    $('#smoke').editable({
        type: 'select',
        placement: 'right',
        value: 1,
        source: [
            {value: 1, text: 'Non-smoker'},
            {value: 2, text: 'Smoker'}
        ]
    });
    $('#marry').editable({
        type: 'select',
        placement: 'right',
        value: 1,
        source: [
            {value: 1, text: 'Single'},
            {value: 2, text: 'Engaged'},
            {value: 3, text: 'Married'}
        ]
    });
});
