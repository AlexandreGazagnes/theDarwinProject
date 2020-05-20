// screen dim
var width;
var height;
var isSmall;

// init easy medium or difficult
var initMethod;

// sections 
var infoId = "info-cont";
var initId = "init-cont";
var stateId = "state-cont";
var actionId = "action-cont";
var graphID = "graph-cont";

// info view
function toogleInfoView() {
    console.debug("toogleInfoView");
    $("#" + infoId).show();
    $("#" + initId).hide();
    $("#" + stateId).hide();
    $("#" + actionId).hide();
    $("#" + graphID).hide();
}

// init view
function toogleInitView(option) {
    console.debug("toogleInitView");
    initMethod = option;
    $("#" + infoId).hide();
    $("#" + initId).show();
    $("#" + stateId).hide();
    $("#" + actionId).hide();
    $("#" + graphID).hide();
}

// app run view
function toogleRunView() {
    console.debug("toogleRunView");
    $("#" + infoId).hide();
    $("#" + initId).hide();
    $("#" + stateId).show();
    $("#" + actionId).show();
    $("#" + graphID).show();
}

// dims
function updateDims() {
    console.debug("updateDims");
    width = $(document).width();
    height = $(document).height();
    console.debug(width, + " , " + height)
}

// sm or not 
function evalIsSmall() {
    console.debug("evalIsSmall");
    updateDims();
    if (width < 576) {
        isSmall = true;
    } else {
        isSmall = false;
    }
    console.debug("document is " + width + "small ? " + isSmall);
}

// order messup in 4*2 grids
function toogleFeatureGrid() {
    console.debug('toogleFeatureGrid')
    evalIsSmall();
    if (isSmall) {
        $("#featureColImg-1").removeClass("order-first");
        $("#featureColImg-3").removeClass("order-first");
    } else {
        $("#featureColImg-1").addClass("order-first");
        $("#featureColImg-3").addClass("order-first");
    }
}

// load
function onLoad() {
    console.debug("onLoad");
    toogleInfoView();
    toogleFeatureGrid();
}

// resize
function onResize() {
    console.debug("onResize");
    $(window).resize(function () {
        console.debug("reized");
        toogleFeatureGrid();
    });
}

// on ready
$(function () {
    onLoad();
    onResize();
});