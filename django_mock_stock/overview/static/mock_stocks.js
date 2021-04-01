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




/* chartjs code */


transfered_data = document.querySelector("#data-transfer").innerHTML
data_as_json = JSON.parse(transfered_data)
close_vals_lst = []
close_dates_lst = []

for(var date in data_as_json["Close"]){
    close_vals_lst.push(data_as_json["Close"][date])
    close_dates_lst.push(date.substring(5,10))
    
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
            backgroundColor: 'rgba(100,20,30,1)',
            borderColor: 'rgba(190,50,140,1)'
        }]
    },
   
});