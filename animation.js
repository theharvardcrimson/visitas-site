// Opening Fade In: THE HARVARD CRIMSON :)
$(function() {
    if (document.cookie == "") {
        $('#splash').show();
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
        createCookie('visited', 'true',  1);
    }
});

function restore() {
    $('.overlay').show();
    $('#splash').fadeOut('slow');
}

// From http://stackoverflow.com/questions/6561687/
function createCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else {
        var expires = "";
    }
    document.cookie = name+"="+value+expires+"; path=/";
}
