console.debug("utils.js loaded")

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
