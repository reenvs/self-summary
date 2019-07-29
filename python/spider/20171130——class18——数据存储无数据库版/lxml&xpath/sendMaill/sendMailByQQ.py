#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr,formataddr

def _format_addr(s):
    name,addr = parseaddr (s)
    print formataddr ((Header (name,'utf-8' ).encode(),addr))
    return formataddr ((Header (name,'utf-8' ).encode(),addr))

#创建发送的信息对象
message=MIMEText('''

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="save" content="history"/>
	<meta name="server" env="online" baike="239" ip="152"></meta>
	<meta name="keywords" content="网络知识 网络爬虫 搜索 SEO"></meta>
	<meta name="description" content="网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常被称为网页追逐者），是一种按照一定的规则，自动的抓取万维网信息的程序或者脚本，已被广泛应用于互联网领域。搜索引擎使用网络爬虫抓取Web网页、文档甚至图片、音频、视频等资源，通过相应的索引技术组织这些信息，提供给搜索用户进行查询。网络爬虫也为中小站点的推广提供了有效的途径。网络爬虫另外一些不常使用的名字还有蚂蚁，自动索引，模拟程序或者"></meta>

	<meta name="csrfToken5" content="b273a01ed8e72c2e1f1c9b4fc9af5934"></meta>
	
	
	<meta http-equiv="X-UA-Compatible" content="IE=edge"/>

	<meta http-equiv="x-dns-prefetch-control" content="on">
	<link rel="dns-prefetch" href="//cache.soso.com"/>
	<link rel="dns-prefetch" href="//pic.baike.soso.com"/>
	<link rel="dns-prefetch" href="//ugc.qpic.cn"/>
	<link rel="dns-prefetch" href="//xui.ptlogin2.qq.com"/>
	<link rel="dns-prefetch" href="//q1.qlogo.cn"/>
	<link rel="dns-prefetch" href="//q2.qlogo.cn"/>
	<link rel="dns-prefetch" href="//q3.qlogo.cn"/>
	<link rel="dns-prefetch" href="//q4.qlogo.cn"/>
	<link rel="dns-prefetch" href="//q.qlogo.cn"/>
	<link rel="dns-prefetch" href="//img01.sogoucdn.com"/>
	<link rel="dns-prefetch" href="//img02.sogoucdn.com"/>
	<link rel="dns-prefetch" href="//img03.sogoucdn.com"/>
	<link rel="dns-prefetch" href="//img04.sogoucdn.com"/>
	<!-- <meta http-equiv="X-UA-Compatible" content="IE=edge"/> -->
	<title>网络爬虫 - 搜狗百科</title>

	<!-- common css -->
	<link rel="stylesheet" href="//cache.soso.com/baike/css/baike_common_rev_201707281728.css" type="text/css" media="screen"/>

	<!-- page individual css -->
	
	<link rel="stylesheet" href="//cache.soso.com/baike/css/sgbk_lemma_base_201711102021.css" type="text/css" media="screen"/>

	<link rel="stylesheet" href="//cache.soso.com/baike/css/sgbk_lemma_module_201707261801.css" type="text/css" media="screen"/>

	<link rel="stylesheet" href="//cache.soso.com/baike/css/sgbk_lemma_type_module_201707261801.css" type="text/css" media="screen"/>


	<!-- common js definition -->
	<script language="javaScript" type="text/javascript" src="https://ui.ptlogin2.qq.com/js/ptloginout.js" ></script>
	<script type="text/javascript" src="//cache.soso.com/baike/js/main_201404021151.js"></script>

	<!-- javascript declaration -->
	
	<script type="text/javascript" src="//cache.soso.com/wenwen/js/wenwen_201401211126.js"></script>


	<link rel="Shortcut Icon" href="/favicon_new.ico"/>
	<link rel="Bookmark" href="/favicon_new.ico"/>


	<script type="text/javascript" src="//cache.soso.com/baike/js/sgbk-jq-1.8.3-20160526.min.js"></script>
	<script src="//cache.soso.com/deploy/js/lib/wenke/main.js"></script>

	<script>jQuery.noConflict();</script>

</head>


<body class="main_bg" onload="if((typeof sbjl=='undefined')||!sbjl.hasNS('proto')) mark(document.body);">
<script type="text/javascript"><!--

if (typeof Tapestry == 'undefined') document.write('<script type="text/javascript" src="//cache.soso.com/baike/js/Form.js"><\/script>');

// --></script>












		<div id="s_page">
			
	
		
	
			<div id="header">
				
	<div class="topnavbox">
		<ul class="topnav">
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">新闻</a></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">网页</a></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">微信</a></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">知乎</a></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">图片</a></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">视频</a></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">明医</a></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">英文</a></li>
			<!-- <li><a href="javascript:;" onclick="redirectToSogou(this);return false;">海外</a><span style="z-index: 1;background: url(//cache.soso.com/baike/i/ico_beta.png) no-repeat scroll 0 0;background-image: -webkit-image-set(url(//cache.soso.com/baike/i/ico_beta.png) 1x, url(//cache.soso.com/baike/i/ico_beta@2x.png) 2x);height: 15px;overflow: hidden;position:absolute;width: 23px;right: -8px;top: 0;"></span></li> -->
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">问问</a></li>
			<li class="cur"><strong>百科</strong></li>
			<li><a href="javascript:;" onclick="redirectToSogou(this);return false;">更多&gt;&gt;</a></li>
		</ul>
	</div>

		     	<a href="/LLogout.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=5&amp;sp=l77860" style="display:none" id="logoutA">true</a>
				


    <div class="login_mod">
        <ul>
            
            
                <li><a id="s_login" href="#" onclick="stget('c.denglu.login', 'baike');DT.reportCLK('c.denglu.login');WKSSO.doLogin();return false;">登录</a></li>
            
        </ul>
    </div>


		        
				<style>
    .search_logo{
        display: block;
        width: 130px;
        height: 34px;
        background: none;
        text-indent: 0;
    }
    .topnav-beta{
        z-index: 1;
        height: 15px;
        overflow: hidden;
        position:absolute;
        width: 23px;
        right: -8px;
        top: 0;
    }
    .topnav-beta img{
        vertical-align: top;
    }
</style>



    <div class="searchbox">
        <div class="search_wrap">
            
            <a href="/" class="sgbk_logo">
                <span class="search_logo">
                            <img src="//cache.soso.com/baike/i/sgbk_logo_@1x.png" alt="搜狗百科" srcset="//cache.soso.com/baike/i/sgbk_logo_@2x.png 2x">
                </span>
            </a>
            
            <form method="post" action="/lemma/default/ShowLemmaDefault,$FinalBorder.$NewSearchBar_0.$Form.sd;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0" name="Form" id="Form" class="search">
<div style="display:none;"><input type="hidden" name="formids" value="TextField_0,Submit_1,Submit_2"/>
<input type="hidden" name="submitmode" value=""/>
<input type="hidden" name="submitname" value=""/>
</div>
                <input type="text" name="TextField_0" value="" id="searchText" x-webkit-speech="" maxlength="100" autocomplete="off" showHelp="true" class="query"/>
                <a class="btn_clear j-search-reset" href="javascript:void(0);"></a>
                <input type="submit" name="Submit_1" id="enterLemma" class="btn_enter" value="进入词条"/>
                <input type="submit" name="Submit_2" id="searchLemma" class="btn_search" value="搜索词条"/>
                <div id="divc" class="smartbox"  style="visibility: hidden;"></div>
            </form>
        </div>
    </div>


<!--<div id="declare-main" class="declare-main declare-index">-->
    <!--<div class="declare">-->
        <!--声明：搜狗百科免费提供信息查询和信息编辑，坚决打击恶意篡改、冒充官方收费代编等违规行为。-->
        <!--<a href="http://baike.sogou.com/ui/disclaimer.html" target="_blank" class="declare-detail">详情&gt;</a>-->
        <!--<a href="javascript:void(0);" id="declare-close" class="declare-close">关闭</a>-->
    <!--</div>-->
<!--</div>-->
<!--<script>-->
    <!--if(localStorage.getItem('disclaimerPC315') == 'true'){-->
        <!--document.getElementById('declare-main').style.display = 'none';-->
    <!--}-->
    <!--document.getElementById('declare-close').onclick = function(){-->
        <!--localStorage.setItem('disclaimerPC315','true');-->
        <!--document.getElementById('declare-main').style.display = 'none';-->
    <!--};-->
<!--</script>-->
			</div> <!-- header -->

		<!--main-->
			<div id="main">
				

	<script>
        window.lemmaData = {"amazon":false,"mbabstract":"网络爬虫(又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常被称为网页追逐者)，是一种按照一定的规则，自动的抓取万维网信息的程序或者脚本，已被广泛应用于互联网领域。搜索引擎使用网络爬虫抓取Web网页、文档甚至图片、音频、视频等资源，通过相应的索引技术组织这些信息，提供给搜索用户进行查询。网络爬虫也为中小站点的推广提供了有效的途径。[1]","contentId":166298392,"lemmaTitle":"网络爬虫","lemmaId":77860};
        
        
        var hasRelationTable=false;
        


	</script>

	<script>
        
        
        var hasCaricatureData=false;
        
	</script>

	<script>
        
        
        var hasYicheData=false;
        
	</script>

	<script>
        
        
        var hasGoodDoctorData=false;
        
	</script>

	<script>
        
        
        var hasDianPingData=false;
        
	</script>

	<script>
        
        
        var hasRelationMenu=false;
        
	</script>

	



		<script>
            var topPicLogo='';
            var topPicUrl='';
            var topPicLink='';
            var topColor='';
            var topTarget=1;
            var lemmaId=77860;
            var weiboUid='';
            var company=false;
            var brand=false;
            var paragraphJson={"paragraph":[{"rawTitle":"相关介绍","property":1,"id":1,"title":"相关介绍"},{"rawTitle":"工作原理","property":1,"id":2,"title":"工作原理"},{"rawTitle":"技术研究","property":1,"id":3,"title":"技术研究"},{"rawTitle":"网页抓取","property":1,"id":4,"title":"网页抓取"},{"rawTitle":"网页分析","property":1,"id":5,"title":"网页分析"},{"rawTitle":"其他补充","property":1,"id":6,"title":"其他补充"},{"rawTitle":"相关新闻","property":1,"id":7,"title":"相关新闻"},{"rawTitle":"搜索策略","property":1,"id":8,"title":"搜索策略"},{"rawTitle":"广度优先搜索策略","property":2,"id":9,"title":"广度优先搜索策略"},{"rawTitle":"最佳优先搜索策略","property":2,"id":10,"title":"最佳优先搜索策略"},{"rawTitle":"深度优先搜索策略","property":2,"id":11,"title":"深度优先搜索策略"}]};
            var landscape='';
            var sizeType='0';

            var ambiguation='';
            var ambiguationTitle='null';

            var schoolJSON='';
            var majorJSON='';
            var teacher=false;
            var starFlower=false;
            var teacherCard='0';
            var teacherFlower='0';
            var teacherWX='null';
            taskIdBack=0;;

            var foreignSchoolJSON=null;
            var isCityBaikeLem='false';
            var cityName='null';
            var isEnterprisePayLemma=false;;
            var enterprisePayWX='null';

            var isBrandPayLemma=false;;
            var brandPayWX='null';

            var lemmaGray=false;;
            var lemmaCouldBeTaken=false;
                var isDoctorData=false;
            var zhihuJSONData=null;
            var isHospitalData=false;
            var sgVedioMovieJSONData=null;
            var isSgVedioTvJSONData=false;
            var sgVedioCartoonJSONData=null;
            var sgVedioVarietyJSONData=null;
            var mainDomain='sogou.com';

		</script>
		<script>
            
            
            var highQuality=true;
            
            

            l = '';
		</script>

		<!-- <div class="breadcrumb"><a href="/">百科首页</a><span>&gt;</span>浏览词条</div> -->

		<!--float header-->
		<div class="header_top">
			<div class="header_wrap">
				<!--  <img src="//cache.soso.com/baike/i/logo/ssbk_logo_s.png" alt="" /> -->
				<script>
              		document.write('<a class="bk_logo_s" href="/" title="到搜狗百科首页"><span class="baike_logo_s">搜狗百科</span></a>');
				</script>

				<div class="head_search_wrap">

					<form method="post" action="/lemma/default/ShowLemmaDefault,$FinalBorder.$NewSearchBar.sf.sd" name="myForm" id="myForm">
						<div style="display:none;">
							<input type="hidden" name="formids" value="TextField,Submit,Submit_0">
							<input type="hidden" name="submitmode" value="">
							<input type="hidden" name="submitname" value="">
						</div>
						<input type="text" id="searchText2" name="TextField" value="" showhelp="true" maxlength="100" class="search_input_s" x-webkit-speech="" autocomplete="off">
						<a class="search_btn" href="javascript:;">搜索词条</a>
						<div id="divc2" class="smartbox" style="visibility: hidden;"></div>
					</form>
				</div>

				<div class="fast_operation">
            

                <a ch="ch.bk.eddit.all" ohref="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860" onclick="return beforeEditCheck(this)" href="javascript:;" class="edit_lemma" target="_self"><i></i>编辑词条</a>

            
					<a href="javascript:;" class="collect_lemma"><i></i>收藏</a>
					<div class="collect_tip">
						查看<a href="/MyWatchlist.htm" target="_blank">我的收藏</a>
					</div>

					<!-- <a class="like_lemma liked" href=""><i></i>喜欢</a> -->
					<div class="share_wrap">
						<a class="share_lemma" href="javascript:;"><i></i>分享</a>
						<div class="share_to" style="display: none;">
							<h4>分享到</h4>
							<a href="javascript:;" class="ico_t_qq"><i></i>腾讯微博</a>
							<a id="share2qzone" href="javascript:;" class="ico_qzone"><i></i>QQ空间</a>
							<a id="share2sinaweibo" href="javascript:;" class="ico_weibo"><i></i>新浪微博</a>
							<a id="share2renren" href="javascript:;" class="ico_renren"><i></i>人人网</a>
						</div>
					</div>
					<script>document.write('<a class="appeal" href="/appeal/appeal.v?type=1&titleArray='+window.encodeURI(lemmaData.lemmaTitle)+'&urlArray='+ window.WKRWDOMAIN('//baike.sogou.com/v') + lemmaData.lemmaId+'.htm" target="_blank"><i></i>投诉</a>')</script>
				</div>

				<div id="login_wrap" class="login_wrap">
            
                <a href="javascript:;" onclick="Baike.Login.checkLogin()">登录</a>
            
				</div>

			</div>
		</div> <!--float header-->

		<div class="video_view_layer single_video">
			<a class="btn_quit" title="退出" href="javascript:;">退出</a>
			<div class="view_wrap">

				<div class="video_view_wrap">
					<div class="video_title_wrap">
						<h2>#title</h2>
					</div>
					<div class="video_view">#video#</div>
				</div>
			</div>
		</div>

		<div class="mask"></div>

		<div class="main_nav">
			<ul>
				<li><a href="/" title="百科首页">首页</a></li>
				<li class="sub">
					<a href="javascript:;" title="精彩百科">精彩百科</a>
					<div class="sub_nav">
						<a href="http://tupu.baike.sogou.com" title="知识图谱" onclick="stget('c.menu.zs', 'baike');DT.reportCLK('c.menu.zs')" target="_blank">知识图谱</a>
						<a href="/city/map.v" target="_blank" onclick="stget('c.menu.cs', 'baike');DT.reportCLK('c.menu.cs')" title="城市百科">城市百科</a>
						<a href="/zt/kangzhan/guide/index.html" target="_blank" onclick="stget('c.menu.kz', 'baike');DT.reportCLK('c.menu.kz')" title="抗战百科" >抗战百科</a>
						<a href="/zt/gxbk/index.html" target="_blank" onclick="stget('c.menu.gx', 'baike');DT.reportCLK('c.menu.gx')" title="高校百科" >高校百科</a>
						<a class="last" href="/zt/jhy/index.html" target="_blank" onclick="stget('c.menu.ts', 'baike');DT.reportCLK('c.menu.ts')" title="图说专题">图说专题</a>
					</div>
				</li>
				<li class="sub">
					<a href="javascript:;" title="任务">任务</a>
					<div class="sub_nav">
						<a href="/userAssignmentInde.v" target="_blank" onclick="stget('c.menu.task', 'baike');DT.reportCLK('c.menu.task')" title="任务中心">任务中心</a>
						<a class="last" href="/activity/collegeIndex.v" target="_blank" onclick="stget('bmsy.gxhd.bj', 'baike');DT.reportCLK('bmsy.gxhd.bj')" title="大学挑战赛">大学挑战赛</a>
					</div>
				</li>
				<li class="sub">
					<a href="javascript:;" title="用户">用户</a>
					<div class="sub_nav">
						<!--<a href="/pgc/profession.v" target="_blank" onclick="stget('ctgwshouye.bj', 'baike');DT.reportCLK('ctgwshouye.bj')" title="词条顾问">词条顾问</a>-->
						<a href="/activity/beeTeam.v" target="_blank" onclick="stget('bm.mft.bj', 'baike');DT.reportCLK('bm.mft.bj')" title="蜜蜂团">蜜蜂团</a>
						<a href="/Ant.v" target="_blank" onclick="stget('bm.myt.bj', 'baike');DT.reportCLK('bm.myt.bj')" title="蚂蚁团">蚂蚁团</a>
						<a href="/ui/FieldGroup/index.html" target="_blank" onclick="stget('team.lingyu', 'baike');DT.reportCLK('team.lingyu')" title="领域小组">领域小组</a>
						<a class="last" href="/rz/hotbk/index.html" target="_blank" onclick="stget('team.reci', 'baike');DT.reportCLK('team.reci')" title="热词团">热词团</a>
					</div>
				</li>

				<li><a href="/shop/index.php?r=gongyi" target="_blank" onclick="stget('c.menu.gy', 'baike');DT.reportCLK('c.menu.gy')" title="公益百科">公益百科</a></li>
				<li><a class="last" href="/shop/" target="_blank" onclick="stget('c.menu.shop', 'baike');DT.reportCLK('c.menu.shop')" title="积分商城">积分商城</a></li>
				<li class="nav_user"><a href="/usercenter/mygrowtask.v" title="个人中心"><i></i>个人中心</a></li>
			</ul>
		</div>

		<!--词条页大背景-->
		
		<!--词条页大背景-->

		

		<!--<div class="semantic_item_wrap" jwcid="@If" condition="ognl:(jumpFromViceLemma || ambiguous) && !viewUnNormalVersion" element="div"> -->
		<!-- <div class="semantic_item_wrap" jwcid="@If" condition="ognl:ambiguous && !viewUnNormalVersion" element="div">


          ambiguous
          <div jwcid="@If" class="semantic_item" condition="ognl :ambiguous && ambiLists != null" element="div">
             <div class="semantic_tip">
                    <span jwcid="@If" condition="ognl:ambiEditor">
                        <div class="option_wrap">
                            <a class="add_semantic" jwcid="@Any" onclick="return checkLock(1,null,null)" href="ognl:'/lemma/CreateV1.e?sp=1&sp=S' + ambiguation + '&sp=T'" ch="ch.bk.item.ed">添加义项</a>
                        </div>
                    </span>
                    <em><span jwcid="@Insert" value="ognl:fromTitle" /></em>是一个多义词，您可以选择查看以下义项：
                </div>
             <ol id="ambi_items" class="semantic_item_list" ch="ch.bk.item">
               <span jwcid="@For" source="prop:ambiLists" value="prop:ambiguationItem" index="prop:ambiguationIdx">
                 <span jwcid="@If" condition="ognl:ambiguationItem.second!=lemmaId">
                   <span jwcid="@If" condition="ognl: (ambiguationItem.first==null) || (ambiguationItem.first.isEmpty()) ">
                       <li><a jwcid="@Any" href="ognl:'/v' + ambiguationItem.second + '.htm?fromTitle='+fromTitle+'&ch=ch.bk.amb'" title="ognl:shortTitle"><span jwcid="@Insert" value="ognl:shortTitle"/></a></li>
                   </span>
                   <span jwcid="@Else">
                       <li><a jwcid="@Any" href="ognl:'/v' + ambiguationItem.second + '.htm?fromTitle='+fromTitle+'&ch=ch.bk.amb'" title="ognl:ambiguationItem.first"><span jwcid="@Insert" value="ognl:ambiguationItem.first"/></a></li>
                   </span>
                 </span><span jwcid="@Else">
                   <li class="current_item"><span jwcid="@Insert" value="ognl:ambiguationItem.first" /></li>
                 </span>
               </span>
             </ol>
             <span jwcid="@If" condition="ognl:ambiLists.size()>9">
               <a id="open_ambi_items" class="open_semantic" title="展开全部义项" href="javascript:;">展开</a>
               <a id="hide_ambi_items" class="open_semantic hide_semantic" style="display:none" title="收起部分义项" href="javascript:;">收起</a>
             </span>
          </div> semantic_item
        </div> --> <!-- semantic_item_wrap -->

		<!-- zol -->

		
		<!--词条页大背景-->
		

		<!--词条页大背景-->
		<!-- zol over -->

		<div class="main_wrap">
			<i class="page_horn"></i>

			<!-- <div class="lemma_wrap"> -->
			<div class="lemma_container">
  	  
	  	  <div class="abstract_wrap">
	  	    

            

	  	    
	          
	          <div class="lemma_toolbar">
	              <ul>
	              	  
		        	  
	               	  <li class="lemma_semantic"><a href="javascript:addAmbi();"><i></i>添加义项</a></li>
	    		      
                      
                          <li class="lemma_synonyms"><a href="/lemma/CreateV1.e?sp=2&amp;sp=l77860" class="synonymsBtn" onclick="return beforeEditCheck(this,'1')"><i></i>同义词</a></li>
                      
	                  <li unwatchBtnTitle="收藏词条" watchBtnTitle="取消收藏" id="watchLemmaBtnElem" title="收藏" class="lemma_collect un_focus" watchUrl="/watchlist/WatchlistAjaxOperation.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860" unwatchUrl="/watchlist/WatchlistAjaxOperation.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=3&amp;sp=l77860">
	                      <a href="javascript:;"><i></i>收藏</a>
	                  </li>
					  <!-- <li class="lemma_like"><a href="javascript:;"><i></i>286678</a></li> -->
	                  <li class="lemma_share"><a href="javascript:;"><i></i>分享</a>
	                      <div class="share_to" style="display: none;">
	                          <h4>分享到</h4>
	                          <a href="javascript:;" class="ico_t_qq"><i></i>腾讯微博</a> 
	                          <a id="share2qzone" href="javascript:;" class="ico_qzone"><i></i>QQ空间</a> 
	                          <a id="share2sinaweibo" href="javascript:;" class="ico_weibo"><i></i>新浪微博</a> 
	                          <a id="share2renren" href="javascript:;" class="ico_renren"><i></i>人人网</a>
                            
	                      </div>
	                  </li>
	              </ul>
	          </div>
	          <div class="lemma_name">
	              <h1 id="title">网络爬虫</h1>
				  <!-- 不管是不是优质词条，都不显示此图标 -->
				  <!-- <a jwcid="@If" condition="prop:highQuality" class="ico_quality_badge" title="优质词条" element="span">优质词条</a> -->
				  <!--义项编辑-->
	              <div class="lemma_focus_wrap">
	                  <a href="/lemma/CreateV1.e?sp=2&amp;sp=l77860" class="btn_edit_lemma" onclick="return beforeEditCheck(this)"><i></i>编辑词条</a>
	              </div>



				  <!--非义项编辑-->
				  <!-- <div jwcid="@If" class="lemma_focus_wrap" condition="ognl:!ambiguous && editable" element="div">
                      <a jwcid="@Any" ohref="prop:editLemmaUrl" href="javascript:;" class="btn_edit_lemma" target="_self" onclick="return beforeEdit(this)" ch="ch.bk.eddit.all"><i></i>编辑词条</a>
                  </div> -->
	              
	              
	              
	          </div> <!-- lemma_name -->

			  <!-- synonym -->
			  <!-- <span jwcid="@If" condition="ognl:jumpFromViceLemma">
                     <p class="semantic_explain">“<span jwcid="@Insert" value="prop:viceLemmaName"/>”一般是指“<span jwcid="@Insert" value="prop:title" />”</p>
              </span> -->
	              
	          
	          
	          <div class="abstract_main">
	              <!-- headpic and icons -->

	              <div class="side_wrap">
                  <div id="lemma_pic" class="lemma_pic">
	                <a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/ugc/baikepic2/4481/20170823231940-1819354231_jpg_350_280_16952.jpg/0" target="_blank"><img title="网络爬虫" alt="" src="http://pic.baike.soso.com/ugc/baikepic2/5641/20170823231940-2048399472_jpg_346_259_54454.jpg/0" width="250" height="200" class=""/></a>
	              </div>

	              
	              
		              <div class="wrap">
			              
						  
						  
					  </div>
                  

					  <!--艺评网-->
                  
                   <div class="wrap">
                   
					</div>
                  
	              </div>

				  <!-- lemma abstract -->
	              <div class="abstract">
	                <div class="edit_abstract"> 
	                <!-- <a jwcid="@If" condition="prop:editable" class="edit_abstract" ohref="prop:editAbstractUrl" href="javascript:;" onclick="return beforeEdit(this)" element="a" ch="ch.bk.eddit.abstract">编辑摘要</a> -->
                </div>
                <p>网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常被称为网页追逐者），是一种按照一定的规则，自动的抓取<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=17200&amp;ss_c=ssc.citiao.link">万维网</a>信息的程序或者脚本，已被广泛应用于互联网领域。搜索引擎使用网络爬虫抓取<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7633433&amp;ss_c=ssc.citiao.link">Web网页</a>、文档甚至图片、音频、视频等资源，通过相应的索引技术组织这些信息，提供给搜索用户进行查询。网络爬虫也为中小站点的推广提供了有效的途径。<sup><a href="#quote1">[1]</a><a name="ref_1"></a></sup></p>
                </div>
            </div> <!-- abstract_main -->
			  <!--同花顺股票展示-->
			  
			  <!--快捷导航-->
          <div class="lemma_content_nav hidden">
              <h2>快速导航</h2>
              <ul class="section_nav"></ul>
          </div>
			  <!--快捷导航-->

			  <!-- 企业词条核实验证信息 -->
			  <!--增加companyObject.code!=null判断，原因在于对于付费版的企业词条，未必存在code值，这种情况下丢失判断会报空指针 前台白页-->
            
            
                <div class="verify_wrapper" id="skyeye" data-type="1" style="display:none">
                    <div class="verify_info">
                        <div class="name"><h2>网络爬虫</h2></div>
                    </div>
                    <div class="verify_badge">
                      <a href="/v100374936.htm#para6" target="_blank" class="badge" title="查看说明"></a>
                      <a class="how" href="/v100374936.htm" target="_blank" title="查看如何获得"><i></i>如何获得</a>
                    </div>
                </div>
            
			  <!-- 企业词条核实验证信息 -->

			  <!-- 品牌词条核实验证信息 -->
            
			  <!-- 品牌词条核实验证信息 -->
            

        </div>
      






				<!--词条个性化内容区-->
				<div class="individuation_content_wrap">

					<!--新闻模块-->
					<div class="news-wrap hidden"></div>
					<!--新闻模块-->

					
          <!--个人档案-->
<div class="section_wrap">
	<!-- <div class="section_title base-info">
		<h2>基本信息栏</h2> 
		<a href="javascript:;" class="edit_content">编辑本段</a>
	</div> -->
	<div class="abstract_tbl_wrap"  ss_c="ssc.jbxxl">
		<table class="abstract_tbl">
			<tbody>
				<tr>
					<td class="abstract_list_wrap"><table class="abstract_list">
							<tbody>
								 
									
								
										<tr>
											<th>中文名</th>
											<td>
												网络爬虫
											</td>
										</tr>
								

								 
									
								
										<tr>
											<th>别    称</th>
											<td>
												网络蜘蛛
											</td>
										</tr>
								

								 
									
								
										<tr>
											<th>应用平台</th>
											<td>
												搜索引擎
											</td>
										</tr>
								

								
							</tbody>
						</table></td>
					<td class="abstract_list_wrap"><table class="abstract_list">
							<tbody>
								 
										<tr>
											<th>外文名</th>
											<td>Computer Robot</td>
										</tr>
								

								 
										<tr>
											<th>目    的</th>
											<td>获取<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=17200&amp;ss_c=ssc.citiao.link">万维网</a>信息</td>
										</tr>
								

								 
										<tr>
											<th>作用</th>
											<td>抓取Web网页、文档甚至图片、音频、视频等资源</td>
										</tr>
								

								
							</tbody>
						</table></td>
				</tr>
			</tbody>
		</table>

		

	</div>
</div>
<!--个人档案-->
<script>
// 展开个人档案
jQuery(".btn_more").toggle(function(){
	stget('c.jbxxl.unfold', 'baike');DT.reportCLK('c.jbxxl.unfold');
	jQuery(this).addClass("hide_more").attr('title', '收起内容').find("span").text("收起内容");
    jQuery(".abstract_tbl").find(".hidden").fadeIn();
	
},function(){
	stget('c.jbxxl.fold', 'baike');DT.reportCLK('c.jbxxl.fold');
	jQuery(this).removeClass("hide_more").attr('title', '展开内容').find("span").text("展开内容");
	jQuery(".abstract_tbl").find(".hidden").hide();
});
</script>

    

					<!-- 大图轮播 -->
					<div class="lemma_scroll_wrap hidden"></div>


					<!--词条目录-->
					<div id="lemma-catalog-container"></div>
					<!--词条目录-->
					<!-- 大事记 -->
					<div id="parastar2" class="section_wrap">
						<div class="section_title">
							<h2 greatevent="true">大事记</h2>
							<!-- <a href="javascript:;" class="edit_content">编辑本段</a>-->
						</div>
						<div class="record_wrapper" datatype="greatEvent" ss_c="ssc.dsj">
						</div><!-- content_wrap -->

					</div><!-- 大事记 -->

					<!--人物光影-->
					<div  id="parastar5" class="section_wrap">
						<div class="section_title">
							<h2>光影集锦</h2>
							<!-- <a class="edit_content" href="javascript:;">编辑本段</a>-->
						</div>
						<div class="image_content" ss_c="ssc.renwuguangying">
							<h3 starpic="true">图册集锦</h3>
							<div class="image_content_wrap" datatype="starPic" starpic="true">


							</div><!--图片集锦-->

							<h3 starvideo="true">花絮视频</h3>
							<div class="image_content_wrap" starvideo="true" datatype="starVideo">
								<div id="content4">
									<div class="tab_content">

										<ul class="video_list" datatype="starVideo">
										</ul>
									</div>

								</div>

							</div><!--花絮视频-->


						</div><!--人物光影内容-->

					</div><!--人物光影section_wrap-->
				</div><!--词条个性化内容区-->

				<!--词条内容区域-->
				<div class="lemma_content_wrap">
					<div class="section_wrap">
						<section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="1" id="1"></a>
									<a name="para1" id="para1">
										相关介绍
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="1" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=1" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><span class="text_img ed_imgfloat_right" style="width: 220px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212102355-461021759.jpg" target="_blank"><img title="网络爬虫" alt="" src="http://pic.baike.soso.com/ugc/baikepic/27264/cut-20140212102404-1378917160.jpg/0" width="220" height="165"/></a><span>网络爬虫</span></span>网络爬虫另外一些不常使用的名字还有蚂蚁，自动索引，模拟程序或者蠕虫。随着网络的迅速发展，万维网成为大量信息的载体，如何有效地提取并利用这些信息成为一个巨大的挑战。搜索引擎（Search Engine），例如传统的通用搜索引擎<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7671535&amp;ss_c=ssc.citiao.link">AltaVista</a>，Yahoo！和Google等，作为一个辅助人们检索信息的工具成为用户访问万维网的入口和指南。但是，这些通用性搜索引擎也存在着一定的局限性，如：</p><p>（1） 不同领域、不同背景的用户往往具有不同的检索目的和需求，通用搜索引擎所返回的结果包含大量用户不关心的网页。</p><p>（2）通用搜索引擎的目标是尽可能大的网络覆盖率，有限的搜索引擎服务器资源与无限的网络数据资源之间的矛盾将进一步加深。</p><p>（3）万维网数据形式的丰富和网络技术的不断发展，图片、数据库、音频、视频多媒体等不同数据大量出现，通用搜索引擎往往对这些信息含量密集且具有一定结构的数据无能为力，不能很好地发现和获取。</p><p>（4）通用搜索引擎大多提供基于关键字的检索，难以支持根据语义信息提出的查询。</p><p>为了解决上述问题，定向抓取相关网页资源的聚焦爬虫应运而生。聚焦爬虫是一个自动下载网页的程序，它根据既定的抓取目标，有选择的访问万维网上的网页与相关的链接，获取所需要的信息。与通用爬虫（general？purpose web crawler）不同，聚焦爬虫并不追求大的覆盖，而将目标定为抓取与某一特定主题内容相关的网页，为面向主题的用户查询准备数据资源。<sup><a href="#quote2">[2]</a><a name="ref_2"></a></sup></p>
								</div>
							</div>
						</section><section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="2" id="2"></a>
									<a name="para2" id="para2">
										工作原理
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="2" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=2" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><span class="text_img ed_imgfloat_right" style="width: 300px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/ugc/baikepic2/6996/20170908202102-1916208626_png_518_279_168397.jpg/0" target="_blank"><img title="网络爬虫" alt="" src="http://pic.baike.soso.com/ugc/baikepic2/6996/20170908202102-1916208626_png_518_279_168397.jpg/300" width="300" height="162"/></a><span>网络爬虫</span></span>网络爬虫是一个自动提取网页的程序，它为搜索引擎从万维网上下载网页，是搜索引擎的重要组成。传统爬虫从一个或若干初始网页的URL开始，获得初始网页上的URL，在<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=57226307&amp;ss_c=ssc.citiao.link">抓取网页</a>的过程中，不断从当前页面上抽取新的URL放入队列，直到满足系统的一定停止条件。聚焦爬虫的工作流程较为复杂，需要根据一定的网页分析算法过滤与主题无关的链接，保留有用的链接并将其放入等待抓取的URL队列。然后，它将根据一定的搜索策略从队列中选择下一步要抓取的网页URL，并重复上述过程，直到达到系统的某一条件时停止。另外，所有被爬虫抓取的网页将会被系统存贮，进行一定的分析、过滤，并建立索引，以便之后的查询和检索；对于聚焦爬虫来说，这一过程所得到的分析结果还可能对以后的抓取过程给出反馈和指导。</p><p>相对于通用网络爬虫，聚焦爬虫还需要解决三个主要问题：</p><p>（1） 对抓取目标的描述或定义；</p><p>（2） 对网页或数据的分析与过滤；</p><p>（3） 对URL的搜索策略。</p><p>抓取目标的描述和定义是决定网页分析算法与URL搜索策略如何制订的基础。而网页分析算法和候选URL排序算法是决定搜索引擎所提供的服务形式和爬虫<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=57226307&amp;ss_c=ssc.citiao.link">网页抓取</a>行为的关键所在。这两个部分的算法又是紧密相关的。</p><p><b>抓取目标描述</b></p><p>现有聚焦爬虫对抓取目标的描述可分为基于目标网页特征、基于目标数据模式和基于领域概念3种。</p><p>基于目标网页特征的爬虫所抓取、存储并索引的对象一般为网站或网页。根据种子样本获取方式可分为：</p><p>（1） 预先给定的初始抓取种子样本；</p><p>（2） 预先给定的网页分类目录和与分类目录对应的种子样本，如Yahoo！分类结构等；</p><p>（3） 通过用户行为确定的抓取目标样例，分为：</p><p>（a） 用户浏览过程中显示标注的抓取样本；</p><p>（b） 通过用户日志挖掘得到访问模式及相关样本。</p><p>其中，网页特征可以是网页的内容特征，也可以是网页的链接结构特征，等等。</p>
								</div>
							</div>
						</section><section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="3" id="3"></a>
									<a name="para3" id="para3">
										技术研究
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="3" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=3" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><span class="text_img ed_imgfloat_right" style="width: 300px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/ugc/baikepic2/6980/20170908202114-1298856863_png_313_246_56184.jpg/0" target="_blank"><img title="网络爬虫" alt="" src="http://pic.baike.soso.com/ugc/baikepic2/6980/20170908202114-1298856863_png_313_246_56184.jpg/300" width="300" height="236"/></a><span>网络爬虫</span></span>基于目标数据模式的爬虫针对的是网页上的数据，所抓取的数据一般要符合一定的模式，或者可以转化或映射为目标数据模式。</p><p>另一种描述方式是建立目标领域的本体或词典，用于从语义角度分析不同特征在某一主题中的重要程度。</p>
								</div>
							</div>
						</section><section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="4" id="4"></a>
									<a name="para4" id="para4">
										网页抓取
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="4" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=4" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><span class="text_img ed_imgfloat_right" style="width: 220px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212102621-2005476100.jpg" target="_blank"><img title="网页的抓取策略" alt="" src="http://pic.baike.soso.com/ugc/baikepic/32253/cut-20140212102628-1832882271.jpg/0" width="220" height="165"/></a><span>网页的抓取策略</span></span>网页的抓取策略可以分为深度优先、广度优先和最佳优先三种。深度优先在很多情况下会导致爬虫的陷入（trapped）问题，目前常见的是广度优先和最佳优先方法。</p><p><b>广度优先搜索策略</b></p><p>广度优先搜索策略是指在抓取过程中，在完成当前层次的搜索后，才进行下一层次的搜索。该算法的设计和实现相对简单。在目前为覆盖尽可能多的网页，一般使用广度优先搜索方法。也有很多研究将广度优先搜索策略应用于聚焦爬虫中。其基本思想是认为与初始URL在一定链接距离内的网页具有主题相关性的概率很大。另外一种方法是将广度优先搜索与网页过滤技术结合使用，先用广度优先策略抓取网页，再将其中无关的网页过滤掉。这些方法的缺点在于，随着抓取网页的增多，大量的无关网页将被下载并过滤，算法的效率将变低。</p><p><b>最佳优先搜索策略</b></p><p>最佳优先搜索策略按照一定的网页分析算法，预测候选URL与目标网页的相似度，或与主题的相关性，并选取评价最好的一个或几个URL进行抓取。它只访问经过网页分析算法预测为“有用”的网页。存在的一个问题是，在爬虫抓取路径上的很多相关网页可能被忽略，因为最佳优先策略是一种局部最优<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=39055688&amp;ss_c=ssc.citiao.link">搜索算法</a>。因此需要将最佳优先结合具体的应用进行改进，以跳出局部最优点。将在第4节中结合网页分析算法作具体的讨论。研究表明，这样的闭环调整可以将无关网页数量降低30%~90%。</p><p><b>深度优先搜索策略</b></p><p>深度优先搜索策略从起始网页开始，选择一个URL进入，分析这个网页中的URL，选择一个再进入。如此一个链接一个链接地抓取下去，直到处理完一条路线之后再处理下一条路线。<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=67302516&amp;ss_c=ssc.citiao.link">深度优先策略</a>设计较为简单。然而门户网站提供的链接往往最具价值，<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=234075&amp;ss_c=ssc.citiao.link">PageRank</a>也很高，但每深入一层，网页价值和PageRank都会相应地有所下降。这暗示了重要网页通常距离种子较近，而过度深入抓取到的网页却价值很低。同时，这种策略抓取深度直接影响着抓取命中率以及抓取效率，对抓取深度是该种策略的关键。相对于其他两种策略而言。此种策略很少被使用。</p>
								</div>
							</div>
						</section><section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="5" id="5"></a>
									<a name="para5" id="para5">
										网页分析
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="5" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=5" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><span class="text_img ed_imgfloat_right" style="width: 273px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/ugc/baikepic2/7271/20170908202219-511748268_png_307_337_60693.jpg/0" target="_blank"><img title="网络爬虫" alt="" src="http://pic.baike.soso.com/ugc/baikepic2/7271/20170908202219-511748268_png_307_337_60693.jpg/300" width="273" height="300"/></a><span>网络爬虫</span></span>网页分析算法可以归纳为基于网络拓扑、基于网页内容和基于用户访问行为三种类型。</p><p><b>网络拓扑的分析算法</b></p><p>基于网页之间的链接，通过已知的网页或数据，来对与其有直接或间接链接关系的对象（可以是网页或网站等）作出评价的算法。又分为网页粒度、网站粒度和网页块粒度这三种。</p><p>1 网页（Webpage）粒度的分析算法</p><p>PageRank和<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=63532809&amp;ss_c=ssc.citiao.link">HITS算法</a>是最常见的链接分析算法，两者都是通过对网页间链接度的递归和规范化计算，得到每个网页的重要度评价。PageRank算法虽然考虑了用户访问行为的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=312792&amp;ss_c=ssc.citiao.link">随机性</a>和Sink网页的存在，但忽略了绝大多数用户访问时带有目的性，即网页和链接与查询主题的相关性。针对这个问题，HITS算法提出了两个关键的概念：权威型网页（authority）和中心型网页（hub）。</p><p>基于链接的抓取的问题是相关页面主题团之间的隧道现象，即很多在抓取路径上偏离主题的网页也指向目标网页，局部评价策略中断了在当前路径上的抓取行为。文献提出了一种基于<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=17865&amp;ss_c=ssc.citiao.link">反向链接</a>（BackLink）的分层式上下文模型（Context Model），用于描述指向目标网页一定物理跳数半径内的网页<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=270440&amp;ss_c=ssc.citiao.link">拓扑图</a>的中心Layer0为目标网页，将网页依据指向目标网页的物理跳数进行层次划分，从外层网页指向内层网页的链接称为反向链接。</p><p>2 网站粒度的分析算法</p><p>网站粒度的资源发现和管理策略也比网页粒度的更简单有效。网站粒度的爬虫抓取的关键之处在于站点的划分和站点等级（SiteRank）的计算。SiteRank的计算方法与PageRank类似，但是需要对网站之间的链接作一定程度抽象，并在一定的模型下计算链接的权重。</p><p>网站划分情况分为按域名划分和按IP地址划分两种。文献讨论了在分布式情况下，通过对同一个域名下不同主机、服务器的IP地址进行站点划分，构造站点图，利用类似PageRank的方法评价SiteRank。同时，根据不同文件在各个站点上的分布情况，构造文档图，结合SiteRank<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=67743011&amp;ss_c=ssc.citiao.link">分布式计算</a>得到DocRank。文献证明，利用分布式的SiteRank计算，不仅大大降低了单机站点的算法代价，而且克服了单独站点对整个网络覆盖率有限的缺点。附带的一个优点是，常见PageRank 造假难以对SiteRank进行欺骗。</p><p>3 网页块粒度的分析算法</p><p>在一个页面中，往往含有多个指向其他页面的链接，这些链接中只有一部分是指向主题相关网页的，或根据网页的链接<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=306987&amp;ss_c=ssc.citiao.link">锚文本</a>表明其具有较高重要性。但是，在PageRank和HITS算法中，没有对这些链接作区分，因此常常给网页分析带来广告等噪声链接的干扰。在网页块级别（Block？level）进行链接分析的算法的基本思想是通过VIPS网页分割算法将网页分为不同的网页块（page block），然后对这些网页块建立page？to？block和block？to？page的链接矩阵，？分别记为Z和X。于是，在page？to？page图上的网页块级别的PageRank为？W？p=X×Z；？在block？to？block图上的BlockRank为？W？b=Z×X。已经有人实现了块级别的PageRank和HITS算法，并通过实验证明，效率和准确率都比传统的对应算法要好。</p><p><b>网页分析算法</b></p><p>基于网页内容的分析算法指的是利用网页内容（文本、数据等资源）特征进行的网页评价。网页的内容从原来的以<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=42705&amp;ss_c=ssc.citiao.link">超文本</a>为主，发展到后来<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=54233623&amp;ss_c=ssc.citiao.link">动态页面</a>（或称为Hidden Web）数据为主，后者的数据量约为直接可见页面数据（PIW，Publicly Indexable Web）的400~500倍。另一方面，多媒体数据、Web Service等各种网络资源形式也日益丰富。因此，基于网页内容的分析算法也从原来的较为单纯的文本检索方法，发展为涵盖网页<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=57321817&amp;ss_c=ssc.citiao.link">数据抽取</a>、<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=231046&amp;ss_c=ssc.citiao.link">机器学习</a>、数据挖掘、语义理解等多种方法的综合应用。本节根据网页数据形式的不同，将基于网页内容的分析算法，归纳以下三类：第一种针对以文本和<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=17803&amp;ss_c=ssc.citiao.link">超链接</a>为主的无结构或结构很简单的网页；第二种针对从结构化的数据源（如<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=319739&amp;ss_c=ssc.citiao.link">RDBMS</a>）动态生成的页面，其数据不能直接批量访问；第三种针对的数据界于第一和第二类数据之间，具有较好的结构，显示遵循一定模式或风格，且可以直接访问。</p><p>【基于文本的网页分析算法】</p><p>1） 纯<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=61261936&amp;ss_c=ssc.citiao.link">文本分类</a>与聚类算法</p><p>很大程度上借用了文本检索的技术。文本分析算法可以快速有效的对网页进行分类和聚类，但是由于忽略了网页间和网页内部的结构信息，很少单独使用。</p><p>2） 超文本分类和聚类算法</p><p>根据网页链接网页的相关类型对网页进行分类，依靠相关联的网页推测该网页的类型。</p>
								</div>
							</div>
						</section><section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="6" id="6"></a>
									<a name="para6" id="para6">
										其他补充
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="6" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=6" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><span class="text_img ed_imgfloat_right" style="width: 300px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/ugc/baikepic2/7263/20170908202237-2066978434_png_354_313_110320.jpg/0" target="_blank"><img title="网络爬虫" alt="" src="http://pic.baike.soso.com/ugc/baikepic2/7263/20170908202237-2066978434_png_354_313_110320.jpg/300" width="300" height="265"/></a><span>网络爬虫</span></span>这些处理被称为网络抓取或者蜘蛛爬行。很多站点，尤其是搜索引擎，都使用爬虫提供最新的数据，它主要用于提供它访问过页面的一个副本，然后，搜索引擎就可以对得到的页面进行索引，以提供快速的访问。蜘蛛也可以在web上用来自动执行一些任务，例如检查链接，确认<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=66232122&amp;ss_c=ssc.citiao.link">html代码</a>；也可以用来<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=57226307&amp;ss_c=ssc.citiao.link">抓取网页</a>上某种特定类型信息，例如抓取<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=789472&amp;ss_c=ssc.citiao.link">电子邮件地址</a>（通常用于<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=268958&amp;ss_c=ssc.citiao.link">垃圾邮件</a>）。</p><p>一个网络蜘蛛就是一种机器人，或者<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=53237365&amp;ss_c=ssc.citiao.link">软件代理</a>。大体上，它从一组要访问的URL链接开始，可以称这些URL为种子。爬虫访问这些链接，它辨认出这些页面的所有超链接，然后添加到这个URL列表，可以称作检索前沿。这些URL按照一定的策略反复访问。</p><p>【主要内容目录】</p><p>· 1爬行策略</p><p>o 1.1 选择策略</p><p>§ 1.1.1 限定访问链接</p><p>§ 1.1.2 路径检索</p><p>§ 1.1.3 聚焦检索</p><p>§ 1.1.4 抓取深层的网页</p><p>§ 1.1.5 Web 3.0检索</p><p>o 1.2 重新访问策略</p><p>o 1.3 平衡礼貌策略</p><p>o 1.4 并行化策略</p><p>· 2 网络爬虫体系结构</p><p>o 2.1 URL规范化</p><p>· 3 爬虫身份识别</p><p>· 4 网络爬虫的例子</p><p>o 4.1 开源的网络爬虫</p><p><b>爬行策略</b></p><p>下述的三种网络特征，造成了设计网页爬虫抓取策略变得很难：</p><p> 它巨大的数据量；</p><p> 它快速的更新频率；</p><p>动态页面的产生。</p><p>它们三个特征一起产生了很多种类的爬虫抓取链接。</p><p>巨大的数据量暗示了爬虫，在给定的时间内，只可以抓取所下载网络的一部分，所以，它需要对它的抓取页面设置优先级；快速的更新频率说明在爬虫抓取下载某网站一个网页的时候，很有可能在这个站点又有很的网页被添加进来，或者这个页面新增的很多页面都是通过<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=101278217&amp;ss_c=ssc.citiao.link">服务器端</a><a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=230334&amp;ss_c=ssc.citiao.link">脚本语言</a>产生的，无穷的参数组合也增加了爬虫抓取的难度，只有一小部分这种组合会返回一些独特的内容。例如，一个很小照片存储库仅仅通过get方式可能提供就给用户三种操作方式。如果这里存着四种分类方式，三种<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=4069827&amp;ss_c=ssc.citiao.link">缩略图</a>方式，两种文件格式，和一个禁止用户提供内容的选项，那么，同样的内容就可以通过48种方式访问。这种数学组合给网络爬虫创造的难处就是，为了获取不同的内容，他们必须筛选无穷仅有微小变化的组合。</p><p>正如爱德华等人所说的：“用于检索的带宽不是无限的，也不是免费的；所以，如果引入衡量爬虫抓取质量或者新鲜度的有效指标的话，不但伸缩性，连有效性都将变得十分必要”（爱德华等人，2001年）。一个爬虫就必须小心的选择下一步要访问什么页面。网页爬虫的行为通常是四种策略组合的结果。</p><p>♦ 选择策略，决定所要下载的页面；</p><p>♦ 重新访问策略，决定什么时候检查页面的更新变化；</p><p>♦ 平衡礼貌策略，指出怎样避免站点超载；</p><p>♦ 并行策略，指出怎么协同达到分布式抓取的效果。</p><p><span class="text_img ed_imgfloat_right" style="width: 220px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212103044-544357933.jpg" target="_blank"><img title="选择策略" alt="" src="http://pic.baike.soso.com/ugc/baikepic/27631/cut-20140212103054-1693096791.jpg/0" width="220" height="165"/></a><span>选择策略</span></span>1.1 选择策略：</p><p>就现在网络资源的大小而言，即使很大的搜索引擎也只能获取网络上可得到资源的一小部分。由劳伦斯河盖尔斯共同做的一项研究指出，没有一个搜索引擎抓取的内容达到网络的16%（劳伦斯河盖尔斯，2001）。网络爬虫通常仅仅下载网页内容的一部分，但是大家都还是强烈要求下载的部分包括最多的相关页面，而不仅仅是一个随机的简单的站点。</p><p>这就要求一个公共标准来区分网页的重要程度，一个页面的重要程度与他自身的质量有关，与按照链接数、访问数得出的受欢迎程度有关，甚至与他本身的网址（后来出现的把搜索放在一个顶级域名或者一个固定页面上的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=62384&amp;ss_c=ssc.citiao.link">垂直搜索</a>）有关。设计一个好的搜索策略还有额外的困难，它必须在<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=72364651&amp;ss_c=ssc.citiao.link">不完全信息</a>下工作，因为整个页面的集合在抓取时是未知的。</p><p>Cho等人（Cho et al，1998）做了第一份抓取策略的研究。他们的数据是<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=527469&amp;ss_c=ssc.citiao.link">斯坦福大学</a>网站中的18万个页面，使用不同的策略分别模仿抓取。排序的方法使用了广度优先，后链计数，和部分pagerank算法。计算显示，如果你想要优先下载pagerank高的页面，那么，部分PageRank策略是比较好的，其次是广度优先和后链计数。并且，这样的结果仅仅是针对一个站点的。</p><p>Najork和Wiener （Najork and Wiener， 2001）采用实际的爬虫，对3.28亿个网页，采用广度优先研究。他们发现广度优先会较早的抓到PageRank高的页面（但是他们没有采用其他策略进行研究）。作者给出的解释是：“最重要的页面会有很多的主机连接到他们，并且那些链接会较早的发现，而不用考虑从哪一个主机开始。”</p><p>Abiteboul （Abiteboul 等人， 2003），设计了一种基于OPIC（在线页面重要指数）的抓取战略。在OPIC中，每一个页面都有一个相等的初始权值，并把这些权值平均分给它所指向的页面。这种算法与Pagerank相似，但是他的速度很快，并且可以一次完成。OPIC的程序首先抓取获取权值最大的页面，实验在10万个幂指分布的模拟页面中进行。并且，实验没有和其它策略进行比较，也没有在真正的WEB页面测试。</p><p><span class="text_img ed_imgfloat_right" style="width: 220px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212103503-1722426589.jpg" target="_blank"><img title="广度优先与深度优先" alt="" src="http://pic.baike.soso.com/ugc/baikepic/27577/cut-20140212103514-1301264923.jpg/0" width="220" height="165"/></a><span>广度优先与深度优先</span></span>Boldi等人（Boldi et al.， 2004）的模拟检索实验进行在 从.it网络上取下的4000万个页面和从webbase得到的1亿个页面上，测试广度优先和深度优先，<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=76668887&amp;ss_c=ssc.citiao.link">随机序列</a>和有序序列。比较的基础是真实页面pageRank值和计算出来的pageRank值的接近程度。令人惊奇的是，一些计算pageRank很快的页面（特别明显的是广度优先策略和有序序列）仅仅可以达到很小的接近程度。</p><p>Baeza-Yates等人（Baeza-Yates et al.， 2005） 在从.gr域名和.cl域名子网站上获取的300万个页面上模拟实验，比较若干个抓取策略。结果显示OPIC策略和站点队列长度，都比广度优先要好；并且如果可行的话，使用之前的爬行抓取结果来指导这次抓取，总是十分有效的。</p><p>Daneshpajouh等人（Daneshpajouh et al.， 2008）设计了一个用于寻找好种子的社区。它们从来自不同社区的高PageRank页面开始检索的方法，迭代次数明显小于使用随机种子的检索。使用这种方式，可以从以前抓取页面之中找到好的种子，使用这些种子是十分有效的。</p><p>1.1.1 限定访问链接</p><p>一个爬虫可能仅仅想找到html页面的种子而避免其他的文件类型。为了仅仅得到html的资源，一个爬虫可以首先做一个http head的请求，以在使用request方法获取所有的资源之前，决定这个网络文件的类型。为了避免要发送过多的head请求，爬虫可以交替的检查url并且仅仅对以html，htm和<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=269931&amp;ss_c=ssc.citiao.link">反斜杠</a>结尾的文件发送资源请求。这种策略会导致很多的html资源在无意中错过，一种相似的策略是将网络资源的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=190718&amp;ss_c=ssc.citiao.link">扩展名</a>同已知是<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=2471330&amp;ss_c=ssc.citiao.link">html文件</a>类型的一组扩展名（如.html，.htm，.asp，.php，.aspx，反斜杠）进行比较。</p><p>一些爬虫也会限制对任何含有“？”的资源（这些是动态生成的）进行获取请求，以避免蜘蛛爬行在某一个站点中陷入下载无穷无尽的URL的困境。</p><p>1.1.2 路径检索</p><p>一些爬虫会尽可能多的尝试下载一个特定站点的资源。Cothey（Cothey，2004）引入了一种路径检索的爬虫，它会尝试抓取需要检索资源的所有URL。例如，给定一个种子地址：它将会尝试检索/hamster/menkey/，/hamster/和/ 。Cothey发现路径检索对发现独立资源，或者一些通常爬虫检索不到的的连接是非常有效的。</p><p>一些路径检索的爬虫也被称为收割机软件，因为他们通常用于收割或者收集所有的内容，可能是从特定的页面或者主机收集相册的照片。</p><p>1.1.3 聚焦抓取</p><p>爬虫所抓取页面的重要程度也可以表述成它与给定查询之间相似程度的函数。网络爬虫尝试下载相似页面，可以称为聚焦检索或者主题检索。关于主题检索和聚焦检索的概念，最早是由Menczer（Menczer 1997； Menczer and Belew， 1998）和Chakrabarti等人首先提出来的（Chakrabarti et al.， 1999）。</p><p>聚焦检索的主要问题是网页爬虫的使用环境，我们希望在实际下载页面之前，就可以知道给定页面和查询之间的相似度。一个可能的方法就是在链接之中设置锚点，这就是在早期时候，<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=69981960&amp;ss_c=ssc.citiao.link">Pinkerton</a>（Pinkerton，1994）曾经在一个爬虫中采用的策略。Diligenti等人（Diligenti等人，2000）建议使用已经抓取页面的内容去推测查询和未访问页的相似度。一个聚焦查询的表现的好坏主要依赖于查询主题内容的丰富程度，通常还会依赖页面查询引擎提供的查询起点。</p><p>1.1.4 抓取深层的网页</p><p>很多的页面隐藏的很深或隐藏在在看不到的网络之中。这些页面通常只有在向数据库提交查询的时候才可以访问到，如果没有链接指向他们的话，一般的爬虫是不能访问到这些页面的。谷歌<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=9906339&amp;ss_c=ssc.citiao.link">站点地图协议</a>和mod oai（Nelson等人，2005）尝试允许发现这些深层次的资源。</p><p>深层页面抓取器增加了抓取网页的链接数。某些情况下，例如Googlebot，WEB抓取的是所有超文本所包含的内容，标签和文本。</p><p>1.1.5 <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=238266&amp;ss_c=ssc.citiao.link">WEB3.0</a>检索</p><p>Web3.0为下一代搜索技术定义了更先进的技术和新的准则，可以概括为<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7616373&amp;ss_c=ssc.citiao.link">语义网络</a>和<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7596939&amp;ss_c=ssc.citiao.link">网站模板</a>解析的概念。第三代检索技术将建立在人机巧妙的联系的基础上。</p><p>1.2重新访问策略</p><p>网络具有动态性很强的特性。抓取网络上的一小部分内容可能会花费真的很长的时间，通常用周或者月来衡量。当爬虫完成它的抓取的任务以后，很多操作是可能会发生的，这些操作包括新建，更新和删除。</p><p>从搜索引擎的角度来看，不检测这些事件是有成本的，成本就是我们仅仅拥有一份过时的资源。最常使用的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=431298&amp;ss_c=ssc.citiao.link">成本函数</a>，是新鲜度和过时性（2000年，Cho 和Garcia-Molina）。</p><table width="100%"><tbody><tr><td>新鲜度：这是一个衡量抓取内容是不是准确的二元值。在时间t内，仓库中页面p的新鲜度是这样定义的：</td><td><span class="text_img ed_imgfloat_right" style="width: 300px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212094152-794455480.jpg" target="_blank"><img title="新鲜度" alt="" src="http://pic.baike.soso.com/p/20140212/bki-20140212094152-794455480.jpg" width="300" height="40"/></a><span>新鲜度</span></span></td></tr></tbody></table><table width="100%"><tbody><tr><td>过时性：这是一个衡量本地已抓取的内容过时程度的指标。在时间t时，仓库中页面p的时效性的定义：</td><td><span class="text_img ed_imgfloat_right" style="width: 300px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212094220-1654844121.jpg" target="_blank"><img title="过时性" alt="" src="http://pic.baike.soso.com/p/20140212/bki-20140212094220-1654844121.jpg" width="300" height="25"/></a><span>过时性</span></span></td></tr></tbody></table><p>在页面抓取中，新鲜度和过时性的发展Coffman等人（Edward G. Coffman，1998）是从事爬虫对象定义的，他们提出了一个相当于新鲜度的概念，但是使用了不同的措词：他们建议爬虫必须最小化过时页面部分。他们指出网络爬行的问题就相当于多个队列，一个投票系统；这里，爬虫是服务器，不同的站点是队列。页面修改是到达的顾客，页面切换的时间是页面进入一个单一站点的间隔。在这个模型下，每一个顾客在投票系统的平均时间，相当于爬虫的平均过时性。</p><p>爬虫的目标是尽可能高的提高页面的新鲜度，同时降低页面的过时性。这一目标并不是完全一样的，第一种情况，爬虫关心的是有多少页面时过时的；在第二种情况，爬虫关心的页面过时了多少。</p><p>两种最简单的重新访问策略是由Cho和Garcia-Molina研究的（Cho 和Garcia-Molina，2003）：</p><p>统一策略：使用相同的频率，重新访问收藏中的所有的链接，而不考虑他们更新频率。</p><p>正比策略：对变化越多的网页，重新访问的频率也越高。网页访问的频率和网页变化的频率直接相关（两种情况下，爬虫的重新抓取都可以采用随机方式，或者固定的顺序）。</p><p>Cho和Garcia-Molina证明了一个出人意料的结果。以平均新鲜度方式衡量，统一策略在模拟页面和真实的网络抓取中都比正比策略出色。对于这种结果的解释是：当一个页面变化太快的时候，爬虫将会将会在不断的尝试重新抓取而浪费很多时间，但是却还是不能保证页面的新鲜度。</p><p>为了提高页面的新鲜度，我们应该宣判变化太快的页面死罪（Cho和Garcia-Molina， 2003a）。最佳的重新访问策略既不是统一策略，也不是正比策略；保持平均页面新鲜度高的最佳方法策略包括忽略那些变化太快的页面，而保持页面平均过时性低的方法则是对每一页按照页面变化率单调变化的策略访问。两种情况下，最佳的策略较正比策略，都更接近统一策略。正如Coffman等人（Edward G.Coffman，1998）所注意到的：“为了最小化页面过时的时间，对任一个页面的访问都应该尽可能的均匀间隔地访问。”对于重新访问的详尽的策略在大体上是不可以达到的，但是他们可以从数学上得到，因为他们依赖于页面的变化。（Cho和Garcia-Molina，2003a）指出指数变化是描述页面变化的好方法，同时（Ipeirotis等人，2005）指出了怎么使用统计工具去发现适合这些变化的参数。注意在这里的重新访问策略认为每一个页面都是相同的（网络上所有的页面价值都是一样的）这不是现实的情况，所以，为了获取更好的抓取策略，更多有关网页质量的信息应该考虑进去。</p><p>1.3 平衡礼貌策略</p><p>爬虫相比于人，可以有更快的检索速度和更深的层次，所以，他们可能使一个站点瘫痪。不需要说一个单独的爬虫一秒钟要执行多条请求，下载大的文件。一个服务器也会很难响应<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=452880&amp;ss_c=ssc.citiao.link">多线程</a>爬虫的请求。</p><p>就像Koster（Koster，1995）所注意的那样，爬虫的使用对很多工作都是很有用的，但是对一般的社区，也需要付出代价。使用爬虫的代价包括：</p><p>网络资源：在很长一段时间，爬虫使用相当的带宽高度并行地工作。</p><p> 服务器超载：尤其是对给定服务器的访问过高时。</p><p> 质量糟糕的爬虫，可能是服务器或者<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=15367&amp;ss_c=ssc.citiao.link">路由器</a>瘫痪，或者会尝试下载自己无法处理的页面。</p><p> 个人爬虫，如果过多的人使用，可能是网络或者服务器阻塞。</p><p>对这些问题的一个部分解决方法是漫游器排除协议（<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=15977&amp;ss_c=ssc.citiao.link">Robots</a> exclusion protocol），也被称为robots.txt议定书（Koster，1996），这份协议对于管理员指明<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=267249&amp;ss_c=ssc.citiao.link">网络服务器</a>的那一部分不能到达是一个标准。这个标准没有包括重新访问一台服务器的间隔的建议，虽然访问间隔是避免服务器超载的最有效的办法。<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=61397379&amp;ss_c=ssc.citiao.link">商业搜索</a>软件，如Ask Jeeves，MSN和Yahoo可以在robots.txt中使用一个额外的 “<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=73602971&amp;ss_c=ssc.citiao.link">Crawl-delay</a>”参数来指明请求之间的延迟。</p><p>对连接间隔时间的第一个建议由Koster 1993年给出，时间是60秒。按照这个速度，如果一个站点有超过10万的页面，即使我们拥有零延迟和无穷带宽的完美连接，它也会需要两个月的时间来下载整个站点，并且，这个服务器中的资源，只有一小部分可以使用。这似乎是不可以接受的。</p><p>Cho（Cho和Garcia-Molina， 2003）使用10秒作为访问的间隔时间，WIRE爬虫（Baeza-Yates and Castillo， 2002）使用15秒作为默认间隔。MercatorWeb（Heydon 和Najork， 1999）爬虫使用了一种自适应的平衡策略：如果从某一服务器下载一个文档需要t秒钟，爬虫就等待10t秒的时间，然后开始下一个页面。Dill等人 （Dill et al.， 2002） 使用1秒。</p><p>对于那些使用爬虫用于研究目的的，一个更详细的成本-效益分析是必要的，当决定去哪一个站点抓取，使用多快的速度抓取的时候，伦理的因素也需要考虑进来。</p><p>访问记录显示已知爬虫的访问间隔从20秒钟到3-4分钟不等。需要注意的是即使很礼貌，采取了所有的安全措施来避免服务器超载，还是会引来一些网络服务器管理员的抱怨的。Brin和Page注意到：运行一个针对超过50万服务器的爬虫，会产生很多的邮件和电话。这是因为有无数的人在上网，而这些人不知道爬虫是什么，因为这是他们第一次见到。（Brin和Page，1998）</p><p>1.4 并行策略</p><p>一个并行爬虫是并行运行多个进程的爬虫。它的目标是最大化下载的速度，同时尽量减少并行的开销和下载重复的页面。为了避免下载一个页面两次，爬虫系统需要策略来处理爬虫运行时新发现的URL，因为同一个URL地址，可能被不同的爬虫进程抓到。</p><p>【参考文献】</p><p>[1] Edwards， J.， McCurley， K. S.， and Tomlin， J. A. （2001）. &quot;An adaptive model for optimizing performance of an incremental web crawler&quot;. In Proceedings of the Tenth Conference on World Wide Web （Hong Kong： Elsevier Science）： 106–113. doi：10.1145/371920.371960.</p><p>[2] Lawrence， Steve； C. Lee Giles （1999）. &quot;Accessibility of information on the web&quot;. Nature 400 （6740）： 107. doi：10.1038/21987.</p><p>[3] Junghoo Cho. Hector Garcia-Molina. Lawrence Page （1998）. Efficient Crawling Through URL Ordering. Computer Networks 30（1-7）： 161-172</p><p>[4] Najork， M. and Wiener， J. L. （2001）. Breadth-first crawling yields high-quality pages. In Proceedings of the 10th international Conference on World Wide Web （Hong Kong， May 01 - 05， 2001）. WWW &apos;01. ACM Press， 114-118.</p><p>[5] Serge Abiteboul， Mihai Preda， Gregory Cobena （2003）. Adaptive on-line page <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=128460918&amp;ss_c=ssc.citiao.link">importance</a> computation.International World Wide Web Conference archive. Proceedings of the 12th international conference on World Wide Web. ACM Press， 280-290.</p><p>[6] Boldi， Paolo； Massimo Santini， Sebastiano Vigna （2004）. &quot;Do Your Worst to Make the Best： Paradoxical Effects in PageRank Incremental Computations&quot;. Algorithms and Models for the Web-Graph. pp. 168–180.</p><p>[7] Ricardo Baeza-Yates， Carlos Castillo， Mauricio Marin， Andrea Rodriguez （2005）. Crawling a country： better strategies than breadth-first for web page ordering. International World Wide Web Conference archive Special interest tracks and posters of the 14th international conference on World Wide Web table of contents （ Chiba， Japan）. ACM Press， 864 - 872.</p><p>[8] Sh. Daneshpajouh， Mojtaba Mohammadi Nasiri， M. Ghodsi （2008）. A Fast <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=675801&amp;ss_c=ssc.citiao.link">Community</a> Based Algorithm for Generating Crawler Seeds Set， In Proceeding of 4th International Conference on Web Information Systems and Technologies （WEBIST-2008）， Funchal， Portugal， May 2008.</p><p>[9] Viv Cothey. Web-crawling reliability （2004）. Journal of the American Society for Information Science and Technology， 55（14）， pp 1228-1238.</p><p>[10] Menczer， F. （1997）. ARACHNID： Adaptive Retrieval Agents Choosing Heuristic Neighborhoods for Information Discovery. In D. Fisher， ed.， Machine Learning： Proceedings of the 14th International Conference （ICML97）. Morgan Kaufmann</p><p>[11] Menczer， F. and Belew， R.K. （1998）. Adaptive Information Agents in Distributed Textual Environments. In K. Sycara and M. Wooldridge （eds.） Proc. 2nd Intl. Conf. on Autonomous Agents （Agents &apos;98）. ACM Press</p><p>[12] Chakrabarti， S.， van den Berg， M.， and Dom， B. （1999）. Focused crawling： a new approach to topic-specific web resource discovery. Computer Networks， 31（11–16）：1623–1640.</p><p>[13] Pinkerton， B. （1994）. Finding what people want： Experiences with the WebCrawler. In Proceedings of the First World Wide Web Conference， Geneva， Switzerland</p><p>[14] M. Diligenti， F.M. Coetzee， S. Lawrence， C.L. Giles， M. Gori （2000）. Focused Crawling Using Context Graphs. 26th International Conference on Very Large Databases，VLDB2000.</p><p>[15] Nelson， Michael L； Herbert Van de Sompel， Xiaoming Liu， Terry L Harrison， Nathan McFarland （2005）. &quot;mod_oai： An <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=25672&amp;ss_c=ssc.citiao.link">Apache</a> Module for Metadata Harvesting&quot;. Cs/0503069.</p><p>[16] Junghoo Cho. Hector Garcia-Molina （2000）. Synchronizing a database to improve freshness. ACM SIGMOD Record archive. Volume 29 ， Issue 2 （June 2000） table of contents. Pages： 117 - 128.</p><p>[17] Jr， E. G. Coffman； Zhen Liu， Richard R. Weber （1998）. &quot;Optimal robot scheduling for Web search engines&quot;. Journal of Scheduling 1 （1）： 15–29.</p><p>[18] Junghoo Cho. Hector Garcia-Molina （2003）. Effective page refresh policies for Web crawlers. ACM Transactions on Database Systems （TODS）. Pages： 390 - 426.</p><p>[19] Cho， Junghoo； Hector Garcia-Molina （2003）. &quot;Estimating <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=10758244&amp;ss_c=ssc.citiao.link">frequency</a> of change&quot;. ACM Trans. Interet Technol. 3 （3）： 256–290.</p><p>[20] Ipeirotis， P.， Ntoulas， A.， Cho， J.， Gravano， L. （2005） Modeling and managing content changes in text databases. In Proceedings of the 21st IEEE International Conference on Data Engineering， pages 606-617， April 2005， Tokyo.</p><p>[21] M. Koster （1995）. Robots in the web：threat or treat？ OII Spectrum， 1995， vol. 2， no9， pp. 8-18.</p><p>[22] M. Koster （1996）. The Web Robots Page. <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=1288013&amp;ss_c=ssc.citiao.link">Available</a> at http：//info./mak/projects/robots/robots.html.</p><p>[23] Koster， M. （1993）. Guidelines for robots writers.</p><p>[24] Baeza-Yates， R. and Castillo， C. （2002）. Balancing volume， quality and freshness in Web crawling. In Soft <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=72042942&amp;ss_c=ssc.citiao.link">Computing</a> Systems – Design， Management and Applications， pages 565–572， Santiago， Chile. IOS Press <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=64959781&amp;ss_c=ssc.citiao.link">Amsterdam</a>.</p><p>[25] Heydon， Allan； Najork， Marc （1999） . Mercator： A Scalable， Extensible Web Crawler. http：//www./cybermetrics/pdf/68.pdf.</p><p>[26] Dill， S.， Kumar， R.， Mccurley， K. S.， Rajagopalan， S.， Sivakumar， D.， and Tomkins， A. （2002）. Self-similarity in the web. ACM Trans. Inter. Tech.， 2（3）：205–223.</p><p><b>网络爬虫体系结构</b></p><p>网页爬虫的高层体系结构。</p><p><span class="text_img ed_imgfloat_right" style="width: 220px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212103555-1049286319.jpg" target="_blank"><img title="网络爬虫体系结构" alt="" src="http://pic.baike.soso.com/ugc/baikepic/27619/cut-20140212103611-2019292641.jpg/0" width="220" height="165"/></a><span>网络爬虫体系结构</span></span>一个爬虫不能像上面所说的，仅仅只有一个好的抓取策略，还需要有一个高度优化的结构。</p><p>Shkapenyuk和Suel（Shkapenyuk和Suel，2002）指出：设计一个短时间内，一秒下载几个页面的颇慢的爬虫是一件很容易的事情，而要设计一个使用几周可以下载百万级页面的高性能的爬虫，将会在系统设计，I/O和网络效率，健壮性和易用性方面遇到众多挑战。</p><p>网路爬虫是搜索引擎的核心，他们算法和结构上的细节被当作商业机密。当爬虫的设计发布时，总会有一些为了阻止别人复制工作而缺失的细节。人们也开始关注主要用于阻止主要搜索引擎发布他们的排序算法的“<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=73562&amp;ss_c=ssc.citiao.link">搜索引擎垃圾</a>邮件”。</p><p>2.1 URL一般化</p><p>爬虫通常会执行几种类型的URL规范化来避免重复抓取某些资源。URL一般化也被称为URL标准化，指的是修正URL并且使其前后一致的过程。这里有几种一般化方法，包括转化URL为小写的，去除逗号（如‘.’ ‘..’等），对非空的路径，在末尾加反斜杠。</p><p><b>爬虫身份识别</b></p><p>网络爬虫通过使用<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=170142&amp;ss_c=ssc.citiao.link">http请求</a>的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=8819996&amp;ss_c=ssc.citiao.link">用户代理</a>字段来向网络服务器表明他们的身份。<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=795592&amp;ss_c=ssc.citiao.link">网络管理员</a>则通过检查网络服务器的日志，使用用户代理字段来辨认哪一个爬虫曾经访问过以及它访问的频率。用户代理字段可能会包含一个可以让管理员获取爬虫更多信息的URL。邮件抓取器和其他怀有恶意的网络爬虫通常不会留任何的用户代理字段内容，或者他们也会将他们的身份伪装成浏览器或者其他的知名爬虫。</p><p>对于网路爬虫，留下用户标志信息是十分重要的；这样，网络管理员在需要的时候就可以联系爬虫的主人。有时，爬虫可能会陷入爬虫陷阱或者是一个服务器超负荷，这时，爬虫主人需要使爬虫停止。对那些有兴趣了解特定爬虫访问时间网络管理员来讲，<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=66376921&amp;ss_c=ssc.citiao.link">用户标识</a>信息是十分重要的。</p><p><b>用户爬虫的例子</b></p><p>以下是一系列已经发布的一般用途的网络爬虫（除了主题检索的爬虫）的体系结构，包括了对不同组件命名和突出特点的简短的描述。</p><p> RBSE （Eichmann，1994）是第一个发布的爬虫。它有两个基础程序。第一个是“spider”，抓取队列中的内容到一个<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=277136&amp;ss_c=ssc.citiao.link">关系数据库</a>中，第二个程序是“mite”，是一个修改后的www的ASCII浏览器，负责从网络上下载页面。</p><p> WebCrawler（Pinkerton，1994）是第一个公开可用的 用来建立<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=53823344&amp;ss_c=ssc.citiao.link">全文索引</a>的一个<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7539248&amp;ss_c=ssc.citiao.link">子程序</a>，他使用库www来下载页面；另外一个程序使用广度优先来解析获取URL并对其排序；它还包括一个根据选定文本和查询相似程度爬行的实时爬虫。</p><p> World Wide Web Worm （McBryan， 1994）是一个用来为文件建立包括标题和URL简单索引的爬虫。索引可以通过<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7865683&amp;ss_c=ssc.citiao.link">grep</a>式的Unix命令来搜索。</p><p> Google Crawler （Brin and Page， 1998）用了一些细节来描述，但是这些细节仅仅是关于使用C++和<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=58828&amp;ss_c=ssc.citiao.link">Python</a>编写的、一个早期版本的体系结构。因为文本解析就是<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=8446516&amp;ss_c=ssc.citiao.link">全文检索</a>和URL抽取的过程，所以爬虫集成了索引处理。这里拥有一个URL服务器，用来给几个爬虫程序发送要抓取的URL列表。在文本解析的时候，新发现的URL传送给URL服务器并检测这个URL是不是已经存在，如果不存在的话，该URL就加入到URL服务器中。</p><p> <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=69114299&amp;ss_c=ssc.citiao.link">CobWeb</a> （da Silva et al.， 1999）使用了一个中央“调度者”和一系列的“分布式的搜集者”。搜集者解析下载的页面并把找到的URL发送给调度者，然后调度者反过来分配给搜集者。调度者使用深度优先策略，并且使用平衡礼貌策略来避免服务器超载。爬虫是使用<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=126312&amp;ss_c=ssc.citiao.link">Perl</a>语言编写的。</p><p> Mercator （Heydon and Najork， 1999； Najork and Heydon， 2001）是一个分布式的，模块化的使用java编写的网络爬虫。它的模块化源自于使用可互换的的“协议模块”和“处理模块”。协议模块负责怎样获取网页（例如使用HTTP），处理模块负责怎样处理页面。标准处理模块仅仅包括了解析页面和抽取URL，其他处理模块可以用来检索文本页面，或者搜集网络数据。</p><p> WebFountain （Edwards et al.， 2001）是一个与Mercator类似的分布式的模块化的爬虫，但是使用C++编写的。它的特点是一个管理员机器控制一系列的蚂蚁机器。经过多次下载页面后，页面的变化率可以推测出来，这时，一个非线性的方法必须用于求解方程以获得一个最大的新鲜度的访问策略。作者推荐在早期检索阶段使用这个爬虫，然后用统一策略检索，就是所有的页面都使用相同的频率访问。</p><p> PolyBot [Shkapenyuk and Suel， 2002]是一个使用C++和Python编写的分布式网络爬虫。它由一个爬虫管理者，一个或多个下载者，一个或多个<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7547902&amp;ss_c=ssc.citiao.link">DNS解析</a>者组成。抽取到的URL被添加到硬盘的一个队列里面，然后使用<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=171812&amp;ss_c=ssc.citiao.link">批处理</a>的模式处理这些URL。平衡礼貌方面考虑到了第二、三级网域，因为第三级网域通常也会保存在同一个网络服务器上。</p><p> WebRACE （Zeinalipour-Yazti and Dikaiakos， 2002）是一个使用java实现的，拥有检索模块和缓存模块的爬虫，它是一个很通用的称作eRACE的系统的一部分。系统从用户得到下载页面的请求，爬虫的行为有点像一个聪明的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=15561&amp;ss_c=ssc.citiao.link">代理服务器</a>。系统还监视订阅网页的请求，当网页发生改变的时候，它必须使爬虫下载更新这个页面并且通知订阅者。WebRACE最大的特色是，当大多数的爬虫都从一组URL开始的时候，WebRACE可以连续地的接收抓取开始的URL地址。</p><p> Ubicrawer （Boldi et al.， 2004）是一个使用java编写的分布式爬虫。它没有中央程序。它有一组完全相同的代理组成，分配功能通过主机前后一致的散列计算进行。这里没有重复的页面，除非爬虫崩溃了（然后，另外一个代理就会接替崩溃的代理重新开始抓取）。爬虫设计为高伸缩性和允许失败的。</p><p> FAST Crawler （Risvik and Michelsen， 2002） 是一个分布式的爬虫，在Fast Search&amp;Transfer中使用，关于其体系结构的一个大致的描述可以在[citation needed]找到。</p><p> Labrador，一个工作在开源项目Terrier Search Engine上的非开源的爬虫。</p><p> TeezirCrawler是一个非开源的可伸缩的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=57226307&amp;ss_c=ssc.citiao.link">网页抓取</a>器，在Teezir上使用。该程序被设计为一个完整的可以处理各种类型网页的爬虫，包括各种<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=2484&amp;ss_c=ssc.citiao.link">JavaScript</a>和HTML文档。爬虫既支持主题检索也支持非主题检索。</p><p> Spinn3r， 一个通过博客构建反馈信息的爬虫。 Spinn3r是基于java的，它的大部分的体系结构都是开源的。</p><p> HotCrawler，一个使用c语言和php编写的爬虫。</p><p> ViREL Microformats Crawler，搜索公众信息作为嵌入到网页的一小部分。</p><p>除了上面列出的几个特定的爬虫结构以外，还有Cho （Cho and Garcia-Molina， 2002）和Chakrabarti （Chakrabarti， 2003）发布的一般的爬虫体系结构。</p><p>4.1 开源爬虫</p><p> DataparkSearch是一个在GNU GPL许可下发布的爬虫搜索引擎。</p><p> GNU Wget是一个在GPL许可下，使用C语言编写的命令行式的爬虫。它主要用于网络服务器和<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=449752&amp;ss_c=ssc.citiao.link">FTP服务器</a>的镜像。</p><p> <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=10500910&amp;ss_c=ssc.citiao.link">Heritrix</a>是一个<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=21620&amp;ss_c=ssc.citiao.link">互联网档案馆</a>级的爬虫，设计的目标为对大型网络的大部分内容的定期存档快照，是使用java编写的。</p><p> Ht：//Dig在它和索引引擎中包括了一个网页爬虫。</p><p> HTTrack用网络爬虫创建网络站点镜像，以便<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=71855911&amp;ss_c=ssc.citiao.link">离线观看</a>。它使用C语言编写，在GPL许可下发行。</p><p> ICDL Crawler是一个用C++编写，跨平台的网络爬虫。它仅仅使用空闲的CPU资源，在ICDL标准上抓取整个站点。</p><p> JSpider是一个在GPL许可下发行的，高度可配置的，可定制的网络爬虫引擎。</p><p> LLarbin由Sebastien Ailleret开发；</p><p> Webtools4larbin由Andreas Beder开发；</p><p> Methabot是一个使用C语言编写的高速优化的，使用命令行方式运行的，在2-clause BSD许可下发布的网页检索器。它的主要的特性是高可配置性，模块化；它检索的目标可以是本地文件系统，HTTP或者FTP。</p><p> <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=9242267&amp;ss_c=ssc.citiao.link">Nutch</a>是一个使用java编写，在Apache许可下发行的爬虫。它可以用来连接<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=123773&amp;ss_c=ssc.citiao.link">Lucene</a>的全文检索套件；</p><p> Pavuk是一个在GPL许可下发行的，使用命令行的WEB站点镜像工具，可以选择使用X11的图形界面。与wget和httprack相比，他有一系列先进的特性，如以<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=107588&amp;ss_c=ssc.citiao.link">正则表达式</a>为基础的文件过滤规则和文件创建规则。</p><p> WebVac是斯坦福WebBase项目使用的一个爬虫。</p><p> WebSPHINX（Miller and Bharat， 1998）是一个由java类库构成的，基于文本的搜索引擎。它使用多线程进行网页检索，html解析，拥有一个<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=64893102&amp;ss_c=ssc.citiao.link">图形用户界面</a>用来设置开始的种子URL和抽取下载的数据；</p><p> WIRE-网络信息检索环境（Baeza-Yates 和 Castillo， 2002）是一个使用C++编写，在GPL许可下发行的爬虫，内置了几种页面下载安排的策略，还有一个生成报告和统计资料的模块，所以，它主要用于网络特征的描述；</p><p> <a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=10654612&amp;ss_c=ssc.citiao.link">LWP</a>：RobotUA（Langheinrich，2004）是一个在Perl5许可下发行的，可以优异的完成并行任务的 Perl类库构成的机器人。</p><p> Web Crawler是一个为.net准备的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=269184&amp;ss_c=ssc.citiao.link">开放源代码</a>的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=711069&amp;ss_c=ssc.citiao.link">网络检索</a>器（C#编写）。</p><p> Sherlock Holmes收集和检索本地和网络上的文本类数据（文本文件，网页），该项目由捷克门户网站中枢（Czech web portal Centrum）赞助并且主用商用于这里；它同时也使用在。</p><p>YaCy是一个基于P2P网络的免费的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=70226213&amp;ss_c=ssc.citiao.link">分布式搜索引擎</a>（在GPL许可下发行）；</p><p> Ruya是一个在广度优先方面表现优秀，基于等级抓取的开放源代码的网络爬虫。在英语和日语页面的抓取表现良好，它在GPL许可下发行，并且完全使用Python编写。按照robots.txt有一个延时的单网域延时爬虫。</p><p> Universal Information Crawler快速发展的网络爬虫，用于检索存储和分析数据；</p><p> Agent Kernel，当一个爬虫抓取时，用来进行安排，并发和存储的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=207266&amp;ss_c=ssc.citiao.link">java框架</a>。</p><p> 是一个使用C#编写，需要SQL Server 2005支持的，在GPL许可下发行的多功能的开源的机器人。它可以用来下载，检索，存储包括电子邮件地址，文件，超链接，图片和网页在内的各种数据。</p><p> Dine是一个多线程的java的http客户端。它可以在<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=101485950&amp;ss_c=ssc.citiao.link">LGPL</a>许可下进行二次开发。</p><p><b>网络爬虫的组成</b></p><p>在网络爬虫的系统框架中，主过程由控制器，解析器，资源库三部分组成。控制器的主要工作是负责给多线程中的各个爬虫线程分配工作任务。解析器的主要工作是下载网页，进行页面的处理，主要是将一些<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7857410&amp;ss_c=ssc.citiao.link">JS脚本</a>标签、CSS代码内容、空格字符、<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=340826&amp;ss_c=ssc.citiao.link">HTML标签</a>等内容处理掉，爬虫的基本工作是由解析器完成。资源库是用来存放下载到的网页资源，一般都采用大型的数据库存储，如<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=449760&amp;ss_c=ssc.citiao.link">Oracle数据库</a>，并对其建立索引。</p><p>【控制器】</p><p>控制器是网络爬虫的<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7906925&amp;ss_c=ssc.citiao.link">中央控制器</a>，它主要是负责根据系统传过来的URL链接，分配一线程，然后启动线程调用爬虫爬取网页的过程。</p><p>【解析器】</p><p>解析器是负责网络爬虫的主要部分，其负责的工作主要有：下载网页的功能，对网页的文本进行处理，如过滤功能，抽取特殊HTML标签的功能，分析数据功能。</p><p>【资源库】</p><p>主要是用来存储网页中下载下来的数据记录的容器，并提供生成索引的目标源。中大型的数据库产品有：Oracle、Sql Server等。</p>
								</div>
							</div>
						</section><section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="7" id="7"></a>
									<a name="para7" id="para7">
										相关新闻
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="7" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=7" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><b>美情报官员透露：斯诺登凭“网络爬虫”小技获机密<sup><a href="#quote3">[3]</a><a name="ref_3"></a></sup></b> </p><p><span class="text_img ed_imgfloat_right" style="width: 220px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/p/20140212/20140212095041-681549053.jpg" target="_blank"><img title="斯诺登" alt="" src="http://pic.baike.soso.com/ugc/baikepic/23282/cut-20140212095050-1614972692.jpg/0" width="220" height="165"/></a><span>斯诺登</span></span> </p><p>2014年2月9日正在调查“<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=60470691&amp;ss_c=ssc.citiao.link">棱镜门</a>”事件的美国情报官员透露，前防务承包商雇员爱德华•斯诺登只凭借比较简单的“网络爬虫”技术就获取了大量机密文件。</p><p> 《<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=184019&amp;ss_c=ssc.citiao.link">纽约时报</a>》援引了多名不愿公开身份情报官员的消息。据报道，经调查发现，斯诺登所使用的是比较廉价、也容易获取的“网络爬虫”或爬行器类软件，通过程序设定自动抓取大量数据，而不是一个人坐在电脑前一一查找、复制、下载大量文件。 </p><p>国家安全局官员坚称，如果斯诺登当时是在国安局位于马里兰州的总部工作，由于总部监控体系可以自动监测到有人获取和下载大量数据的行为，他恐怕早就被锁定和抓获，但他当时所在的夏威夷站点还未能更新监控系统。 </p><p>据报道，斯诺登获取大量数据当时还是一度引起注意，他也为此事接受过多次内部质询，但他辩称自己作为技术承包商雇员只是在进行例行系统维护，凭这一理由蒙混过关。</p>
								</div>
							</div>
						</section><section>
							<div class="section_title">
								<h2>
									<!-- 为了兼容以前的锚点而设置的 -->
									<a name="8" id="8"></a>
									<a name="para8" id="para8">
										搜索策略
									</a>
								</h2>
								<a onclick="return beforeEditCheck(this);" paragraphId="8" href="/Create.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=2&amp;sp=l77860&amp;sp=8" title="编辑本段" class="btn_edit"><i></i>编辑</a>
							</div> <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
									<p><span class="text_img ed_imgfloat_right" style="width: 300px"><a class="ed_image_link" title="点击查看大图" href="http://pic.baike.soso.com/ugc/baikepic2/7247/20170908202315-1755846338_png_352_273_49599.jpg/0" target="_blank"><img title="网络爬虫" alt="" src="http://pic.baike.soso.com/ugc/baikepic2/7247/20170908202315-1755846338_png_352_273_49599.jpg/300" width="300" height="233"/></a><span>网络爬虫</span></span>网页的抓取策略可以分为深度优先、广度优先和最佳优先三种。深度优先在很多情况下会导致爬虫的陷入(trapped)问题，目前常见的是广度优先和最佳优先方法。 </p>
								</div>
							</div>
						</section><section>
							 <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
            <a name="para9" id="para9"></a>
            <h3>广度优先搜索策略</h3>
        
									<p><a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=7085366&amp;ss_c=ssc.citiao.link">广度优先搜索</a>策略是指在抓取过程中，在完成当前层次的搜索后，才进行下一层次的搜索。该算法的设计和实现相对简单。在目前为覆盖尽可能多的网页，一般使用广度优先搜索方法。也有很多研究将广度优先搜索策略应用于聚焦爬虫中。其基本思想是认为与初始URL在一定链接距离内的网页具有主题相关性的概率很大。另外一种方法是将广度优先搜索与网页过滤技术结合使用，先用广度优先策略<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=57226307&amp;ss_c=ssc.citiao.link">抓取网页</a>，再将其中无关的网页过滤掉。这些方法的缺点在于，随着抓取网页的增多，大量的无关网页将被下载并过滤，算法的效率将变低。</p>
								</div>
							</div>
						</section><section>
							 <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
            <a name="para10" id="para10"></a>
            <h3>最佳优先搜索策略</h3>
        
									<p>最佳优先搜索策略按照一定的网页分析算法，预测候选URL与目标网页的相似度，或与主题的相关性，并选取评价最好的一个或几个URL进行抓取。它只访问经过网页分析算法预测为“有用”的网页。存在的一个问题是，在爬虫抓取路径上的很多相关网页可能被忽略，因为最佳优先策略是一种局部最优<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=39055688&amp;ss_c=ssc.citiao.link">搜索算法</a>。因此需要将最佳优先结合具体的应用进行改进，以跳出局部最优点。将在第4节中结合网页分析算法作具体的讨论。研究表明，这样的闭环调整可以将无关网页数量降低30%~90%。</p>
								</div>
							</div>
						</section><section>
							 <!-- section_title -->
							<div class="section_content">
								<div class="rich_text_area">
									<!-- 二级标题 -->
									
            <a name="para11" id="para11"></a>
            <h3>深度优先搜索策略</h3>
        
									<p><a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=5920602&amp;ss_c=ssc.citiao.link">深度优先搜索</a>策略从起始网页开始，选择一个URL进入，分析这个网页中的URL，选择一个再进入。如此一个链接一个链接地抓取下去，直到处理完一条路线之后再处理下一条路线。<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=67302516&amp;ss_c=ssc.citiao.link">深度优先策略</a>设计较为简单。然而门户网站提供的链接往往最具价值，<a class="ed_inner_link" target="_blank" href="/lemma/ShowInnerLink.htm?lemmaId=234075&amp;ss_c=ssc.citiao.link">PageRank</a>也很高，但每深入一层，网页价值和PageRank都会相应地有所下降。这暗示了重要网页通常距离种子较近，而过度深入抓取到的网页却价值很低。同时，这种策略抓取深度直接影响着抓取命中率以及抓取效率，对抓取深度是该种策略的关键。相对于其他两种策略而言。此种策略很少被使用。</p>
								</div>
							</div>
						</section>
					</div> <!-- section_wrap -->
				</div> <!-- lemma_detail_wrap -->

				<!-- 街景 -->
				<div class="lemma_landscape" style="display:none">
					<div class="section_title">
						<h2><a id="paralandScape" name="paralandScape">街景地图</a></h2>
						<a id="j-count-map" href="javascript:;" target="_blank" title="去腾讯地图查看更多街景">
							<span class="source"><i class="ico_t_map"></i>去腾讯地图查看更多街景</span></a>
					</div>
					<div class="landscape_wrap" style="width:710px;height:400px">
					</div>
				</div><!-- 街景 -->

				<!-- 图册 -->
				<div class="album_container_wrap"></div>
				<!-- 词条关系 已废弃 2014.10.30-->
				<!--<span jwcid="@lemmaRelation/LemmaRelationComponent" lemmaTitle="prop:title"></span>-->

				<!--参考资料-->
				<div class="lemma_relevant relevant_consult">
					<div class="title_wrap">
						<h3>参考资料：</h3>
					</div>
					<div class="relevant_wrap">
						<span class="list_number">1.</span>
						<div class="data_wrap">
							<!-- <span jwcid="@If" condition="ognl: ref.type != null"> -->
							
		                            
		                              <!-- <p><a jwcid="@Any" target="_blank" href="ognl:ref.href"><span jwcid="@SizeInsert" value="ognl:ref.href" size="75"/></a></p> -->
		                            	<p class="relevant_item">
				                            <span><a name="quote1" id="quote1" href="http://soft.chinabyte.com/database/438/12832438.shtml" title="网络爬虫概述" class="relevant_link" target="_blank">网络爬虫概述</a></span>
				                            
				                                <a href="#ref_1" title="跳转到文中引用处" class="icoQuoteJump"></a>
				                            
                                        </p>
                                        
		                            
		                            
		                        
							
							<!-- </span> -->
						</div>
						
                            <span class="relevant_from">
                                
                                
                                
                            </span>
                        
					</div><div class="relevant_wrap">
						<span class="list_number">2.</span>
						<div class="data_wrap">
							<!-- <span jwcid="@If" condition="ognl: ref.type != null"> -->
							
		                            
		                              <!-- <p><a jwcid="@Any" target="_blank" href="ognl:ref.href"><span jwcid="@SizeInsert" value="ognl:ref.href" size="75"/></a></p> -->
		                            	<p class="relevant_item">
				                            <span><a name="quote2" id="quote2" href="http://www.kuqin.com/searchengine/20071111/2272.html" title="网络爬虫技术相关介绍" class="relevant_link" target="_blank">网络爬虫技术相关介绍</a></span>
				                            
				                                <a href="#ref_2" title="跳转到文中引用处" class="icoQuoteJump"></a>
				                            
                                        </p>
                                        
		                            
		                            
		                        
							
							<!-- </span> -->
						</div>
						
                            <span class="relevant_from">
                                
                                
                                
                            </span>
                        
					</div><div class="relevant_wrap">
						<span class="list_number">3.</span>
						<div class="data_wrap">
							<!-- <span jwcid="@If" condition="ognl: ref.type != null"> -->
							
		                            
		                              <!-- <p><a jwcid="@Any" target="_blank" href="ognl:ref.href"><span jwcid="@SizeInsert" value="ognl:ref.href" size="75"/></a></p> -->
		                            	<p class="relevant_item">
				                            <span><a name="quote3" id="quote3" href="http://news.xinhuanet.com/2014-02/10/c_126104709.htm" title="美报说斯诺登凭简单技术获取大量机密文件" class="relevant_link" target="_blank">美报说斯诺登凭简单技术获取大量机密文件</a></span>
				                            
				                                <a href="#ref_3" title="跳转到文中引用处" class="icoQuoteJump"></a>
				                            
                                        </p>
                                        
		                            
		                            
		                        
							
							<!-- </span> -->
						</div>
						
                            <span class="relevant_from">
                                
                                
                                
                            </span>
                        
					</div>
				</div><!--lemma_relevant-->

				<!--扩展阅读-->
				<div ch="ch.bk.extended" class="lemma_relevant relevant_extend">
					<div class="title_wrap">
						<h3>扩展阅读：</h3>
					</div>
					<div class="relevant_wrap">
						<span class="list_number">1.</span>
						<div class="data_wrap">
                            
                                <p class="relevant_item"><a href="http://www.guancha.cn/Science/2013_12_14_192613.shtml" title="互联网上，人类只是少数派，爬虫毁灭世界" class="relevant_link" target="_blank"><span>互联网上，人类只是少数派，爬虫毁灭世界</span></a></p>
                            
							
						</div>
						
					</div><div class="relevant_wrap">
						<span class="list_number">2.</span>
						<div class="data_wrap">
                            
                                <p class="relevant_item"><a href="http://cq.cqnews.net/sz/2012-08/07/content_18351513.htm" title="重庆建&quot;网上消费维权服务站&quot; &quot;网络爬虫&quot;监管电商" class="relevant_link" target="_blank"><span>重庆建"网上消费维权服务站" "网络爬虫"监管电商</span></a></p>
                            
							
						</div>
						
					</div><div class="relevant_wrap">
						<span class="list_number">3.</span>
						<div class="data_wrap">
                            
                                <p class="relevant_item"><a href="http://www.edu.cn/lun_wen_zhai_bao_1089/20101203/t20101203_548515.shtml" title="基于Heritrix网络爬虫算法的研究与应用" class="relevant_link" target="_blank"><span>基于Heritrix网络爬虫算法的研究与应用</span></a></p>
                            
							
						</div>
						
					</div>
				</div><!--lemma_relevant-->

				<!--词条标签：-->
				<div ch="ch.bk.tags" class="lemma_relevant">
					<div class="title_wrap">
						<h3>词条标签：</h3>
					</div>
					<div class="relevant_wrap">
                      
                        <a href="/Search.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=S%E7%BD%91%E7%BB%9C%E7%9F%A5%E8%AF%86&amp;sp=1" target="_blank" class="lemma_tag">
                          网络知识
                        </a>
                      
                        <a href="/Search.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=S%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&amp;sp=1" target="_blank" class="lemma_tag">
                          网络爬虫
                        </a>
                      
                        <a href="/Search.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=S%E6%90%9C%E7%B4%A2&amp;sp=1" target="_blank" class="lemma_tag">
                          搜索
                        </a>
                      
                        <a href="/Search.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=SSEO&amp;sp=1" target="_blank" class="lemma_tag">
                          SEO
                        </a>
                      
					</div>
				</div><!--lemma_relevant-->

				<script type="text/javascript" src="//cache.soso.com/baike/js/json_201202142237.js"></script>
				<script type="text/javascript" src="//cache.soso.com/baike/js/sbjl_core_201202142215.js"></script>
				<script type="text/javascript" src="//cache.soso.com/baike/js/editorDialog_201710192103.js"></script>
				<script type="text/javascript" src="//cache.soso.com/baike/js/PageActions_201706281513.js"></script>

				<!-- 词条评价与免责声明
                <span jwcid="@lemma:ShowLemmaEvaluateStar" lemmaId="prop:lemmaId" score="prop:score"></span> -->

				<!--合作编辑者-->
				<div class="lemma_relevant">
	<div class="title_wrap">
    	<h3>合作编辑者：</h3>
	</div>
    <div class="relevant_wrap">				
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_cc92664f644a64b8f5d8731eb479b0ba" data-uid="u_cc92664f644a64b8f5d8731eb479b0ba" title="walking dead" class="showEditorInfo" target="_blank">
				walking dead
				
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="true" href="/usercenter/home.v?uid=u_3477d9c87dc685d886fd3168b8bcf2e3" data-uid="u_3477d9c87dc685d886fd3168b8bcf2e3" title="紫伦" class="showEditorInfo" target="_blank">
				紫伦
				
				
					<i class="user_tag" title="公益之星"></i>
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_a13995c4349069914c6cdd871d088dfe" data-uid="u_a13995c4349069914c6cdd871d088dfe" title="牛魔王变身指环" class="showEditorInfo" target="_blank">
				牛魔王变身指环
				
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_3d0448e581afb2eb01aa4cd1534b0524" data-uid="u_3d0448e581afb2eb01aa4cd1534b0524" title="校讯-艺设" class="showEditorInfo" target="_blank">
				校讯-艺设
				
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_eaf0addd249b3bf30283b9cc20e8f18c" data-uid="u_eaf0addd249b3bf30283b9cc20e8f18c" title="百科用户" class="showEditorInfo" target="_blank">
				百科用户
				
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_5ca26c63e091e7028fb9e976de396c74" data-uid="u_5ca26c63e091e7028fb9e976de396c74" title="一片空白" class="showEditorInfo" target="_blank">
				一片空白
				
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_290a8cd2756e7bbf85ccfe5edd4811a0" data-uid="u_290a8cd2756e7bbf85ccfe5edd4811a0" title="百科用户" class="showEditorInfo" target="_blank">
				百科用户
				
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_81121d0022e2064ba288ed1fe014795f" data-uid="u_81121d0022e2064ba288ed1fe014795f" title="百科用户" class="showEditorInfo" target="_blank">
				百科用户
				
				
			</a>
		
	

	    	，  
	    
	    	<!-- <span jwcid="@application:UserLinkWithCh" userName="ognl:history.editorName" userId="ognl:history.editorId" ch="ch.bk.uc.coeditors"/>-->
	    	
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_48607b6abb927cb8bee682605d2310ae" data-uid="u_48607b6abb927cb8bee682605d2310ae" title="无" class="showEditorInfo" target="_blank">
				无
				
				
			</a>
		
	

	    	，  
	    
	    
	    	<a href="/ShowHistory.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=l77860" class="more">更多</a>
	    
	</div>
</div>


				<!--免责声明 start-->
				<div class="lemma_relevant">
					<div class="statement">
						<div class="statement_wrap">
							<h2 class="statement_title">免责声明</h2>
							<span class="statement_left"></span>
							<p class="statement_txt">
								搜狗百科词条内容由用户共同创建和维护，不代表搜狗百科立场。如果您需要医学、法律、投资理财等专业领域的建议，我们强烈建议您独自对内容的可信性进行评估，并咨询相关专业人士。
							</p>
							<span class="statement_right"></span>
						</div>
					</div>
				</div>
				<!--免责声明 end-->

			</div> <!-- lemma_container -->
			<!--</div>  lemma_wrap -->



			<!-- 边栏 -->
			<div class="side_bar" id="side_bar">
    



				<!--教师送花按钮-->
				<div id="j-teacher-flower-btn"></div>
				<!--教师献花学生排行榜-->
				<div id="j-teacher-student-list"></div>

				

				

				<!--图书-->
				<!--图书口碑-->
				<div id="j-book-module"></div>
				<!--图书热评-->
				<div id="j-book-comment"></div>
				<!--看了又看-->
				<div id="j-book-view"></div>
				<!--图书排行榜-->
				<div id="j-book-rank"></div>
				<!--图书结束-->






				<!-- <span jwcid="@If" condition="prop:showRelative">
                  <span jwcid="@lemma:ShowRelativeLemma" resultList="prop:resultList" />
                </span> -->


				<!--相关词条-->
				<span id = "side_bar_before_baike"></span>
				<!--lemmaTaken-->
				
				<!--问问模块-->
				<div id="j-wenwen-module"></div>

				<!--微博秀-->
				<div class="side_column_wrap hidden" id="side-module-weibo">
					<div class="title_wrap">
						<h3>名人说</h3>
					</div>
					<div class="lemma_info" style="overflow: hidden;width: 230px;">
					</div>
				</div>
				<!--微博秀-->

				<!-- 权威认证 -->
				

				<div class="side_column_wrap">
					<div class="title_wrap">
						<h3>词条信息</h3>
					</div>

					<div class="lemma_info">
						<ul class="lemma_data">
							<li><span>创建者：</span>
	
	
	
		
		
			<a publicStar="false" href="/usercenter/home.v?uid=u_9f61909cc648403d2fcbbdb55a38263e" data-uid="u_9f61909cc648403d2fcbbdb55a38263e" title="吹泡泡的兔子" class="showEditorInfo" target="_blank">
				吹泡泡的兔子
				
				
			</a>
		
	
</li>
							
							<li><span>编辑次数：</span><em><a href="/ShowHistory.e;jsessionid=8EA4987CE03FB0A8DB3D608FE8512AF0?sp=l77860" target="_blank">26&nbsp;次</a></em></li>
							<li><span>词条浏览：</span><em id="lemma_pv">66681&nbsp;次</em></li>
							<li><span>最近更新：</span>17.11.08</li>
							
						</ul>

						<!-- 词条分享 -->
						
					</div>
				</div>  <!--side_column_wrap-->



				<!--AD-->
				<div class="side_column_wrap hidden" id="side-module-ad"></div>

				<!--
                <div class="side_banner">
                    <a href="http://wenwen.soso.com/z/2014.html?ch=ww.bk.2014"  target="_blank"><img src="//cache.soso.com/baike/news_baike/star/150x90.jpg" /></a>
                </div>
                -->
				<!-- for element locate -->
				<span id = "side_bar_last_anchor"></span>

			</div>
			<!--side_bar-->

		</div> <!-- main_wrap -->

		<!-- 边栏 -->
		<div id="floatLayer" class="float_layer">
			<div class="side_catalogue">
				<a id="sideNavBtnPrev" class="btn_up" href="javascript:;"><i></i></a>
				<div class="side_catalog_wrap">
					<ul id="sideNavListWrap">
          
             <li>
                <a raw="true" href="#para1" title="相关介绍" class="headline1"><i></i>相关介绍</a>  
             </li>
             
          
             <li>
                <a raw="true" href="#para2" title="工作原理" class="headline1"><i></i>工作原理</a>  
             </li>
             
          
             <li>
                <a raw="true" href="#para3" title="技术研究" class="headline1"><i></i>技术研究</a>  
             </li>
             
          
             <li>
                <a raw="true" href="#para4" title="网页抓取" class="headline1"><i></i>网页抓取</a>  
             </li>
             
          
             <li>
                <a raw="true" href="#para5" title="网页分析" class="headline1"><i></i>网页分析</a>  
             </li>
             
          
             <li>
                <a raw="true" href="#para6" title="其他补充" class="headline1"><i></i>其他补充</a>  
             </li>
             
          
             <li>
                <a raw="true" href="#para7" title="相关新闻" class="headline1"><i></i>相关新闻</a>  
             </li>
             
          
             <li>
                <a raw="true" href="#para8" title="搜索策略" class="headline1"><i></i>搜索策略</a>  
             </li>
             
          
             
             <li>
                <a raw="true" href="#para9" title="广度优先搜索策略" class="headline2">广度优先搜索策略</a>
             </li>
          
             
             <li>
                <a raw="true" href="#para10" title="最佳优先搜索策略" class="headline2">最佳优先搜索策略</a>
             </li>
          
             
             <li>
                <a raw="true" href="#para11" title="深度优先搜索策略" class="headline2">深度优先搜索策略</a>
             </li>
          
					</ul>
				</div>
				<a id="sideNavBtnNext" class="btn_down dis_btn_down" href="javascript:;"><i></i></a>
			</div>
			<a id="back_top" class="back_top" href="javascript:;" title="返回顶部"><i></i></a>
		</div>

		<div class="innerlink_wrap" id="innerLinkFloatWrap" style="display:none">
			<div class="innerlink_content">
				<a id="innerLinkFloatImgLink" href="javascript:;" class="innerlink_pic"><img id="innerLinkFloatImg" src="" alt=""></a>
				<p id="innerLinkFloatAbstract">摘要<a id="innerLinkFloatMore" href="#">更多&gt;&gt;</a></p>
			</div>
		</div>
		<!-- 左文右图 -->
<script type="text/html" id="textImage_show">
<div class="txt-pic-wrap j-list-container">
  <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
  <div class="txt-pic j-list-item">
      <div class="tp-content">
        <p class="tp-txt"><%=m.description%></p>
      </div>
      <div class="tp-img">
        <a target="_blank" href="<%=m.media.bigSrc ? m.media.bigSrc : m.media.src%>" class="ed_image_link">
          <img width="158" src="<%=m.media.src%>">
        </a>
      </div>
  </div>
  <% } %>
  <a class="all-open hide" href="javascript:void(0);" maxrow="5" onclick="module.toggleList(this);return false"><span class="text">收起</span><i class="all-icon"></i></a>
</div>
</script>
<!-- 左图右文 -->
<script type="text/html" id="imageText_show">
<div class="txt-pic-wrap j-list-container">
  <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
  <div class="txt-pic txt-pic-left j-list-item">
      <div class="tp-content">
        <p class="tp-txt"><%=m.description%></p>
      </div>
      <div class="tp-img">
        <a target="_blank" href="<%=m.media.bigSrc ? m.media.bigSrc : m.media.src%>" class="ed_image_link">
          <img width="158" src="<%=m.media.src%>">
        </a>
      </div>
  </div>
  <% } %>
  <a class="all-open hide" href="javascript:void(0);" maxrow="5" onclick="module.toggleList(this);return false"><span class="text">收起</span><i class="all-icon"></i></a>
</div>
</script>
<!-- 角色介绍 -->
<script type="text/html" id="role_show">
<div class="character_wrap lemma_module_wrap">
  <ul class="character_list input_list_wrap">
    <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
    <li>
      <div class="pic_wrap">
        <a target="_blank" href="<%=m.media.bigSrc ? m.media.bigSrc : m.media.src%>" class="ed_image_link">
          <img width="158" src="<%=m.media.src%>">
        </a>
      </div>
      <div class="content">
        <div class="actor"><%=m.role%><%if(m.actor){%>（<%=m.actor%> 饰）<%}%><%if(m.dubbing){%>&nbsp;&nbsp;配音：<%=m.dubbing%><%}%> </div>
        <div class="intro"><%=m.description%></div>
      </div>
    </li>
    <% } %>
  </ul>
  <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" maxrow="5" onclick="module.toggleList(this);return false">收起</a></div>  
</div>
</script>
<!-- 综艺节目 -->
<script type="text/html" id="variety_show">
  <div class="lemma_module_wrap program_list layer_content">
      <div class="module_list_title">
        <span class="column column1">播出时间</span>
        <span class="column column2">节目名称</span>
        <span class="column column3">播出平台</span>
        <span class="column column4">简介</span>
      </div>
      <ul class="module_list input_list_wrap">
        <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
        <li>
            <div class="column column1"><%=m.time%></div>
            <div class="column column2"><%=m.name%></div>
            <div class="column column3"><%=m.platform || "----"%></div>
            <div class="column column4"><%=m.description || "----"%></div>
        </li>
        <%}%>    
      </ul>  
      <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>  
  </div>
</script>
<!-- artNet tpl -->
<script type="text/html" id="artNet_show" dataType="artNet">
<section class="work_wrap">
<div class="section_title">
<h2><a id="para_art" name="para_art">代表作品</a></h2>
<%var url = obj.url;%>
<a class="more artNet" target="_blank" href="<%=url%>">更多作品&gt;&gt;</a>
</div>
<div class="works_list">
<ul>
<%var l = Math.min(4, obj.content.length);%>
<%for(var i=0;i<l;i++){
  var src = obj.content[i].src;
    var bigSrc = obj.content[i].bigSrc;
    var title = obj.content[i].title;%>
  <li>
  <a class="pic_wrap ed_image_link" href="<%=bigSrc%>" target="_blank">
  <img width="162" height="162" src="<%=src%>"title="<%=title%>" alt="" />
  </a>
  </li>
<%}%>
</ul>
</div>
</section>
</script>

<!--greatEvent tpl-->
<script type="text/html" id="greatEvent_show" dataType="greatEvent">
<%if(!module_data.greatEvent.isFold){%>
  <%if(module_data.greatEvent.isDescend){obj.reverse();}%>
  <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
    <div class="record_unit" <% if (i > 3) {%>style="display:none"<%}%>>
      <i class="ico_dot"></i>
      <span class="arrow"></span>
      <h3 class="title"><%=m.time%></h3>
      <div class="content <% if(m.description.replace(/<[^<>]+>/g, '').length <= 150) {%>fewer_txt<%}%>">
          <h4><%=m.title%></h4>
          <% if(m.picUrl){ %>
          <span style="width: 218px" class="text_img ed_imgfloat_right"><a target="_blank" href="<%=m.picUrl%>" title="点击查看大图" class="ed_image_link"><img src="<%=m.picUrl%>" width="218" height="164"></a></span>
          <% }else if(m.mediaType == 'pic'){%>
          <span style="width: 218px" class="text_img ed_imgfloat_right">
              <a target="_blank" href="<%=m.media.bigSrc ? m.media.bigSrc : m.media.src%>" title="点击查看大图" class="ed_image_link">
                  <img src="<%=m.media.src%>" width="218" height="164">
              </a>
          </span>
          <% }else if(m.mediaType == 'album'){%>
          <span  style="width: 224px"  class="album_wrap ed_imgfloat_right"><span class="album_cover_wrap"><span class="album_cover_img"><a href="javascript" title="<%=m.media.title%>" class="ed_image_link" target="_blank"><img src="<%=m.media.coverUrl%>" width="218" height="164" data-id="<%=m.media.id%>" data-total="<%=m.media.total%>" alt="<%=m.media.title%>"></a></span><i class="ico_album"></i></span><span class="album_bg"></span><span class="album_bg_bottom"></span></span>
          <%}%>
          <p><%=m.description%></p>
      </div>
    </div>
  <%}%>
  <% if(obj.length > 4) {%>
    <div class="more_record">
      <i class="ico_dot"></i>
      <a class="more" href="javascript:;">查看更多<i class="arrow"></i></a>
    </div>
  <%}%>
<% }else if(module_data.greatEvent.isFold){%>
    <div class="record_title_wrap">
    <a class="btn_prev_record" href="javascript:;"><i></i></a>
    <div class="wrap">
      <ul class="title_list">
      <%if(module_data.greatEvent.isDescend){obj.reverse();}%>
      <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
      <%if(i == 0){%>
        <li class="current"><div class="title"><%=m.time%></div><i></i></li>
      <%}else{%>
        <li><div class="title"><%=m.time%></div><i></i></li>
      <%}%>
      <%}%>
      </ul>
    </div>
    <a class="btn_next_record" href="javascript:;"><i></i></a>
  </div>
  <div class="record_content_bg">
      <div class="record_content_wrap">
        <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
          <div class="content" <%if(i == 0){%>style="display:block;"<%}else{%>style="display:none;"<%}%>>
            <% if(m.picUrl){ %>
            <a target="_blank" href="<%=m.picUrl%>" class="pic_wrap ed_image_link">
              <img width="218" height="164" src="<%=m.picUrl%>">
            </a>
            <% }else if(m.mediaType == 'pic'){%>
            <a target="_blank" href="<%=m.media.bigSrc ? m.media.bigSrc : m.media.src%>" class="pic_wrap ed_image_link">
              <img width="218" height="164" src="<%=m.media.src%>">
            </a>
            <% }else if(m.mediaType == 'album'){%>
            <a target="_blank" href="<%=m.media.coverUrl%>" class="pic_wrap ed_image_link">
              <img width="218" height="164" src="<%=m.media.coverUrl%>">
            </a>
            <%}%>
            <h3><%=m.title%></h3>
            <%var summaryCon = '';
            var descriptionNow = m.description;
            if(BaikeNew.lenAddTagA(descriptionNow,300).strLen > 300){
              summaryCon = BaikeNew.spliceText(descriptionNow, BaikeNew.lenAddTagA(descriptionNow,300).cutLen, 3);
            }else{
              summaryCon = descriptionNow;
            }%>
            <%if(BaikeNew.lenAddTagA(descriptionNow,300).strLen > 300){%>
            <p class="summary" style="display: block;"><%=summaryCon%><a class="open" href="javascript:;"><i></i>展开</a></p>
            <%}else{%>
            <p class="summary" style="display: block;"><%=summaryCon%></p>
            <%}%>
            <p class="detail" style="display: none;"><%=m.description%><a class="hide" href="javascript:;"><i></i>收起</a></p>
          </div>
        <%}%>
      </div>
  </div>
<%}%>
</script>

<!--embed tpl-->
<script type="text/html" id="embed_show" dataType="embed">
                        <embed wmode="direct" flashvars="vid={$vid}&amp;autoplay=1" src="http://imgcache.qq.com/tencentvideo_v1/player/TencentPlayer.swf?max_age=86400&amp;v=20130507" quality="high" name="tenvideo_flash_player_1376292540651" id="tenvideo_flash_player_1376292540651" bgcolor="#000000" width="980" height="472" align="middle" allowscriptaccess="always" allowfullscreen="true" type="application/x-shockwave-flash" pluginspage="http://get.adobe.com/cn/flashplayer/" style="width: 650px; height: 472px;" />
</script>
<!--starVideo tpl-->
<script type="text/html" id="starVideo_show" dataType="starVideo">
                    <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
                  <li title="<%=m.name%>">
                                <a href="javascript:;" class="video_preview<%=(i==0?' current_video':'')%>" vid="<%=m.videoId%>"><i class="ico_play"></i><img width="140" height="80" src="<%=m.picUrl%>"></a>
                                <p class="work_name"><a href="javascript:;"><%=(m.name.length > 10 ? m.name.substring(0, 10) + '...' : m.name)%></a></p>
                              </li>
                    <%}%>
</script>

<!--starPic  tpl-->
<script type="text/html" id="starPic_show" dataType="starPic">
                    <div class="image_album_title">
                      <ul id="tab3" class="image_album_title_list">
                        <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
                            <li class="tab_btn<%=(i==0?' current_tab':'')%>">
                                <div><%=m.tag%></div>
                                <span class="angle"></span>
                              </li>
                        <%}%>
                      </ul>
                    </div>
                    <div id="content3">
                      <%for(var i=0;i<obj.length;i++){var m = obj[i];var _l = m.starPicCollections.length;%>
                          <div class="tab_content<%=(i==0?'':' hidden')%>">
                                  <a class="btn_prev_album btn_prev_album_dis" href="javascript:;"></a>
                                  <a class="btn_next_album<%=(_l <= 4?' btn_next_album_dis':'')%>" href="javascript:;"></a>
                                  <div class="album_mod_wrap">
                                      <ul index="0">
                                        <%var _o = m.starPicCollections;for(var j=0;j<_l;j++){var n = _o[j];%>
                                         <li>
                                             <div>
                                                  <a href="javascript:;" title="<%=n.name%>" class="album_cover_pic ed_image_link" contenteditable="false" draggable="false" unselectable="on"><img <%=(i>0?'data-src="'+n.pageUrl+'"':'src="'+n.pageUrl+'"')%> data-total="<%=n.dataTotal%>" data-position="1" data-id="<%=n.dataId%>" contenteditable="false" draggable="false" unselectable="on" alt="<%=n.name%>" style="display:none;"></a>
                                              </div>
                                             <p class="album_name"><a href="#"><%=n.name%></a><span><%=n.dataTotal%>张</span></p>
                                         </li>
                                       <%}%>
                                     </ul>
                                  </div>
                            </div>
                        <%}%>
                    </div>
</script>
<script type="text/html" id="movie_show">
    <div class="lemma_module_wrap" dataType="movie">
      <div class="layer_content">      
      <div class="list_title_wrap">
          <span class="movie_time">上映时间</span>
          <span class="movie_name">剧名</span>
          <span class="movie_role">扮演角色</span>
          <span class="movie_director">导演</span>
          <span class="movie_cast">合作演员</span>
        </div>
        <ul class="input_list_wrap">        
       <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
       <li class="mod_content_wrap">
            <div class="movie_time"><%=m.time%></div>
              <div class="movie_name"><%=m.name%></div>
              <div class="movie_role"><%if(m.role.length==0){%>----<%}%><%=m.role.join("；")%></div>
              <div class="movie_director"><%if(m.director.length==0){%>----<%}%><%=m.director.join("；")%></div>
              <div class="movie_cast"><%if(m.cast.length==0){%>----<%}%><%=m.cast.join("；")%></div>         
        </li>
        <%}%>    
        </ul>  
        <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>  
      </div>
    </div>
    </script>

<script type="text/html" id="tv_show">
    <div class="lemma_module_wrap" dataType="tv">
      <div class="layer_content">
        <div class="list_title_wrap">
          <span class="movie_time">上映时间</span>
          <span class="movie_name">剧名</span>
          <span class="movie_role">扮演角色</span>
          <span class="movie_director">导演</span>
          <span class="movie_cast">合作演员</span>
        </div>
        <ul class="input_list_wrap">
         <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
         <li class="mod_content_wrap">
              <div class="movie_time"><%=m.time%></div>
              <div class="movie_name"><%=m.name%></div>
              <div class="movie_role"><%if(m.role.length==0){%>----<%}%><%=m.role.join("；")%></div>
              <div class="movie_director"><%if(m.director.length==0){%>----<%}%><%=m.director.join("；")%></div>
              <div class="movie_cast"><%if(m.cast.length==0){%>----<%}%><%=m.cast.join("；")%></div>         
          </li>
          <%}%>
        </ul>  
        <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>   
      </div>
    </div>
    </script>

     <script type="text/html" id="adv_show">
    <div class="lemma_module_wrap" dataType="adv">
      <div class="layer_content">
        <div class="list_title_wrap">
          <span class="adv_time">代言时间</span>
          <span class="adv_name">代言产品</span>
          <span class="adv_time">代言时间</span>
          <span class="adv_name">代言产品</span> 
        </div>
          <ul class="input_list_wrap">          
        <%for(var i=0;i<obj.length;i++){var m = obj[i];%>
        <li class="mod_content_wrap">
          <div class="adv_time"><%=m.time%></div>
          <div class="adv_name"><%=m.name%></div>
          <% i++; var m = obj[i]; if(m){%>
          <div class="adv_time"><%=m.time%></div>
          <div class="adv_name"><%=m.name%></div>
          <%}%>
        </li>
        <%}%>
          </ul>  
          <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div> 
      </div>
    </div>
   </script>
  <script type="text/html" id="honor_show">
    <div class="lemma_module_wrap" datatype="honor">
        <%for(var i=0; i<obj.length; i++){ var mo=obj[i];%>
        <div class="layer_content">
            <h2 class="honor_title"><%=mo.awardType%></h2>
            <div class="list_title_wrap">
                <span class="honor_time">时间</span>
                <span class="honor_ceremony">颁奖典礼</span>
                <span class="honor_receive">所获荣誉</span>
                <span class="honor_name">获奖作品</span>
                <span class="honor_remark">备注</span>
            </div>
            <ul class="input_list_wrap">
                <%for(var j=0; j<mo.detail.length; j++){ var row=mo.detail[j];%>
                <li class="mod_content_wrap">
                    <div class="honor_time"><%=row.time%></div>
                    <div class="honor_ceremony"><%if(row.ceremony){%><%=row.ceremony%><%}else{%>----<%}%></div>
                    <div class="honor_receive"><%=row.honor%></div>
                    <div class="honor_name"><%if(row.works){%>《<%=row.works%>》<%}else{%>----<%}%></div>
                    <div class="honor_remark"><%if(row.remark){%><%=row.remark%><%}else{%>----<%}%></div>
                </li>
                <%}%>
            </ul>
            <div class="mod_btn_wrap hidden">
                <a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a>
            </div>
        </div>
        <%}%>
    </div>
  </script>

   <script type="text/html" id="concert_show">
  <div class="lemma_module_wrap" dataType="concert">
     <div class="layer_content concert_record">
         <div class="list_title_wrap">
             <span class="concert_time">举办时间</span>
             <span class="concert_name">演唱会名称</span>
             <span class="concert_number">总场次</span>
         </div>
        <ul class="input_list_wrap">
          <% for(var j=0; j<obj.length;j++){var r=obj[j];%>
        <li class="mod_content_wrap">
            <div class="concert_wrap">
                <div class="concert_time"><%=r.time%></div>
                <div class="concert_name"><%=r.name%></div>
                <div class="concert_number">
                  <span class="num"><%if(r.number){%><%=r.number%>场<%}else{%>----<%}%></span>
                  <%if(r.detail.length){%><a href="javascript:void(0)" title="查看详情" class="btn_show_detail" onclick="module.toggleSubList(this);return false">展开</a><%}%>
                </div>
            </div>
            <div class="detail_wrap hidden">
                <ol class="concert_list">
                    <% for(var i=0; i<r.detail.length; i++){ var row=r.detail[i];%>
                    <li><%=row.time%> <%=row.place%> <%=row.venue%></li>
                    <%}%>
                </ol>
            </div>
        </li>
        <%}%>
        </ul>  
      <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>
    </div>
  </div>
  </script>

   <script type="text/html" id="music_show">
    <div class="lemma_module_wrap" dataType="music">
       <div class="layer_content music_work no_content">
          <% if(obj.album.length){%>
          <div>
            <div class="sub_title_wrap">
                <h4>专辑</h4>
            </div>
             <div class="list_title_wrap" id="album_title">
                 <span class="album_name">专辑名</span>
                 <span class="album_time">发行日期</span>
                 <span class="album_lang">语言</span>
                 <span class="album_content">曲目详情</span>
             </div>
             <ul class="input_list_wrap" id="album_container"> 
             <% for(var j=0; j<obj.album.length;j++){var r=obj.album[j];%>
                <li class="mod_content_wrap">
                    <div class="album_intro">
                        <div class="album_name"><%=r.name%></div>
                        <div class="album_time"><%=r.time%></div>
                        <div class="album_lang"><%if(r.lang){%><%=r.lang%><%}else{%>----<%}%></div>
                        <div class="album_content">
                            <a class="btn_show_detail" title="查看详情" href="#" onclick="module.toggleSubList(this);return false">查看详情</a>
                        </div>
                    </div>
                    <div class="album_detail_wrap detail_wrap hidden">
                      <ul class="album_detail_list">
                        <%for(var i=0; i<r.detail.length; i++){ var index = i < 9 ? '0' + (i+1) : i+1;%>              
                        <li><%=index%>．&nbsp;&nbsp;<%=r.detail[i]%></li>
                        <%}%>
                      </ul>
                    </div>
                </li>
                <%}%>
             </ul> 
          </div>
          <%}%>
          <% if(obj.single.length){%>
          <div>
              <div class="sub_title_wrap">
                  <h4>精选单曲</h4>
              </div>
              <div class="list_title_wrap" id="single_title">
                   <span class="single_name">歌曲名</span>
                   <span class="single_lang">语言</span>
                   <span class="single_time">发行时间</span>
              </div>
              <ul class="input_list_wrap" id="single_container">              
            <%for(var i=0;i<obj.single.length;i++){var row=obj.single[i];%>
            <li class="mod_content_wrap">
                <div class="single_name"><%=row.name%></div>
                <div class="single_lang"><%if(row.lang){%><%=row.lang%><%}else{%>----<%}%></div>
                <div class="single_time"><%if(row.time){%><%=row.time%><%}else{%>----<%}%></div>
            </li>
            <%}%>
              </ul>
          </div>
          <%}%>
        </div>
    </div>
  </script>

  <script type="text/html" id="resume_show">
    <div class="lemma_module_wrap" dataType="resume">
      <div class="layer_content">
        <div class="list_title_wrap">
          <span class="resume_time">时间</span>
          <span class="resume_detail">履历详情</span>
        </div>
        <ul class="input_list_wrap">
          <%for(var i=0; i<obj.length; i++){ var row=obj[i];%>
          <li class="mod_content_wrap">
            <div class="resume_time"><%=row.time%></div>
            <div class="resume_detail"><%=row.detail%></div>
          </li>
          <%}%>
        </ul>      
        <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>     
      </div>
    </div>
  </script>

  <!-- 演员表 -->
  <script type="text/html" id="actor_show">  
  <div class="lemma_module_wrap" dataType="actor">
     <div class="layer_content">
    <div class="list_title_wrap">
      <span class="episode_role">角色</span>
      <span class="episode_actor">演员</span>
      <span class="episode_dubbing">配音</span>
      <span class="episode_remarks">备注</span>
    </div>
        <ul class="input_list_wrap">
          <%for(var i=0; i<obj.length; i++){ var row=obj[i];%>
          <li class="mod_content_wrap">
            <div class="episode_role"><%=row.role%></div>
            <div class="episode_actor"><%=row.actor%></div>
            <div class="episode_dubbing"><%if(row.dubbing.length==0){%>----<%}%><%=row.dubbing%></div>
            <div class="episode_remarks"><%if(!row.remarks || row.remarks.length == 0){%>----<%}%><%=row.remarks%></div>
          </li>
          <%}%>
        </ul>
        <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>     
    </div>
  </div>
  </script>
  <!-- 经典赛事 -->
  <script type="text/html" id="match_show">  
  <div class="lemma_module_wrap" dataType="match">
     <div class="layer_content">
    <div class="list_title_wrap">
      <span class="match_time">时间</span>
      <span class="match_name">赛事</span>
      <span class="match_achievement">成绩</span>
      <span class="match_rank">名次</span>
      <span class="match_remarks">备注</span>
    </div>
        <ul class="input_list_wrap">
          <%for(var i=0; i<obj.length; i++){ var row=obj[i];%>
          <li class="mod_content_wrap">   
            <div class="match_time"><%=row.time%></div>
            <div class="match_name"><%=row.name%></div>
            <div class="match_achievement"><%if(row.achievement.length==0){%>----<%}%><%=row.achievement%></div>
            <div class="match_rank"><%if(row.rank.length==0){%>----<%}%><%=row.rank%></div>
            <div class="match_remarks"><%if(row.remarks.length==0){%>----<%}%><%=row.remarks%></div>
          </li>
          <%}%>
        </ul>
        <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>     
    </div>
  </div>
  </script>
  <!-- 职员表 -->
  <script type="text/html" id="staff_show">
  <% var fieldTitle = {
    producer: '出品人', casting: '选角导演', execProducer: '制作人', dubbing: '配音导演', 
    supervisor: '监制', artDirector: '艺术指导', distributor: '发行', artDesign: '美术设计',
    director: '导演', actionDirector: '动作指导', assocDirector: '副导演', stylist: '造型设计', 
    writer: '编剧', costumeDesign: '服务设计', originalStory: '原著', visualEffect: '视觉特效', 
    photography: '摄影', recording: '录音', music: '配乐', bestBoy: '剧务', 
    editor: '剪辑', script: '场记', propertyMaster: '道具', setDecorator: '布景师', 
    gaffer: '灯光'
    };
    var fields = [];
    var values = [];
    for(field in fieldTitle){
        var value = obj[field] ? obj[field].join('，') : null;
        if(value){
            fields.push(field);
            values.push(value);
        }
    }
  %> 
  <div class="lemma_module_wrap" dataType="staff">
     <div class="layer_content">
        <ul class="input_list_wrap staff_list">
        <%for(var i = 0; i < fields.length; i++){%>
        <li class="mod_content_wrap">
            <div class="staff_name">
                <div class="title"><%=fieldTitle[fields[i]]%>：</div>
                <div class="name"><%=values[i++]%></div>
            </div>
            <% if(i < fields.length){ %>
            <div class="staff_name">
                <div class="title"><%=fieldTitle[fields[i]]%>：</div>
                <div class="name"><%=values[i]%></div>
            </div>
            <% } %>
        </li>
        <%}%>
     </ul>
      <div class="mod_btn_wrap hidden"><a class="btn_hide" title="收起" href="#" onclick="module.toggleList(this);return false">收起</a></div>     
    </div>
  </div>
  </script>
  
  <!--分集剧情-->
  <script type="text/html" id="plot_show">
      <div class="plot_search_wrap">
          <a class="btn_plot_search" href="javascript:;"><span>分集查询</span><i></i></a>
          <div class="plot_list hidden">
              <ul>
                  <li>
                  <%for(var i = 1; i <= obj.length; i++){%>
                      <a class="episode" href="javascript:;"><%=i%>集</a>
                      <%if(i % 10 === 0 && i < 50){%>
                          </li><li>
                      <%}else if(i % 10 === 0 && i >= 50){%>
                          </li><li class="hidden">
                      <%}%>
                  <%}%>
                  </li>
              </ul>
              <%if(obj.length > 50){%>
              <a class="btn_more_plot" href="javascript:;" title="展开"><span>展开</span><i></i></a>
              <%}%>
          </div>
      </div>
      <ul class="plot_wrap">
          <%for(var i = 0; i < obj.length; i++){ var row = obj[i];%>
          <%if(i < 5){%>
          <li>
          <%}else{%>
          <li class="hidden">
          <%}%>
              <div class="title"><%= row.title%></div>
              <p>
                  <%if(row.mediaType === 'pic'){%>
                      <span class="text_img ed_imgfloat_right" style="width: <%=row.media.width%>px;">
                          <a class="ed_image_link" title="点击查看大图" href="<%=row.media.bigSrc%>" target="_blank">
                              <img width="<%=row.media.width%>" height="<%=row.media.height%>" alt="<%=row.media.title%>" src="<%=row.media.src%>">
                          </a>
                          <span><%=row.media.title%></span>
                      </span>
                  <%}else if(row.mediaType === 'album'){%>
                      <span class="ed_imgfloat_right album_wrap <%= row.media.width > row.media.height ? 'album_horizontal_main' : 'album_vertical_main'%>">                 
                          <span class="album_cover_wrap">                   
                              <span class="album_cover_img">                          
                                  <a href="javascript:;" title="<%= row.media.title%>" class="ed_image_link">                             
                                      <img width="<%= row.media.width%>" height="<%= row.media.height%>" src="<%= row.media.coverUrl%>" data-total="<%= row.media.total%>" data-id="<%= row.media.id%>" alt="<%= row.media.title%>">
                                  </a>                        
                              </span>                         
                              <i class="ico_album"></i>                       
                          </span>                       
                          <span class="album_bg"></span>                        
                          <span class="album_bg_bottom"></span>                    
                      </span>
                  <%}else if(row.mediaType === 'video'){%>
                      <span class="text_img ed_imgfloat_right video">
                          <a class="ed_image_link" href="javascript:void(0);" style="display:block">  
                              <i class="ico_play"></i>
                              <img elem-type="video" src="<%= row.media.picUrl%>" width="<%= row.media.width%>" height="<%= row.media.height%>" title="<%= row.media.title%>" data-vid="<%= row.media.vid%>" data-url="<%= row.media.videoUrl%>">
                          </a>
                          <span><%= row.media.title%></span>
                      </span>
                  <%}%>
                  <%= row.content%>
              </p>
          </li>
          <%}%>
      </ul>
      <%if(obj.length > 5){%>
      <div class="plot_nav_wrap">
          <div class="plot_nav">
              <%for(var i = 1, l = obj.length; i <= l; i+=5){%>
                  <%if(i + 5 <= l){%>
                      <%if(i === 1){%>
                          <a class="current_plots" href="javascript:;" data-start="<%=i%>" data-end="<%= i + 4 %>"><%=i%>-<%= i + 4 %>集</a>
                      <%}else{%>
                          <a href="javascript:;" data-start="<%=i%>" data-end="<%= i + 4 %>"><%=i%>-<%= i + 4 %>集</a>
                      <%}%>
                  <%}else if(i === l){%>
                      <a href="javascript:;" data-start="<%=l%>" data-end="<%=l%>"><%=l%>集</a>
                  <%}else{%>
                      <a href="javascript:;" data-start="<%=i%>" data-end="<%=l%>"><%=i%>-<%=l%>集</a>
                  <%}%>
              <%}%>
          </div>
      </div>
      <a class="btn_all_plot" href="javascript:;" title="查看全部剧情"><span>查看全部剧情</span><i></i></a>
      <%}%>
</script>

<!--医疗视频-->
<script type="text/html" id="medical_video_show">
        <div class="section_content">
            <div class="rich_text_area">
                <div class="video-box">
                    <div class="play-panel">
                        <a href="#" class="show-panel" id="j-medical-video">
                            <img width="440" height="328" src="<%= obj.pic %>" alt="<%= obj.expertAbs %>">
                            <span class="play-btn"></span>
                        </a>
                        <div class="flash-panel" style="display: none;">
                            <embed src="http://sogou.player.vodjk.com/player.swf" flashvars="<%= obj.videoUrl %>" quality="high" width="440" height="328" align="middle" allowScriptAccess="always" allowFullscreen="true" type="application/x-shockwave-flash" wmode="transparent"></embed>
                        </div>
                    </div>
                    <div class="side-panel">
                        <div class="hd">
                            <div class="m">
                                <strong>主讲人：</strong><span><%= obj.expertName %></span>
                            </div>
                            <%var hospitalSep = obj.expertAbs.indexOf('|');%>
                            <div class="sub"><%= obj.expertAbs.slice(0, hospitalSep) %>医院</div>
                            <div class="sub"><%= obj.expertAbs.slice(hospitalSep + 1) %></div>
                        </div>
                        <h6>相关视频</h6>
                        <ul class="v-lst" id="j-count-medical-reative">
                            <%for(var i = 0, l = obj.other.length; i < l; i++){ var item = obj.other[i];%>
                            <li>
                                <a href="<%= item.videoUrl %>" class="show-panel" target="_blank" title="<%= item.name %>">
                                    <span class="video-pic-panel">
                                        <img width="120" height="70" src="<%= item.pic %>" alt="<%= item.name %>">
                                        <span class="mask"></span>
                                        <span class="play-btn"></span>
                                    </span>
                                    <span class="video-t"><%= item.name %></span>
                                </a>
                            </li>
                            <%}%>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <a class="haodf-from" id="j-count-vodjk" href="http://www.vodjk.com/" target="_blank" title="跳转到健康第一线">以上内容来自健康第一线</a>
</script>

<!--图书-->
<script type="text/html" id="side_book_show">
    <div class="side_column_wrap">
        <div class="title_wrap">
            <h3>口碑</h3>
        </div>
        <div class="book_evaluate">
            <ul>
                <li>
                    <%if(obj.amazon.url){%>
                    <span class="site"><a id="j-amazon-link" href="<%=obj.amazon.url%>&tag=sogoubk_20150120-23" title="浏览亚马逊图书页" target="_blank">亚马逊</a></span>
                    <%}else{%>
                    <span class="site">亚马逊</span>
                    <%}%>
                    <div class="book_mark"><span style="width: 0%"></span></div>
                    <span id="side_book_amazone_score" class="score" data-score="<%=obj.amazon.score || 0 %>">暂无评分</span>
                </li>
                <li>
                    <span class="site">豆瓣</span>
                    <div class="book_mark"><span style="width:0%"></span></div>
                    <span id="side_book_douban_score" class="score" data-score="0">暂无评分</span>
                </li>
            </ul>
            <%if(obj.amazon.rank){%>
            <p class="rank">亚马逊图书排名 NO.<%=obj.amazon.rank%></p>
            <%}%>
            <div class="wrap">
                <%if(obj.wechatCode){%>
                <a class="btn_price" href="javascript:;" data-image="<%=obj.wechatCode%>"><i></i>在线比价</a>
                <%}%>
                <%if(obj.amazon.url){%>
                <a class="btn_buy" href="<%=obj.amazon.url%>" target="_blank"><i></i>购买本书</a>
                <%}%>
            </div>
        </div>
    </div>
</script>

<!-- 大图轮播模块A -->
<script type="text/html" id="lemma_bigpic_a">
  <div class="scroll_title">
    <!--有图内容是p显示，内容显示完到结果页p隐藏-->
    <p class="scroll_title_num"><span class="j-scroll-indicator">1</span>/<%=obj.imgInfo.length%></p>
    <h2><%=obj.modelTitle%></h2>
</div>
<!--内容区域 start-->
<div class="scroll_wrap">
    <!--左箭头 上一个-->
    <a class="scroll_arrow scroll_arrow_left j-left-btn" href="javascript:;">上一个</a>
    <ul class="scroll_wrap_list j-bigpic" style="width: 21300px;">
        <% for(var i=0; i<obj.imgInfo.length; i++){ var img = obj.imgInfo[i];%>
        <li>
            <div class="scroll_img"><img width="340" height="200" src="<%=img.imgUrl%>" alt="<%=img.imgTitle%>" title="<%=img.imgTitle%>"></div>
            <div class="scroll_content">
                <h3><a href="/v<%=img.refLemmaId%>.htm" target="_blank"><%=img.imgTitle%></a></h3>
                <p class="scroll_content_txt"><%=img.imgDesc%></p>
                <dl>
                    <dt>相关词条：</dt>
                    <% for(var j=0; j<obj.similarLemma.length; j++){ var lemma = obj.similarLemma[j];%>
                    <dd><a class="lemma_item" title="<%=lemma.title%>" href="/v<%=lemma.lemmaId%>.htm" target="_blank"><%=lemma.title%></a></dd>
                    <% }%>
                </dl>
            </div>
        </li>
        <% }%>
    </ul>
    <!--右箭头 下一个-->
    <a class="scroll_arrow scroll_arrow_right j-right-btn" href="javascript:;">下一个</a>
</script>
<!-- 大图轮播模块B -->
<script type="text/html" id="lemma_bigpic_b">
  <div class="scroll_title">
      <h2><%=obj.modelTitle%></h2>
  </div>
  <div class="scroll_more_wrap">
      <a class="scroll_arrow scroll_arrow_left j-left-btn" href="javascript:;">上一个</a>
      <ul class="scroll_mod_list scroll_mod_list_l j-bigpic" style="width: 21300px;">
          <% for(var i=0; i<obj.imgInfo.length; i++){ var img = obj.imgInfo[i]; %>
          <li>
              <a href="/v<%=img.refLemmaId%>.htm" class="scroll_mod_item scroll_mod_l" target="_blank">
                  <img width="230" height="150" src="<%=img.imgUrl%>" alt="<%=img.imgTitle%>" title="<%=img.imgTitle%>"/>
                  <div class="scroll_mod_con"><%=img.imgTitle%></div>
              </a>
              <p class="scroll_mod_txt"><%=img.imgDesc%><a href="/v<%=img.refLemmaId%>.htm" target="_blank" style="margin-left:1em">详情&gt;&gt;</a></p>
          </li>
          <% } %>
      </ul>
      <ul class="scroll_mod_num"></ul>
      <a class="scroll_arrow scroll_arrow_right j-right-btn" href="javascript:;">下一个</a>
  </div>
</script>
		<div class="guide_popup step1">
			<i class="arrow"></i>
			<div class="content">点击编辑词条，进入编辑页面</div>
			<a class="btn" href="javascript:;"></a>
		</div>
		<div class="guide_mask" style="display:none; width:100%; height:100%;"></div>

		<!-- datas for javascript -->

		<script type="text/javascript">
            var lId = '77860';
            var cId = '166298392';
            img = new Image().src="/api/pv?lid="+lId;
		</script>

		<script>
            //目录展开
            jQuery(".lemma_detail .open_btn").toggle(function(){
                jQuery(".lemma_detail_catalogue").fadeIn();
                jQuery(this).addClass("hide_btn").attr('title', '收起目录').text("收起目录");
            },function(){
                jQuery(".lemma_detail_catalogue").fadeOut();
                jQuery(this).removeClass("hide_btn").attr('title', '展开目录').text("展开目录");
            });

            jQuery(function(){
                var body = jQuery('body');

                var additionalInfoType=jQuery("#additionalInfoType").attr("qid");

                if("1"==additionalInfoType){
                    jQuery('.evaluate_video').unbind('click').on('click', function(event){
                        jQuery('.mask').css({"height":body.height(),"width":jQuery(window).width()}).show();
                        jQuery('body').append('<div class="video_layer_wrap"></div>');
                        var video_view = jQuery('.video_layer_wrap');
                        video_view.prepend('<a class="btn_quit" href="javascript:;" title="close"></a>').append(jQuery('#video_tpl').val()).show();

                        jQuery('.btn_quit').unbind('click').on('click', function(event){
                            jQuery('.mask').hide();
                            jQuery('.video_layer_wrap').remove();
                            return false;
                        });

                        return false;
                    });
                }


                var jRankWray=jQuery(".rank_wrap");
                var jRankTip=jQuery(".tip");
                jRankWray.hover(
                    function (){
                        jRankTip.show();
                    },
                    function(){
                        jRankTip.hide();
                    }
                );

            });
		</script>

		<script type="text/javascript" src="//cache.soso.com/baike/js/share_201710192103.js"></script>
		<script type="text/javascript" src="//cache.soso.com/baike/js/lemma_201710192103.js"></script>
		<script type="text/javascript" src="//cache.soso.com/baike/js/baikeSideRelation_201508291250.js"></script>
		<script type="text/javascript" src="//cache.soso.com/baike/js/zol_201405121927.js"></script>
		<!--<script jwcid="@Js" src="literal:showInnerLinkFloat_js" />-->
		<script type="text/javascript" src="//cache.soso.com/baike/js/checkLock_201706281513.js"></script>
		<script language="javascript" src="//qzs.qq.com/tencentvideo_v1/js/tvp/tvp.player.js" charset="utf-8"></script>
		<script type="text/javascript" src="//tv.sohu.com/upload/swf/showVrsPlayer.js" charset="utf-8"></script>
		<script type="text/javascript">
            PageActions.activate("ShowLemmaDefault")
		</script>
		<script>

            if (sbjl.byId("lemma_pic") != null){
                window.lemmaData.lemmaPic = sbjl.firstTag(sbjl.byId("lemma_pic"), "img").src;
            }
            window.module_data = {"greatEvent":{"title":"大事记","content":[]}}
;
            window.module_data && module.render(window.module_data);

            //如果是新手任务页面过来，给出tips
            if(/taskId=-[43]/.test(location.href)){
                var match = location.href.match(/taskId=-[43]/);
                $btn = jQuery('.btn_edit_lemma').addClass('highlight');
                var href = $btn.attr('href');
                $btn.attr('href', href + (href.indexOf("?") ? "&" : "?") + match);
                var left = $btn.offset().left + $btn.outerWidth();
                //禁止滚动
                jQuery(document.body).height(jQuery(window).height()).css("overflow", "hidden");
                jQuery('.step1').css("left", left + "px").show();
                jQuery('.guide_mask').height(jQuery(document).height()).show();
            }
		</script>
		<!-- <script src="//cache.soso.com/baike/js/ad_lemma.js"></script> -->

	<!--cache-->

	<script>
        var editLimitDialog = null;

        function beforeEdit(elem) {
            var lemmaId = document.getElementById("lemmaId");
            if (lemmaId != null) {
                lemmaId = lemmaId.innerHTML;
                Zhishi.Ajax.sendRequest("GET", '/api/el?' + "lemmaId="
                    + encodeURIComponent(lemmaId), {
                    onSuccess : function(d) {
                        if (d == '1') {
                            // open a dialog
                            editLimitDialog = new Zhishi.Dialog(
                                '<span class="layer_title">友情提示</span>', 400,
                                220, true, '/cache/EditLimitTip.html', {});
                            editLimitDialog.show();
                        } else
                        if(elem.getAttribute('ohref')){
                            document.location = elem.getAttribute('ohref');
                        }else{
                            document.location = elem.href;
                        }

                    }
                });
            } else {
                if(elem.getAttribute('ohref')){
                    document.location = elem.getAttribute('ohref');
                }else{
                    document.location = elem.href;
                }
            }
            return false;
        }
        <!--
            function beforeEditCheck(elem,isSynonyms) {
                window.RNV(function(){
                    isSynonyms?jQuery.cookie('clickedEditBtn', '2', {path: '/'}):jQuery.cookie('clickedEditBtn', '1', {path: '/'});
                    WKSSO.doLogin(function(){window.location.reload()});
                }, function () {
                    Baike.version.checkVerifying(window.lemmaId,function(){
                        var type=0;
                        if(highQuality){
                            type=2;
                        }

                        var check=checkLock(type,null,null,null,isSynonyms);
                        if(!check){
                            return false;
                        }
                        var nowHour = new Date().getHours();
                        if (nowHour >= 22 || nowHour < 9) {
                            new WW.U.Dialog({
                                type : 'confirm',
                                title : '提示',
                                message : '<p style="padding: 50px 100px;">亲爱的用户，现在提交词条可能需要较长时间审核。确认要编辑么？</p>',
                                callback : function(state) {
                                    if(state){
                                        beforeEdit(elem);
                                    }
                                    return true;
                                }
                            });
                            return false;

                        }else{
                            return beforeEdit(elem);
                        }
                    });
                }, true).verify();
                return false;
            }
        -->
	</script>
	<div class="shortcut_link_wrap">
		<div class="link_column">
			<div class="title"><i class="ico_guide"></i>新手指引</div>
			<ul>
				<li><a href="http://baike.sogou.com/help/#dictionary_what" target="_blank">了解百科</a></li>
				<li class="left"><a href="http://baike.sogou.com/help/#standard_dictionary_name" target="_blank">编辑规范</a></li>
				<li><a href="http://baike.sogou.com/help/#user_integral" target="_blank">用户体系</a></li>
				<li class="left"><a href="http://baike.sogou.com/shop/" target="_blank">商城兑换</a></li>
			</ul>
		</div>
		<div class="link_column">
			<div class="title"><i class="ico_answer"></i>问题解答</div>
			<ul>
				<li><a href="http://baike.sogou.com/help/#question" target="_blank">关于审核</a></li>
				<li class="left"><a href="http://baike.sogou.com/help/#question" target="_blank">关于编辑</a></li>
				<li><a href="http://baike.sogou.com/help/#question" target="_blank">关于创建</a></li>
				<li class="left"><a href="http://baike.sogou.com/help/#question" target="_blank">常见问题</a></li>
			</ul>
		</div>
		<div class="link_column">
			<div class="title"><i class="ico_feedback"></i>意见反馈及投诉</div>
			<ul>
				<li>
					<script>document.write('<a href="/appeal/appeal.v?type=1&titleArray='+window.encodeURI(lemmaData.lemmaTitle)+'&urlArray='+
                        window.WKRWDOMAIN('//baike.sogou.com/v')+lemmaData.lemmaId+'.htm" target="_blank" onclick="stget(\'ss.tj.bj\', \'baike\');DT.reportCLK(\'ss.tj.bj\', \'baike\')">举报与质疑</a>')</script>
				</li>
				<li class="left"><a href="/appeal/appeal.v?type=2&amp;titleArray=网络爬虫&amp;urlArray=//baike.sogou.com/v77860.htm" onclick="stget('ss.tj.bj', 'baike');DT.reportCLK('ss.tj.bj')" target="_blank">举报非法用户</a></li>
				<li><a href="/appeal/appeal.v?type=3&amp;titleArray=网络爬虫&amp;urlArray=//baike.sogou.com/v77860.htm" onclick="stget('ss.tj.bj', 'baike');DT.reportCLK('ss.tj.bj')" target="_blank">未通过申诉</a></li>
				<li class="left"><a href="/appeal/appeal.v?type=4&amp;titleArray=网络爬虫&amp;urlArray=//baike.sogou.com/v77860.htm" onclick="stget('ss.tj.bj', 'baike');DT.reportCLK('ss.tj.bj')" target="_blank">反馈侵权信息</a></li>
			</ul>
		</div>
		<div class="link_column last">
			<div class="title"><i class="ico_cooperation"></i>对外合作</div>
			<ul>
				<li><a href="mailto:sogoubaike@sogou-inc.com">邮件合作</a></li>
				<li class="left"><a href="http://ld.sogou.com/cate?cid=462527" target="_blank">官方圈子</a></li>
				<li><a target="_blank" href="http://weibo.com/sosobaike">官方微博</a></li>
				<li class="left"><a target="_blank" href="//cache.soso.com/baike/images/baikeerweima.jpg">微信公众号</a></li>
			</ul>
		</div>
	</div>


			</div>
		

	<!--footer-->
	<div id="s_footer" class="wa_mode" wa_mode="soso.footer">
		<ul id="s_service">
			<li><a href="http://fuwu.sogou.com" target="_blank">企业推广</a></li>
			<li><a href="http://pinyin.sogou.com" target="_blank">输入法</a></li>
			<li><a href="http://ie.sogou.com/?f=pinyingw" target="_blank">浏览器</a></li>
			<li><a href="http://mail.sogou.com" target="_blank">搜狗免费邮箱</a></li>
			<li><a href="http://job.sogou.com" target="_blank">诚聘英才</a></li>
			<li><a href="http://baike.sogou.com/help/#user_protocol" target="_blank">用户协议</a></li>
			<li><a href="http://corp.sogou.com/private.html" target="_blank">隐私政策</a></li>
			<li><a href="/help/" target="_blank">编辑帮助</a></li>
			<li><a href="/appeal/appeal.v?type=5">意见反馈及投诉</a></li>
		</ul>
		<p>&copy;
			<script>document.write(new Date().getFullYear())</script> Sogou Inc.
			<a class="g" target="_blank" href="http://www.miibeian.gov.cn">京ICP证050897号</a>
			<a href="http://www.sogou.com/docs/terms.htm" class="g">免责声明 </a>
			<span class="ba"> </span>
		</p>
	</div>

		</div>
	


	<script type="text/javascript" src="//cache.soso.com/baike/js/baike_201706292035.js"></script>
	<script src="//cache.soso.com/deploy/js/lib/sso/pc/main.js"></script>
	<script type="text/javascript" src="//cache.soso.com/baike/js/base_201707271947.js"></script>
	<script type="text/javascript" src="//cache.soso.com/baike/js/sb_new_201711202120.js"></script>
	<script type="text/javascript" src="//cache.soso.com/baike/js/jquery_cookie_201402251613.js"></script>
	<script type="text/javascript" src="//cache.soso.com/baike/js/common_new_201710192103.js"></script>
	<script language="JavaScript" type="text/javascript" src="//cache.soso.com/deploy/js/an_v6.js"></script>
	<script src="//cache.soso.com/deploy/js/lib/dt/main.js"></script>
	<script type="text/javascript">Zhishi.Login.init('s_user');</script>

<script src="//cache.soso.com/deploy/js/lib/monitor/main.js"></script>
<script src="//cache.soso.com/deploy/js/lib/wenke/main.js"></script>
<script src="//cache.soso.com/deploy/js/lib/cs/main.js"></script>
<!--<script src="//cache.soso.com/baike/js/check_hijack.js"></script>-->
<!--<script>-->
<!--(function(){var getDomainPrefix=function(){var domain='wenwen';switch(location.host.toLowerCase()){case'wenwen.sogou.com':case'wenwen.m.sogou.com':domain='wenwen';break;case'ld.sogou.com':domain='ld';break;case'zhinan.sogou.com':domain='zhinan';break;case'baike.sogou.com':case'baike.m.sogou.com':domain='baike';break;default:break;}-->
<!--return domain;};var getCookie=function(name){var nameEQ=escape(name)+"=";var ca=document.cookie.split(';');for(var i=0;i<ca.length;i++){var c=ca[i];while(c.charAt(0)==' ')c=c.substring(1,c.length);if(c.indexOf(nameEQ)==0)return unescape(c.substring(nameEQ.length,c.length));}-->
<!--return null;};var serialize=function(obj){if(typeof obj!='object'){return obj;}-->
<!--var r=[];for(var k in obj){r.push(k+'='+encodeURIComponent(obj[k]));}-->
<!--return r.join('&');};var report=function(hjDetailInfo){var domain=getDomainPrefix();var img=new Image();img.onload=img.onerror=function(){img=img.onload=img.onerror=null;}-->
<!--var _url='//dm.wenwen.sogou.com/f/'+domain+'/hj?';if(location.protocol==='https:'){_url='//wenwenapi.sogou.com/dm/f/'+domain+'/hj?';}-->
<!--var ssuid=getCookie('dt_ssuid');if(ssuid){hjDetailInfo.dt_ssuid=ssuid;}-->
<!--hjDetailInfo.rnd=Math.random();img.src=_url+serialize(hjDetailInfo);};if(!String.prototype.endsWith){String.prototype.endsWith=function(searchString,position){var subjectString=this.toString();if(typeof position!=='number'||!isFinite(position)||Math.floor(position)!==position||position>subjectString.length){position=subjectString.length;}-->
<!--position-=searchString.length;var lastIndex=subjectString.lastIndexOf(searchString,position);return lastIndex!==-1&&lastIndex===position;};}-->
<!--var scriptElements=document.getElementsByTagName('script');var scriptElementsLength=scriptElements.length;for(var x=0;x<scriptElementsLength;x++){var domainList=[".sogou.com",".qq.com",".idqqimg.com",".gtimg.cn",".gtimg.com",".soso.com","soso.qstatic.com",".sohu.com",".sogoucdn.com",".go2map.com",".google-analytics.com",".itc.cn"];var src=scriptElements[x].getAttribute('src');if(src){var aEle=document.createElement('a');aEle.href=src;var hitBlackList=true;for(var i=0;i<domainList.length;i++){if(aEle.hostname.endsWith(domainList[i])){hitBlackList=false;}}-->
<!--if(hitBlackList){report({"src":src});}}}})();-->
<!--</script>-->
<script language="JavaScript" type="text/javascript"><!--
Tapestry.register_form('Form');
Tapestry.onsubmit('Form', function(event) { Tapestry.require_field(event, 'searchText', '请输入你要查找的内容。'); });

// --></script></body>
</html>
''',"html","utf-8")
#信息中添加发送者
message['Subject']=Header("问候","utf-8")
message[ 'From']=_format_addr ('一号爬虫<838206775@qq.com>')
message[ 'To']=_format_addr( '管理员<343627649@qq.com>')

smtp=smtplib.SMTP()
smtp.connect("smtp.qq.com",25)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.set_debuglevel(1)
smtp.login("838206775@qq.com","jfntntsqfchgbeab")
smtp.sendmail("838206775@qq.com",["343627649@qq.com","hqhx2017@163.com"],message.as_string())
