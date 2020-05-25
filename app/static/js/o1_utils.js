console.debug("utils.js")

////////////////////////////////////////////////////////
//      Utils.js
////////////////////////////////////////////////////////


// dummy call to have various states on sever side
function dummyCall() {
    $.ajax({
        type: "GET",
        url: "/dummycall?algoId=" + algoId,
        // async: false, // Mode synchrone
        success: function (data) {
            console.debug('OK')
        }
    });
}

// a range function
function range(start, end) {
    var array = new Array();
    for (var i = start; i < end; i++) {
        array.push(i);
    }
    return array;
}

// zip
function zip(arrays) {
    return arrays[0].map(function (_, i) {
        return arrays.map(function (array) { return array[i] })
    });
}


