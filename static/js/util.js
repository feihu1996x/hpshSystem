function init_chart(chartList){
    /*
        初始化echarts实例
    */
    chartList.forEach(function(item, index, arr){
       echarts.init(document.getElementById(item["elemId"]));         
    });
}

function init_jedate(chartList) {
    /*
        初始化jedate实例
    */
    $("#start_date").jeDate({
        format:"YYYY-MM-DD",
        isTime:false,
        isinitVal : true,
        minDate:"2014-09-19",
        okfun: function(obj){
            /*
                点击确定按钮，选定日期后的回调函数
            */
            var start_date = $("#start_date").val(),
                end_date = $("#end_date").val();
            
            // 刷新echarts图表数据
            chartList.forEach(function(item, index, arr){
                var elemId = item["elemId"],
                    dims = item["dims"];
                flush_chart(start_date, end_date, elemId, dims);
            });
        }
    }); 
    
    $("#end_date").jeDate({
        format:"YYYY-MM-DD",
        isTime:false,
        isinitVal : true,
        minDate:"2014-09-19",
        okfun: function(obj){
            /*
                点击确定按钮，选定日期后的回调函数
            */
            var start_date = $("#start_date").val(),
                end_date = $("#end_date").val();
            
            // 刷新echarts图表
            chartList.forEach(function(item, index, arr){
                var elemId = item["elemId"],
                    dims = item["dims"];
                flush_chart(start_date, end_date, elemId, dims);
            });
        }
    }); 
}


function flush_chart(start_date, end_date, elem, dims) {
    /*
        刷新图表
    */
    var url = "",
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "dims": dims
        };

    console.log(params);

    $.get(url, params, function(json_data){
        // 向服务器请求数据，
        // 并用其填充echarts图表
        if (json_data.code === 0) {
           set_chart_data(elem, json_data.data);
        }
    });
}

function set_chart_data(elem, data){
    /*
        填充图表数据
    */
    var title = data["data"],
        xAxis = data["xAxis"],
        series = data["series"],
        names = [];

    series.forEach(function(item, index, arr){
        names.push(value["name"]);
    });

    var option = {
        title: {
            text: title
        },
        tooltip: {},
        legend: {
            data: names
        },
        xAxis: {
            data: xAxis
        },
        yAxis: {},
        series: series
    };

    var chart = echarts.getInstanceByDom(document.getElementById(elem));
    chart.setOption(option);
}
