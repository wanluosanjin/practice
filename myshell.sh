#set -uxe
readfile(){
	echo $1
	while read A
	do
	echo $A
	done <$1
}

killalli(){
	killall -i -I $1
}

killjobs(){
	jobs -p | xargs kill
}

lsall(){ echo $1;ls=`l $1`; for file in $ls; do echo "$1/$file"; read enter ; if [[ $enter = "y" ]];then lsall "$1/$file"; fi; done ; }

rmonebyone(){
	for a in `ls`
	do 
	echo $a; echo $(less $a)
	read rm
	if [[ $rm = 'rm' ]]
	then
		rm $rm
	fi
	done
}
l1(){
	for name in `l $1`; do if [[ -d ${1}${name} ]]; then  echo ${1}${name}; l ${1}${name};read; fi; done
}
# find $1 -maxdepth 1 |xargs ls -ld
# l |xargs ls
treefile(){
	find $1 -maxdepth $2 -print 2>/dev/null|awk '!/\.$/ {for (i=1;i<NF;i++){d=length($i);if ( d < 5 && i != 1 )d=5;printf("%"d"s","|")}
print "---"$NF}' FS='/'
}
treedir(){
	find $1 -maxdepth $2 -type d -print 2>/dev/null|awk '!/\.$/ {for (i=1;i<NF;i++){d=length($i);if ( d < 5 && i != 1 )d=5;
printf("%"d"s","|")}print "---"$NF}' FS='/'
}
#dd
# dmesg|tail
#export -f ls1 readfile
#替换回车
#sed ":a;N;s/\n/ /g;ta"
#sed ":a;N;s/\n/ /g;ba"

