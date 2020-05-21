console.debug("back.js loaded")


////////////////////////////////////////////////////////
//      VAR
////////////////////////////////////////////////////////

// // funts and states algo
var algoInitilalized = false;
var algoId = "";
var year = 0;

var functsData; // store all functs add spec
var initFormData; // store init data wheb Algo created
var staticState;
var dynamicState;

// coordonates
var popCoords = [["x", "y"], [1, 1], [2, 2]];
var xsCoords = [["years", "x"], [0.0, 10.0]];
var ysCoords = [["years", "y"], [0.0, 10.0]];
var yearsCoords = [["years", "last_new_year"], [0.0, 0.0]];


////////////////////////////////////////////////////////
//      Load and Init Funct Methods
////////////////////////////////////////////////////////

// get all functs data dicts
function getFunctsData() {
    console.debug("getFunctsData");
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
    console.debug("updateFunctInitData");
    var strFunct = $("#funct option:selected").val();
    let functObject = functsData[strFunct];
    $("#functLevel").html(functObject['level']);
    $("#functExpression").html(functObject['expression']);
    $("#functDimension").html(functObject['dim']);
    let urlImg = "/static/img/functs/" + strFunct + ".png";
    $("#functSrcImg").attr("src", urlImg);
}


function onBackLoad() {
    console.debug("onBackLoad");
    getFunctsData();
    updateFunctInitData();
}


function onFunctInitChange() {
    console.debug("onFunctInitChange");
    $("#funct").change(function () {
        console.debug('onFunctInitChange --> funct selected has changed');
        updateFunctInitData();
    });
}



////////////////////////////////////////////////////////
//      get Algo info static or dynamic
////////////////////////////////////////////////////////

function getStaticState() {
    console.debug('getStaticState');
    // $.ajax({
    //     type: "GET",
    //     url: "/staticstate?algoId=" + algoId,
    //     // async: false, // Mode synchrone
    //     success: function (data) {
    //         // $("#ajaxResponse").html(data);
    //         $("#staticId").html(data["id"]);
    //         $("#staticName").html(data["name"]);
    //         let strFunct = $("#funct option:selected").val();
    //         $("#staticFunct").html(functsData[strFunct]["name"]);
    //         $("#staticLevel").html(functsData[strFunct]["level"]);
    //         $("#staticExpression").html(functsData[strFunct]["expression"]);
    //         $("#staticDimension").html(functsData[strFunct]["dim"]);
    //         $("#staticObjective").html(data["objective"]);
    //         $("#staticInterval").html(data["interval"]);
    //         $("#staticSeedParents").html(data["seed_parents"]);
    //         $("#staticKillRate").html(data["kill_rate"]);
    //         $("#staticAverageChildNumb").html(data["average_child_numb"]);
    //     }
    // });
}


function getDynamicState() {
    console.debug('getDynamicState');
    // $.ajax({
    //     type: "GET",
    //     url: "/dynamicstate?algoId=" + algoId,
    //     // async: false, // Mode synchrone
    //     success: function (data) {
    //         $("#rowLen").html(data["len_current_population"]);
    //         $("#rowYear").html(data["year"]);
    //         console.debug(data["repartition_current_population"])
    //         $("#rowOriginal").html(data["repartition_current_population"]["first"]);
    //         $("#rowNormal").html(data["repartition_current_population"]["normal"]);
    //         $("#rowMutant").html(data["repartition_current_population"]["random"]);
    //         $("#rowBest").html(data["best_current_population"].slice(0, 3)).toString();
    //     }
    // });
}




function handleInitMethod(data) {
    console.debug("handleInitMethod");
    getStaticState();
    getDynamicState();
    // updateCharts();

}

function doBeginnerInit() {
    console.debug('doBeginnerInit')
    $.ajax({
        type: "POST",
        url: "/initfrommodel",
        // async: false, // Mode synchrone
        success: function (idAlgo) {
            algoInitilalized = true;
            algoId = idAlgo;
            fromLandingToRunView()
            handleInitMethod();
            console.debug("onBeginnerInit -->request OK / algoId = " + idAlgo);
        }
    });
}

function doExpertInit(e) {
    console.debug("doExpertInit")
    e.preventDefault(); // avoid to execute the actual submit of the form.
    $.ajax({
        type: "POST",
        url: "/initfromuser",
        // async: false, // Mode synchrone
        data: $(this).serialize(), // serializes the form's elements.
        success: function (idAlgo) {
            algoInitilalized = true;
            algoId = idAlgo;
            fromInitToRunView();
            handleInitMethod(idAlgo);
            console.debug("onExpertInit -->request OK algoId = " + idAlgo);
        }
    });
}


////////////////////////////////////////////////////////
//      init submit form --> run
////////////////////////////////////////////////////////

function onIntermediateInit() {
    console.debug('onIntermediateInit');
    // event handler
    // $("#init-form").submit(function (e) {
    //     console.debug(" onIntermediateInit --> form submited")
    //     doExpertInit(e);
    // });
}

function onExpertInit() {
    console.debug('onExpertInit');
    // event handler
    $("#init-form").submit(function (e) {
        console.debug(" onExpertInit --> form submited")
        doExpertInit(e);
    });
}


////////////////////////////////////////////////////////
//      landing BTN landing --> init form
////////////////////////////////////////////////////////


function onBeginnerBtn() {
    console.debug('onBeginnerInit');
    // event handler
    $("#btnGo0Text-0").click(function (e) {
        console.debug('onBeginnerInit --> btnGo0Text 0 clicked')
        doBeginnerInit();
    });
    $("#btnGo1Text-0").click(function (e) {
        console.debug('onBeginnerInit --> btnGo1Text 0 clicked')
        doBeginnerInit();
    });
}

function onIntermediateBtn() {
    console.debug('onIntermediateBtn');
    $("#btnGo0Text-1").click(function (e) {
        console.debug('onIntermediateBtn --> btnGo0Text 2 clicked')
        fromLandingToInitView();
    });
    $("#btnGo1Text-1").click(function (e) {
        console.debug('onIntermediateBtn --> btnGo1Text 2 clicked')
        fromLandingToInitView();
    });
}

function onExpertBtn() {
    console.debug('onExpertBtn');
    $("#btnGo0Text-2").click(function (e) {
        console.debug('onExpertBtn --> btnGo0Text 2 clicked')
        fromLandingToInitView();
    });
    $("#btnGo1Text-2").click(function (e) {
        console.debug('onExpertBtn --> btnGo1Text 2 clicked')
        fromLandingToInitView();
    });
}