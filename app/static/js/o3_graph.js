console.debug("graph.js")

////////////////////////////////////////////////////////
//      Graph.js
////////////////////////////////////////////////////////


// Make Charts
////////////////////////////////////////////////////////////

// make a chart 
function drawPopChart() {
    console.debug("drawPopChart")
    // disable animation for all / GLOBAL
    Chart.defaults.global.animation = false;
    // context
    let ctx = document.getElementById('popChart').getContext('2d');
    // population data
    let populationDataset = {
        label: "Current population",
        data: dynamicState.graph.current_population,
        pointRadius: 2,
        backgroundColor: "#007bff",
    }
    // template data
    let templateDataset = {}
    if (showTemplate) {
        templateDataset = {
            label: "Function",
            data: staticState.funct_template,
            pointRadius: 0.1,
            backgroundColor: "rgba(220, 53, 69, 0.01)",
        }
    }
    // scales
    let myScales = {
        xAxes: [{
            type: 'linear',
            position: 'bottom'
        }]
    }
    // options
    let myOptions = {
        maintainAspectRatio: true,
        responsive: true,
        hover: {
            animationDuration: 0, // duration of animations when hovering an 
        },
        showLines: false, // disable for all datasets
        responsiveAnimationDuration: 0, // animation duration after a resiz
        scales: myScales
    }
    // datasets
    let myDatasets = [
        populationDataset,
        templateDataset,
    ]
    // make the chart
    var scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: myDatasets,
            options: myOptions,
        }
    });
    // scatterChart.canvas.parentNode.style.height = '200px';
    // scatterChart.canvas.parentNode.style.width = '333px';
}


// make a chart 
function drawXsChart() {
    console.debug("drawXsChart")
    // context
    let ctx = document.getElementById('xsChart').getContext('2d');
    //data
    xLabels.push(dynamicState.graph.xs_last[0]);
    xsCoords.push(dynamicState.graph.xs_last[1]);
    // labels 
    let labels = xLabels;
    // dataset
    let datasets = [
        {
            label: "x' value evolution during years",
            // backgroundColor: "rba(100, 100,100, 0.0)",
            borderColor: "#007bff",
            pointRadius: 0.1,
            fill: false,
            data: xsCoords,
        },
    ];
    // options
    let options = {};
    var xsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: options
    });
    //     chart.canvas.parentNode.style.height = '200px';
    //     chart.canvas.parentNode.style.width = '333px';
}

function drawYsChart() {
    console.debug("drawYsChart")
    let ctx = document.getElementById('ysChart').getContext('2d');
    ysCoords.push(dynamicState.graph.ys_last[1]);
    let labels = xLabels;
    let datasets = [
        {
            label: "y' value evolution during years",
            // backgroundColor: "rba(100, 100,100, 0.0)",
            borderColor: "#007bff",
            data: ysCoords,
            fill: false,
            pointRadius: 0.1,
        },
    ];
    // options
    let options = {};
    var xsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: datasets
        },
        options: options
    });
    //     chart.canvas.parentNode.style.height = '200px';
    //     chart.canvas.parentNode.style.width = '333px';
}

// make a chart 
function drawYearsChart() {
    console.debug("drawYearssChart")
    // // update coords
    // if (dynamicState.year != 0) {
    //     yearsCoords.push(dynamicState.graph.years_last);
    // }
    // // data
    // let data = google.visualization.arrayToDataTable(yearsCoords);
    // // options
    // let options = {
    //     // title: "year of best found solution evolution during years",
    //     hAxis: { title: 'years', }, // minValue: xMin, maxValue: xMax
    //     vAxis: { title: 'year of best solution', }, // minValue: yMin, maxValue: yMax 
    //     legend: 'none',
    //     width: graphWidth,
    //     heigh: graphHeight
    // };
    // // init chart on DOM element and push
    // var chart = new google.visualization.LineChart(document.getElementById('yearsChart'));
    // chart.draw(data, options);


    // // context
    // let   ctx = document.getElementById('yearsChart').getContext('2d');

    // // labels 
    // let labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];

    // // dataset
    // let datasets = [
    //     {
    //         label: 'My First dataset',
    //         backgroundColor: "#007bff",
    //         borderColor: "#007bff",
    //         data: [0, 10, 5, 2, 20, 30, 45]
    //     },
    // ];

    // // options
    // let options = {};

    // var chart = new Chart(ctx, {
    //     type: 'line',
    //     data: {
    //         labels: labels,
    //         datasets: datasets
    //     },
    //     options: options
    // });

    // chart.canvas.parentNode.style.height = '200px';
    // chart.canvas.parentNode.style.width = '333px';
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