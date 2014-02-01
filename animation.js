// Opening Fade In: THE HARVARD CRIMSON :)
$(function() {
    setTimeout(function() {
        $('.overlay').hide();
    }, 0);
    $('.opening').fadeIn(2000);
    setTimeout(function() {
        $('.cute').fadeIn('slow');
    }, 1500);

    setTimeout(restore, 4000);
    $(window).keydown(restore);
    $(window).click(restore);
    
});

function restore() {
    $('.overlay').show();
    $('#splash').fadeOut('slow');
}
