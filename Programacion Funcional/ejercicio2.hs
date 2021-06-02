--funcion del sen,cos,tan
calculadora::String->Float->[Float]

calculadora "sin" b= map sin [1..b]
calculadora "cos" b= map cos [1..b]
calculadora "tan" b= map tan [1..b]
calculadora "exp" b= map exp [1..b]
calculadora "log" b= map log [1..b]
--[sin x| x<- [1..n]]