from flask import render_template,request,redirect,url_for
from app import app,db,bootstrap
from app.forms import addForm,delForm,teaSearch,stuCh,nothingForm
from app.forms import LoginForm,RegisterForm,stuForm,teaForm,updForm
from app.model import UserRegister,UserLogin,StudentShow,TeacherShow

@app.route('/hello')
def hello():
    return render_template("hello.html")


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'JO' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        user_name = request.form.get('username')
        password = request.form.get('password')
        user_type = request.form.get('user_type')
        User = UserLogin(user_name,password,user_type)
        if(User.validate()):
            if(user_type == 's'):
                return redirect(url_for("stuShow",id=user_name))
            else:
                return redirect(url_for("teaShow",id=user_name))
    return render_template("login.html",title='登 录',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user_name = request.form.get('username')
        password = request.form.get('password')
        user_type = request.form.get('user_type')
        User = UserRegister(user_name,password,user_type)
        User.register()
        return redirect(url_for("login",id=user_name))
    return render_template("register.html",title='注 册',form=form)

@app.route('/stuShow?<id>', methods=['GET', 'POST'])
def stuShow(id):
    stu = StudentShow(id)
    form = stuForm()
    orderInfo = stu.show2()
    if request.method == 'POST':
        order = request.form.get('order')
        c = request.form.get('Choose')
        if(order):
            orderInfo = stu.order()
            return render_template("studentshow.html",title='学生查看',stu=[stu.show1(),
                                                            orderInfo],form=form)
        if(c):
            return redirect(url_for("stuChoose",id=id))
    return render_template("studentshow.html",title='学生查看',stu=[stu.show1(),
                                                    orderInfo],form=form)

@app.route('/stuChoose?<id>', methods=['GET', 'POST'])
def stuChoose(id):
    stu = StudentShow(id)
    form = stuCh()
    c = stu.show3()
    if request.method == 'POST':
        cname = request.form.get('cname')
        stu.Choose(cname)
        return redirect(url_for("stuShow",id=id))
    return render_template("stuChooseCourse.html",title="选课",form=form,CourseName=c)

@app.route('/deal_choose?<id>', methods=['GET', 'POST'])
def dealChoose(id):
    teacher = TeacherShow(id)


@app.route('/teaShow?<id>', methods=['GET', 'POST'])
def teaShow(id):
    form1 = teaForm()
    form2 = teaSearch()
    teacher = TeacherShow(id)
    teacher.createView()
    if request.method == 'POST':
        group_name = request.form.get('group_name')
        group_course = request.form.get('group_course')
        del_or_add = request.form.get('del_or_add')
        search_name = request.form.get('search_name')
        search_course = request.form.get('search_course')
        scc = request.form.get('stu_choose_course')
        if(group_name):
            info = teacher.group_name()
            return render_template("teachershow.html",title='老师查看',tea=info,form1=form1,
                                                                        form2=form2)
        if(group_course):
            info = teacher.group_course()
            print(info)
            return render_template("teachershow.html",title='老师查看',tea=info,form1=form1,
                                                                        form2=form2)
        if(search_name):
            print(search_name)
            info = teacher.search_name(search_name)
            print(info)
            return render_template("teachershow.html",title='老师查看',tea=info,form1=form1,
                                                                        form2=form2)
        if(search_course):
            print(search_course)
            info = teacher.search_course(search_course)
            print(info)
            return render_template("teachershow.html",title='老师查看',tea=info,form1=form1,
                                                                        form2=form2)

        if(del_or_add == '1'):
            return redirect(url_for('teacheradd',id=id))
        if(del_or_add == '2'):
            return redirect(url_for('teacherdel',id=id))
        if(del_or_add == '3'):
            return redirect(url_for('teacherupd',id=id))
        if(scc):
            print(scc)
            print('scc')
            return redirect(url_for('dealchoose',id=id))


    info = teacher.show()
    return render_template("teachershow.html",title='老师查看',tea=info,form1=form1,
                                                                form2=form2)

@app.route('/teacheradd?<id>', methods=['GET', 'POST'])
def teacheradd(id):
        addform = addForm()
        teacher = TeacherShow(id)
        if request.method == 'POST':
            a = request.form.get('sid')
            b = request.form.get('sname')
            c = request.form.get('cid')
            d = request.form.get('cname')
            e = int(request.form.get('grade'))
            print(type(a),type(b),type(c),type(d),type(e))
            teacher.addGrade([a,b,c,d,e])
            return redirect(url_for("teaShow",id=id))
        return render_template("teacheradd.html",title='添加',form=addform)

@app.route('/teacherdel?<id>', methods=['GET', 'POST'])
def teacherdel(id):
    delform = delForm()
    teacher = TeacherShow(id)
    if request.method == 'POST':
        b = request.form.get('sid')
        d = request.form.get('cname')
        teacher.delGrade([b,d])
        return redirect(url_for("teaShow",id=id))

    return render_template("teacherdel.html",title='删除',form=delform)

@app.route('/teacherupd?<id>', methods=['GET', 'POST'])
def teacherupd(id):
    teacher = TeacherShow(id)
    updform = updForm()
    if request.method == 'POST':
        b = request.form.get('sname')
        d = request.form.get('cname')
        e = int(request.form.get('grade'))
        print(b,d,e)
        print(type(b),type(d),type(e))
        teacher.update(b,d,e)
        return redirect(url_for("teaShow",id=id))

    return render_template("teacherupd.html",title='修改',form=updform)

@app.route('/dealchoose?<id>', methods=['GET', 'POST'])
def dealchoose(id):
    teacher = TeacherShow(id)
    form =  nothingForm()
    info = teacher.shownothing()

    if request.method == 'POST':
        b = request.form.get('sname')
        d = request.form.get('cname')
        teacher.agreeCourse(b,d)
        return redirect(url_for("teaShow",id=id))
    return render_template("deal_choose.html",title='查看学生选课',info=info,form=form)
