
$(document).ready(function() {
    $("#rating_1").click(function () {
        $("#rating_5").toggleClass("color2");
        $("#rating_4").toggleClass("color2");
        $("#rating_3").toggleClass("color2");
        $("#rating_2").toggleClass("color2");
        $("#rating_1").toggleClass("color2");
        let rating = 100;
        document.cookie = 'rating' + '=' + rating;
    });
    $("#rating_2").click(function () {
        $("#rating_5").toggleClass("color2");
        $("#rating_4").toggleClass("color2");
        $("#rating_3").toggleClass("color2");
        $("#rating_2").toggleClass("color2");
        $("#rating_1").toggleClass("color3");
        let rating = 80;
        document.cookie = 'rating' + '=' + rating;
    });
    $("#rating_3").click(function () {
        $("#rating_5").toggleClass("color2");
        $("#rating_4").toggleClass("color2");
        $("#rating_3").toggleClass("color2");
        $("#rating_2").toggleClass("color3");
        $("#rating_1").toggleClass("color3");
        let rating = 60;
        document.cookie = 'rating' + '=' + rating;
    });
    $("#rating_4").click(function () {
        $("#rating_5").toggleClass("color2");
        $("#rating_4").toggleClass("color2");
        $("#rating_3").toggleClass("color3");
        $("#rating_2").toggleClass("color3");
        $("#rating_1").toggleClass("color3");
        let rating = 40; 
        document.cookie = 'rating' + '=' + rating;
    });
    $("#rating_5").click(function () {
        $("#rating_5").toggleClass("color2");
        $("#rating_4").toggleClass("color3");
        $("#rating_3").toggleClass("color3");
        $("#rating_2").toggleClass("color3");
        $("#rating_1").toggleClass("color3");
        let rating = 20; 
        document.cookie = 'rating' + '=' + rating;
    });
    $( "#follow" ).on('click', function() {
        isChecked = $('#seguir_autor').is(':checked')

        if(isChecked){ 
            $('#seguir_autor').prop( "checked", false ).val('False');
            $( "#follow" ).toggleClass( "color3" );
        }
        else{ 
            $( '#seguir_autor' ).prop( "checked", true ).val('True');
            $( "#follow" ).toggleClass( "color1" )
        }
        });

    $( "#reset" ).on( "click", function() {
        $( '.rating' ).toggleClass( "color3" );
    });

    $(".libro_id").on('click', function () {
        var $item = $(this).prev().text();
        document.cookie = 'libro_id' + '=' + $item + '; path=/; SameSite=Lax';
    });
    });
