<%--
  Created by IntelliJ IDEA.
  User: Dell
  Date: 2018/10/23
  Time: 13:47
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
    <script src="/static/js/jquery-1.11.1.min.js"></script>
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
</head>
<script>

</script>
<body>
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

</body>
<script src="/static/js/jquery.canvasjs.min.js"></script>
</html>
