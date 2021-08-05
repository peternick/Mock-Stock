
ticker_data_string = document.querySelector("#data_transfer").innerHTML
ticker_data = JSON.parse(ticker_data_string)

document.querySelector("#stock_price").innerHTML = 'Current Stock Price: $' + ticker_data['info']['currentPrice']
document.querySelector("#main_title").innerHTML = ticker_data['info']['shortName'] + '(' + ticker_data['info']['symbol'] + ')'

updateGraph(ticker_data)

function updateGraph(ticker_data){
    
    hist_dic = ticker_data['hist']["Open"]
    open_vals_lst = []
    open_dates_lst = []
    for(var date in hist_dic){
        open_vals_lst.push(hist_dic[date])
        if(ticker_data["time_interval"] == "less_than_days"){
            local_date_formt = new Date(Date.parse(date))
            local_time = local_date_formt.getHours() + ':' + stndrd_minutes(local_date_formt.getMinutes())
            open_dates_lst.push(local_time)
        }
        else{
            open_dates_lst.push(date.substring(0,10))
        }
        
    }
    chrt_cntxt = document.querySelector("#stock_chart").getContext('2d')
    var myLineChart = new Chart(chrt_cntxt, {
        type: 'line',
        maintainAspectRatio: false,
        data: {
            labels: open_dates_lst,
            datasets: [{
                label: 'Open stock value',
                data: open_vals_lst,
                fill: false,
                pointRadius: 3,
                pointHitRadius: 4,
                borderColor: 'rgba(190,100,30,0.6)',
            }]
        },
    
    });

}



function stndrd_minutes(minutes){
    let minutes_str = ""
    if(minutes < 10){
        minutes_str = "0" + minutes
    }
    else{
        minutes_str = minutes + ""
    }

    return minutes_str
}