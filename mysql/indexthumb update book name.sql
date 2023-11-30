update book,(SELECT LEFT(TRIM(SUBSTRING(description,POSITION(' - ' IN description)+3)),255) aaa,bookid id FROM test.indexthumb) as temp
set name=aaa
where book.id=temp.id