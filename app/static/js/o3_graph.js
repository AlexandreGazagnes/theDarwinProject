console.debug("graph.js")

////////////////////////////////////////////////////////
//      Graph.js
////////////////////////////////////////////////////////


// Make Charts
////////////////////////////////////////////////////////////

// make a chart 
function drawPopChart() {
    console.debug("drawPopChart")

    // context
    let ctx = document.getElementById('popChart').getContext('2d');

    // datasets
    let datasets = [
        {
            // label: 'Scatter Dataset',
            data: dynamicState.graph.current_population,
            pointRadius: 2,
            backgroundColor: "#007bff",
        },
    ]

    // scales
    let scales = {
        xAxes: [{
            type: 'linear',
            position: 'bottom'
        }]
    }

    // options
    let options = {
        maintainAspectRatio: false,
        animation: {
            duration: 0 // general animation time
        },
        hover: {
            animationDuration: 0 // duration of animations when hovering an item
        },
        // responsiveAnimationDuration: 0, // animation duration after a resiz

        scales: scales
    }

    // make the chart
    var scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: datasets,
            options: options
        }
    });

    scatterChart.canvas.parentNode.style.height = '200px';
    scatterChart.canvas.parentNode.style.width = '333px';
}





// make a chart 
function drawXsChart() {
    console.debug("drawXsChart")

    // context
    var ctx = document.getElementById('xsChart').getContext('2d');

    // labels 
    let labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

    // dataset
    let datasets = [
        {
            label: 'My First dataset',
            backgroundColor: "#007bff",
            borderColor: "#007bff",
            data: [0, 10, 5, 2, 20, 30, 45]
        },
    ];

    // options
    let options = {};

    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: options
    });

    chart.canvas.parentNode.style.height = '200px';
    chart.canvas.parentNode.style.width = '333px';
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