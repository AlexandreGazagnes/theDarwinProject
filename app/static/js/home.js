// ------------------------------------------
//  home.js
// ------------------------------------------



//import log
console.log("js init loaded")


// display the form
function toggleView_0() {
    // funct log
    console.log("toggleView_0 called");
    $("#firstSection").slideUp();
    $("#secondSection").slideDown();
}


function makeInitFromModel() {
    console.log("makeInitFromModel")
    var url = "/initfrommodel";
    $.ajax({
        type: "POST",
        url: url,
        // data: form.serialize(), // serializes the form's elements.
        success: function (data) {
            // $("#secondSection").slideUp();
            $("#thirdSection").slideDown();
            $("#fourthSection").slideDown();
            console.log("before " + typeof (data) + " -- > " + data); // BEFORE
            var data = JSON.parse(data)
            console.log("after " + typeof (data) + " -- > " + data); // AFTER
            console.log("keys acces " + data.name + " " + data.id);
            $("#ajaxResponse").html(data);
            $("#rowName").html(data["id"]);
            $("#rowYear").html(data["year"]);
        }
    });
}

//dont didplay initForm and load basic model
function toggleView_1() {
    console.log("toggleView_1 called");
    $("#firstSection").slideUp();
    makeInitFromModel();
}




// // just return the state
// function getState() {
//     $.ajax({
//         type: "GET",
//         url: "/state",
//         success: function (data) {
//             // $("#ajaxResponse").html(data);
//         }
//     });
// }

$(function () {
    // form init object
    $("#initFormUser").submit(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        var form = $(this);
        var url = "/initfromuser";
        $.ajax({
            type: "POST",
            url: url,
            data: form.serialize(), // serializes the form's elements.
            success: function (data) {
                $("#secondSection").slideUp();
                $("#thirdSection").slideDown();
                $("#fourthSection").slideDown();
                console.log("before " + typeof (data) + " -- > " + data); // BEFORE
                var data = JSON.parse(data)
                console.log("after " + typeof (data) + " -- > " + data); // AFTER
                console.log("keys acces " + data.name + " " + data.id);
                $("#ajaxResponse").html(data);
                $("#rowName").html(data["id"]);
                $("#rowYear").html(data["year"]);
            }
        });
    });
}); 