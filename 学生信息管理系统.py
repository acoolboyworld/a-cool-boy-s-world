filename='student.txt'
import os
def show_choose():
    print("==========================学生信息管理系统==========================")
    print()
    print("-----------------------------功能菜单------------------------------")
    print()
    print("                         1.录入学生信息")
    print("                         2.查找学生信息")
    print("                         3.删除学生信息")
    print("                         4.修改学生信息")
    print("                         5.排序学生信息")
    print("                         6.统计学生总数")
    print("                         7.显示学生信息")
    print("                         0.退出信息管理系统")
    print()
    print("------------------------------------------------------------------")

def main():
    while True:
        show_choose()
        choice=int(input('请选择：'))
        if choice in [0,1,2,3,4,5,6,7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n\n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用')
                    break #退出系统
                else:
                    continue
            elif choice == 1:
                insert()   #录入学生信息
            elif choice == 2:
                search()   #查找学生信息
            elif choice == 3:
                delete()   #删除学生信息
            elif choice == 4:
                modify()   #修改学生信息
            elif choice == 5:
                sort()     #排序学生信息
            elif choice == 6:
                total()    #统计学生信息
            elif choice == 7:
                show()     #显示学生信息

def insert():
    stu_list=[]  #用于存储学生信息的列表
    while True:
        stu_name=input('请输入姓名：')
        if not stu_name:
            break
        stu_id = input('请输入学号（如1001）：')
        if not stu_id:  # 使用布尔值，若布尔值为0，则为False,若布尔值为非0，则为Ture。
            break
        try:
            stu_score_eng=int(input('请输入英语成绩：'))
            stu_score_py=int(input('请输入Python成绩：'))
            stu_score_math = int(input('请输入Math成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入！！！')
            continue
        #将录入的学生信息保存到字典中
        stu_info={'学号':stu_id,'姓名':stu_name,'English成绩':stu_score_eng,'Python成绩':stu_score_py,'Math成绩':stu_score_math}
        #将学生信息添加到列表中
        stu_list.append(stu_info)

        answer = input('是否继续添加？y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break   #退出循环
        #调用save（）函数用于储存学生信息
    save(stu_list)
    print('学生信息录入完毕!!!')

def save(lst):
    '''存储学生信息'''
    try:
        stu_txt = open(filename,'a',encoding='utf-8')  #追加模式打开，encoding 防止乱码
    except:
        stu_txt = open(filename,'w',encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    """查找学生信息：
    1.按ID查找
    2.按姓名查找"""
    stu_query = []  # 存储需要查询的信息
    while True:
        id = ''  # 初始化为空
        name = ''
        if os.path.exists(filename):  # 如果文件存在
            mode = input('按ID查找请输入1，按姓名查找请输入2:')  # 输入的是字符串
            if mode == '1':
                id = input('请输入学生ID:')
            elif mode == '2':
                name = input('请输入学生的姓名:')
            else:
                print('您的输入有误，请重新输入:')
                search()

            with open(filename, 'r', encoding='utf-8') as rfile:  # 以读的形式打开
                student = rfile.readlines()  # 将包含字典的字符串放入列表中
                for item in student:  # 遍历列表中的字符串形式的字典
                    d = dict(eval(item))  # 剥掉引号，转为字典

                    if id != '':  # 如果输入的ID不为空
                        if d['学号'] == id:  # 输入的ID等于列表中的ID
                            stu_query.append(d)  # 需要查询的信息添加到另一个列表
                    elif name != '':  # 如果输入的姓名不为空
                        if d['姓名'] == name:  # 等于已有的
                            stu_query.append(d)  # 添加需要查询的东西

            # 显示查询结果
            show_student(stu_query)  # 显示需要查询的信息
            # 清空列表
            stu_query.clear()  # 清空这个暂时的列表

            answer = input('是否要继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:  # 文件不存在
            print('暂未保存学生信息')
            return

def show_student(lst):
    """显示查找的学生信息"""
    if len(lst) == 0:  # 需要查询的列表为空
        print('没有查询到学生信息，无数据显示！！！')
        return  # 返回调用的地方，所以这里的后面代码不执行
    # 定义标题的显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('学号 ', '姓名', 'English成绩',
                              'python成绩', 'Math成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('学号'),
                                 item.get('姓名'),
                                 item.get('English成绩'),
                                 item.get('Python成绩'),
                                 item.get('Math成绩'),
                                 int(item.get('English成绩')) + int(item.get('Python成绩')) + int(item.get('Math成绩'))
                                 ))

def delete():
    '''删除学生信息'''
    show()
    while True:
        del_stu_id=input('请输入要删的学生的ID：')
        if del_stu_id !='':
            if os.path.exists(filename):  #os.path.exists(path),如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
                with open(filename,'r',encoding='utf-8') as file:  #以读的形式打开文件
                    stu_old=file.readlines()    #每一行元素作为独立字符串，放入列表中
            else:
                stu_old=[]
            flag = False  #标记是否删除  （目前不知道是啥意思）
            if stu_old:  #如果存stu_old存在，则执行下一步  上面的else创建了stu_old=[]
                with open(filename,'w',encoding='utf-8') as wfile:
                    d = {}
                    for item in stu_old:
                        d = dict(eval(item))  #eval() 函数剥去引号，dict转变为字典
                        if d['学号']!=del_stu_id:    #当删除的学号不存在时，执行下一步
                            wfile.write(str(d)+'\n')    #这里是‘w’将原内容覆盖，写入出了要删除内容外的所有内容
                        else:
                            flag=True  #表示删除
                    if flag:
                        print(f'ID为{del_stu_id}的学生信息已被删除')
                    else:
                        print(f'没有找到ID为{del_stu_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()   #删除之后要重新显示所有学生信息
            answer=input('是否继续删除？y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break

def modify():
    '''修改学生信息'''
    show()
    flag = True
    if os.path.exists(filename):   #如果文件存在
        with open(filename,'r',encoding='utf-8') as rfile:  #以读的方式打开
            stu_old = rfile.readlines()
    else:
        return
    mod_stu_id = input('请输入要修改的学生ID：')
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in stu_old:
            d=dict(eval(item))
            if d['学号']==mod_stu_id:
                print('找到学生信息，可以修改他的相关信息！')
                #重新输入这个学生的信息
                while True:
                    try:
                        d['姓名']=input('请输入姓名：')
                        d['English成绩']=int(input('请输入Enlish成绩：'))
                        d['Python成绩']=int(input('请输入Python成绩：'))
                        d['Math成绩']=int(input('请输入Math成绩：'))
                    except:
                        print('您输入的有误，请重新输入!')
                    else:
                        break      #退出循环与while True对应
                wfile.write(str(d)+'\n')

            else:    #输入的学号不存在
                wfile.write(str(d)+'\n')  #写入空字符
                flag = False
            if not flag:
                print('对不起，没有你要查的ID！')
            else:
                print('修改成功！！！')
        answer=input('是否继续修改其他学生信息？y/n\n')
        if answer=='y' or answer=='Y':
            modify()

def sort():
    """排序模块
    1.升序
    2.降序
    又细分为：
    1.按英语成绩
    2.按python
    3.按Java
    4.按总成绩"""
    show()  # 先显示所有的学生信息
    if os.path.exists(filename):  # 文件存在
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_list = rfile.readlines()  # 将每一行元素作为独立字符串，放入列表当中
        student_new = []  # 之后把所有信息添加到这里
        for item in stu_list:
            d = dict(eval(item))
            student_new.append(d)
    else:  # 文件不存在，还没录入生成
        return

    """升序、降序"""
    asc_or_desc = input('请选择(0.升序  1.降序):')
    if asc_or_desc == '0':
        asc_or_desc_boll = False
    elif asc_or_desc == '1':
        asc_or_desc_boll = True
    else:
        print('您的输入有误，请重新输入:')
        sort()

    """按什么排序"""
    mode = input('请选择排序方式(1.按英语成绩排序  2.按python成绩排序  3.按数学成绩排序  0.按总成绩排序)\n')
    if mode == '1':
        student_new.sort(key=lambda x: int(x['English成绩']), reverse=asc_or_desc_boll)    # x：x表示是一个字典
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['Python成绩']), reverse=asc_or_desc_boll)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['Math成绩']), reverse=asc_or_desc_boll)
    elif mode == '0':
        student_new.sort(key=lambda x: int(x['English成绩']) + int(x['Python成绩']) + int(x['Math成绩']), reverse=asc_or_desc_boll)
    else:
        print('您的输入有误，请重新输入！！！')
        sort()

    show_student(student_new)  # 展示排序后的

def total():
    """显示总共多少名学生"""
    if os.path.exists(filename):  # 如果文件存在
        with open(filename, 'r', encoding='utf-8') as rfile:  # 只读方式打开
            students = rfile.readlines()  # 将每一行元素作为独立字符串，放入列表当中
            if students:  # 列表不为空
                print(f'一共有{len(students)}名学生')  # 统计列表长度，即为学生个数
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存信息')

def show():
    """显示模块"""
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:  # 读文件，文件里面数据全为字典
            students = rfile.readlines()  # 将每个字典作为列表中的一个元素
            for item in students:  # 遍历学生列表
                student_lst.append(eval(item))  # 向列表中添加字典
            if student_lst:  # 不为空
                show_student(student_lst)  # 显示出来
    else:
        print('暂未保存学生信息')

if __name__ == '__main__':
    main()
