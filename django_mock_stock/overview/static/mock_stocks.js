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
// var myLineChart = null;
var lineChartsList = []

function updateGraphs(charts_data_lst, interval){
    var sp_ctx = document.getElementById('sp_chart').getContext('2d');
    var dow_ctx = document.getElementById('dow_chart').getContext('2d');
    var nasdaq_ctx = document.getElementById('nasdaq_chart').getContext('2d');
    let chrt_cntxts = []
    chrt_cntxts.push(sp_ctx)
    chrt_cntxts.push(dow_ctx)
    chrt_cntxts.push(nasdaq_ctx)

    var cntxt_index = 0
    for(var chart_data of charts_data_lst){
        data_as_json = JSON.parse(chart_data)
        close_vals_lst = []
        close_dates_lst = []

        for(var date in data_as_json["Close"]){
            console.log(date)
            close_vals_lst.push(data_as_json["Close"][date])
            if(interval == "less_than_days"){
                local_date_formt = new Date(Date.parse(date))
                local_time = local_date_formt.getHours() + ':' + local_date_formt.getMinutes()
                close_dates_lst.push(local_time)
            }
            else{
                close_dates_lst.push(date.substring(0,10))
            }
            
        }

        var myLineChart = new Chart(chrt_cntxts[cntxt_index], {
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
        lineChartsList.push(myLineChart)
        cntxt_index++
    }
}


sp_transfered_data = document.querySelector("#data_transfer_sp").innerHTML
dow_transfered_data = document.querySelector("#data_transfer_dow").innerHTML
nasdaq_transfered_data = document.querySelector("#data_transfer_nasdaq").innerHTML
interval_unit = document.querySelector("#interval_time").innerHTML


transfered_data_lst = []
transfered_data_lst.push(sp_transfered_data)
transfered_data_lst.push(dow_transfered_data)
transfered_data_lst.push(nasdaq_transfered_data)
updateGraphs(transfered_data_lst, interval_unit)
// interval_unit_sp = document.querySelector("#interval_time_sp").innerHTML
// data_as_json_sp = JSON.parse(transfered_data_sp)
// close_vals_lst = []
// close_dates_lst = []

// for(var date in data_as_json_sp["Close"]){
//     close_vals_lst.push(data_as_json_sp["Close"][date])
//     if(interval_unit_sp == "less_than_days"){
//         local_date_formt = new Date(Date.parse(date))
//         local_time = local_date_formt.getHours() + ':' + local_date_formt.getMinutes()
//         close_dates_lst.push(local_time)
//     }
//     else{
//         close_dates_lst.push(date.substring(0,10))
//     }
    
// }

// var ctx = document.getElementById('myChart').getContext('2d');
// var myLineChart = new Chart(ctx, {
//     type: 'line',
//     maintainAspectRatio: false,
//     data: {
//         labels: close_dates_lst,
//         datasets: [{
//             label: 'Close stock value',
//             data: close_vals_lst,
//             fill: false,
//             pointRadius: 3,
//             pointHitRadius: 4,
//             borderColor: 'rgba(190,100,30,0.6)',
//         }]
//     },

// });