import pymysql

class UserLogin():
    def __init__(self,username,password,user_type):
        self.con = pymysql.connect("localhost",'root','0','mydb')
        self.username = username
        self.password = password
        self.user_type = user_type
        self.cursor = self.con.cursor()

    def CommitSQL(self,sql):
        self.cursor.execute(sql)
        self.con.commit()
        return self.cursor.fetchone()[0]

    def validate(self):
        sql = "select * from login where id='%s'and lpass='%s' and ltype='%s'\
                        "%(self.username,self.password,self.user_type)
        self.cursor.execute(sql)
        self.con.commit()
        if(self.cursor.fetchall()):
            return True
        else : return False


class UserRegister():
    def __init__(self,username,password,user_type):
        self.con = pymysql.connect("localhost",'root','0','mydb')
        self.cursor = self.con.cursor()
        self.username = username
        self.password = password
        self.user_type = user_type

    def CommitSQL(self,sql):
        self.cursor.execute(sql)
        self.con.commit()

    def register(self):
        sql = "insert into login (id,lpass,ltype) \
                values ('%s','%s','%s')" %(self.username,self.password,self.user_type)
        self.CommitSQL(sql)

class StudentShow():
    def __init__(self,id):
        self.con = pymysql.connect("localhost",'stu','0','mydb')
        self.cursor = self.con.cursor()
        self.id = id

    def show1(self):
        sql = "select * from student where sid = '%s' " % self.id
        return self.CommitSQL(sql)
    def show2(self):
        sql = "select * from sc where sid = '%s'" % self.id
        return self.CommitSQL(sql)

    def show3(self):
        cn = self.CommitSQL("select cid,cname from course")
        res = []
        for i in cn:
            res.append(i[1])
        return res

    def order(self):
        sql = "select * from sc where sid = '%s' order by grade" %self.id
        return self.CommitSQL(sql)

    def Choose(self,cname):
        info = self.show1()
        sql = "select cid,cname from course where cname='%s'"%cname
        res = self.CommitSQL(sql)
        print(info[0][0],info[0][1],res[0][0],res[0][1])
        sql2 = "insert into nothing (sid,sname,cid,cname) values('%s','%s','%s','%s')"\
                            %(info[0][0],info[0][1],res[0][0],res[0][1])
        self.cursor.execute(sql2)
        self.con.commit()

    def CommitSQL(self,sql):
        self.cursor.execute(sql)
        self.con.commit()
        return self.cursor.fetchall()

class TeacherShow():
    def __init__(self,id):
        self.con = pymysql.connect("localhost",'root','0','mydb')
        self.cursor = self.con.cursor()
        self.id = id
        #SET SQL_SAFE_UPDATES = 0;

    def show(self):
        sql = "select * from teacherView"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def createView(self):
        sql = "drop view if exists teacherView"
        self.CommitSQL(sql)
        sql = "create view teacherView as select sid,sname,cname,grade from\
         sc where cid in ( select cid from tc where tid = '%s')"%self.id
        self.CommitSQL(sql)
        print("teacherview created  ")


    def shownothing(self):
        sql = "select * from nothing where Sid in(\
        select sid from teacherView)"
        return self.CommitSQL(sql)


    def agreeCourse(self,sname,cname):
        info = self.CommitSQL("select * from nothing where sname = '%s' and \
                                        cname = '%s'"%(sname,cname))
        print(len(info))
        for i in info:
            self.addGrade([[0],i[1],i[2],i[3],0])
            self.cursor.execute("delete from nothing where Sid='%s' and \
                                            Cid='%s'" %(i[0],i[2]))
            self.con.commit()


    def CommitSQL(self,sql):
        self.cursor.execute(sql)
        self.con.commit()
        return self.cursor.fetchall()

    def group_name(self):
        sql = "select * from teacherView order by sname,grade desc"
        return self.CommitSQL(sql)

    def group_course(self):
        sql = "select * from teacherView order by cname,grade desc"
        return self.CommitSQL(sql)

    def search_name(self,name):
        sql = "select * from teacherView where sname = '%s'"%name
        return self.CommitSQL(sql)

    def search_course(self,course):
        sql = "select * from teacherView where cname = '%s'"%course
        return self.CommitSQL(sql)

    def update(self,sname,cname,grade):
        sql = "update sc set grade = %d where sname = '%s' and cname = '%s' "\
                            %(grade,sname,cname)
        self.cursor.execute(sql)
        self.con.commit()

    def addGrade(self,stuInfo):
        sql = "call addto('%s','%s','%s','%s',%d,@a);"\
                %(stuInfo[0],stuInfo[1],stuInfo[2],stuInfo[3],stuInfo[4])

        self.CommitSQL(sql)
        self.cursor.execute("select @a")
        self.con.commit()
        print('got or error?',self.cursor.fetchone()[0])

    def delGrade(self,stuInfo):
        k = self.CommitSQL("select sid from teacherView where sid='%s'"%stuInfo[0])
        if(k):
            sql = "delete from sc where sid = '%s' and cname = \
                                '%s'"%(stuInfo[0],stuInfo[1])
            self.cursor.execute(sql)
            self.con.commit()
