page=require("webpage").create()
page.onResourceRequested=function(request){
	console.log("request:"+JSON.stringify(request,undefined,4))
}

page.onResourceReceived=function(response){
	console.log("response:"+JSON.stringify(response,undefined,4))
	
}

page.open("http://movie.mtime.com/227434/")
phantom.exit()
