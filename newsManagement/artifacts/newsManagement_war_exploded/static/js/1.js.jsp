<script>

window.onload = function () {

    var array=new Array()
    var data=[];
<c:forEach items="${eventLines}" var="eventline" varStatus="status">
    for(var i=1;i<=1;i++)
    {
        var a={};
        a.name="${eventline.title}";
        a.type="spline";
        a.toolTipContent="{customPropperty}:{y}";
        a.ValueFormatString="#0.## P";
        a.showInLegend=true;
        a.dataPoints=[];

    <c:forEach items="${eventline.eventList}" var="event" varStatus="eventstatus">
        var datapoint={};
        var startTime = new Date("${event.startTime}");
        var Startyear=startTime.getFullYear();
        var Startmonth=startTime.getMonth();
        var Startday=startTime.getDate()-1;
        var Starthour=startTime.getHours();
        var Startminute=startTime.getMinutes();
        datapoint.x=new Date(Startyear,Startmonth,Startday,Starthour,Startminute,0);
        datapoint.y=parseInt("${event.passion}");
        datapoint.customPropperty="${event.title}";
        a.dataPoints.push(datapoint);
    </c:forEach>
        data.push(a)
    }

</c:forEach>
    alert(data[0].dataPoints[0].y)
    alert(data[0].dataPoints[1].y)


    var chart = new CanvasJS.Chart("chartContainer", {

        animationEnabled: true,
        title:{
            text: "Daily Event Line Trend"
        },
        axisX: {
            valueFormatString: "YY-MM-DD hh:mm"
        },
        axisY: {
            title: "Pages (in P)",
            includeZero: false,
            suffix: " P"
        },
        legend:{
            cursor: "pointer",
            fontSize: 16,
            itemclick: toggleDataSeries
        },
        toolTip:{
            shared: true
        },
        data: data
    });
    chart.render();

    function toggleDataSeries(e){
        if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
            e.dataSeries.visible = false;
            alert("hah")
        }
        else{
            e.dataSeries.visible = true;
        }
        chart.render();
    }

}
