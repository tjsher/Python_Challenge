<%@ page import="java.sql.*"%>
<%@ page language="java" contentType="text/html; charset=GB18030"
pageEncoding="GB18030"%> 

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=GB18030">
<title>ѧ����Ϣ�鿴</title>
<link rel="stylesheet" href="css/table.css">
</head>
<body>
<body style="background: url(img/2.jpg);">
<%
request.setCharacterEncoding("GBK");

Class.forName("com.mysql.jdbc.Driver");
String url="jdbc:mysql://localhost:3306/exp1?user=u10&password=root&useUnicode=true&characterEncoding=utf8&serverTimezone=GMT%2B8&useSSL=false";
Connection conn=DriverManager.getConnection(url);
String scno = (String)session.getAttribute("Sname");
Statement stmt=conn.createStatement();
String sql="select sno, sname, ssex, sage, sdept from student where sno=?";
PreparedStatement pst=conn.prepareStatement(sql);
pst.setString(1, scno);
out.println("��ӭ"+scno+"��½��");
ResultSet rs=pst.executeQuery();
%>
<h2>ѧ����Ϣ��</h2>
<div class="table-wrapper">
    <table class="fl-table">
        <thead>
        <tr>
            <th>���</th>
            <th>ѧ��</th>
            <th>����</th>
            <th>�Ա�</th>
            <th>����</th>
            <th>ϵ��</th>
        </tr>
        <%
int i=0;
while(rs.next()){
%>
<tr>
<td height=20><%=i+1 %></td>
<td ><%=rs.getString(1) %></td>
<td ><%=rs.getString(2) %></td>
<td ><%=rs.getString(3)%></td>
<td ><%=rs.getInt(4)%></td>
<td ><%=rs.getString(5) %></td>

</tr>

<%
i=i+1;
}
conn.close();
%>
        </thead>
    </table>
</div>
</body>
</html>