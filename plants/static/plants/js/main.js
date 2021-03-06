function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function (e) {
      $('#profile-img-tag').attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
  }
}
$("#file-input").change(function(){
  readURL(this);
});


$("#analyze-button").click(function(e) {
  e.preventDefault();
  $("[name='formSubmit']").click();
});


$(document).ready(function(){
	"use strict";

	var window_width 	 = $(window).width(),
	window_height 		 = window.innerHeight,
	header_height 		 = $(".default-header").height(),
	header_height_static = $(".site-header.static").outerHeight(),
	fitscreen 			 = window_height - header_height;


	$(".fullscreen").css("height", window_height)
	$(".fitscreen").css("height", fitscreen);

     
     // -------   Active Mobile Menu-----//

    $(".menu-bar").on('click', function(e){
        e.preventDefault();
        $("nav").toggleClass('hide');
        $("span", this).toggleClass("lnr-menu lnr-cross");
        $(".main-menu").addClass('mobile-menu');
    });
     
    $('select').niceSelect();
    $('.img-pop-up').magnificPopup({
        type: 'image',
        gallery:{
        enabled:true
        }
    });


    $('.play-btn').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        fixedContentPos: false
    });


    $(document).ready(function() {
        $('#mc_embed_signup').find('form').ajaxChimp();
    });      
    // -------   Mail Send ajax

 });


 function removeHash () { 
    history.pushState("", document.title, window.location.pathname
                                                       + window.location.search);
}

// ===== Scroll to Top ==== 
var btn = $('#top-button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});


// ===== PreLoader ==== 

    // preloader js
    $(window).on('load', function() { // makes sure the whole site is loaded
      $('#preloader_spinner').delay(1500).fadeOut(); // will first fade out the loading animation
      $('#preloader').delay(1600).fadeOut('slow'); // will fade out the white DIV that covers the website.
      $('dup-body').delay(1600).css({'overflow':'visible'});
      })
