$(document).ready(function () {
    var jsonData;
    $.ajax({
        type: 'GET',
        url: '/getJson',
        dataType: 'json',
        async: false,
        success: function (data) {
            jsonData = data;
        }
    });
    console.log(jsonData);
    /*********vue*********/
    var app = new Vue({
        delimiters: ['[[', ']]'],
        el: "#table",
        data: function () {
            return {
                trendings: jsonData
            }
        }
    })
    /*********vue*********/
});



