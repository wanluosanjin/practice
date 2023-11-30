var app = new Vue({
    el: '#app',
    data: {
        mod: 0,//0是图片,1是teacher,2是book//要先把数据准备好再切换mod,否则计算属性会蹦错
        bookteacher:'',
        bookname:'',
        page:0,
        pagedata: {},
        teacherdata:{},
        bookdata:{}
    },
    methods: {
        changemod(mod){
            this.mod=mod;
        },
        刷新title(title){
            document.getElementsByTagName("title")[0].innerText = title;
        },
        刷新pagedata: function(pagenum){
            axios.get('next',{
                params:{
                    pagenum:pagenum,
                },
                headers: {'content-type': 'application/json'},
            })
            .then(resp => {
                this.pagedata=resp.data;
                this.page=pagenum;
                this.刷新title('page '+pagenum);
                this.changemod(0);
                //可能是axios是多线程
            });//这里蹦错,Error in created hook: "TypeError: Cannot read property 'pageNumber' of undefined"
        },
        刷新teacherdata(teacher){//teacher不用encodeurl
            teacher=encodeURI(teacher);
            axios.get('teacher?teacher='+teacher,{
                // params:{
                //     //在param里用参数会被编码,而且与浏览器的不同,[]不会被替代
                //     teacher:encodeURI(this.pagedata.content[event.target.id].teacher),
                // },
                headers: {'content-type': 'application/json'},
            })
            .then(resp => {
                this.teacherdata=resp.data;//data不符合格式
                this.changemod(1);
            });bookName
        },
        刷新bookdata(teacher,bookname){//包括bookteacher和bookname
            axios.get('book',{
                params:{
                    teacher:teacher,
                    bookname:bookname
                },
                headers: {'content-type': 'application/json'},
            })
            .then(resp => {
                this.bookdata=resp.data;
                this.bookteacher=teacher;
                this.bookname=bookname;
                this.changemod(2);
            });
        },
        点击: function(event) {
            if (event) {
                if (this.mod==0) {
                    if(this.pagedata[event.target.id].teacher=="[]"){
                        this.bookthumb(this.pagedata[event.target.id].bookName.split(' ',1));
                    } else{
                        this.刷新teacherdata(this.pagedata[event.target.id].teacher);
                    }
                } else if(this.mod==1){//teacher模式下载过则切换book,未下载则下载
                    this.bookthumb(this.teacherdata[event.target.id].bookName.split(' ',1));
                    // if(this.teacherdata[event.target.id].downloaded){
                    //     this.刷新bookdata(this.teacherdata[event.target.id].teacher,this.teacherdata[event.target.id].bookName)
                    // } else {
                    // params:{//bookid后不知为何多加了个[]
                    // bookid:this.teacherdata[event.target.id].bookName.split(' ',1),
                    // }
                    //     this.刷新title("下载"+this.teacherdata[event.target.id].bookName.split(' ',1));
                    // }
                }
            }
        },
        bookthumb(num){
            axios.get('bookthumb?bookid='+num,{
            });
        },
        getExists(teacher,bookid,bookname){
            teacher=encodeURI(teacher);
            bookname=encodeURI(bookid+' '+bookname);
            axios.get('exists?teacher='+teacher+'&'+'bookname='+bookname,{
                headers: {'content-type': 'application/json'},
            })
            .then(resp => {
                return resp.data;
            });
        },
        下一页: function() {
            this.刷新pagedata(this.page+1);
        },
        上一页: function() {
            if(this.page==0){
                alert("已经是第一页了");
                return;
            }
            this.刷新pagedata(this.page-1);
        },
    },
    computed: {
        getbookid: function(){
            return function(index){
                //计算属性不能有参数,但可以用闭包传参
                //计算属性必须考虑是否初始化,条件和数据之间有延迟
                //条件改变则重新计算,此时如果新条件未初始化则崩错
                // if(!'content' in this.pagedata)return null;
                return this.pagedata[index].id;
            }
        },
        paths: function(){//图片自动更新
            let a = this.pagedata;
            if(!a)return null;//不判断初始化容易崩错,computed在一开始似乎就会计算
            if(this.mod==0){
                let paths = [];
                //数组有foreach方法
                for(var i=0; i<a.length; i++){
                    //文件名有id和空格
                    let url = 'indexthumb/'+a[i].teacher+'/'+a[i].bookName.split(" ")[0];
                    //把路径拆开再组装,其实直接把\改为/也可以
                    paths.push(encodeURI('imgs/'+url+'.jpg'))
                }
                return paths;
            }else if(this.mod==1){
                let paths = [];
                for(var i=0; i<this.teacherdata.length; i++){
                    let url = 'indexthumb/'+this.teacherdata[i].teacher+'/'+this.teacherdata[i].bookName.split(" ")[0];
                    paths.push(encodeURI('imgs/'+url+'.jpg'))
                }
                return paths;
            }else if(this.mod==2){
                let paths = [];
                for(var i=0; i<this.bookdata.length; i++){
                    let url = 'bookthumb/'+this.bookteacher+'/'+this.bookname+'/'+this.bookdata[i];
                    paths.push(encodeURI('imgs/'+url));
                }
                return paths;
            }i

        },
        title: function(){//浮字
            return function(index){
                let a = this.pagedata;
                if(!a)return null;//不判断初始化容易崩错,computed在一开始似乎就会计算
                if(this.mod==0){
                    return a[index].teacher+" "+a[index].bookName;
                }else if(this.mod==1){
                    let title = '';
                    if (this.teacherdata[index].downloaded) {
                        title+="已下载 "
                    }
                    title+=this.teacherdata[index].teacher+" ";
                    return title+=this.teacherdata[index].bookName;
                }
                return "";
            }
        },
        
    },

    created() {  //全局监听键盘事件
        var _this = this;//chrome删除这句后再加上就失效了
        this.刷新pagedata(0);
        document.onkeydown = function(e) {
            //这里面似乎只能用_this,因为里面的this被document占用
            let key = window.event.keyCode;
            if (key == 68) {//d
                _this.下一页();
            }
            else if(key == 65){//a
                _this.上一页();
            }
            else if(key == 71){//g
                let pagenum = prompt("请输入页数：", "0");
                _this.刷新pagedata(Number(pagenum));
            }
            else if(key == 66){//b
                if (_this.mod==1) {
                    _this.changemod(0)
                } else if (_this.mod==2){
                    _this.changemod(1);
                }
            }
            else if(key == 84){//t
                let teacher = prompt("[]","[]");
                _this.刷新teacherdata(teacher);
            }
        };
    }
  })