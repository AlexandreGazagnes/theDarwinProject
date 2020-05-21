console.debug("back.js loaded")


////////////////////////////////////////////////////////
//      VAR
////////////////////////////////////////////////////////

// // funts and states algo
var algoInitilalized = false;
var algoId = "";
var year = 0;

var functsData; // store all functs add spec
var initForm; // store init data wheb Algo created
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

function updateStaticState() {
    console.debug("updateStaticState");
    ["Id", "Name", "Objective", "Interval", "Seed_parents", "Kill_rate", "Average_child_numb"].forEach((elem) => {
        $("#static" + elem).html(staticState[elem.toLowerCase()]);
    });
    let strFunct = $("#funct option:selected").val();
    ["Name", "Level", "Expression", "Dimension"].forEach((elem) => {
        $("#staticFunct" + elem).html(functsData[strFunct][elem.toLowerCase()]);
    });
}

function getStaticState() {
    console.debug("'getStaticState");
    $.ajax({
        type: "GET",
        url: "/staticstate?algoId=" + algoId,
        // async: false, // Mode synchrone
        success: function (data) {
            staticState = data;
            updateStaticState();
        }
    });
}

function updateDynamicState() {
    console.debug("updateDynamicState");
    let firstList = ["Year", "Len_current_population", "Best_current_population"];
    firstList.forEach((elem) => {
        $("#dynamic" + elem).html(dynamicState[elem.toLowerCase()]);
    });
    ["First", "Normal", "Random"].forEach((elem) => {
        $("#dynamic" + elem).html(dynamicState["repartition_current_population"][elem.toLowerCase()]);
    });
}

function getDynamicState() {
    console.debug("getDynamicState");
    $.ajax({
        type: "GET",
        url: "/dynamicstate?algoId=" + algoId,
        // async: false, // Mode synchrone
        success: function (data) {
            dynamicState = data;
            updateDynamicState();
        }
    });
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
        data: initForm, // serializes the form's elements.
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
        initForm = $(this).serialize();
        console.debug(" onExpertInit --> form submited");
        doExpertInit(e);
    });
}


////////////////////////////////////////////////////////
//      landing BTN landing --> init form
////////////////////////////////////////////////////////

function onBeginnerBtn() {
    console.debug('onBeginnerInit');
    let idxs = ["0", "1"];
    idxs.forEach((elem) => {
        $("#btnGo" + elem + "Text-0").click(function (e) {
            console.debug('onBeginnerInit --> btnGo' + elem + 'Text 0 clicked')
            doBeginnerInit();
        });
    });
}

function onIntermediateBtn() {
    console.debug('onIntermediateBtn');
    let idxs = ["0", "1"];
    idxs.forEach((elem) => {
        $("#btnGo" + elem + "Text-1").click(function (e) {
            console.debug('onBeginnerInit --> btnGo' + elem + 'Text 1 clicked')
            fromLandingToInitView();
        });
    });

}

function onExpertBtn() {
    console.debug('onExpertBtn');
    let idxs = ["0", "1"];
    idxs.forEach((elem) => {
        $("#btnGo" + elem + "Text-2").click(function (e) {
            console.debug('onBeginnerInit --> btnGo' + elem + 'Text 2 clicked')
            fromLandingToInitView();
        });
    });
}



    // $("#btnGo0Text-1").click(function (e) {
    //     console.debug('onIntermediateBtn --> btnGo0Text 2 clicked')
    //     fromLandingToInitView();
    // });
    // $("#btnGo1Text-1").click(function (e) {
    //     console.debug('onIntermediateBtn --> btnGo1Text 2 clicked')
    //     fromLandingToInitView();
    // });