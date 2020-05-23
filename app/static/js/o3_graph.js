console.debug("graph.js")

////////////////////////////////////////////////////////
//      Graph.js
////////////////////////////////////////////////////////


// Make Charts
////////////////////////////////////////////////////////////

// make a chart 
function drawPopChart() {
    console.debug("drawPopChart")
    // update coords && data
    let data = google.visualization.arrayToDataTable(dynamicState.graph.current_population);
    // options
    let options = {
        // title: 'current population',
        hAxis: { title: 'x', }, //minValue: xMin, maxValue: xMax
        vAxis: { title: 'y', }, // minValue: yMin, maxValue: yMax 
        legend: 'none',
        width: graphWidth,
        heigh: graphHeight,
        pointSize: pointSize,
        pointShape: pointShape
    };
    // init chart on DOM element and push
    let chart = new google.visualization.ScatterChart(document.getElementById('popChart'));
    chart.draw(data, options);
}

// make a chart 
function drawXsChart() {
    console.debug("drawXsChart")
    // update coords
    if (dynamicState.year != 0) {
        xsCoords.push(dynamicState.graph.xs_last);
    }
    // data
    let data = google.visualization.arrayToDataTable(xsCoords);
    // options
    let options = {
        // title: "best 'x' value evolution during years",
        hAxis: { title: 'years', }, // minValue: xMin, maxValue: xMax
        vAxis: { title: 'x', }, // minValue: yMin, maxValue: yMax 
        legend: 'none',
        width: graphWidth,
        heigh: graphHeight
    };
    // init chart on DOM element and push
    let chart = new google.visualization.LineChart(document.getElementById('xsChart'));
    chart.draw(data, options);
}

function drawYsChart() {
    console.debug("drawYsChart")
    // update coords
    if (dynamicState.year != 0) {
        ysCoords.push(dynamicState.graph.ys_last);
    }
    // data
    let data = google.visualization.arrayToDataTable(ysCoords);
    // options
    let options = {
        // title: "best 'y' value evolution during years",
        hAxis: { title: 'years', }, //  minValue: xMin, maxValue: xMax 
        vAxis: { title: 'y', }, // minValue: yMin, maxValue: yMax 
        legend: 'none',
        width: graphWidth,
        heigh: graphHeight
    };
    // init chart on DOM element and push
    let chart = new google.visualization.LineChart(document.getElementById('ysChart'));
    chart.draw(data, options);
}

// make a chart 
function drawYearsChart() {
    console.debug("drawYearssChart")
    // update coords
    if (dynamicState.year != 0) {
        yearsCoords.push(dynamicState.graph.years_last);
    }
    // data
    let data = google.visualization.arrayToDataTable(yearsCoords);
    // options
    let options = {
        // title: "year of best found solution evolution during years",
        hAxis: { title: 'years', }, // minValue: xMin, maxValue: xMax
        vAxis: { title: 'year of best solution', }, // minValue: yMin, maxValue: yMax 
        legend: 'none',
        width: graphWidth,
        heigh: graphHeight
    };
    // init chart on DOM element and push
    var chart = new google.visualization.LineChart(document.getElementById('yearsChart'));
    chart.draw(data, options);
}



//      update
//////////////////////////////////////////////////////////////////

function updateCharts() {
    console.debug("updateCharts");
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawPopChart);
    google.charts.setOnLoadCallback(drawXsChart);
    google.charts.setOnLoadCallback(drawYsChart);
    google.charts.setOnLoadCallback(drawYearsChart);

}