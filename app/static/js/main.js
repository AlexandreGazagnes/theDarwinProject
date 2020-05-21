console.debug("main.js loaded")

// on ready
$(function () {
    // front
    onFrontLoad();
    onFrontResize();

    // back
    onBackLoad();
    onFunctInitChange();

    //landing btn
    onBeginnerBtn();
    onIntermediateBtn();
    onExpertBtn();


    //Init submit
    onIntermediateInit();
    onExpertInit();

});




