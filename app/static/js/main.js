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
    onExpertBtn();
    onExpertInit();


    //Init submit
    onIntermediateInit();
    onExpertInit();

});




