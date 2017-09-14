$(document).ready(function () {
    /*********vue*********/
    var app = new Vue({
        el: "#layout",
        data: function () {
            return {
                transactions: []
            }
        },
        created: function () {
            var sumData = [];
            $.ajax({
                type: 'GET',
                url: '/getJson',
                dataType: 'json', 
                success: function(data) {
                    console.log(data);
                },
                error: function(xhr, type) {
                }
            });
            this.transactions = sumData;//这里的this是vue对象，如果放到jquery里面就不是vue对象了
            //console.log(this.transactions);
        }
    })
    /*********vue*********/
});



