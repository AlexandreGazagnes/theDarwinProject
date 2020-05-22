console.debug("var.js")

////////////////////////////////////////////////////////
//      Var.js
////////////////////////////////////////////////////////


//      FRONT
////////////////////////////////////////////////////////

// screen dim
var width;
var height;
var isSmall;

// animation
var loadingSpeed = 2000;
var transitionSpeed = 1000;

// init easy medium or difficult
var initMethod;

// sections 
var infoId = "info-cont";
var initId = "init-cont";
var stateId = "state-cont";
var actionId = "action-cont";
var graphID = "graph-cont";


//      BACK
////////////////////////////////////////////////////////

// // funts and states algo
var algoInitilalized = false;
var algoId = "";
var year = 0;

var functsData; // store all functs add spec
var initForm; // store init data wheb Algo created
var staticState;
var dynamicState;


//      GRAPH
////////////////////////////////////////////////////////

// coordonates
var firstGraphCall = true;
// var popCoords = [["x", "y"], [0.0, 0.0]];
var xsCoords = [["years", "x"], [0.0, 0.0]];
var ysCoords = [["years", "y"], [0.0, 0.0]];
var yearsCoords = [["years", "last_new_year"], [0.0, 0.0]];


// coorodnates
var population = [["x", "y"], [1, 1], [2, 2]];
var xs_last = [["years", "x"], [0.0, 10.0]];
var ys_last = [["years", "y"], [0.0, 10.0]];
var years_last = [["years", "last_new_year"], [0.0, 0.0]];

// scatter
var pointSize = 6;
var pointShape = "circle";

