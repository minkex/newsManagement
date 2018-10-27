Date.prototype.format = function(format)
{
 var o = {
 "M+" : this.getMonth()+1, //month
 "d+" : this.getDate(),    //day
 "h+" : this.getHours(),   //hour
 "m+" : this.getMinutes(), //minute
 "s+" : this.getSeconds(), //second
 "q+" : Math.floor((this.getMonth()+3)/3),  //quarter
 "S" : this.getMilliseconds() //millisecond
 }
 if(/(y+)/.test(format)) format=format.replace(RegExp.$1,
 (this.getFullYear()+"").substr(4 - RegExp.$1.length));
 for(var k in o)if(new RegExp("("+ k +")").test(format))
 format = format.replace(RegExp.$1,
 RegExp.$1.length==1 ? o[k] :
 ("00"+ o[k]).substr((""+ o[k]).length));
 return format;
}



function getDates(filters){
		var tab = filters.tab;
        var startTime = new Date(Date.parse(filters.startTime.replace(/-/g,  "/")));
        var endTime = new Date(Date.parse(filters.endTime.replace(/-/g,  "/")));
        var length = 0;   //日期跨度变量

        if( 0 == tab ) {
            length = (endTime.getTime() - startTime.getTime()) / (1000*24*60*60) + 1;
        } else if( 1 == tab ) {
            length = (endTime.getFullYear() - startTime.getFullYear()) * 12 + (endTime.getMonth() - startTime.getMonth()) + 1;
        } else {
            length = endTime.getFullYear() - startTime.getFullYear() + 1;
        }

        var xAxis = new Array(length);
        xAxis[0] = filters.startTime;
        for( var i = 1; i < length; i++ ) {
            if( 0 == tab ) {
                startTime.setDate( startTime.getDate() + 1 );
                xAxis[i] = startTime.format("yyyy-MM-dd");
            } else if( 1 == tab ) {
                startTime.setMonth( startTime.getMonth() + 1 );
                xAxis[i] = startTime.format("yyyy-MM");
            } else {
                startTime.setFullYear( startTime.getFullYear() + 1 );
                xAxis[i] = startTime.format("yyyy");
            }
        }

        return xAxis;

}



window.onload = function () {
 	var needDate={
 	    "startTime":"2018-06-18",
 		"endTime":"2018-10-06",
 		"tab":0
 	}
 	var date=getDates(needDate);
	var y = 100;    
	var data = [];
	var dataSeries = { type: "line" };
	var dataPoints = [];

	for (var i = 0; i < date.length; i += 1) {
		y += Math.round(Math.random() * 10 - 5);
		dataPoints.push({
			x: new Date(dat),
			y: y
		});
	}
	dataSeries.dataPoints = dataPoints;
	data.push(dataSeries);
 
//Better to construct options first and then pass it as a parameter
	var options = {
		zoomEnabled: true,
		animationEnabled: true,
		title: {
			text: "EventLine Title"
		},
		axisX:{
			valueFormatString:"DD MMM,YY"
		},
		axisY: {
			includeZero: false,
			lineThickness: 1
		},
		data: data  // random data
    };
 
var chart = new CanvasJS.Chart("chartContainer", options);
var startTime = new Date();
chart.render();
var endTime = new Date();
document.getElementById("timeToRender").innerHTML = "Time to Render: " + (endTime - startTime) + "ms";
 
}