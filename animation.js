// Opening Fade In: THE HARVARD CRIMSON :)
$(function() {
    setTimeout(function() {
        $('.overlay').hide();
    }, 0);
    $('.opening').fadeIn(2500);
    setTimeout(function() {
        $('.cute').fadeIn('slow');
    }, 2000);
    setTimeout(function() {
        $('#msg').fadeIn('fast');
    }, 3000);
    setTimeout(function() {
        $('#splash').fadeOut();
        $('.overlay').show();
    }, 6000);
    
    $(window).keydown(function() {
        $('.overlay').show();
        $('#splash').fadeOut('slow');
    });
    
});
