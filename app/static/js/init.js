//import log
console.log("js init loaded")


function toggleView() {
    // funct log
    console.log("toggleView called");
    $("#firstSection").slideUp();
    $("#secondSection").slideDown();
}


$(function () {
    // auto loaded js and jquery


    $("#ajaxBTN").click(function () {
        console.log("ajaxBTN called");
        $.ajax({
            url: "/hello",
            success: function (result) {
                $("#ajaxResponse").html(result);
            }
        });

    });



}); 