page=require("webpage").create()

page.includeJs("http://cdn.static.runoob.com/libs/jquery/1.10.2/jquery.min.js",function(){
	p=page.evaluate(function(){
		var $pArray=$("p");
		return $pArray
	})
	console.log(p)
	phantom.exit()
})

page.open("http://blog.csdn.net/yuexianchang/article/details/53306892")

