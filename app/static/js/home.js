// ------------------------------------------
//  home.js
// ------------------------------------------


//import log
console.log("js init loaded")

var algo_initilalized = false;


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


// getDynamicState
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


// handleInitMethod
function handleInitMethod() {
    console.log("handleInitMethod")
    $("#firstSection").slideUp();
    $("#secondSection").slideUp();
    $("#thirdSection").slideDown();
    $("#fourthSection").slideDown();
    $("#fithSection").slideDown();
    getStaticState();
    getDynamicState();
    algo_initilalized = true;
    updateCharts();
}


// makeInitFromModel
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


// makeInitFromUser
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


// range
function range(start, end) {
    var array = new Array();
    for (var i = start; i < end; i++) {
        array.push(i);
    }
    return array;
}


function getXLim() {
    var arrData = [-42, -42];
    $.ajax({
        type: "GET",
        url: "/getxlim",
        async: false, // Mode synchrone
        success: function (data) {
            arrData = [data.min, data.max];
            // console.log("data " + typeof (data) + " --> " + data.toString());
            // console.log("data " + typeof (data.min) + " --> " + data.min.toString());
            console.log("arrData " + typeof (arrData) + " --> " + arrData.toString());
            // console.log("arrData " + typeof (arrData[0]) + " --> " + arrData[0].toString());

        }
    });
    return arrData;
}


function getYLim() {
    var arrData = [-42, -42];
    $.ajax({
        type: "GET",
        url: "/getylim",
        async: false, // Mode synchrone
        success: function (data) {
            arrData = [data.min, data.max];
        }
    });
    return arrData;
}


function getPopulation() {
    var arrData = [-42, -42];
    $.ajax({
        type: "GET",
        url: "/getpopulation",
        async: false, // Mode synchrone
        success: function (data) {
            console.log(data);
            arrData = data;
        }
    });
    return arrData;
}

function drawChart() {
    if (algo_initilalized) {
        var xLim = getXLim();
        console.log("xLim " + typeof (xLim) + " --> " + xLim.toString());
        var yLim = getYLim();
        console.log("yLim " + typeof (yLim) + " --> " + yLim.toString());
        var xMin = xLim[0];
        var xMax = xLim[1];
        var yMin = yLim[0];
        var yMax = yLim[1];
        var population = getPopulation();
        console.log("population " + typeof (population) + " --> " + population.toString());
        console.log("population " + typeof (population[0]) + " --> " + population[0].toString());
        console.log("population " + typeof (population[1]) + " --> " + population[1].toString());

    } else {
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var population = [['x', 'y'], [1, 1], [2, 2]]
    }
    var data = google.visualization.arrayToDataTable(population);
    var options = {
        title: 'current population',
        hAxis: { title: 'x', minValue: xMin, maxValue: xMax },
        vAxis: { title: 'y', minValue: yMin, maxValue: yMax },
        legend: 'none'
    };

    var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}



function updateCharts() {
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);
}


// run
function run() {
    $("#runForm").submit(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        console.log("run");
        var form = $(this);
        var years = form.find("#years").val();
        var speed = form.find("#speed").val();
        var speed = 1000 * (1 / speed)
        if (speed > 1000) {
            var speed = 1000
        }
        var arrRange = range(0, years);
        arrRange.forEach(function (item, index) {
            setTimeout(function () {
                $.ajax({
                    type: "POST",
                    url: "/run",
                    // async: false, // Mode synchrone
                    success: function (data) {
                        getDynamicState();
                        updateCharts();
                    }
                });
            }, index * speed);
        });
    });
}


// on ready
$(function () {
    makeInitFromUser();
    run();
}); 