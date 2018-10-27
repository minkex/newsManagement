<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html lang="zh-cn">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="/static/css/1.css">
    <!-- Fontfaces CSS-->
    <link href="/static/template/css/font-face.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/font-awesome-4.7/css/font-awesome.min.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/font-awesome-5/css/fontawesome-all.min.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/mdi-font/css/material-design-iconic-font.min.css" rel="stylesheet" media="all">

    <!-- Bootstrap CSS-->
    <link href="../../static/template/vendor/bootstrap-4.1/bootstrap.min.css" rel="stylesheet" media="all">

    <!-- Vendor CSS-->
    <link href="/static/template/vendor/animsition/animsition.min.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/bootstrap-progressbar/bootstrap-progressbar-3.3.4.min.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/wow/animate.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/css-hamburgers/hamburgers.min.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/slick/slick.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/select2/select2.min.css" rel="stylesheet" media="all">
    <link href="/static/template/vendor/perfect-scrollbar/perfect-scrollbar.css" rel="stylesheet" media="all">
    <link href="/static/template/css/theme.css" rel="stylesheet" media="all">
    <script src="/static/js/jquery-1.11.1.min.js"></script>
    <!--<script type="text/javascript" src="/static/js/1.js.jsp"></script>-->
</head>
<body>

<script>
    $(document).ready(function () {
        $.ajax(
            {
                type:"get",
                url:"/news.action?startTime=2018-01-01%2000:00:00%20&endTime=%202018-01-30%2023:59:59%20&limit=5",
                data:{

                },
                success:function (da) {
                    var data=[];
                    var eventlines=da.result.eventLines
                    for(var i=0;i<eventlines.length;i++ ){
                        var tbody=document.getElementsByTagName("tbody")[0];
                        var tr=document.createElement("tr")
                        tbody.appendChild(tr)
                        var td1=document.createElement("td")
                        td1.innerText=eventlines[i].eventlineTitle
                        var td2=document.createElement("td")
                        td2.innerText=eventlines[i].eventLineStartTime
                        var td3=document.createElement("td")
                        td3.innerText=eventlines[i].passion
                        var td4=document.createElement("td")
                        td4.innerText=eventlines[i].passionNow
                        var td5=document.createElement("td")
                        td5.setAttribute("class","text-right")
                        var a=document.createElement("a")
                        a.setAttribute("href","/eventline.jsp?eventlineId="+eventlines[i].eventLineId+"&startTime="+eventlines[i].eventLineStartTime)
                        a.setAttribute("class","a_post")
                        a.innerText="查看"
                        td5.appendChild(a)
                        tr.appendChild(td1)
                        tr.appendChild(td2)
                        tr.appendChild(td3)
                        tr.appendChild(td4)
                        tr.appendChild(td5)

                        var a={};
                        a.name=eventlines[i].eventlineTitle;
                        a.type="spline";
                        a.toolTipContent="{customPropperty}:{y}";
                        a.ValueFormatString="#0.## P";
                        a.showInLegend=true;
                        a.dataPoints=[];
                        var eventLineEvents=eventlines[i].eventLineEvents
                        for(var j=0;j<eventLineEvents.length;j++)
                        {
                            var datapoint={};
                            var startTime = new Date(eventLineEvents[j].eventStartTime);
                            var Startyear=startTime.getFullYear();
                            var Startmonth=startTime.getMonth();
                            var Startday=startTime.getDate();
                            var Starthour=startTime.getHours();
                            var Startminute=startTime.getMinutes();
                            datapoint.x=new Date(Startyear,Startmonth,Startday,Starthour,Startminute,0);
                            datapoint.y=parseInt(eventLineEvents[j].passion);
                            datapoint.customPropperty=eventLineEvents[j].eventTitle;
                            a.dataPoints.push(datapoint);
                        }
                        data.push(a)
                    }
                    var chart = new CanvasJS.Chart("chartContainer", {

                        animationEnabled: true,
                        title:{
                            text: "当前最热事件线趋势图"
                        },
                        axisX: {
                            valueFormatString: "YY-MM-DD HH:MM"
                        },
                        axisY: {
                            title: "文章数 (in P)",
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

                        }
                        else{
                            e.dataSeries.visible = true;
                        }
                        chart.render();
                    }

                },
                error:function () {
                    alert("系统异常，请稍后重试！")
                }

            }
        )

    })

</script>

<div class="whole_navigation">
    <div class="logo">
        <img src="../../static/img/3.png">
    </div>
    <div class="navigation">
        <ul>
            <li><a id="current_a1" href=""><strong>首页</strong></a></li>
        </ul>
    </div>

</div>
<div class="whole_content">
    <div class="content">
        <div class="content_plat">
            <div id="search2">
                <div class="menu">
                    <select>
                        <option>2018-08-31至2018-09-29</option>
                        <option></option>
                        <option></option>
                    </select>
                    <div class="key_search">
                        <input type="text" name="" placeholder="请输入关键词"/>
                        <i></i>
                    </div>
                </div>
                <div class="mutl_graph">
                    <div id="chartContainer" style="height: 370px; width: 100%;"></div>
                    <span id="timeToRender" style="display: block;"></span>
                </div>
                <div style="width: 1080px ">
                    <div class="main-content">
                        <div class="section__content section__content--p30">
                            <div class="container-fluid">
                                <div class="row">
                                    <div class="col-lg-12">
                                        <div class="table-responsive table--no-card m-b-30">
                                            <table class="table table-borderless table-striped table-earning">
                                                <thead>
                                                <tr>
                                                    <th>事件线</th>
                                                    <th>开始时间</th>
                                                    <th>总热度</th>
                                                    <th>当前热度</th>
                                                    <th class="text-right">操作</th>
                                                </tr>
                                                </thead>
                                                <tbody>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>

    </div>

</div>




<script src="/static/js/jquery.canvasjs.min.js"></script>
</body>
</html>