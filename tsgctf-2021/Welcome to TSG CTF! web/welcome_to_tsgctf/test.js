const flag = 'DUMMY{DUMMY}';

a = {
	//"test":true
	"constructor" : {
		"constructor" : {
			"toString" : true
		}
	}
}

if (typeof a === 'object' && a[flag] === true) {
	console.log("Nice! flag");
}else{
	console.log("You failed...");
}

console.log(a.toString())
