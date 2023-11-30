var app = new Vue({
    el: '#vue2',
    data: {
        teachernum:0,
        booknum:0,
        pagedata:{},
    },
    methods: {
        下一本: function() {
            axios.get('/booknext',{
                params:{
                    teachernum:this.teachernum,
                    booknum:this.booknum,
                },
                headers: {'content-type': 'application/json'},
            })
            .then(resp => {
                this.pagedata=resp.data;
            });
        },
        上一本: function() {
            axios.get('/bookup',{
                params:{
                    teachernum:this.teachernum,
                    booknum:this.booknum,
                },
                headers: {'content-type': 'application/json'},
            })
            .then(resp => {
                this.pagedata=resp.data;
            });
        },
    },
    computed: {
        paths: function(){//图片自动更新
            let a = this.pagedata;
            if(!a.content)return null;//不判断初始化容易崩错,computed在一开始似乎就会计算
            if(this.mod==0){
                let paths = [];
                //数组有foreach方法
                for(var i=0; i<a.content.length; i++){
                    //文件名有id和空格
                    let url = 'indexthumb/'+a.content[i].teacher+'/'+a.content[i].id+' '+a.content[i].name;
                    //把路径拆开再组装,其实直接把\改为/也可以
                    paths.push(encodeURI('imgs/'+url+'.jpg'))
                }
                return paths;
            }else if(this.mod==1){
                let paths = [];
                for(var i=0; i<this.teacherdata.length; i++){
                    let url = 'indexthumb/'+this.teacherdata[i].teacher+'/'+this.teacherdata[i].id+' '+this.teacherdata[i].name;
                    paths.push(encodeURI('imgs/'+url+'.jpg'))
                }
                return paths;
            }

        },
        title: function(){//浮字
            return function(index){
                let a = this.pagedata;
                if(!a.content)return null;//不判断初始化容易崩错,computed在一开始似乎就会计算
                if(this.mod==0){
                    return a.content[index].name;
                }else if(this.mod==1){
                    return this.teacherdata[index].name;
                }
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
                _this.下一本();
            }
            else if(key == 65){//a
                _this.上一本();
            }
        };
    }
  })