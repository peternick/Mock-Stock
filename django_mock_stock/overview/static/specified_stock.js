
ticker_data_string = document.querySelector("#data_transfer").innerHTML
filtered_data_str = pyJsonStr_to_jsJsonStr(ticker_data_string)
ticker_data = JSON.parse(ticker_data_string)

updateGraph(ticker_data)

function updateGraph(ticker_data){
    hist_dic = ticker_data['hist']["Open"]
    open_vals_lst = []
    open_dates_lst = []
    for(var date in hist_dic){
        open_vals_lst.push(hist_dic[date])
        if(ticker_data["time_interval"] == "less_than_days"){
            local_date_formt = new Date(Date.parse(date))
            local_time = local_date_formt.getHours() + ':' + local_date_formt.getMinutes()
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

function repl_correct_wrd(match, nth_str, offset, entire_str){
    repl = match.substring(0,1) + "\""
    if(match.substring(0,1) === "\'"){
        repl = "\"" + match.substring(1,2) 
    }

    return repl
}

function pyJsonStr_to_jsJsonStr(python_json_str){
    replace_singQuotes = python_json_str.replaceAll(/\W\'|\'\W/g, /* "\"" */ repl_correct_wrd)
    none_with_quotes = ticker_data_string.replaceAll(/None/g, "\"None\"")
    conv_to_js_bools = ticker_data_string.replaceAll(/False/g, "false").replaceAll(/True/g, "true")
    
    return conv_to_js_bools
}