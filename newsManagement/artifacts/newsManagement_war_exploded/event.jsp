<%--
  Created by IntelliJ IDEA.
  User: Dell
  Date: 2018/10/18
  Time: 21:10
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html><%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="/static/css/1.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="image/png" href="/static/template/assets/images/icon/favicon.ico">
    <link rel="stylesheet" href="/static/template/assets/css/bootstrap.min.css">
    <link rel="stylesheet" href="/static/template/assets/css/font-awesome.min.css">
    <link rel="stylesheet" href="/static/template/assets/css/themify-icons.css">
    <link rel="stylesheet" href="/static/template/assets/css/metisMenu.css">
    <link rel="stylesheet" href="/static/template/assets/css/owl.carousel.min.css">
    <link rel="stylesheet" href="/static/template/assets/css/slicknav.min.css">
    <!-- amcharts css -->
    <link rel="stylesheet" href="https://www.amcharts.com/lib/3/plugins/export/export.css" type="text/css" media="all" />
    <!-- Start datatable css -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.18/css/dataTables.bootstrap4.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/responsive/2.2.3/css/responsive.bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/responsive/2.2.3/css/responsive.jqueryui.min.css">
    <!-- style css -->
    <link rel="stylesheet" href="/static/template/assets/css/typography.css">
    <link rel="stylesheet" href="/static/template/assets/css/default-css.css">
    <link rel="stylesheet" href="/static/template/assets/css/styles.css">
    <link rel="stylesheet" href="/static/template/assets/css/responsive.css">
    <!-- modernizr css -->
    <script src="/static/template/assets/js/vendor/modernizr-2.8.3.min.js"></script>
    <script src="/static/js/jquery-1.11.1.min.js"></script>
    <script src="/static/js/jquery.canvasjs.min.js"></script>
    <script src="/static/js/cytoscape.min.js"></script>

    <script src="/static/js/wordcloud2.js"></script>
    <script src="/static/js/highcharts.js"></script>
    <script src="/static/js/exporting.js"></script>
    <script src="/static/js/oldie.js"></script>
    <script src="/static/js/wordcloud.js"></script>
</head>
<script>

    $(function(){
        function getuuid() {
            var s = [];
            var hexDigits = "0123456789abcdef";
            for (var i = 0; i < 36; i++) {
                s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
            }
            s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
            s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
            s[8] = s[13] = s[18] = s[23] = "-";

            var uuid = s.join("");
            return uuid;
        }
        function GetQueryString(name)
        {
            var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
            var r = window.location.search.substr(1).match(reg);//search,查询？后面的参数，并匹配正则
            if(r!=null)return  unescape(r[2]); return null;
        }
        $.ajax(
            {
                type:"get",
                url:"/news_event.action?eventId="+GetQueryString("eventId"),
                data:{
                    
                },
                success:function (da) {
                    var news=da.result.news;
                    for(var i=0;i<news.length;i++){
                        var tbody=document.getElementsByTagName("tbody")[0]
                        var tr=document.createElement("tr")
                        tbody.appendChild(tr);
                        var td1=document.createElement("td")
                        td1.innerText=news[i].newsTitle
                        tr.appendChild(td1)
                        var td2=document.createElement("td")
                        td2.innerText=news[i].newsTime
                        tr.appendChild(td2)
                    }
                    var scape={};
                    scape.container=document.getElementById('cy');
                    scape.style=[
                        { selector: 'node[label = "EventNode"]',
                            css: {'background-color': '#6FB1FC', 'content': 'data(name)'}
                        },
                        { selector: 'node[label = "EntityNode"]',
                            css: {'background-color': '#F5A45D', 'content': 'data(title)'}
                        },
                        { selector: 'edge',
                            css: {'content': 'data(relationship)', 'target-arrow-shape': 'triangle'}
                        }
                    ];
                    scape.layout={ name: 'breadthfirst'}
                    scape.elements={};
                    scape.elements.nodes=[];
                    scape.elements.edges=[];
                    var eventdata={};
                    eventdata.data={};
                    eventdata.data.id="00000000";
                    eventdata.data.name=da.eventId;
                    eventdata.data.label="EventNode"
                    scape.elements.nodes.push(eventdata)
                    var entities=da.result.entities
                    for(var i=0;i<entities.length;i++){
                        var entitydata={};
                        var edge={};
                        entitydata.data={};
                        edge.data={}
                        var uuid=getuuid();
                        entitydata.data.id=uuid;
                        entitydata.data.title=entities[i];
                        entitydata.data.label="EntityNode";
                        scape.elements.nodes.push(entitydata)
                        edge.data.source="00000000";
                        edge.data.target=uuid;
                        edge.data.relationship='related';
                        scape.elements.edges.push(edge)
                    }

                    cytoscape(scape);
                    //词云
                    var keyword=da.result.keywords;
                    var t=[];
                    for(var i=0;i<keyword.length;i++){
                        var obj={};
                        obj.name=keyword[i][0]

                        obj.weight=keyword[i][1]
                        t.push(obj)
                    }
                    Highcharts.chart('container1', {
                        series: [{
                            type: 'wordcloud',
                            data: t
                        }],
                        title: {
                            text: '关键词云'
                        }
                    });
                    var entities=da.result.entities;
                    var tt=[];
                    for(var i=0;i<entities.length;i++){
                        var obj={};
                        obj.name=entities[i][0]

                        obj.weight=entities[i][1]
                        tt.push(obj)
                    }
                    Highcharts.chart('container2', {
                        series: [{
                            type: 'wordcloud',
                            data: tt
                        }],
                        title: {
                            text: '实体词云'
                        }
                    });
                },
                error:function () {
                    alert("系统异常，请稍后重试！")
                }
            }


        )

    });
