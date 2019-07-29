page=require("webpage").create()
phantom.outputEncoding="gbk"

console.log(page.settings.userAgent)
page.settings.userAgent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"

page.open("http://movie.mtime.com/227434/",function(status){
	console.log(status)
	if(status==="success"){
		console.log("-------")
		var t=page.evaluate(function(){
			var t=document.getElementById("ratingRegion").innerText
			console.log("*****************************")
			return t
		})
		console.log(t)
		phantom.exit()
	}
})