DELIMITER $
create procedure addto (in idi char(10),in namei char(10),
in idj char(10),in namej char(10), in gra smallint,out a char(20))
begin
if( idi in (select sid from student)) then
if(gra < 100 and gra > 0) then
/*if(idj in (select cid from course where cid in (select cid 
from sc where sid = idi))) then*/
insert into sc (sid,sname,cid,cname,grade) values
				(idi,namei,idj,namej,gra);
set @a = 'got!';
/*else
set a = 'vcid';
end if;*/
else
set a = 'vgra';
end if;
else
set a = 'vsid';
end if;
end
$
DELIMITER ;
