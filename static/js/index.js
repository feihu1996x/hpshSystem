(function(){
    var chartList=[
        {
            "elemId" : "chart0",  
            "dims" : "chart0"
        }, 
        {
            "elemId" : "chart1",  
            "dims" : "chart1"
        }
    ];

    // 初始化echarts实例
    init_chart(chartList);

    // 初始化jedate实例
    init_jedate(chartList);

    // 启用登录
    login();
})();

