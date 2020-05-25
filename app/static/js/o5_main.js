console.debug("main.js")

////////////////////////////////////////////////////////
//      Main.js
////////////////////////////////////////////////////////


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

    // init form
    onIntermediateInit();
    onExpertInit();

    // run form
    onRunSubmit();
});




