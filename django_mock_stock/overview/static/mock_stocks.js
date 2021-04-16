// THIS IS CODE FOR YAHOO FINANCE API

// const fetch = require("node-fetch"); 
// fetch("https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart?interval=5m&symbol=AMRN&range=1d&region=US", {
// 	"method": "GET",
// 	"headers": {
// 		"x-rapidapi-key": "f0ce186f6fmsh4a4c6a04e92e5c2p176685jsn3616dcafde61",
// 		"x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com"
// 	}
// })
// .then(response => {
// 	console.log(response);
// })
// .catch(err => {
// 	console.error(err);
// });


//  animation code

let articles = document.querySelectorAll(".article"); 

for (i = 0; i < articles.length; i++) {
    let article = articles[i];
    article.onmouseenter = function(){
        article.style.borderColor = 'black';
    }
    article.onmouseleave = function(){
        article.style.borderColor = 'grey';
    }
}




//  chartjs code 

transfered_data = document.querySelector("#data-transfer").innerHTML
interval_unit = document.querySelector("#interval-time").innerHTML
data_as_json = JSON.parse(transfered_data)
close_vals_lst = []
close_dates_lst = []

for(var date in data_as_json["Close"]){
    close_vals_lst.push(data_as_json["Close"][date])
    if(interval_unit == "less_than_days"){
        local_date_formt = new Date(Date.parse(date))
        local_time = local_date_formt.getHours() + ':' + local_date_formt.getMinutes()
        close_dates_lst.push(local_time)
    }
    else{
        close_dates_lst.push(date.substring(0,10))
    }
    
}
// console.log(data_as_json["Close"])


var ctx = document.getElementById('myChart').getContext('2d');
var myLineChart = new Chart(ctx, {
    type: 'line',
    maintainAspectRatio: false,
    data: {
        labels: close_dates_lst,
        datasets: [{
            label: 'Close stock value',
            data: close_vals_lst,
            fill: false,
            pointRadius: 3,
            pointHitRadius: 4,
            borderColor: 'rgba(190,100,30,0.6)',
        }]
    },

});