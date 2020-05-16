// ------------------------------------------
//  home.js
// ------------------------------------------


// global var
var algoInitilalized = false;
var algoId = "";
var year = 0;


// function dummyCall() {
//     $.ajax({
//         type: "GET",
//         url: "/dummycall?algoId=" + algoId,
//         // async: false, // Mode synchrone
//         success: function (data) {
//             console.debug('OK')
//         }
//     });
// }


// display the form on first click
function toggleView_0() {
    console.debug("toggleView_0 called");
    $("#firstSection").slideUp();
    $("#secondSection").slideDown();
}


// Once Algo initilialied gather static info of the lago 
// idependant from run method
function getStaticState() {
    console.debug("getStaticState")
    $.ajax({
        type: "GET",
        url: "/staticstate?algoId=" + algoId,
        // async: false, // Mode synchrone
        success: function (data) {
            // $("#ajaxResponse").html(data);
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


// Once Algo initilialied gather dynamic info of the lago 
// OVER dependant from run method
function getDynamicState() {
    console.debug("getDynamicState")
    $.ajax({
        type: "GET",
        url: "/dynamicstate?algoId=" + algoId,
        // async: false, // Mode synchrone
        success: function (data) {
            $("#rowLen").html(data["len_current_population"]);
            $("#rowYear").html(data["year"]);
            $("#rowBest").html(data["best_current_population"]);
        }
    });
}


// Init an object fill static and dynamic state
// init graph and change global val
function handleInitMethod(data) {
    console.debug("handleInitMethod")
    $("#firstSection").slideUp();
    $("#secondSection").slideUp();
    $("#thirdSection").slideDown();
    $("#fourthSection").slideDown();
    $("#fithSection").slideDown();

    getStaticState();
    getDynamicState();
    updateCharts();
}


//Manage init algo method from the button model
// makeInitFromModel
function makeInitFromModel() {
    console.debug("makeInitFromModel")
    $("#firstSection").slideUp();
    $.ajax({
        type: "POST",
        url: "/initfrommodel",
        // async: false, // Mode synchrone
        success: function (data) {
            algoInitilalized = true;
            algoId = data;
            console.log("algoId = " + data);
            handleInitMethod();
        }
    });
}


//Manage init algo method from the button user custom algo
// makeInitFromUser
function makeInitFromUser() {
    $("#initFormUser").submit(function (e) {
        console.log("makeInitFromUser")
        e.preventDefault(); // avoid to execute the actual submit of the form.
        $.ajax({
            type: "POST",
            url: "/initfromuser",
            data: algoID,
            // async: false, // Mode synchrone
            data: $(this).serialize(), // serializes the form's elements.
            success: function (data) {
                algoInitilalized = true;
                algoId = data;
                console.log("algoId = " + data);
                handleInitMethod(data);
            }
        });
    });
}


// a range function
function range(start, end) {
    var array = new Array();
    for (var i = start; i < end; i++) {
        array.push(i);
    }
    return array;
}


// once algo init call x min and max
function getLim(c) {
    var arrData = [-42, -42];
    $.ajax({
        type: "GET",
        url: "/get" + c + "lim?algoId=" + algoId,
        async: false, // Mode synchrone
        success: function (data) {
            arrData = [data.min, data.max];
        }
    });
    return arrData;
}


// once algo init call all x,y pairs for the population
function getGraphData(d) {
    var arrData = [-42, -42];
    $.ajax({
        type: "GET",
        url: "/get" + d + "?algoId=" + algoId,
        async: false, // Mode synchrone
        success: function (data) {
            arrData = data;
        }
    });
    return arrData;
}


// once algo init call all x,y pairs for the population
function getPopulation() {
    return getGraphData('population');
}


function getXs() {
    return getGraphData('xs');

}


function getYs() {
    return getGraphData('ys');
}


function getYears() {
    return getGraphData('years');
}



// make a chart 
function drawPopChart() {

    // gather x lims, y lims and population
    if (algoInitilalized) {
        var xLim = getLim("x");
        var yLim = getLim("y");
        var xMin = xLim[0];
        var xMax = xLim[1];
        var yMin = yLim[0];
        var yMax = yLim[1];
        var population = getGraphData('population');
    } else {
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var population = [['x', 'y'], [1, 1], [2, 2]]
    }

    // scatter
    console.log("population = " + population);
    var data = google.visualization.arrayToDataTable(population);

    // options
    var options = {
        title: 'current population',
        hAxis: { title: 'x', minValue: xMin, maxValue: xMax },
        vAxis: { title: 'y', minValue: yMin, maxValue: yMax },
        legend: 'none'
    };

    // init chart on DOM element and push
    var chart = new google.visualization.ScatterChart(document.getElementById('populationChart'));
    chart.draw(data, options);
}


// make a chart 
function drawXsChart() {

    // gather x lims, y lims and population
    if (year > 0) {
        // var xLim = getLim("x");
        // var yLim = getLim("y");
        // var xMin = xLim[0];
        // var xMax = xLim[1];
        // var yMin = yLim[0];
        // var yMax = yLim[1];
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var xs = getGraphData('xs');
    } else {
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var xs = [["years", "x"], [1, 1], [2, 2]];
    }

    // scatter
    console.log("xs = " + xs);
    var data = google.visualization.arrayToDataTable(xs);

    // options
    var options = {
        title: 'xs evolution in year',
        hAxis: { title: 'years', minValue: xMin, maxValue: xMax },
        vAxis: { title: 'x', minValue: yMin, maxValue: yMax },
        legend: 'none'
    };

    // init chart on DOM element and push
    var chart = new google.visualization.ScatterChart(document.getElementById('xsChart'));
    chart.draw(data, options);
}




// make a chart 
function drawYsChart() {

    // gather x lims, y lims and population
    if (year > 0) {
        // var xLim = getLim("x");
        // var yLim = getLim("y");
        // var xMin = xLim[0];
        // var xMax = xLim[1];
        // var yMin = yLim[0];
        // var yMax = yLim[1];
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var ys = getGraphData('ys');
    } else {
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var ys = [["years", "x"], [1, 1], [2, 2]];
    }

    // scatter
    console.log("ys = " + ys);
    var data = google.visualization.arrayToDataTable(ys);

    // options
    var options = {
        title: 'ys evolution in year',
        hAxis: { title: 'years', minValue: xMin, maxValue: xMax },
        vAxis: { title: 'y', minValue: yMin, maxValue: yMax },
        legend: 'none'
    };

    // init chart on DOM element and push
    var chart = new google.visualization.ScatterChart(document.getElementById('ysChart'));
    chart.draw(data, options);
}

// make a chart 
function drawYearsChart() {

    // gather x lims, y lims and population
    if (year > 0) {
        // var xLim = getLim("x");
        // var yLim = getLim("y");
        // var xMin = xLim[0];
        // var xMax = xLim[1];
        // var yMin = yLim[0];
        // var yMax = yLim[1];
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var years = getGraphData('years');
    } else {
        var xMin = 0;
        var xMax = 15;
        var yMin = 0;
        var yMax = 15;
        var years = [["years", "x"], [1, 1], [2, 2]];
    }

    // scatter
    console.log("years = " + years);
    var data = google.visualization.arrayToDataTable(years);

    // options
    var options = {
        title: 'ys evolution in year',
        hAxis: { title: 'years', minValue: xMin, maxValue: xMax },
        vAxis: { title: 'y', minValue: yMin, maxValue: yMax },
        legend: 'none'
    };

    // init chart on DOM element and push
    var chart = new google.visualization.ScatterChart(document.getElementById('yearsChart'));
    chart.draw(data, options);
}



// manage chart creation
function updateCharts() {
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawPopChart);
    google.charts.setOnLoadCallback(drawXsChart);
    google.charts.setOnLoadCallback(drawYsChart);
    google.charts.setOnLoadCallback(drawYearsChart);
}


// run
function run() {
    $("#runForm").submit(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        console.debug("run");
        var form = $(this);
        var years = form.find("#years").val();
        var speed = form.find("#speed").val();

        // prevent for speed < 1 (ie 0.1 --> sleep 10 sec)
        var speed = 1000 * (1 / speed)
        if (speed > 1000) {
            var speed = 1000
        }

        // years --> for i in range :) 
        var arrRange = range(0, years);
        arrRange.forEach(function (item, index) {
            setTimeout(function () { // be carrefull with setTimeoit != sleep() --> it is an async fuct
                $.ajax({
                    type: "POST",
                    url: "/run?algoId=" + algoId,
                    // async: false, // Mode synchrone
                    success: function (data) {
                        year++;
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