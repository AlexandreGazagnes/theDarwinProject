console.debug("back.js")

////////////////////////////////////////////////////////
//      BACK.js
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

// based on the hmtl selected funct update data and graph
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

// if use change the function on init form
function onFunctInitChange() {
    console.debug("onFunctInitChange");
    $("#funct").change(function () {
        console.debug('onFunctInitChange --> funct selected has changed');
        updateFunctInitData();
    });
}

// on load init funct data for the init form
function onBackLoad() {
    console.debug("onBackLoad");
    getFunctsData();
    updateFunctInitData();
}


//      get update Algo info static or dynamic data  
////////////////////////////////////////////////////////

// update static State data in html
function updateStaticState() {
    console.debug("updateStaticState");
    ["Id", "Name", "Objective", "Interval", "Seed_parents", "Kill_rate", "Average_child_numb",].forEach((elem) => {
        $("#static" + elem).html(staticState[elem.toLowerCase()]);
    });
    let strFunct = $("#funct option:selected").val();
    ["Name", "Level", "Expression", "Dimension"].forEach((elem) => {
        $("#staticFunct" + elem).html(functsData[strFunct][elem.toLowerCase()]);
    });
}

// get static state --> make api call and save static state data
function getStaticState(forceSync = false) {
    console.debug("'getStaticState");
    let args_dict = {
        type: "GET",
        url: "/staticstate?algoId=" + algoId,
        success: function (data) {
            staticState = data;
            updateStaticState();
        }
    }
    if (forceSync) {
        args_dict.async = false;
    }
    $.ajax(args_dict);
}

// update dynamic State data in html
function updateDynamicState() {
    console.debug("updateDynamicState");
    let firstList = ["Year", "Len_current_population", "Best_current_population", "Kill_number", "Saved_people", "New_people_number"];
    firstList.forEach((elem) => {
        $("#dynamic" + elem).html(dynamicState[elem.toLowerCase()]);
    });
    ["First", "Normal", "Random"].forEach((elem) => {
        $("#dynamic" + elem).html(dynamicState["repartition_current_population"][elem.toLowerCase()]);
    });

    ["Random_child_nb", "Normal_child_nb",].forEach((elem) => {
        $("#dynamic" + elem).html(dynamicState["new_people_composition"][elem.toLowerCase()]);
    });
}

// get dynamic state --> make api call and save dynmaic state data
function getDynamicState(forceSync = false) {
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

//  DO CALL SERVER To INIT an ALGO INSTANCE
////////////////////////////////////////////////////////

// whent init update various data and graphs
function handleInitMethod(data) {
    console.debug("handleInitMethod");
    getStaticState();
    getDynamicState();
    updateCharts();
}

// init Algo on back end based on the easiest model
function doBeginnerInit(forceSync = false) {
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

// init Algo on back end based on the form-ini vals
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


//      init submit form --> run
////////////////////////////////////////////////////////

// event handler
function onIntermediateInit() {
    console.debug('onIntermediateInit');
    // event handler
    // $("#init-form").submit(function (e) {
    //     console.debug(" onIntermediateInit --> form submited")
    //     doExpertInit(e);
    // });
}

// event handler
function onExpertInit() {
    console.debug('onExpertInit');
    // event handler
    $("#init-form").submit(function (e) {
        initForm = $(this).serialize();
        console.debug(" onExpertInit --> form submited");
        doExpertInit(e);
    });
}


//      landing BTN landing --> init form
////////////////////////////////////////////////////////

// beginner btn --> go to run and init an object
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

// intermediate btn --> go to init view
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

// expert btn --> go to init view
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


//      DO Run
////////////////////////////////////////////////////////

// post run for 1 year
function postRun(forceSync = false) {
    console.debug("postRun");
    $.ajax({
        type: "POST",
        url: "/run?algoId=" + algoId,
        // async: false, // Mode synchrone
        success: function (data) {
            dynamicState = data;
            updateDynamicState();
            updateCharts();
        }
    });
}

// loop regadring form data
function manageRun(e) {
    console.debug("manageRun");
    // avoid to execute the actual submit of the form.
    e.preventDefault();

    // local vars
    let form = $("#run-form");
    let years = form.find("#years").val();
    let speed = form.find("#speed").val();

    // prevent for speed < 1 (ie 0.1 --> sleep 10 sec)
    speed = 1000 * (1 / speed)
    if (speed > 1000) {
        speed = 1000
    }
    // years --> for i in range :) 
    let arrRange = range(0, years);
    arrRange.forEach(function (item, index) {
        setTimeout(function () { // be carrefull with setTimeoit != sleep() --> it is an async fuct
            postRun();
        }, index * speed);
    });
}

// event handler
function onRunSubmit() {
    console.debug("onRunSubmit")
    $("#run-form").submit(function (e) {
        console.debug("onRunSubmit --> run submitted")
        manageRun(e);
    });
}
