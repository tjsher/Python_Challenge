import pymysql
import random
# --coding:uft-8--
db = pymysql.connect("localhost",'root','0','mydb')
cursor = db.cursor()
names = ['你','好','也','大','家','副','拉','赤','系','朴']
courses = ['离散数学','数据结构','算法导论','操作系统','数据库','毛概','数学','概率论','英语',
'拳击','跑步','马概','思修','睡觉','砍树','拔草','喝水']
sex = ['男','女']
majors = ['计算机','造船','造火箭','造车','造飞机']
def stuInsert():
    for i,namei in enumerate(names):#student
        for j,namej in enumerate(names):
            random_name = namei + namej
            random_id = '20161060' + str(i) + str(j)
            random_sex = sex[random.randint(0,1)]
            random_age = random.randint(18,22)
            random_major = majors[random.randint(0,4)]
            print(random_name,random_id,random_sex,random_age,random_major)
            cursor.execute("insert into student (sid,sname,ssex,sage,smajor) values \
                            ('%s','%s','%s','%s','%s')"% (random_id,random_name, \
                            random_sex,random_age,random_major))
            db.commit()

def teaInsert():
    tnames = ['王为','李号','刘看','李纳','钱安','张凯','冬名','周至','郭言','郑里',
    '音位','矿叶','安泉','威里','动时','水阿','首莫']
    stuff = ['教授','副教授','讲师']
    for i,namei in enumerate(tnames):
        random_id = '20001060' + str(i)
        random_major = majors[random.randint(0,4)]
        random_stuff = stuff[random.randint(0,2)]
        print(i,namei,random_id,random_major,random_stuff)
        cursor.execute("insert into teacher (tid,tname,tstuff,tmajor) values \
                        ('%s','%s','%s','%s')"% (random_id,namei, \
                        random_stuff,random_major))
        db.commit()
        cid = str(i)
        course = courses[i]
        cmajor = random_major
        print(cid,cmajor,course)
        cursor.execute("insert into course (cid,cname,cmajor) values \
                        ('%s','%s','%s')"% (cid,course,cmajor))
        db.commit()



def courseInsert():
    for i,course in enumerate(courses):
        cid = str(i)
        cmajor = majors[random.randint(0,4)]
        print(cid,cmajor,course)
        cursor.execute("insert into course (cid,cname,cmajor) values \
                        ('%s','%s','%s')"% (cid,course,cmajor))
        db.commit()

def scInsert():
    cursor.execute("select sid,sname,smajor,cid,cname,cmajor from student,course where \
                    student.smajor=course.cmajor")
    db.commit()
    Mj = cursor.fetchall()
    for i in Mj:
        cursor.execute("insert into sc values('%s','%s','%s','%s',%d)"%(i[0],i[1],
                    i[3],i[4],random.randint(0,100)))
        db.commit()

def tcInsert():
    cursor.execute("select tid,tname,tmajor,cid,cname,cmajor from teacher,course where \
                    teacher.tmajor=course.cmajor")
    db.commit()
    Mj = cursor.fetchall()
    t = []
    c =['离散数学']
    a = []
    for i in Mj:
        if(i[4] not in c):
            c.append(i[4])
            print(len(c))
            a.append(t[random.randint(0,len(t) - 1)])
            t = []
        t.append(i)
    for i in a:
        print(i)
        cursor.execute("insert into tc (tid,tname,cid,cname) values\
            ('%s','%s','%s','%s')"%(i[0],i[1],i[3],i[4]))
        db.commit()


stuInsert()
teaInsert()
scInsert()
tcInsert()
