$(document).ready(function(){

    $(".next").click(function(){ var current_fs, next_fs, previous_fs; //fieldsets
        var opacity;
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();
    

    
        //Add Class Active
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
    
        //show the next fieldset
        next_fs.show(); 
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // for making fielset appear animation
                opacity = 1 - now;
    
                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({'opacity': opacity});
            }, 
            duration: 600
        });
    });

    

    
    $(".next1").click(function(){

        if($('input[name="q1').groupVal() === undefined){
            $("div.alertbox").fadeIn(300).delay(2000).fadeOut(500);
        	
        } else  {
            var current_fs, next_fs, previous_fs; //fieldsets
            var opacity;
            current_fs = $(this).parent();
            next_fs = $(this).parent().next();
        

        
           //Add Class Active
           $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        
           //show the next fieldset
           next_fs.show(); 
           //hide the current fieldset with style
           current_fs.animate({opacity: 0}, {
               step: function(now) {
                   // for making fielset appear animation
                   opacity = 1 - now;
       
                   current_fs.css({
                       'display': 'none',
                       'position': 'relative'
                   });
                   next_fs.css({'opacity': opacity});
               }, 
               duration: 600
           });
        }
        
        
     
    });

    $(".next2").click(function(){

        if($('input[name="q2').groupVal() === undefined){
            $("div.alertbox").fadeIn(300).delay(2000).fadeOut(500);
        } else  {
            var current_fs, next_fs, previous_fs; //fieldsets
            var opacity;
            current_fs = $(this).parent();
            next_fs = $(this).parent().next();
        

        
           //Add Class Active
           $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        
           //show the next fieldset
           next_fs.show(); 
           //hide the current fieldset with style
           current_fs.animate({opacity: 0}, {
               step: function(now) {
                   // for making fielset appear animation
                   opacity = 1 - now;
       
                   current_fs.css({
                       'display': 'none',
                       'position': 'relative'
                   });
                   next_fs.css({'opacity': opacity});
               }, 
               duration: 600
           });
        }
        
        
     
    });

    ///////// 3rd question
    $(".next3").click(function(){

        if($('input[name="q3').groupVal() === undefined){
            $("div.alertbox").fadeIn(300).delay(2000).fadeOut(500);
        } else  {
            var current_fs, next_fs, previous_fs; //fieldsets
            var opacity;
            current_fs = $(this).parent();
            next_fs = $(this).parent().next();
        

        
           //Add Class Active
           $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        
           //show the next fieldset
           next_fs.show(); 
           //hide the current fieldset with style
           current_fs.animate({opacity: 0}, {
               step: function(now) {
                   // for making fielset appear animation
                   opacity = 1 - now;
       
                   current_fs.css({
                       'display': 'none',
                       'position': 'relative'
                   });
                   next_fs.css({'opacity': opacity});
               }, 
               duration: 600
           });
        }
        
        
     
    });

    ///////// 4th question
    $(".next4").click(function(){

        if($('input[name="q4').groupVal() === undefined){
            $("div.alertbox").fadeIn(300).delay(2000).fadeOut(500);
        } else  {
            var current_fs, next_fs, previous_fs; //fieldsets
            var opacity;
            current_fs = $(this).parent();
            next_fs = $(this).parent().next();
        

        
           //Add Class Active
           $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        
           //show the next fieldset
           next_fs.show(); 
           //hide the current fieldset with style
           current_fs.animate({opacity: 0}, {
               step: function(now) {
                   // for making fielset appear animation
                   opacity = 1 - now;
       
                   current_fs.css({
                       'display': 'none',
                       'position': 'relative'
                   });
                   next_fs.css({'opacity': opacity});
               }, 
               duration: 600
           });
        }
   
    });

    $(".next5").click(function(){

        if($('input[name="q5').groupVal() === undefined){
            $("div.alertbox").fadeIn(300).delay(2000).fadeOut(500);
        } else  {
            var current_fs, next_fs, previous_fs; //fieldsets
            var opacity;
            current_fs = $(this).parent();
            next_fs = $(this).parent().next();
        

        
           //Add Class Active
           $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        
           //show the next fieldset
           next_fs.show(); 
           //hide the current fieldset with style
           current_fs.animate({opacity: 0}, {
               step: function(now) {
                   // for making fielset appear animation
                   opacity = 1 - now;
       
                   current_fs.css({
                       'display': 'none',
                       'position': 'relative'
                   });
                   next_fs.css({'opacity': opacity});
               }, 
               duration: 600
           });
        }
   
    });

    $(".submit").click(function(e){
        $("#msform").submit();
    });

    
    $(".previous").click(function(){
        
        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();
        
        //Remove class active
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
        
        //show the previous fieldset
        previous_fs.show();
    
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // for making fielset appear animation
                opacity = 1 - now;
    
                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previous_fs.css({'opacity': opacity});
            }, 
            duration: 600
        });
    });
    
    $('.radio-group .radio').click(function(){
        $(this).parent().find('.radio').removeClass('selected');
        $(this).addClass('selected');
    });
   
    });
    jQuery.fn.extend({
        groupVal: function() {
            return $(this).filter(':checked').val();
        }
    });