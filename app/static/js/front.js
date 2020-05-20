// screen dim
var width;
var height;
var isSmall;

// init easy medium or difficult
var optionChoice;

// sections 
var infoId = "info-cont";
var showInfoCont = true;

var initId = "init-cont";
var showInitCont = false;

var stateId = "state-cont";
var showStateCont = false;

var actionId = "action-cont";
var showActionCont = false;

var graphID = "graph-cont";
var showGraphCont = false;

// info view
function toogleInfoView() {
    console.log("toogleInfoView");
    $("#" + infoId).show();
    $("#" + initId).hide();
    $("#" + stateId).hide();
    $("#" + actionId).hide();
    $("#" + graphID).hide();
}

// init view
function toogleInitView() {
    console.log("toogleInitView");
    $("#" + infoId).hide();
    $("#" + initId).show();
    $("#" + stateId).hide();
    $("#" + actionId).hide();
    $("#" + graphID).hide();
}

// app run view
function toogleRunView() {
    console.log("toogleRunView");
    $("#" + infoId).hide();
    $("#" + initId).hide();
    $("#" + stateId).show();
    $("#" + actionId).show();
    $("#" + graphID).show();
}



function updateWidth() {
    console.log("updateWidth");
    width = $(document).width()
    console.log(width)
}

function updateHeight() {
    console.log("updateHeight");
    height = $(document).height()
    console.log(height)
}

function evalIsSmall() {
    console.log("evalIsSmall");
    updateWidth();
    if (width < 576) {
        isSmall = true;
    } else {
        isSmall = false;
    }
    console.log("document is " + width + "small ? " + isSmall);
    return isSmall;
}


function toogleFeatureGrid() {
    console.log('toogleFeatureGrid')
    if (isSmall) {
        $("#featureColImg-1").removeClass("order-first");
        $("#featureColImg-3").removeClass("order-first");
    } else {
        $("#featureColImg-1").addClass("order-first");
        $("#featureColImg-3").addClass("order-first");
    }
}


function onLoad() {
    console.log("onLoad");
    toogleInfoView();
    evalIsSmall();
    toogleFeatureGrid();
}


function onResize() {
    console.log("onResize");
    $(window).resize(function () {
        console.log("reized");
        evalIsSmall();
        toogleFeatureGrid();
    });
}


// on ready
$(function () {
    onLoad();
    onResize();
});