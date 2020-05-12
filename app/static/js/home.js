//import log
console.log("js init loaded")


function toggleView() {
    // funct log
    console.log("toggleView called");
    $("#firstSection").slideUp();
    $("#secondSection").slideDown();
}


$(function () {

    $("#initForm").submit(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        var form = $(this);
        var url = "/init";
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(), // serializes the form's elements.
            success: function (data) {
                $("#firstSection").slideUp();
                $("#secondSection").slideUp();
                $("#thirdSection").slideDown();
                $("#fourthSection").slideDown();
                $("#ajaxResponse").html(data);
            }
        });
    });

}); 