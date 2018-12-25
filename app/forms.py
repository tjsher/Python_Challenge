from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,RadioField
from wtforms import IntegerField,BooleanField,SubmitField,SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='请输入户名')])
    password = PasswordField('密码',validators=[DataRequired(message='请输入密码')])
    user_type = StringField('用户类型',validators=[DataRequired(message='请输入')])
    submit = SubmitField('登录',id="sub")

class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(message='请输入户名')])
    password = PasswordField('密码',validators=[DataRequired(message='请输入密码')])
    user_type = StringField('用户类型',validators=[DataRequired(message='请输入')])
    submit = SubmitField('注册',id="sub")

class stuForm(FlaskForm):
    order = BooleanField('order')
    submit = SubmitField('提交')
    Choose = BooleanField('我要选课')

class stuCh(FlaskForm):
    cname = StringField("课程名")
    submit = SubmitField('提交')


class teaForm(FlaskForm):
    submit = SubmitField('提交')
    group_name = BooleanField('按姓名查看')
    del_or_add= RadioField('增删改',choices=((1,'增'),(2,'删'),(3,'改')))
    group_course = BooleanField('按课程名查看')
    stu_choose_course = BooleanField('查看学生选课情况')

class teaSearch(FlaskForm):
    search_name = StringField('名字')
    search_course = StringField('课程')
    submit = SubmitField('提交')

class addForm(FlaskForm):
    submit = SubmitField('添加')
    sname = StringField('学生姓名',validators=[DataRequired(message='请输入')])
    sid = StringField('学号',validators=[DataRequired(message='请输入')])
    cname = StringField('课程名',validators=[DataRequired(message='请输入')])
    cid = StringField('课程号',validators=[DataRequired(message='请输入')])
    grade = IntegerField('成绩',validators=[DataRequired(message='请输入')])

class nothingForm(FlaskForm):
    submit = SubmitField('同意选课')
    sname = StringField('姓名',validators=[DataRequired(message='请输入')])
    cname = StringField('课程名',validators=[DataRequired(message='请输入')])

class delForm(FlaskForm):
    submit = SubmitField('删除')
    sid = StringField('学号',validators=[DataRequired(message='请输入')])
    cname = StringField('课程号',validators=[DataRequired(message='请输入')])

class updForm(FlaskForm):
    submit = SubmitField('修改')
    sname = StringField('姓名',validators=[DataRequired(message='请输入')])
    cname = StringField('课程名',validators=[DataRequired(message='请输入')])
    grade = IntegerField('成绩',validators=[DataRequired(message='请输入')])
