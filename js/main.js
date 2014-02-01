$(document).ready(function() {
    // Activate mobile-friendly menu when clicking Sections link.
    $('#masthead-nav-mobile a').click(function(e) {
        e.preventDefault();
        var nav = $('#masthead-nav');
        var opening = nav.css('display') == 'none' || nav.is(':hidden');
        nav.stop().slideToggle(300);
        if (opening)
            $('#masthead-nav-mobile').stop().animate({boxShadow: '3px 3px 10px #aaaaaa'}, 100);
        else
            $('#masthead-nav-mobile').stop().animate({boxShadow: 'none'}, 200);
    });

    $(window).resize(function() {
        if ($(window).width() >= 480) {
            $('#masthead-nav').removeAttr('style');
        }
    });

});