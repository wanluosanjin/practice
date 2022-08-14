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