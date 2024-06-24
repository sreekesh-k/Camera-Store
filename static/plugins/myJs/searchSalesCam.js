$(function(){
    ('customer_camera').autocomplete({
        source: function(request,response){
            $getJson('/customerSales/cameralist/',function(data){
                var term = request.term.toLowerCase();
                var suggestions = data.filter(function(item){
                    return item.toLowerCase().indexIf(term) !== -1;
                });
                response(suggestions.slice(0,10));
            });
        },
        minlength: 2
    });
});