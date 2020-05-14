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

// What about this funct
function getStaticState() {
    console.log("getStaticState")
    $.ajax({
        type: "GET",
        url: "/staticstate",
        // async: false, // Mode synchrone
        success: function (data) {
            $("#ajaxResponse").html(data);
            $("#rowId").html(data["id"]);
            $("#rowName").html(data["name"]);
            $("#rowObjective").html(data["objective"]);
            $("#rowInterval").html(data["interval"]);
            $("#rowSeedParents").html(data["seed_parents"]);
            $("#rowKillRate").html(data["kill_rate"]);
            $("#rowAverageChildNumb").html(data["average_child_numb"]);
        }
    });
}

function getDynamicState() {
    console.log("getDynamicState")
    $.ajax({
        type: "GET",
        url: "/dynamicstate",
        // async: false, // Mode synchrone
        success: function (data) {
            $("#ajaxResponse").html(data);
            $("#rowLen").html(data["len_current_population"]);
            $("#rowYear").html(data["year"]);
            $("#rowBest").html(data["best_current_population"]);
        }
    });
}

function handleInitMethod() {
    console.log("handleInitMethod")
    $("#firstSection").slideUp();
    $("#secondSection").slideUp();
    $("#thirdSection").slideDown();
    $("#fourthSection").slideDown();
    getStaticState();
    getDynamicState();
}

function makeInitFromModel() {
    console.log("makeInitFromModel")
    $("#firstSection").slideUp();
    $.ajax({
        type: "POST",
        url: "/initfrommodel",
        // async: false, // Mode synchrone
        success: function (data) {
            handleInitMethod();
        }
    });
}


function makeInitFromUser() {
    $("#initFormUser").submit(function (e) {
        console.log("makeInitFromUser")
        e.preventDefault(); // avoid to execute the actual submit of the form.
        $.ajax({
            type: "POST",
            url: "/initfromuser",
            // async: false, // Mode synchrone
            data: $(this).serialize(), // serializes the form's elements.
            success: function (data) {
                handleInitMethod();
            }
        });
    });
}


function range(start, end) {
    var array = new Array();
    for (var i = start; i < end; i++) {
        array.push(i);
    }
    return array;
}

function run() {
    $("#runForm").submit(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        console.log("run");
        var form = $(this);
        // console.log("raw form " + typeof (form) + " --> " + form)
        // var formS = form.serialize();
        // console.log("ser form " + typeof (formS) + " --> " + formS)
        var years = form.find("#years").val();
        var speed = form.find("#speed").val();
        // console.log("years : " + typeof (years) + " --> " + years.toString());
        var speed = 1000 * (1 / speed)
        // console.log("speed : " + typeof (speed) + " --> " + speed.toString());
        var arrRange = range(0, years);
        // console.log("arrRange : " + typeof (arrRange) + " --> " + arrRange.toString());
        arrRange.forEach(function (item, index) {
            console.log("BEFORE API CALL item " + item.toString() + " index " + index.toString());
            $.ajax({
                type: "POST",
                url: "/run",
                async: false, // Mode synchrone
                success: function (data) {
                    // console.log("AFTER  API CALL - BEFORE GETDYNAMIC item " + item.toString() + " index " + index.toString());
                    getDynamicState();
                    console.log("AFTER  API CALL - AFTER GETDYNAMIC item " + item.toString() + " index " + index.toString());


                }
            });
            // console.log("before sleep " + index.toString());
            // setTimeout(function () { console.log("sleep " + speed.toString()); }, speed);
            // console.log("after sleep " + index.toString())
        });
    });
}


$(function () {
    makeInitFromUser();
    run();
}); 