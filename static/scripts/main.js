$(document).ready(function(){


    $(".auto").autocomplete({
                        closeOnBlue: true,
                        minLength: 0,
                        valueKey: 'title',
                        appendMethod: 'replace',
                        source: [function(q, add) {
                            $.getJSON("product_query?s=" + encodeURIComponent(q), function(resp) {
                                console.log(resp);
                                add(resp);
                            })
                        }]
                    });





});


