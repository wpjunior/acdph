function setFancyBox () {
    $("#album a.photo").fancybox({
	'overlayOpacity': 0.7,
	'transitionIn'	:	'elastic',
	'transitionOut'	:	'elastic',
	'speedIn'		:	600, 
	'speedOut'		:	200,
	'titlePosition': 'over',
    });
}

$(document).ready(function(e) {
    setFancyBox();
});