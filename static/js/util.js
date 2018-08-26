function init_chart(chartList){
    /*
        初始化echarts实例
    */
    chartList.forEach(function(item, index, arr){
       echarts.init(document.getElementById(item["elemId"]), 'light');         
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
    var url = GET_DATA_URL,
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
        } else {
            alert(json_data.msg);
        }
    });
}

function set_chart_data(elem, data){
    /*
        填充图表数据
    */
    var title = data["title"],
        xAxis = data["xAxis"],
        series = data["series"],
        names = [];

    series.forEach(function(item, index, arr){
        names.push(item["name"]);
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


function login(){
    /*
        用户登录与注销
    */
    $("#login").click(function(){
        var elem = $(this);
        
        if(elem.val() === "登录"){  // 发送登录请求
            var url = USER_LOGIN_URL,
                params = {
                    "fwork_id": $("#username").val(),
                    "fpassword": $("#password").val()
                };

            $.post(url, params, function(json_data){
                if (0 === json_data.code) {
                    // 用户名、密码验证通过
                    elem.val("注销");
                    alert(json_data.msg);
                } else {
                    alert(json_data.msg);
                }
            });
        } else {  // 发送注销请求
            var url = USER_LOGOUT_URL;
            
            $.post(url, {}, function(json_data){
                if (0 === json_data.code) {
                    elem.val("登录");
                    alert(json_data.msg);
                } else {
                    alert(json_data.msg);
                }       
            });
        }
    });
}
