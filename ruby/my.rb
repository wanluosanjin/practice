def lss path
    Dir.entries path
end
#autoload
#def A.a  def self.a 效果不同,后者无法接受示例对象,只能A调用

#    [6..n,123]
class A
    class <<A 
        def a  
            p a
        end
    end
    def aa
        p aa 
    end
end 
class AAA
    def aaa()
        puts"aaaaaa"  "bbbbb"
    end
end
3.times do 
    p AAA.new.class
end
p AAA.new.methods.length
p AAA.methods.length
p "aaaa".methods.length,String.methods.length


def go (n)
    p n
    [6..n]
end
go(10).map{|n|p n}