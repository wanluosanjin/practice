for a in `ls` ; do echo $a; echo $(less $a); read rm;
if [[ $rm = 'rm' ]];
then
	rm $rm
fi
done
lsall(){ echo $1;ls=`l $1`; for file in $ls; do echo "$1/$file"; read enter ; if [[ $enter = "y" ]];then lsall "$1/$file"; fi; done ; }
#替换回车
sed ":a;N;s/\n/ /g;ta"
sed ":a;N;s/\n/ /g;ba"

