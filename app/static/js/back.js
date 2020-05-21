console.debug("back.js loaded")

// // funts and states algo
var algoInitilalized = false;
var algoId = "";
var year = 0;

var functsData; // store all functs add spec
var initFormData; // store init data wheb Algo created
var staticState;
var dynamicState;

// coorodnates
var popCoords = [["x", "y"], [1, 1], [2, 2]];
var xsCoords = [["years", "x"], [0.0, 10.0]];
var ysCoords = [["years", "y"], [0.0, 10.0]];
var yearsCoords = [["years", "last_new_year"], [0.0, 0.0]];




// get all functs data dicts
function getFunctsData() {
    console.debug("getFunctsData")
    $.ajax({
        type: "GET",
        url: "/functsdata",
        async: false, // Mode synchrone
        success: function (data) {
            functsData = data;
        }
    });
}


function updateFunctInitData() {
    console.debug("updateFunctInitData")
    var strFunct = $("#funct option:selected").val();
    let functObject = functsData[strFunct];
    $("#functLevel").html(functObject['level']);
    $("#functExpression").html(functObject['expression']);
    $("#functDimension").html(functObject['dim']);
    let urlImg = "/static/img/functs/" + strFunct + ".png";
    $("#functSrcImg").attr("src", urlImg);
}


function onBackLoad() {
    console.debug("onBackLoad")
    getFunctsData();
    updateFunctInitData();
}


function onFunctInitChange() {
    console.debug("onFunctInitChange")
    $("#funct").change(function () {
        console.debug('onFunctInitChange --> funct selected has changed')
        updateFunctInitData();
    });
}

