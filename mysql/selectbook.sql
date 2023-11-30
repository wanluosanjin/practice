SELECT book.id,name,teacher,teacherid FROM test.book join teacher t
where book.teacherid = t.id and t.teacher='[]'

#SELECT book.id,name,teacher,teacherid FROM test.book join 
#(SELECT * FROM test.teacher where teacher="[復八磨直兎]") as aaa 
#where book.teacherid = aaa.id;