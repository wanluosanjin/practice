# mvn dependency:get -Dartifact="org.springframework:spring-context:5.2.6.RELEASE:jar:javadoc"

#变量有域
function addcp($jar){
    $script:cp=$script:cp+$jar+";"
}

$cp=""
$mysql="C:\\Users\\onelor\\Documents\\code\\mysql-connector-java-8.0.22\\mysql-connector-java-8.0.22.jar"

$cp+=$mysql
$cp+=";"

$springcore="C:\Users\onelor\.m2\repository\org\springframework\spring-core\5.2.6.RELEASE\spring-core-5.2.6.RELEASE.jar"
$springaop="C:\Users\onelor\.m2\repository\org\springframework\spring-aop\5.2.6.RELEASE\spring-aop-5.2.6.RELEASE.jar"
$springbeans="C:\Users\onelor\.m2\repository\org\springframework\spring-beans\5.2.6.RELEASE\spring-beans-5.2.6.RELEASE.jar"
$springexpression="C:\Users\onelor\.m2\repository\org\springframework\spring-expression\5.2.6.RELEASE\spring-expression-5.2.6.RELEASE.jar"
$springcontext="C:\Users\onelor\.m2\repository\org\springframework\spring-context\5.2.6.RELEASE\spring-context-5.2.6.RELEASE.jar"

$cp=$cp+$springcore+";"+$springbeans+";"+$springaop+";"+$springexpression+";"+$springcontext+";"

$springjcl="C:\Users\onelor\.m2\repository\org\springframework\spring-jcl\5.2.6.RELEASE\spring-jcl-5.2.6.RELEASE.jar"
addcp($springjcl)
addcp(".\class")
echo "input*for update all,input aaa for aaa.java"
$a=read-host
$a+=".java"
# class/aaa并不是环境变量 只编译aaa出错
#classpath 不能带package名
# 对java来说package本身就是一个路径
javac -cp $cp -encoding UTF-8 -Xlint:unchecked -d ./class $a
echo "write aaa for start java aaa"
$a=read-host
if($a -eq "aaa"){
    java -cp $cp aaa.My
}
