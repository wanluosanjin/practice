insert ignore into blankrow
select num,cha from(
SELECT
    @rownum:=@rownum+1 AS rownum,bookid,
    if(@rownum!=bookid,bookid-@rownum,null)as cha,
    if(@rownum!=bookid,@rownum:=bookid,null)as num
FROM indexthumb,
    (SELECT @rownum:=0) as temp1)as temp2  where cha is not null
