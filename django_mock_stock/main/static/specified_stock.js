
ticker_data_string = document.querySelector("#data_transfer").innerHTML
filtered_data_str = pyJsonStr_to_jsJsonStr(ticker_data_string)
ticker_data = JSON.parse(filtered_data_str)

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

// TODO: test for more edge cases
function repl_correct_wrd(match, nth_str, offset, entire_str){
    let repl = match.substring(0,1) + "\""
    if(match.substring(0,1) === "\'"){
        repl = "\"" + match.substring(1,2) 
    }

    return repl
}

// TODO: test for more edge cases
function pyJsonStr_to_jsJsonStr(python_json_str){
    let replace_singQuotes = python_json_str.replaceAll(/\W\'|\'\W/g, /* "\"" */ repl_correct_wrd)
    let none_with_quotes = replace_singQuotes.replaceAll(/None/g, "\"None\"")
    let conv_to_js_bools = none_with_quotes.replaceAll(/False/g, "false").replaceAll(/True/g, "true")
    
    return conv_to_js_bools
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