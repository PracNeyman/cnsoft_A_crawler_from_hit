import requests
import re
from redis import Redis

url = 'http://www.kuaidaili.com/free/inha/2/'
text = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=device-width,initial-scale=1.0, maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
<title>国内高匿免费HTTP代理IP - 快代理</title>

<meta name="keywords" content="高匿代理,国内代理,代理服务器,免费代理服务器,代理ip,ip代理,高匿代理ip,免费代理,免费代理ip" />
<meta name="description" content="快代理专业为您提供国内高匿免费HTTP代理服务器。" />


<link rel="stylesheet" href="http://img.kuaidaili.com/css/all.css?v=14" media="screen" />

<style>
    .tag_area2 { margin:10px 0 0px 0; text-align: left; }
    .tag_area2 .label { background-color:#c1c1bf;text-decoration:none; font-size:13px; padding:3px 5px 3px 5px;}
    .tag_area2 .label.active, .tag_area2 .label.active:hover { background-color:#468847; }
    .tag_area2 .label:hover { background-color:#aaa; }
    tbody a { color:#777; }
    tbody a:hover { text-decoration:none; }
</style>


<meta name="renderer" content="webkit">
<meta name="baidu-site-verification" content="AO3Q6dKj9R" />
<meta name="sogou_site_verification" content="9ELczs5cQc"/>
<meta name="360-site-verification" content="feeadcad97dd7093f9abb1ee5285f031" />
</head>

<body>
<div class="body">
<!--start header-->

    <!--PC端header-->
    <div id="navigationBar" class="topnav topnav-has" style="z-index: 1000;">
        <div class="navigation-inner">
            <div class="logo">
                <h1>
                    <a href="/" class="logo-img">
                        <img class="logo-lit" src="http://img.kuaidaili.com/img/kdl-logo.png" alt="">
                    </a>
                </h1>
            </div>
            <div class="categories" id="nav-con">
                <ul class="menu">
                    <li id="menu_free" class="presentation">
                        <h2><a href="/free/">免费代理</a></h2>
                    </li>
                    <li id="menu_pricing" class="presentation">
                        <h2><a href="/pricing/">购买代理</a></h2>
                    </li>
                    <li id="menu_ops" class="presentation">
                        <h2><a href="/ops/">开放代理</a></h2>
                    </li>
                    <li id="menu_dps" class="presentation has-menu">
                        <h2><a href="/dps/">私密代理</a></h2>
                    </li>
                    <li id="menu_kps" class="presentation">
                        <h2><a href="/kps/">独享代理</a></h2></h2>
                    </li>
                    <li id="menu_fetch" class="presentation has-menu">
                        <h2><a href="/fetch/">代理提取</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="/fetch/">提取开放代理</a></li>
                                <li><a href="/dps/fetch/">提取私密代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_apidoc" class="presentation has-menu">
                        <h2><a href="/apidoc/">API接口</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="/apidoc/">开放代理API</a></li>
                                <li><a href="/dps/apidoc/">私密代理API</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_help" class="presentation has-menu">
                        <h2><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></h2>
                    </li>
                </ul>
            </div>
            <div class="operation">
                <span class="unlogin">
                    <a href="/login/" class="qc-btn link-dl"><span>登录</span></a>
                    <span class="stick">|</span>
                    <a href="/regist/" class="qc-btn link-dl"><span>注册</span></a>
                </span>
                <a href="/usercenter/" class="qc-btn link-name welcome-link"><span class="welcome"></span></a>
                <a href="/usercenter/" class="qc-btn link-mc"><span>会员中心</span></a><span id="noti"></span>
            </div>
        </div>
    </div>

    <!--手机端header-->
    <div id="navigationMobileBar" class="topnav-m topnav-m-has" style="z-index: 101;">
        <div class="navigation-inner" id="navDefault" style="transition: left 0s ease-in-out; transform: translateZ(0px); position: absolute; width: 100%; left: 0px;">
            <div class="navigation-bar m-nav-1" id="navigation-bar">
                <div class="area-left">
                    <div class="logo">
                        <h1>
                            <a href="/" class="logo-img">
                                <img class="logo-lit" src="http://img.kuaidaili.com/img/kdl-logo.png" alt="">
                                <img class="logo-dark" src="http://img.kuaidaili.com/img/kdl-logo.png" alt="">
                            </a>
                        </h1>
                    </div>
                </div>
                <div class="area-right">
                    <a href="javascript:;" class="nav-mobile-button m-more">
                        <span class="button-img"></span>
                    </a>
                    <a href="javascript:;" class="nav-mobile-button m-close">
                        <span class="button-img"></span>
                    </a>
                </div>
            </div>
            <div class="categories-mobile" id="navDefaultSub" style="opacity: 0; transition: opacity 0.4s ease-in-out; transform: translateZ(0px); display: none;">
                <ul id="m_top_menu" class="menu">
                    <li class="presentation nav-right"><h2><a href="/free/">免费代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/pricing/">购买代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/ops/">开放代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/dps/">私密代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/kps/">独享代理</a></h2></li>
                    <li class="presentation nav-down">
                        <h2><a href="javascript:void(0);">代理提取</a></h2>
                        <div class="nav-down-menu" style="display: none;">
                            <ul class="nav-down-menu-detail">
                                <li><a class="title" href="/dps/fetch/">提取私密代理</a></li>
                                <li><a class="title" href="/fetch/">提取开放代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="presentation nav-down">
                        <h2><a href="javascript:void(0);">API接口</a></h2>
                        <div class="nav-down-menu" style="display: none;">
                            <ul class="nav-down-menu-detail">
                                <li><a class="title" href="/dps/apidoc/">私密代理API</a></li>
                                <li><a class="title" href="/apidoc/">开放代理API</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="presentation nav-right"><h2><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></h2></li>
                </ul>
                <ul class="op">
                    <li><a href="/usercenter/" class="op-btn btn-style-2">会员中心</a></li>
                </ul>
                <div class="sign-in">
                    <a href="/usercenter/"class="sign-in-links welcome-link"><span class="welcome"></span></a>
                    <span class="unlogin">
                        <a id="m_login_btn" href="/login/" class="sign-in-links">登录</a>
                        <span class="stick">|</span>
                        <a id="m_opt_btn" href="/regist/" class="sign-in-links">注册</a>
                    </span>
                </div>
                <div class="contact">
                    <a href="tel:4000580638" class="ct-num">
                        <i class="icon"></i>
                        <span>400-058-0638</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

<!--end header-->


<div id="content">



<div class="con-pt"></div>
<div class="con-body">
<div>
    <div class="tag_area2" >
        <a id="tag_inha" class="label" href="/free/inha/">国内高匿代理</a> 
        <a id="tag_intr" class="label" href="/free/intr/">国内普通代理</a> 

        <span class="buy"><a href="/pricing/">购买更多代理>></a></span>
    </div>

    <div id="list" style="margin-top:15px;">
        <table class="table table-bordered table-striped">
          <thead>
              <tr>
                <th>IP</th>
                <th>PORT</th>
                <th>匿名度</th>
                <th>类型</th>
                <th>位置</th>
                <th>响应速度</th>
                <th>最后验证时间</th>
              </tr>
            </thead>
            <tbody>

                <tr>
                    <td data-title="IP">121.232.147.42</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2017-09-03 17:35:19</td>
                </tr>

                <tr>
                    <td data-title="IP">116.28.111.14</td>
                    <td data-title="PORT">808</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 广东省 中山市 电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2017-09-03 16:35:19</td>
                </tr>

                <tr>
                    <td data-title="IP">121.232.147.159</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2017-09-03 15:35:23</td>
                </tr>

                <tr>
                    <td data-title="IP">121.232.144.101</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2017-09-03 14:35:14</td>
                </tr>

                <tr>
                    <td data-title="IP">121.232.148.141</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-03 13:35:02</td>
                </tr>

                <tr>
                    <td data-title="IP">118.117.138.167</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2017-09-03 12:35:05</td>
                </tr>

                <tr>
                    <td data-title="IP">121.232.145.15</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-03 11:34:37</td>
                </tr>

                <tr>
                    <td data-title="IP">182.129.241.103</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2017-09-03 10:34:44</td>
                </tr>

                <tr>
                    <td data-title="IP">222.208.67.56</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2017-09-03 09:34:56</td>
                </tr>

                <tr>
                    <td data-title="IP">125.67.73.243</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">0.8秒</td>
                    <td data-title="最后验证时间">2017-09-03 08:35:15</td>
                </tr>

                <tr>
                    <td data-title="IP">121.232.148.97</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">0.4秒</td>
                    <td data-title="最后验证时间">2017-09-03 07:35:08</td>
                </tr>

                <tr>
                    <td data-title="IP">121.232.146.253</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">0.9秒</td>
                    <td data-title="最后验证时间">2017-09-03 06:35:10</td>
                </tr>

                <tr>
                    <td data-title="IP">182.129.248.79</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-03 05:34:36</td>
                </tr>

                <tr>
                    <td data-title="IP">60.214.154.2</td>
                    <td data-title="PORT">53281</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 山东省 枣庄市 联通</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-03 04:35:10</td>
                </tr>

                <tr>
                    <td data-title="IP">117.90.6.70</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">0.5秒</td>
                    <td data-title="最后验证时间">2017-09-03 03:35:08</td>
                </tr>

            </tbody>
        </table>
        <p>注：表中响应速度是中国测速服务器的测试数据，仅供参考。响应速度根据你机器所在的地理位置不同而有差异。</p>

        <div id="listnav">
        <ul><li>第</li><li><a href="/free/inha/1/">1</a></li><li><a href="/free/inha/2/" class="active">2</a></li><li><a href="/free/inha/3/">3</a></li><li><a href="/free/inha/4/">4</a></li><li><a href="/free/inha/5/">5</a></li><li><a href="/free/inha/6/">6</a></li><li>...</li><li><a href="/free/inha/1810/">1810</a></li><li><a href="/free/inha/1811/">1811</a></li><li>页</li></ul>
        </div>

        <div class="btn center be-f"><a id="tobuy" href="/pricing/" target="_blank">购买更多代理</a></div>
    </div>
</div>
</div>

</div>


<div class="footer">
    <div class="con-body clearfix">
        <div class="footer-left">
            <a href="/" class="logo-link"><img height="35" src="/img/footer-logo.png"/></a>
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a><span>|</span></li>
            <li><a href="http://help.kuaidaili.com/contract/" target="_blank">服务条款</a><span>|</span></li>
            <li><a href="http://help.kuaidaili.com/law/" target="_blank">法律声明</a><span>|</span></li>
            <li><a href="/sitemap.xml">网站地图</a><span>|</span></li>
            <li><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></li>
        </ul>
        <p class="foot-owner">© 2013-2017 Kuaidaili.com 版权所有 <a href="http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action" target="_blank">京ICP备16054786号</a></p>
        </div>
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
            <a class="safe02" href="http://webscan.360.cn/index/checkwebsite/url/www.kuaidaili.com" target="_blank"></a>
        </div>
    </div>
</div>
<div class="m-footer">
    <div class="con-body">
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a></li>
            <li><a href="http://help.kuaidaili.com/contract/" target="_blank">服务条款</a></li>
            <li><a href="http://help.kuaidaili.com/law/" target="_blank">法律声明</a></li>
            <li><a href="/sitemap.xml">网站地图</a></li>
            <li><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></li>
        </ul>
        <p class="foot-owner">©2013-2017 Kuaidaili.com 版权所有</p>
        <a class="foot-owner">京ICP备16054786号</a>
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
            <a class="safe02" href="http://webscan.360.cn/index/checkwebsite/url/www.kuaidaili.com" target="_blank"></a>
        </div>
    </div>
</div>
<div id="mNavMask" style="position: fixed; top: 0px; left: 0px; bottom: 0; right: 0; width: 100%; z-index: 100; height: 100%; display: none; background: rgba(0, 0, 0, 0.74902);"></div>
<ul class="onMShow">
    <li>

    <a class="online-chat" href="javascript:void(0);"><br>

            <span class="bt3"></span>
            <div class="two">在线咨询QQ: 3255904996<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="tel:4000580638"><br>
            <span class="bt2"></span>
            <div class="two">客服电话：400-058-0638<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="/support/"><br>
            <span class="bt1"></span>
            <div>提交工单</div>
        </a>
    </li>
</ul>
<a href="javascript:void(0);" id="top_btn" class="label btt" style="display:none;"><span class="btn-top"></span></a>

</div>


<script type="text/javascript" src="http://img.kuaidaili.com/js/all.js?v=2"></script>

<script type="text/javascript">
$("#tag_inha").addClass("active")
$(document).ready(function() {
});
</script>

<script type="text/javascript">
var chat_url = "https://static.meiqia.com/dist/standalone.html?_=t&eid=72194";
$(document).ready(function() {
    $('.online-chat').click(function () {
        if($.os.ios || $.os.android){
            window.open(chat_url);
        }
        else{
            var from_left = document.documentElement.clientWidth - 760;
            var from_top = 300;
            if (window.screen.height < 1000) from_top = 200;
            window.open(chat_url, "_blank", "location=0, status=0, left="+from_left+", top="+from_top+", width=700, height=540");
        }
    });
});
</script>
<script type="text/javascript">
var menu = "menu_free";
if(menu) $('#'+menu).addClass('active');
var ucm = "";
if(ucm){
    $('#ucm_'+ucm).addClass('active');
    $('#ucm_'+ucm+' a i').addClass('icon-white');
}

var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?7ed65b1cc4b810e9fd37959c9bb51b31";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','http://img.kuaidaili.com/ga/ga.js','ga');
ga('create', 'UA-76097251-1', 'auto');
ga('send', 'pageview');

</script>




<!--[if lt IE 9]><link rel="stylesheet" href="http://img.kuaidaili.com/css/ie.css?v=9" media="screen" /><![endif]-->
</body>
</html>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="format-detection" content="telephone=no">
<meta name="viewport" content="width=device-width,initial-scale=1.0, maximum-scale=1.0,minimum-scale=1.0,user-scalable=no">
<title>国内高匿免费HTTP代理IP - 快代理</title>

<meta name="keywords" content="高匿代理,国内代理,代理服务器,免费代理服务器,代理ip,ip代理,高匿代理ip,免费代理,免费代理ip" />
<meta name="description" content="快代理专业为您提供国内高匿免费HTTP代理服务器。" />


<link rel="stylesheet" href="http://img.kuaidaili.com/css/all.css?v=14" media="screen" />

<style>
    .tag_area2 { margin:10px 0 0px 0; text-align: left; }
    .tag_area2 .label { background-color:#c1c1bf;text-decoration:none; font-size:13px; padding:3px 5px 3px 5px;}
    .tag_area2 .label.active, .tag_area2 .label.active:hover { background-color:#468847; }
    .tag_area2 .label:hover { background-color:#aaa; }
    tbody a { color:#777; }
    tbody a:hover { text-decoration:none; }
</style>


<meta name="renderer" content="webkit">
<meta name="baidu-site-verification" content="AO3Q6dKj9R" />
<meta name="sogou_site_verification" content="9ELczs5cQc"/>
<meta name="360-site-verification" content="feeadcad97dd7093f9abb1ee5285f031" />
</head>

<body>
<div class="body">
<!--start header-->

    <!--PC端header-->
    <div id="navigationBar" class="topnav topnav-has" style="z-index: 1000;">
        <div class="navigation-inner">
            <div class="logo">
                <h1>
                    <a href="/" class="logo-img">
                        <img class="logo-lit" src="http://img.kuaidaili.com/img/kdl-logo.png" alt="">
                    </a>
                </h1>
            </div>
            <div class="categories" id="nav-con">
                <ul class="menu">
                    <li id="menu_free" class="presentation">
                        <h2><a href="/free/">免费代理</a></h2>
                    </li>
                    <li id="menu_pricing" class="presentation">
                        <h2><a href="/pricing/">购买代理</a></h2>
                    </li>
                    <li id="menu_ops" class="presentation">
                        <h2><a href="/ops/">开放代理</a></h2>
                    </li>
                    <li id="menu_dps" class="presentation has-menu">
                        <h2><a href="/dps/">私密代理</a></h2>
                    </li>
                    <li id="menu_kps" class="presentation">
                        <h2><a href="/kps/">独享代理</a></h2></h2>
                    </li>
                    <li id="menu_fetch" class="presentation has-menu">
                        <h2><a href="/fetch/">代理提取</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="/fetch/">提取开放代理</a></li>
                                <li><a href="/dps/fetch/">提取私密代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_apidoc" class="presentation has-menu">
                        <h2><a href="/apidoc/">API接口</a></h2>
                        <div class="menu-list">
                            <ul>
                                <li><a href="/apidoc/">开放代理API</a></li>
                                <li><a href="/dps/apidoc/">私密代理API</a></li>
                            </ul>
                        </div>
                    </li>
                    <li id="menu_help" class="presentation has-menu">
                        <h2><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></h2>
                    </li>
                </ul>
            </div>
            <div class="operation">
                <span class="unlogin">
                    <a href="/login/" class="qc-btn link-dl"><span>登录</span></a>
                    <span class="stick">|</span>
                    <a href="/regist/" class="qc-btn link-dl"><span>注册</span></a>
                </span>
                <a href="/usercenter/" class="qc-btn link-name welcome-link"><span class="welcome"></span></a>
                <a href="/usercenter/" class="qc-btn link-mc"><span>会员中心</span></a><span id="noti"></span>
            </div>
        </div>
    </div>

    <!--手机端header-->
    <div id="navigationMobileBar" class="topnav-m topnav-m-has" style="z-index: 101;">
        <div class="navigation-inner" id="navDefault" style="transition: left 0s ease-in-out; transform: translateZ(0px); position: absolute; width: 100%; left: 0px;">
            <div class="navigation-bar m-nav-1" id="navigation-bar">
                <div class="area-left">
                    <div class="logo">
                        <h1>
                            <a href="/" class="logo-img">
                                <img class="logo-lit" src="http://img.kuaidaili.com/img/kdl-logo.png" alt="">
                                <img class="logo-dark" src="http://img.kuaidaili.com/img/kdl-logo.png" alt="">
                            </a>
                        </h1>
                    </div>
                </div>
                <div class="area-right">
                    <a href="javascript:;" class="nav-mobile-button m-more">
                        <span class="button-img"></span>
                    </a>
                    <a href="javascript:;" class="nav-mobile-button m-close">
                        <span class="button-img"></span>
                    </a>
                </div>
            </div>
            <div class="categories-mobile" id="navDefaultSub" style="opacity: 0; transition: opacity 0.4s ease-in-out; transform: translateZ(0px); display: none;">
                <ul id="m_top_menu" class="menu">
                    <li class="presentation nav-right"><h2><a href="/free/">免费代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/pricing/">购买代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/ops/">开放代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/dps/">私密代理</a></h2></li>
                    <li class="presentation nav-right"><h2><a href="/kps/">独享代理</a></h2></li>
                    <li class="presentation nav-down">
                        <h2><a href="javascript:void(0);">代理提取</a></h2>
                        <div class="nav-down-menu" style="display: none;">
                            <ul class="nav-down-menu-detail">
                                <li><a class="title" href="/dps/fetch/">提取私密代理</a></li>
                                <li><a class="title" href="/fetch/">提取开放代理</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="presentation nav-down">
                        <h2><a href="javascript:void(0);">API接口</a></h2>
                        <div class="nav-down-menu" style="display: none;">
                            <ul class="nav-down-menu-detail">
                                <li><a class="title" href="/dps/apidoc/">私密代理API</a></li>
                                <li><a class="title" href="/apidoc/">开放代理API</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="presentation nav-right"><h2><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></h2></li>
                </ul>
                <ul class="op">
                    <li><a href="/usercenter/" class="op-btn btn-style-2">会员中心</a></li>
                </ul>
                <div class="sign-in">
                    <a href="/usercenter/"class="sign-in-links welcome-link"><span class="welcome"></span></a>
                    <span class="unlogin">
                        <a id="m_login_btn" href="/login/" class="sign-in-links">登录</a>
                        <span class="stick">|</span>
                        <a id="m_opt_btn" href="/regist/" class="sign-in-links">注册</a>
                    </span>
                </div>
                <div class="contact">
                    <a href="tel:4000580638" class="ct-num">
                        <i class="icon"></i>
                        <span>400-058-0638</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

<!--end header-->


<div id="content">



<div class="con-pt"></div>
<div class="con-body">
<div>
    <div class="tag_area2" >
        <a id="tag_inha" class="label" href="/free/inha/">国内高匿代理</a> 
        <a id="tag_intr" class="label" href="/free/intr/">国内普通代理</a> 

        <span class="buy"><a href="/pricing/">购买更多代理>></a></span>
    </div>

    <div id="list" style="margin-top:15px;">
        <table class="table table-bordered table-striped">
          <thead>
              <tr>
                <th>IP</th>
                <th>PORT</th>
                <th>匿名度</th>
                <th>类型</th>
                <th>位置</th>
                <th>响应速度</th>
                <th>最后验证时间</th>
              </tr>
            </thead>
            <tbody>
                
                <tr>
                    <td data-title="IP">121.232.147.92</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2017-09-05 03:35:51</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.232.146.42</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">0.4秒</td>
                    <td data-title="最后验证时间">2017-09-05 02:35:32</td>
                </tr>
                
                <tr>
                    <td data-title="IP">182.42.36.100</td>
                    <td data-title="PORT">808</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 山东省 烟台市 电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2017-09-05 01:35:34</td>
                </tr>
                
                <tr>
                    <td data-title="IP">117.90.1.45</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">0.5秒</td>
                    <td data-title="最后验证时间">2017-09-05 00:35:40</td>
                </tr>
                
                <tr>
                    <td data-title="IP">182.129.242.35</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-04 23:35:38</td>
                </tr>
                
                <tr>
                    <td data-title="IP">111.155.116.217</td>
                    <td data-title="PORT">8123</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 陕西省  铁通</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-04 22:35:37</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.232.145.32</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2017-09-04 21:35:43</td>
                </tr>
                
                <tr>
                    <td data-title="IP">171.215.236.55</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-04 20:35:40</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.232.146.159</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-04 19:35:35</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.232.146.107</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">3秒</td>
                    <td data-title="最后验证时间">2017-09-04 18:35:40</td>
                </tr>
                
                <tr>
                    <td data-title="IP">61.157.198.66</td>
                    <td data-title="PORT">8080</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">四川省内江市 电信</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2017-09-04 17:35:43</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.232.147.4</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 江苏省 镇江市 电信</td>
                    <td data-title="响应速度">1.0秒</td>
                    <td data-title="最后验证时间">2017-09-04 16:35:33</td>
                </tr>
                
                <tr>
                    <td data-title="IP">110.73.6.125</td>
                    <td data-title="PORT">8123</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">广西壮族自治区南宁市  联通</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2017-09-04 15:35:44</td>
                </tr>
                
                <tr>
                    <td data-title="IP">182.129.241.84</td>
                    <td data-title="PORT">9000</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 四川省 遂宁市 电信</td>
                    <td data-title="响应速度">1秒</td>
                    <td data-title="最后验证时间">2017-09-04 14:35:32</td>
                </tr>
                
                <tr>
                    <td data-title="IP">121.40.208.69</td>
                    <td data-title="PORT">1080</td>
                    <td data-title="匿名度">高匿名</td>
                    <td data-title="类型">HTTP</td>
                    <td data-title="位置">中国 浙江省 杭州市 阿里云</td>
                    <td data-title="响应速度">2秒</td>
                    <td data-title="最后验证时间">2017-09-04 13:35:33</td>
                </tr>
                
            </tbody>
        </table>
        <p>注：表中响应速度是中国测速服务器的测试数据，仅供参考。响应速度根据你机器所在的地理位置不同而有差异。</p>

        <div id="listnav">
        <ul><li>第</li><li><a href="/free/inha/1/" class="active">1</a></li><li><a href="/free/inha/2/">2</a></li><li><a href="/free/inha/3/">3</a></li><li><a href="/free/inha/4/">4</a></li><li><a href="/free/inha/5/">5</a></li><li>...</li><li><a href="/free/inha/1811/">1811</a></li><li><a href="/free/inha/1812/">1812</a></li><li>页</li></ul>
        </div>

        <div class="btn center be-f"><a id="tobuy" href="/pricing/" target="_blank">购买更多代理</a></div>
    </div>
</div>
</div>

</div>


<div class="footer">
    <div class="con-body clearfix">
        <div class="footer-left">
            <a href="/" class="logo-link"><img height="35" src="/img/footer-logo.png"/></a>
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a><span>|</span></li>
            <li><a href="http://help.kuaidaili.com/contract/" target="_blank">服务条款</a><span>|</span></li>
            <li><a href="http://help.kuaidaili.com/law/" target="_blank">法律声明</a><span>|</span></li>
            <li><a href="/sitemap.xml">网站地图</a><span>|</span></li>
            <li><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></li>
        </ul>
        <p class="foot-owner">© 2013-2017 Kuaidaili.com 版权所有 <a href="http://www.miitbeian.gov.cn/state/outPortal/loginPortal.action" target="_blank">京ICP备16054786号</a></p>
        </div>
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
            <a class="safe02" href="http://webscan.360.cn/index/checkwebsite/url/www.kuaidaili.com" target="_blank"></a>
        </div>
    </div>
</div>
<div class="m-footer">
    <div class="con-body">
        <ul class="foot-link clearfix">
            <li><a href="/about/">关于我们</a></li>
            <li><a href="http://help.kuaidaili.com/contract/" target="_blank">服务条款</a></li>
            <li><a href="http://help.kuaidaili.com/law/" target="_blank">法律声明</a></li>
            <li><a href="/sitemap.xml">网站地图</a></li>
            <li><a href="http://help.kuaidaili.com" target="_blank">帮助中心</a></li>
        </ul>
        <p class="foot-owner">©2013-2017 Kuaidaili.com 版权所有</p>
        <a class="foot-owner">京ICP备16054786号</a>
        <div class="foot-safe clearfix">
            <a class="safe01" href="https://ss.knet.cn/verifyseal.dll?sn=e161117110108652324qkr000000&ct=df&a=1&pa=0.3305956236561214" target="_blank"></a>
            <a class="safe02" href="http://webscan.360.cn/index/checkwebsite/url/www.kuaidaili.com" target="_blank"></a>
        </div>
    </div>
</div>
<div id="mNavMask" style="position: fixed; top: 0px; left: 0px; bottom: 0; right: 0; width: 100%; z-index: 100; height: 100%; display: none; background: rgba(0, 0, 0, 0.74902);"></div>
<ul class="onMShow">
    <li>
  
    <a class="online-chat" href="javascript:void(0);"><br>
  
            <span class="bt3"></span>
            <div class="two">在线咨询QQ: 3255904996<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="tel:4000580638"><br>
            <span class="bt2"></span>
            <div class="two">客服电话：400-058-0638<br>周一至周六 9:00-18:00</div>
        </a>
    </li>
    <li>
        <a href="/support/"><br>
            <span class="bt1"></span>
            <div>提交工单</div>
        </a>
    </li>
</ul>
<a href="javascript:void(0);" id="top_btn" class="label btt" style="display:none;"><span class="btn-top"></span></a>

</div>


<script type="text/javascript" src="http://img.kuaidaili.com/js/all.js?v=2"></script>

<script type="text/javascript">
$("#tag_inha").addClass("active")
$(document).ready(function() {
});
</script>

<script type="text/javascript">
var chat_url = "https://static.meiqia.com/dist/standalone.html?_=t&eid=72194";
$(document).ready(function() {
    $('.online-chat').click(function () {
        if($.os.ios || $.os.android){
            window.open(chat_url);
        }
        else{
            var from_left = document.documentElement.clientWidth - 760;
            var from_top = 300;
            if (window.screen.height < 1000) from_top = 200;
            window.open(chat_url, "_blank", "location=0, status=0, left="+from_left+", top="+from_top+", width=700, height=540");
        }
    });
});
</script>
<script type="text/javascript">
var menu = "menu_free";
if(menu) $('#'+menu).addClass('active');
var ucm = "";
if(ucm){
    $('#ucm_'+ucm).addClass('active');
    $('#ucm_'+ucm+' a i').addClass('icon-white');
}

var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?7ed65b1cc4b810e9fd37959c9bb51b31";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','http://img.kuaidaili.com/ga/ga.js','ga');
ga('create', 'UA-76097251-1', 'auto');
ga('send', 'pageview');

</script>




<!--[if lt IE 9]><link rel="stylesheet" href="http://img.kuaidaili.com/css/ie.css?v=9" media="screen" /><![endif]-->
</body>
</html>


"""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

r = Redis()
IPs = re.findall("<td data-title=\"IP\">(.*?)</td>", text)
for IP in IPs:
    print(IP)
    try:
        requests.get(url='http://www.baidu.com')
        print('OK')
        r.rpush('IPs', IP)
        print('success')
    except:
        continue
