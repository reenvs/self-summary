//创建webpage对象
page=require("webpage").create()
system=require("system")

var args=system.args
//phantomjs a3.js http://movie.mtime.com/227434/
console.log(args)

phantom.outputEncoding="gbk"
var t=Date.now()
console.info("时间："+t)

page.open(args[1],function(status){
	if(status==='success'){
		t=Date.now()-t
		console.info("打开该网页用时:"+t+"毫秒")
	}
phantom.exit()
})
