$(document).ready(function() {
    $('.reveal').hide();
    
    $('#submit-act').click(function(){
        $(form).attr('text', readonly);
        $('.reveal').slideDown(5000);
    });
    
    
    
});