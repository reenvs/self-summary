//创建一个web页面对象
var page=require("webpage").create()
//设置phantom的输出字符集
phantom.outputEncoding="gbk"

//设置视口大小
page.viewportSize={"width":1024,"height":768}
//设置裁剪矩形大小
page.clipRect={"top":200,"left":200,"width":300,"height":200}

//打开一个网站,open(url,callback)
page.open("http://movie.mtime.com/227434/",function(status){
	console.log("网站打开状态："+status)
	if(status==='success'){
		//把当前网页保存成一个图片
		page.render("cc.png")
	}
	//退出
	phantom.exit()
})

