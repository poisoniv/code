$(document).ready(function(){

$(".auto").autocomplete({
    valueKey: 'title',
    appendMethod: 'replace',
    source: [function(q, add) {
        $.getJSON("query?s=" + encodeURIComponent(q), function(resp) {
            console.log(resp);
            add(resp);
        })
    }]
});

});