</script>
<body>
<div class="whole_navigation">
    <div class="logo">
        <img src="/static/img/3.png">
    </div>
    <div class="navigation">
        <ul>
            <li><a id="current_a1" href=""><strong>首页</strong></a></li>
        </ul>
    </div>

</div>
<div class="whole_content">
    <div class="content">
        <div class="content_plat" style="height: 1200px">
            <div id="search2">
                <div class="card">
                    <div class="card-body">
                        <h4 class="header-title">事件包含新闻：</h4>
                        <div class="data-tables">
                            <table id="dataTable" class="text-center">
                                <thead class="bg-light text-capitalize">
                                <tr>
                                    <th>标题</th>
                                    <th>时间</th>
                                </tr>
                                </thead>
                                <tbody>

                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                <div style="width: 1080px; ">
                    <div class="row" style="margin-top: 40px">
                        <div class="col-lg-12">
                            <div class="card">
                                <div class="card-header">
                                    <h4>事件信息</h4>
                                </div>
                                <div class="card-body">
                                    <div class="default-tab">
                                        <nav>
                                            <div class="nav nav-tabs" id="nav-tab" role="tablist">
                                                <a class="nav-item nav-link active" id="nav-home-tab" data-toggle="tab" href="#nav-home" role="tab" aria-controls="nav-home"
                                                   aria-selected="true">事件实体</a>
                                                <a class="nav-item nav-link" id="nav-contact-tab" data-toggle="tab" href="#nav-contact" role="tab" aria-controls="nav-contact"
                                                   aria-selected="false">舆论聚合</a>
                                            </div>

                                        </nav>
                                        <div class="tab-content pl-3 pt-2" id="nav-tabContent">
                                            <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">
                                                <div class="row">
                                                    <div class="col-lg-12">
                                                        <div id="cy"></div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="tab-pane fade" id="nav-contact" role="tabpanel" aria-labelledbyaria-labelledby="nav-contact-tab">
                                                <div class="row">
                                                    <div class="col-lg-12">
                                                        <div  style="width: 1020px;background-color: #f9f9f9;">
                                                            <div id="container1" style="height: 270px;"></div>
                                                        </div>
                                                        <div  style="width: 1020px;background-color: #f9f9f9;">
                                                            <div id="container2" style="height:270px;"></div>
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

            </div>
        </div>

    </div>

</div>
<script src="/static/template/assets/js/vendor/jquery-2.2.4.min.js"></script>
<!-- bootstrap 4 js -->
<script src="/static/template/assets/js/popper.min.js"></script>
<script src="/static/template/assets/js/bootstrap.min.js"></script>
<script src="/static/template/assets/js/owl.carousel.min.js"></script>
<script src="/static/template/assets/js/metisMenu.min.js"></script>
<script src="/static/template/assets/js/jquery.slimscroll.min.js"></script>
<script src="/static/template/assets/js/jquery.slicknav.min.js"></script>

<!-- Start datatable js -->
<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js"></script>
<script src="https://cdn.datatables.net/1.10.18/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.10.18/js/dataTables.bootstrap4.min.js"></script>
<script src="https://cdn.datatables.net/responsive/2.2.3/js/dataTables.responsive.min.js"></script>
<script src="https://cdn.datatables.net/responsive/2.2.3/js/responsive.bootstrap.min.js"></script>
<!-- others plugins -->
<script src="/static/template/assets/js/plugins.js"></script>
<script src="/static/template/assets/js/scripts.js"></script>

</body>
</html>
