from cx_Oracle import connect
from datetime import datetime

#메뉴만들기 (함수)
#1. 학생 등록 (입력) / 2. 강의장 조회 / 3. 학생 조회
# 4. 학생정보를 파일로 내보내기 / 0. 종료
con = connect("ekdh3904/fogus12@192.168.0.12:1521/xe"); 

cur = con.cursor()
def register_student():
    name = input("학생 이름 : ")
    birthday = input("학생 생일 YYYY/mm/dd :")
    class_number = int(input("학생 강의장 : "))
    mid_test = int(input("학생 중간고사 성적 : "))
    final_test = int(input("학생 기말고사 성적 : "))
    
    
    
    
    
    sql = f"insert into mar11_student values(mar11_student_seq.nextval,'{name}',TO_DATE('{birthday}', 'YYYY/MM/DD'), {class_number},";
    sql += f"{mid_test}, {final_test})"
 
    cur.execute(sql)
    
    if(cur.rowcount==1):
        print("등록 완료!")
        con.commit()
def showClass():
    sql = "select * from mar11_class"
    cur.execute(sql)
    
    for class_no, location in cur:
        print(f"{class_no}강의장 / {location}")
    con.close()
    
def showStudent():
    sql = "select * from mar11_student"
    cur.execute(sql)
    
    for sno, name,birthday,class_no, mid_test, final_test in cur:
        
        d = datetime.strftime(birthday, "%Y/%m/%d/(%A)")
        now = datetime.now()
        age = now.year - birthday.year
        average = (mid_test + final_test) / 2
        print(f"이름 : {name} / 생일 : {d} / 나이 : {age}")
        print(f"강의장 : {class_no}강의장 / 중간점수 : {mid_test}/ 기말점수 : {mid_test}")
        print(f"평균점수 : {average}")
    con.close() 
def makeFile():
    sql = "select * from mar11_student"
    cur.execute(sql)
    
          
    file = open("C:/Users/sdedu/Desktop/메추라기/student.csv", "w", encoding="UTF-8")
    file.write("이름, 생일, 강의장, 중간고사, 기말고사\n")
    for name, birthday, class_number,mid_test,final_test in cur:
        file.write(f"{name},'{birthday}',{class_number},{mid_test},{final_test}\n ")
        
    
    print("작성 완료!")
    file.close()

def execute_program():
 
    while True:
        option = int(input("1. 학생 등록 / 2. 강의장 조회 / 3. 학생 조회/ 4.파일로 내보내기 / 0. 종료"))
        if option == 1:
            register_student()
        elif option == 2:
            showClass()
        elif option == 3:
            showStudent()
        elif option == 4:
            makeFile()
        elif option == 0:
            print("프로그램을 종료합니다.")
            break
        else:
            print("옵션을 잘못 입력하셨습니다.")
            continue
 
        

execute_program()











