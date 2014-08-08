$(document).ready(function(){
	$('.moreInfo').hide();
	$('.afterSignup').hide();

	//$('.header').hide();
	$('.btn-info').click(function(){
		$('.header').fadeOut(1000, function(){
			$('.moreInfo').fadeIn(1000);
		});

	});

	$('.btn-signUp').click(function(){
		$('.moreInfo').fadeOut(1000, function(){
			$('.afterSignup').fadeIn(1000);
		});
	});

});
