# pip install pypiwin32

from win32com.client import Dispatch
from itertools import product 
import pikepdf
from tkinter import *    #tkinter 모듈 모두를 가져온다
from tkinter import messagebox # 메세지박스 사용
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
from tkinter.scrolledtext import ScrolledText 
import tkinter.font
import time
import os
# import webbrowser
# import pkg_resources.py2_warn


def help_file() : # 메세지박스 띄우기
    messagebox.showinfo("HELP", "\nFind PDF password Version 1.0 (Trial Version)\n\n"+
                                "Combination     : User's minimum combination setting   \n"+
                                "Dictionary         : Apply password list or password file \n"+
                                "All Combination : Apply all possible combinations (Not recommended)\n\n"+
                                "   - Password length MIN  :  2\n"+
                                "   - Password length MAX  :  6 or less\n\n"+
                                "                                     For more than 7, contact \n\n"+
                                "  For 100,000 cases, it takes about 7 minutes\n" +
                                "  (The time required may vary depending on the computer\n" +
                                "   specifications)\n\n" +
                                " [Notic] CLose the PDF Program and run it.\n" +
                                "                                                  Date : 12/28/2022\n" +
                                "                                                  jyh4ever@gmail.com\n\n\n\n")                                
 
def Precautions() :
    messagebox.showinfo("Precautions", "\nLet's keep the password.\n\n"+
                                "When setting a password,   \n"+
                                "if you set more than 8 characters with a combination of \n"+
                                "numbers, letters, and special characters,\n\n"+
                                "There are many combinations of cases,\n"+
                                "so it is not easy because it takes a lot of time even for\n"+
                                "a computer with good performance. \n"+
                                "(Wouldn't it be better to use a super computer?)\n\n" +
                                "Let's protect passwords, which are considered more important\n" +
                                "than anything else in the digital age, when possible.\n\n" +
                                "                                                  let's be careful\n\n\n\n") 
    # webbrowser.open('www.google.co.kr')
    # return True  
    
def func_exit() : # func_exit 함수 선언 
    window.quit() 
    window.destroy() # 창 종료

# 대상 파일 찾기
def file_find_fun_tab1():
    global find_name_tab1
    dis_file = ''
    cur_dir = os.getcwd()   # 현재 Director
    window.filename = filedialog.askopenfilename(initialdir = cur_dir,title = "choose your file",filetypes = (("pdf files","*.pdf"),("pdf files","*.pdf")))
    dis_file = os.path.basename(window.filename)  # 파일명만 추출
    find_name_tab1 = window.filename 
    lb_hi = Label(tab1, text=dis_file, bg='gray96', fg='gray1',width=0,padx=5, pady=5,justify=[RIGHT])
    lb_hi.place(x=150,y=40)
    return

def file_find_fun_tab2():
    global find_name_tab2
    dis_file = ''
    cur_dir = os.getcwd()   # 현재 Director
    window.filename = filedialog.askopenfilename(initialdir = cur_dir,
                      title = "choose your file",filetypes = (("pdf files","*.pdf"),("pdf files","*.pdf")))
    dis_file = os.path.basename(window.filename)  # 파일명만 추출
    find_name_tab2 = window.filename 
    lb_hi = Label(tab2, text=dis_file, bg='gray96', fg='gray1',width=0,padx=5, pady=5,justify=[RIGHT])
    lb_hi.place(x=150,y=40)
    return

def text_find_fun_tab2():
    global find_text_tab2
    dis_file = ''
    cur_dir = os.getcwd()   # 현재 Director
    window.filename = filedialog.askopenfilename(initialdir = cur_dir,
                      title = "choose your file",filetypes = (("Text files", "*.txt"),("all files", "*.*")))
    dis_file = os.path.basename(window.filename)  # 파일명만 추출
    find_text_tab2 = window.filename 
    lb_hi = Label(tab2, text=dis_file, bg='gray96', fg='gray1',width=0,padx=5, pady=5,justify=[RIGHT])
    lb_hi.place(x=150,y=80)
    return

def file_find_fun_tab3():
    global find_name_tab3 
    dis_file = ''
    cur_dir = os.getcwd()   # 현재 Director
    window.filename = filedialog.askopenfilename(initialdir = cur_dir,
                      title = "choose your file",filetypes = (("pdf files","*.pdf"),("pdf files","*.pdf")))
    dis_file = os.path.basename(window.filename)  # 파일명만 추출
    find_name_tab3 = window.filename 
    lb_hi = Label(tab3, text=dis_file, bg='gray96', fg='gray1',width=0,padx=5, pady=5,justify=[RIGHT])
    lb_hi.place(x=150,y=40)
    return

def ok_function_tab1(): 
    global public_cancel
    global find_name_tab1

    public_cancel = False
    error_msg_clear(1) 

    q_result =messagebox.askokcancel("Confirm/Cancel","Would you like to proceed?")

    if (q_result == True) : 
        validity_check_fun(1)  # 유효성 검사 메세지 
        find_length_min_tab1 = entry_length_min_tab1.get()
        find_length_max_tab1 = entry_length_max_tab1.get()
        find_number_tab1 = entry_number_tab1.get()
        if (find_type_var_tab1.get() == 1 or find_type_var_tab1.get() == 2 or find_type_var_tab1.get() == 3 or find_type_var_tab1.get() == 4) :   
            find_string_tab1 = entry_string_tab1.get()
        else :   
            find_string_tab1 = ''
        find_special_tab1 = entry_special_tab1.get()
        char_varify = chars_create(find_number_tab1,find_string_tab1,find_special_tab1,find_type_var_tab1.get(),int(find_length_max_tab1))

        result_value = 0
        if (find_name_tab1 == None or find_name_tab1 == '' ) : 
            result_value = 1 
            error_file_exists(1)
        if (varify_min_max(1,char_varify,int(find_length_min_tab1),int(find_length_max_tab1)) == False) :   
            result_value = 1  
            error_display_length(1)
        if (varify_num(find_number_tab1) == False) :   # 문자(숫자) 입력 체크
            result_value = 2  
            error_display_number(1) 
        if (varify_char(find_string_tab1,find_type_var_tab1.get()) == False) :    # 문자(String) 입력 체크
            result_value = 3
            error_display_char(1)
        if (varify_special(find_special_tab1) == False) :    # 특수문자(String) 입력 체크 허용  !@#$%^&*()_+-=,./<>?;:{}[]|\
            result_value = 4
            error_display_special(1)
        if ((len(find_number_tab1) == 0) and (len(find_string_tab1) == 0) and (len(find_special_tab1) == 0)) :
            result_value = 6
            error_display_number(1)
            error_display_char(1)
            error_display_special(1)
        if (char_varify =='') :   
            result_value = 5
            error_display_password_input(1)

        if (result_value == 0) :    # ERROR 없으면 실행
            if (file_password_check1(1) == True) and (file_password_check2(1) == True) :   # 암호가 걸렸는지 체크
                password_check_display(1)  # 암호가 안걸려 있음 표시
            else :   
                result_confirm_func(1,int(find_length_min_tab1),int(find_length_max_tab1),char_varify)

def ok_function_tab2(): 
    global public_cancel
    global find_name_tab2
    global find_text_tab2
    global display_cycle_value

    public_cancel = False
    result_value = 0
    
    error_msg_clear(2) 
    q_result =messagebox.askokcancel("Confirm/Cancel","Would you like to proceed?")
    if (q_result == True) :  
        # find 실행  text file을 읽음
        if (find_name_tab2 == None or find_name_tab2 == '' ) :                                 # pdf 파일 체크
            result_value = 1 
            error_file_exists(2)
        if (find_type_var_tab2.get() == 1) and (find_text_tab2 == None or find_text_tab2 == '' ) :   # TEXT 파일 체크
            result_value = 1 
            error_file_exists(2)
        if (find_type_var_tab2.get() == 2) :   
            text_area.bind()      #scrolledtext 값을 세팅
            text_tmp   = text_area.get(1.0,'end')
            text_array = text_tmp.split('\n')
            if (text_tmp == None or text_tmp == '' ) :   # TEXT 파일 체크
                result_value = 1 
                error_input_data_exists(2)

        if (find_type_var_tab2.get() == 1) and (result_value == 0) :   
            with open(find_text_tab2, mode="rt") as file : 
                if (file_password_check1(2) == True) and (file_password_check2(2) == True) :   # 암호가 걸렸는지 체크
                    password_check_display(2)  # 암호가 안걸려 있음 표시
                else :
                    result_value = 0
                    file_box = file.readlines()                      # 파일 사이즈
                    chars_case_num_total = len(file_box)  # 파일 라인길이
                    chars_case_num_count = 0    
                    for line in file_box :   
                        char_varify = ''.join(line).replace('\n','')     #   string.replace("\n","")
                        chars_case_num_count = chars_case_num_count + 1  # 진행율 카운트
                        description_display(2,char_varify) 
                        progress_percentage = percentage_fun(chars_case_num_count,chars_case_num_total)  # 소숫점 이하 3자리까지 백분율 표시
                        Progress_display(2,progress_percentage) # 진행율을 보여줌
                        p_var = DoubleVar()
                        progressbar = tkinter.ttk.Progressbar(tab2, maximum=chars_case_num_total,mode="determinate", length=350, variable = p_var )
                        progressbar.pack()
                        progressbar.place(x=150,y=305)
                        p_var.set(chars_case_num_count)          # progress 진행값
                        progressbar.update()  # ui없데이트

                        if (char_varify != '') :   # TEXT 파일의 라인에 값이 없으면 PASS   
                            result_value = result_confirm_func_tab2(2,char_varify) 
                            if result_value == 1 : 
                                break
                        # CANCEL check 결과 
                        if result_value == 2 :
                            lb_hi = Label(tab2, text='[ CANCEL  ]', fg='red',width=12, height=1,padx=5, pady=5, justify=[RIGHT])
                            lb_hi.place(x=500,y=350)
                            break    
                    #file.close()
        elif (find_type_var_tab2.get() == 2) and (result_value == 0) :
            if (file_password_check1(2) == True) and (file_password_check2(2) == True) :   # 암호가 걸렸는지 체크
                    password_check_display(2)  # 암호가 안걸려 있음 표시
            else :
                result_value = 0
                chars_case_num_total = len(text_array) -1 # 파일 라인길이
                chars_case_num_count = 0
                for text_i in text_array:
                    char_varify = ''.join(text_i).replace('\n','')     #   string.replace("\n","")
                    chars_case_num_count = chars_case_num_count + 1    # 진행율 카운트
                    description_display(2,char_varify) 
                    progress_percentage = percentage_fun(chars_case_num_count,chars_case_num_total)  # 소숫점 이하 3자리까지 백분율 표시
                    Progress_display(2,progress_percentage) # 진행율을 보여줌
                    p_var = DoubleVar()
                    progressbar = tkinter.ttk.Progressbar(tab2, maximum=chars_case_num_total,mode="determinate", length=350, variable = p_var )
                    progressbar.pack()
                    progressbar.place(x=150,y=305)
                    p_var.set(chars_case_num_count)          # progress 진행값
                    progressbar.update()  # ui없데이트
                        
                    if(text_i != '' or text_i == None) :  
                        result_value = result_confirm_func_tab2(2,char_varify) 
                        if result_value == 1 : 
                            break
                    # CANCEL check 결과 
                    if result_value == 2 :
                        lb_hi = Label(tab2, text='[ CANCEL  ]', fg='red',width=12, height=1,padx=5, pady=5, justify=[RIGHT])
                        lb_hi.place(x=500,y=350)
                        break
               
        # file check 결과 
        if result_value == 0 :   
            lb_hi = Label(tab2, text='[Not Found]', fg='red',width=12, height=1,padx=5, pady=5, justify=[RIGHT])
            lb_hi.place(x=500,y=350)
        
                

def ok_function_tab3(): 
    global public_cancel
    global find_name_tab3

    public_cancel = False
    error_msg_clear(3) 
    q_result =messagebox.askokcancel("Confirm/Cancel","Would you like to proceed?")
    if (q_result == True) :  
        validity_check_fun(3)  # 유효성 검사 메세지
        find_length_min_tab3 = entry_length_min_tab3.get()
        find_length_max_tab3 = entry_length_max_tab3.get()
        find_number_tab3 = entry_number_tab3.get()
        if (find_type_var_tab3.get() == 1 or find_type_var_tab3.get() == 2 or find_type_var_tab3.get() == 3 or find_type_var_tab3.get() == 4) :   
            find_string_tab3 = entry_string_tab3.get()
        else :   
            find_string_tab3 = ''
        find_special_tab3 = entry_special_tab3.get()
        char_varify = chars_create(find_number_tab3,find_string_tab3,find_special_tab3,find_type_var_tab3.get(),int(find_length_max_tab3))
        result_value = 0
        if (find_name_tab3 == None or find_name_tab3 == '' ) : 
            result_value = 1  
            error_file_exists(3)
        if (varify_min_max(3,char_varify,int(find_length_min_tab3),int(find_length_max_tab3)) == False) :  
            result_value = 1  
            error_display_length(3)
        if (varify_num(find_number_tab3) == False) :   # 문자(숫자) 입력 체크
            result_value = 2  
            error_display_number(3) 
        if (varify_char(find_string_tab3,find_type_var_tab3.get()) == False) :    # 문자(String) 입력 체크
            result_value = 3
            error_display_char(3)
        if (varify_special(find_special_tab3) == False) :    # 특수문자(String) 입력 체크 허용  !@#$%^&*()_+-=,./<>?;:{}[]|\
            result_value = 4
            error_display_special(3)
        if ((len(find_number_tab3) == 0) and (len(find_string_tab3) == 0) and (len(find_special_tab3) == 0)) :
            result_value = 6
            error_display_number(3)
            error_display_char(3)
            error_display_special(3)
        if (char_varify =='') :   
            result_value = 5
            error_display_password_input(3)

        if (result_value == 0) :    # ERROR 없으면 실행
            if (file_password_check1(3) == True) and (file_password_check2(3) == True) :   # 암호가 걸렸는지 체크
                password_check_display(3)  # 암호가 안걸려 있음 표시
            else :   
                result_confirm_func(3,int(find_length_min_tab3),int(find_length_max_tab3),char_varify)

def validity_check_fun(tab_value) :    # 유효성 검사 메세지
    if (tab_value == 1) :
        lb_hi = Label(tab1, text="preparation and validity check...............", fg='blue',width=48, height=1, justify=[LEFT])
        lb_hi.place(x=150,y=390)
    else :   
        lb_hi = Label(tab3, text="preparation and validity check...............", fg='blue',width=48, height=1, justify=[LEFT])
        lb_hi.place(x=150,y=390)
    lb_hi.update()

def cancel_function() : 
    global public_cancel
    public_cancel = True
    # sys.exit() 
    # window.quit()
    # window.destroy()

def description_display(tab_value,password_found) : 
    if (tab_value == 1) :   
        lb_hi = Label(tab1, text=password_found, bg='gray92', fg='gray1',width=35, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=240,y=260)  
    elif (tab_value == 2) : 
        lb_hi = Label(tab2, text=password_found, bg='gray92', fg='gray1',width=35, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=240,y=260)  
    elif (tab_value == 3) : 
        lb_hi = Label(tab3, text=password_found, bg='gray92', fg='gray1',width=35, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=240,y=260)  

def password_found_display(tab_value,password_found_confirm) : 
    if (tab_value == 1) :    
        lb_hi = Label(tab1, text=password_found_confirm, bg='gray80', fg='gray1',width=48, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=150,y=350)
    elif (tab_value == 2) :   
        lb_hi = Label(tab2, text=password_found_confirm, bg='gray80', fg='gray1',width=48, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=150,y=350)
    elif (tab_value == 3) :   
        lb_hi = Label(tab3, text=password_found_confirm, bg='gray80', fg='gray1',width=48, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=150,y=350)

def password_found_end(tab_value) :
    if (tab_value == 1) :   
        lb_hi = Label(tab1, text='[ Find !! ]', fg='Blue',width=11, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=500,y=350) 
    elif (tab_value == 2) :  
        lb_hi = Label(tab2, text='[ Find !! ]', fg='Blue',width=11, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=500,y=350)
    elif (tab_value == 3) :  
        lb_hi = Label(tab3, text='[ Find !! ]', fg='Blue',width=11, height=1,padx=5, pady=5, justify=[RIGHT])
        lb_hi.place(x=500,y=350)  

def Progress_display(tab_value,current_rate) :
    if (tab_value == 1) :    
        lb_hi = Label(tab1, text="( "+str(current_rate)+"% )", fg='Blue',width=0, height=1,padx=2, pady=5)
        lb_hi.place(x=150,y=260)
    elif (tab_value == 2) : 
        lb_hi = Label(tab2, text="( "+str(current_rate)+"% )", fg='Blue',width=0, height=1,padx=2, pady=5)
        lb_hi.place(x=150,y=260)
    elif (tab_value == 3) : 
        lb_hi = Label(tab3, text="( "+str(current_rate)+"% )", fg='Blue',width=0, height=1,padx=2, pady=5)
        lb_hi.place(x=150,y=260)

def password_check_display(tab_value) : 
    if (tab_value == 1) : 
        lb_hi = Label(tab1, text="There is no password in the file.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13) 
    elif (tab_value == 2) : 
        lb_hi = Label(tab2, text="There is no password in the file.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)
    elif (tab_value == 3) : 
        lb_hi = Label(tab3, text="There is no password in the file.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13) 

def error_display_password_input(tab_value) : 
    if (tab_value == 1) :   
        lb_hi = Label(tab1, text=" PW Combination dose not exist.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)
    elif (tab_value == 2) : 
        lb_hi = Label(tab2, text=" PW Combination dose not exist.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)
    elif (tab_value == 3) : 
        lb_hi = Label(tab3, text=" PW Combination dose not exist.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)

def error_file_exists(tab_value) : 
    if (tab_value == 1) :  
        lb_hi = Label(tab1, text=" The file does not exist.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)
    elif (tab_value == 2) :
        lb_hi = Label(tab2, text=" The file does not exist.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)
    elif (tab_value == 3) :
        lb_hi = Label(tab3, text=" The file does not exist.", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)

def error_input_data_exists(tab_value) : 
    if (tab_value == 2) :
        lb_hi = Label(tab2, text=" INPUT does not exist.   ", fg='red', width=0, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=150,y=13)  

def error_display_length(tab_value) :  # tab 1, 3
    if (tab_value == 1) :   
        lb_hi = Label(tab1, text="Length ERROR !!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=500,y=80)
    elif (tab_value == 3) :
        lb_hi = Label(tab3, text="Length ERROR !!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=500,y=80)

def error_display_number(tab_value) : # tab 1, 3
    if (tab_value == 1) :   
        lb_hi = Label(tab1, text="NUM Type ERROR!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=500,y=120) 
    elif (tab_value == 3) :  
        lb_hi = Label(tab3, text="NUM Type ERROR!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=500,y=120)

def error_display_char(tab_value) : # tab 1, 3
    if (tab_value == 1) :
        lb_hi = Label(tab1, text="CHR Type ERROR!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  
        lb_hi.place(x=500,y=160) 
    elif (tab_value == 3) : 
        lb_hi = Label(tab3, text="CHR Type ERROR!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  
        lb_hi.place(x=500,y=160)

def error_display_special(tab_value) : # tab 1, 3
    if (tab_value == 1) :
        lb_hi = Label(tab1, text="Special  ERROR!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  
        lb_hi.place(x=500,y=220) 
    elif (tab_value == 3) : 
        lb_hi = Label(tab3, text="Special  ERROR!", fg='red', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  
        lb_hi.place(x=500,y=220)

def Non_active_check() :   
    # global scroll_text_tab2
    if (find_type_var_tab2.get() == 1) :  # Text File 선택
        Select_button_tab2 = Button(tab2, text= " Select file ",state = NORMAL,command=text_find_fun_tab2)   
        Select_button_tab2.place(x=520, y=80)
        # Input Clear button
        clear_button_tab2 = Button(tab2, text= " Input clear ",padx=0, pady=2,state = DISABLED,command=input_clear_fun_tab2,font=font8)  
        clear_button_tab2.place(x=520, y=120)
        # text file save button 
        textsave_button_tab2 = Button(tab2, text= "TextFileSave ",padx=0, pady=1,state = DISABLED,command=textsave_fun_tab2,font=font8)
        textsave_button_tab2.place(x=520, y=150)
    elif(find_type_var_tab2.get() == 2) :  # INPUT DATA 선택
        Select_button_tab2 = Button(tab2, text= " Select file ",state = DISABLED,command=text_find_fun_tab2)   
        Select_button_tab2.place(x=520, y=80)
        # Input Clear button
        clear_button_tab2 = Button(tab2, text= " Input Clear ",padx=0, pady=2,state = NORMAL,command=input_clear_fun_tab2,font=font8)  
        clear_button_tab2.place(x=520, y=120)
        # text file save button 
        textsave_button_tab2 = Button(tab2, text= "TextFileSave ",padx=0, pady=1,state = NORMAL,command=textsave_fun_tab2,font=font8)
        textsave_button_tab2.place(x=520, y=150)

# Input Data CLEAR
def input_clear_fun_tab2() :     #  *****************************************************************************
    #global scroll_text_tab2
    text_area.delete(1.0,'end')
    text_area.bind()
    text_area.focus()


    return
    
    

# TEXT File Save 구현 *******************************************************************
def textsave_fun_tab2() : 

    dis_textfile = ''
    
    text_area.bind()     #scrolledtext 값을 세팅
    text_tmp   = text_area.get(1.0,'end')
    text_array = text_tmp.split('\n')
    text_name_select = ''.join(text_tmp).replace('\n','')
    if (text_name_select == '' or text_name_select == None) :   # input data exists check
        error_input_data_exists(2)
        return

    window.txt_filename = filedialog.asksaveasfilename(filetypes=(("Text files", "*.txt"),("all files", "*.*")), title="Create TEXT File ",
                                                        initialfile='noname.txt')
    dis_textfile = os.path.basename(window.txt_filename)  # 파일명만 추출
    lb_hi = Label(tab2, text=dis_textfile,fg='blue',width=0,justify=[RIGHT])
    lb_hi.place(x=520,y=175)

    if (window.txt_filename != '' and window.txt_filename != None) :  
        Text_file = open(window.txt_filename,"w")   # scroll 위젯값을 파일로 보냅니다.
        for text_i in text_array:
            if(text_i != '' or text_i == None) :
                Text_file.write(text_i+'\n')
        Text_file.close()
    return


def varify_min_max(tab_value,chars_v,find_len_min,find_len_max) :   # tab 1, 3
    if ((tab_value == 1) and 
       (0 > find_len_min or find_len_min > find_len_max)) :
        return False
    elif ((tab_value == 3) and 
          (0 > find_len_min or find_len_min > find_len_max)) :
        return False
    else :   
        return True     

# 문자형 숫자 입력 체크  
def varify_num(find_num) :  
    var_flag = 0 
    for vi in range(0,len(find_num)) :   
        if (find_num[vi] < '0' or find_num[vi] > '9') : 
            var_flag = 1
            break  
    if (var_flag == 1 or find_num is None) :    
        return False
    else :   
        return True

#문자형 스트링 입력 체크     
def varify_char(find_str,find_tvar) :   # tvar 1 그대로 2 소문자 , 3 대문자 , 4 둘다
    var_flag = 0 
    if find_tvar == 1 :   
        pass
    else :   
        for vi in range(0,len(find_str)) :   
            if (((find_str[vi] < 'a' or find_str[vi] > 'z') and find_tvar == 2) or
                ((find_str[vi] < 'A' or find_str[vi] > 'Z') and find_tvar == 3)) :   
                var_flag = 1
                break  
            if (find_tvar == 4) :   
                if ((find_str[vi] >= 'a' and find_str[vi] <= 'z') or   
                    (find_str[vi] >='A' and find_str[vi] <= 'Z')) :   
                    pass
                else :   
                    var_flag = 1
                    break

    if (var_flag == 1) :   
        return False
    else :   
        return True
    
#특수문자 스트링 입력 체크     
def varify_special(find_spe) :   # tvar 1 소문자 , 2 대문자 , 3 둘다
    var_flag = 0
    for vi in range(0,len(find_spe)) :   
        if ('!' == find_spe[vi] or '#' == find_spe[vi] or '$' == find_spe[vi] or '%' == find_spe[vi] or
            '^' == find_spe[vi] or '&' == find_spe[vi] or '*' == find_spe[vi] or '(' == find_spe[vi] or
            ')' == find_spe[vi] or '+' == find_spe[vi] or '-' == find_spe[vi] or '=' == find_spe[vi] or
            ',' == find_spe[vi] or '.' == find_spe[vi] or '/' == find_spe[vi] or '<' == find_spe[vi] or
            '>' == find_spe[vi] or '?' == find_spe[vi] or '@' == find_spe[vi] or '_' == find_spe[vi] or
            '{' == find_spe[vi] or '}' == find_spe[vi] or '[' == find_spe[vi] or ']' == find_spe[vi] or 
            ';' == find_spe[vi] or ':' == find_spe[vi] or '`' == find_spe[vi] or '~' == find_spe[vi] or 
            '|' == find_spe[vi] or '\\' == find_spe[vi] )  : 
            pass
        else :
            var_flag = 1
            break
        
    if (var_flag == 1) :   
        return False
    else :   
        return True

def error_msg_clear(tab_value) :
    if (tab_value == 1):   
        lb_hi = Label(tab1, text=" ", bg='gray94', width=40,justify=[RIGHT])  # 파일 존재 
        lb_hi.place(x=150,y=13)
        lb_hi = Label(tab1, text="Trials 2~6 allowed  ", fg='red', width=20, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=500,y=80)  
        lb_hi = Label(tab1, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  # 숫자형
        lb_hi.place(x=500,y=120)
        lb_hi = Label(tab1, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  # 문자형
        lb_hi.place(x=500,y=160)
        lb_hi = Label(tab1, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  # 특수문자
        lb_hi.place(x=500,y=220)
        lb_hi = Label(tab1, text=" ", bg='gray94', width=12, height=1,padx=2, pady=2,justify=[RIGHT])   # 진행 백뷴율
        lb_hi.place(x=150,y=260)
        lb_hi = Label(tab1, text=" ", bg='gray94', width=12, height=1,padx=5, pady=5, justify=[RIGHT])  # password found Display END]
        lb_hi.place(x=500,y=350)
        lb_hi = Label(tab1, text=" ", bg='gray80', fg='gray1',width=48, height=1,padx=5, pady=5)  # password
        lb_hi.place(x=150,y=350)
        lb_hi = Label(tab1, text=" ", bg='gray94',width=48, height=1, justify=[LEFT])  # Message 총 비교건수
        lb_hi.place(x=150,y=390)
    elif (tab_value == 2) :    # tab2에서 왔음  
        lb_hi = Label(tab2, text=" ", bg='gray94', width=40,justify=[RIGHT])  # 파일 존재 
        lb_hi.place(x=150,y=13)
        lb_hi = Label(tab2, text=" ", bg='gray94', width=20, height=1,justify=[RIGHT])   # TEXT File명
        lb_hi.place(x=520,y=175)
        lb_hi = Label(tab2, text=" ", bg='gray94', width=12, height=1,padx=2, pady=2,justify=[RIGHT])   # 진행 백뷴율
        lb_hi.place(x=150,y=260)
        lb_hi = Label(tab2, text=" ", bg='gray94', width=12, height=1,padx=5, pady=5, justify=[RIGHT])  # password found Display END]
        lb_hi.place(x=500,y=350)
        lb_hi = Label(tab2, text=" ", bg='gray80', fg='gray1',width=48, height=1,padx=5, pady=5)  # password
        lb_hi.place(x=150,y=350)
    elif (tab_value == 3) :    # tab3에서 왔음  
        lb_hi = Label(tab3, text=" ", bg='gray94', width=40,justify=[RIGHT])  # 파일 존재 
        lb_hi.place(x=150,y=13)
        lb_hi = Label(tab3, text="Trials 2~6 allowed  ", fg='red', width=20, height=1,padx=5, pady=5,justify=[RIGHT])
        lb_hi.place(x=500,y=80)  
        lb_hi = Label(tab3, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  # 숫자형
        lb_hi.place(x=500,y=120)
        lb_hi = Label(tab3, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  # 문자형
        lb_hi.place(x=500,y=160)
        lb_hi = Label(tab3, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])  # 특수문자
        lb_hi.place(x=500,y=220)
        lb_hi = Label(tab3, text=" ", bg='gray94', width=12, height=1,padx=2, pady=2,justify=[RIGHT])   # 진행 백뷴율
        lb_hi.place(x=150,y=260)
        lb_hi = Label(tab3, text=" ", bg='gray94', width=12, height=1,padx=5, pady=5, justify=[RIGHT])  # password found Display END]
        lb_hi.place(x=500,y=350)
        lb_hi = Label(tab3, text=" ", bg='gray80', fg='gray1',width=48, height=1,padx=5, pady=5)  # password
        lb_hi.place(x=150,y=350)
        lb_hi = Label(tab3, text=" ", bg='gray94',width=48, height=1, justify=[LEFT])  # Message 총 비교건수
        lb_hi.place(x=150,y=390)

def chars_create(c_find_number,c_find_string,c_find_special,c_find_var,c_find_max_length) :   
    chars_cre = ''
    if ( c_find_number != '') :   
        chars_cre = c_find_number

    if ( c_find_string != '' and c_find_var == 1) :   
        chars_cre = chars_cre + c_find_string
    elif ( c_find_string != '' and c_find_var == 2) :   
        chars_cre = chars_cre + c_find_string.lower() 
    elif ( c_find_string != '' and c_find_var == 3) :   
        chars_cre = chars_cre + c_find_string.upper() 
    elif ( c_find_string != '' and c_find_var == 4) :   
        chars_cre = chars_cre + c_find_string.lower() + c_find_string.upper()

    if (c_find_special != '') :   
        chars_cre = chars_cre + c_find_special

    chars_cre = ''.join(set(chars_cre))  # set로 변환 후 join 함수사용 중복문자 제거 순서 보정 없음 순저보정시 dict.fromkeys(word) 
    return chars_cre

#백분율 소숫점 3자리까지 문자열 
def percentage_fun(i_current,i_total) :   
    percentage_str= str(i_current/i_total*100) 
    percentage_dis=''
    percentage_flag = 0
    new_count = 0
    for j_val in range(0,len(percentage_str)) :  
        if (new_count > 3) :  
            break 
        elif (percentage_flag == 0 and percentage_str[j_val] != '.')  : 
            percentage_dis = percentage_dis +percentage_str[j_val]
        elif (percentage_str[j_val] == '.' or percentage_flag == 1) :
            percentage_flag = 1
            new_count = new_count + 1  
            percentage_dis = percentage_dis +percentage_str[j_val]
    if (new_count < 4) :   
        for k in range(new_count,4) :   
            percentage_dis = percentage_dis + '0'
    return percentage_dis

# tab2 password check main
def result_confirm_func_tab2(tab_value,password) : 
    global public_cancel
    global find_name_tab2

    find_name = ''
    find_name = find_name_tab2          # tab2에서 왔음
    find_type_var = find_type_var_tab2
    success_flag = 0

    if (public_cancel == True) :   
        success_flag = 2              #  진행 취소
    try:   
        pikepdf.open(find_name, password = password)  #pdf
        password_found_display(tab_value,password)
        password_found_end(tab_value) 
        success_flag = 1
    except :  
        pass

    return success_flag
        
    


# find_name 변수 공통 사용
def result_confirm_func(tab_value,r_find_length_min,r_find_length_max,chars) :  
    global public_cancel  
    global find_name_tab1
    global find_name_tab3
    global display_cycle_value

    find_name = ''
    #find_type_var = 1     
    if (tab_value == 1):   
        find_name = find_name_tab1    # tab1에서 왔음
        #find_type_var = find_type_var_tab1
    elif (tab_value == 3) :   
        find_name = find_name_tab3    # tab3에서 왔음
        #find_type_var = find_type_var_tab3

    public_cancel = False

    chars_case_num = 0   # 진행 토탈 경우의 수-------

    for t_i in range(r_find_length_min,r_find_length_max+1) : 
        count_allpass = product(chars,repeat=t_i)  
        chars_case_num = chars_case_num+ len(list(count_allpass))

    #lb_hi = Label(tab1, text="Preparing and calculating processing time...............", fg='blue',width=48, height=1, justify=[RIGHT])
    if (tab_value == 1):
        lb_hi = Label(tab1, text="Number of cases MAX : "+str(format(chars_case_num,',')), fg='blue',width=48, height=1, justify=[LEFT])
        lb_hi.place(x=150,y=390)
    elif (tab_value == 3) :
        lb_hi = Label(tab3, text="Number of cases MAX : "+str(format(chars_case_num,',')), fg='blue',width=48, height=1, justify=[LEFT])
        lb_hi.place(x=150,y=390)

    chars_case_num_count = 0

    now = time.strftime("[%H:%M:%S]")

    success_flag = 0

    for length in range(r_find_length_min,r_find_length_max+1) :   

        allpass=product(chars,repeat=length)
        
        for password in allpass:
            password = ''.join(password)  
            chars_case_num_count = chars_case_num_count + 1 # 진행율 카운트
            if (chars_case_num_count % display_cycle_value == 0 or chars_case_num_count == 1) :
                description_display(tab_value,password)         # Description 값을 표시 , 표시주기 변경
                progress_percentage = percentage_fun(chars_case_num_count,chars_case_num)  # 소숫점 이하 3자리까지 백분율 표시
                Progress_display(tab_value,progress_percentage) # 진행율을 보여줌.
                # progress bar
                if (tab_value == 1): 
                    p_var = DoubleVar()
                    progressbar = tkinter.ttk.Progressbar(tab1, maximum=chars_case_num,mode="determinate", length=350, variable = p_var )
                    progressbar.pack()
                    progressbar.place(x=150,y=305)
                    p_var.set(chars_case_num_count)          # progress 진행값
                    progressbar.update()  # ui없데이트
                elif (tab_value == 3) :   
                    p_var = DoubleVar()
                    progressbar = tkinter.ttk.Progressbar(tab3, maximum=chars_case_num,mode="determinate", length=350, variable = p_var )
                    progressbar.pack()
                    progressbar.place(x=150,y=305)
                    p_var.set(chars_case_num_count)          # progress 진행값
                    progressbar.update()  # ui없데이트
            
            if (public_cancel == True) :   
                success_flag = 2   #  진행 취소
                break

            try:   
                pikepdf.open(find_name, password = password)  #pdf
                password_found_display(tab_value,password)
                password_found_end(tab_value) 
                success_flag = 1
                break
            except :  
                continue  


        if success_flag == 1  or success_flag == 2:
            break
        else :  
            continue  

    if success_flag == 0 : 
        if (tab_value == 1):   
            lb_hi = Label(tab1, text='[Not Found]', fg='red',width=12, height=1,padx=5, pady=5, justify=[RIGHT])
            lb_hi.place(x=500,y=350)
        elif (tab_value == 3):  
            lb_hi = Label(tab3, text='[Not Found]', fg='red',width=12, height=1,padx=5, pady=5, justify=[RIGHT])
            lb_hi.place(x=500,y=350) 
    elif success_flag == 2 :
        if (tab_value == 1):
            lb_hi = Label(tab1, text='[ CANCEL  ]', fg='red',width=12, height=1,padx=5, pady=5, justify=[RIGHT])
            lb_hi.place(x=500,y=350) 
        elif (tab_value == 3):  
            lb_hi = Label(tab3, text='[ CANCEL  ]', fg='red',width=12, height=1,padx=5, pady=5, justify=[RIGHT])
            lb_hi.place(x=500,y=350) 


def file_password_check1(tab_value) : 
    global find_name_tab1
    global find_name_tab2
    global find_name_tab3

    find_name = ''

    if (tab_value == 1):   
        find_name = find_name_tab1    # tab1에서 왔음
    elif (tab_value == 2) :   
        find_name = find_name_tab2    # tab2에서 왔음
    elif (tab_value == 3) :   
        find_name = find_name_tab3    # tab3에서 왔음

    flag_check = True
    try:   
        pikepdf.open(find_name, password = "1")  #pdf
        flag_check = True
    except :  
        flag_check = False
    return flag_check

def file_password_check2(tab_value) : 
    global find_name_tab1
    global find_name_tab2
    global find_name_tab3

    find_name = ''

    if (tab_value == 1):   
        find_name = find_name_tab1    # tab1에서 왔음
    elif (tab_value == 2) :   
        find_name = find_name_tab2    # tab2에서 왔음
    elif (tab_value == 3) :   
        find_name = find_name_tab3    # tab3에서 왔음
    flag_check = True
    try:   
        pikepdf.open(find_name, password = "2")  #pdf
        flag_check = True
    except :  
        flag_check = False
    return flag_check


# GUI  Main Body   ===============================================================================
global public_cancel 
global display_cycle_value
public_cancel = False
display_cycle_value = 50  # UI 표시 주기  Description, Progress

window = tk.Tk()       # window를 통행 TK()를 선언
font10=tkinter.font.Font(family="맑은 고딕", size=10)
font8=tkinter.font.Font(family="맑은 고딕", size=8)

window.title("  PDF Password Found")
notebook=tkinter.ttk.Notebook(window, width=640, height=480)   # 크기 지정
window.resizable(False, False)
cur_dir = os.getcwd()   # 현재 Director

tab1=Frame(window)
notebook.add(tab1, text="   Combination   ")
tab2=Frame(window)
notebook.add(tab2, text="   Dictionary    ")
tab3=Frame(window)
notebook.add(tab3, text=" All Combination ")
notebook.pack()

menu = Menu(window)

# MENU 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label=" H E L P ", command=help_file,font=font10)  
menu_file.add_command(label=" N o t e ", command=Precautions,font=font10) 
menu_file.add_separator()                                      # 메뉴 구분선
menu_file.add_command(label=" Exit ",command=func_exit,font=font10)
menu.add_cascade(label="MENU",menu=menu_file,font=font10)                  # 메뉴 UI

window.config(menu=menu)


#-------------------------------------------------------------------------------------------

# 파일명 표시 위치
global find_name_tab1
global find_name_tab2
global find_text_tab2
#global scroll_text_tab2
global find_name_tab3

find_name_tab1 = ''
find_name_tab2 = ''
find_text_tab2 = ''
#scroll_text_tab2 = ''
find_name_tab3 = ''

text_input_flag = 1 # Text File-1, Input-2

# tab1 GUI ================================================================================================
# pdf destination  입력
lb_hi = Label(tab1, text=" PDF  Destination ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=40)
lb_hi = Label(tab1, text=find_name_tab1, fg="gray1", bg="gray96", width=48,height=1,padx=5, pady=5,justify=[RIGHT])  # 파일명
lb_hi.place(x=150,y=40)

Select_button_tab1 = Button(tab1, text= " Select file ",command=file_find_fun_tab1)   # File Search Function 기능 구현
Select_button_tab1.place(x=520, y=40)
  
# Password Length  입력
lb_hi = Label(tab1, text="Password Length", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=80)

entry_length_min_tab1 = tk.Entry(tab1,bg="gray94", fg="gray1",  width=50, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_length_min_tab1=2      
entry_length_min_tab1.insert(0,find_length_min_tab1)
entry_length_min_tab1.pack(side=tk.LEFT,padx=10,pady=5)
entry_length_min_tab1.place(x=150,y=80,width=70,height=30)
lb_hi = Label(tab1, text=" ~ ", bg='gray93', fg='gray1',width=5, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=220,y=80)
entry_length_max_tab1 = tk.Entry(tab1,bg="gray94", fg="gray1", width=50, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_length_max_tab1=6        
entry_length_max_tab1.insert(1,find_length_max_tab1)
entry_length_max_tab1.pack(side=tk.LEFT,padx=10,pady=5)
entry_length_max_tab1.place(x=270,y=80,width=70,height=30)
lb_hi = Label(tab1, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])
lb_hi.place(x=350,y=80)

# password combination 입력
lb_hi = Label(tab1, text="PW Combination ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=120)
# password combination 숫자형 입력
lb_hi = Label(tab1, text=" N u m ", bg='gray90', fg='gray1',width=8, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=150,y=120)
entry_number_tab1 = tk.Entry(tab1,fg="gray1", bg="gray94", width=100, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_number_tab1=''              # 찾고자하는 숫자형 선택 맥스 4개까지 check 할것
entry_number_tab1.insert(0,find_number_tab1)
entry_number_tab1.pack(side=tk.LEFT)
entry_number_tab1.place(x=240,y=120,width=260,height=30)

# password combination 문자형 입력
lb_hi = Label(tab1, text=" Char  ", bg='gray90', fg='gray1',width=8, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=150,y=160)
entry_string_tab1 = tk.Entry(tab1,fg="gray1", bg="gray94", width=100, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_string_tab1=''              # 찾고자하는 문자형 선택 맥스 4개까지 check 할것
entry_string_tab1.insert(0,find_string_tab1)
entry_string_tab1.pack(side=tk.LEFT)
entry_string_tab1.place(x=240,y=160,width=260,height=30)

find_type_var_tab1 = IntVar()  # 여기에 int형으로 값을 저장한다
btn_find_type_var1_tab1=Radiobutton(tab1,text="Ignore",value=1, variable=find_type_var_tab1)
btn_find_type_var1_tab1.select()   # default 값으로 선택 지정
btn_find_type_var2_tab1=Radiobutton(tab1,text="Lower ",value=2, variable=find_type_var_tab1)
btn_find_type_var3_tab1=Radiobutton(tab1,text="Upper ",value=3, variable=find_type_var_tab1)
btn_find_type_var4_tab1=Radiobutton(tab1,text="Both  ",value=4, variable=find_type_var_tab1)

btn_find_type_var1_tab1.pack() 
btn_find_type_var1_tab1.place(x=235,y=190)
btn_find_type_var2_tab1.pack()
btn_find_type_var2_tab1.place(x=305,y=190)
btn_find_type_var3_tab1.pack()
btn_find_type_var3_tab1.place(x=375,y=190)
btn_find_type_var4_tab1.pack()
btn_find_type_var4_tab1.place(x=445,y=190)

# password combination 특수문자 입력
lb_hi = Label(tab1, text="Special", bg='gray90', fg='gray1',width=8, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=150,y=220)
entry_special_tab1 = tk.Entry(tab1,fg="gray1", bg="gray94", width=100, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_special_tab1=''              # 찾고자하는 특수문자형 선택 맥스 4개까지 check 할것
entry_special_tab1.insert(0,find_special_tab1)
entry_special_tab1.pack(side=tk.LEFT)
entry_special_tab1.place(x=240,y=220,width=260,height=30)

# Description password Search Display
lb_hi = Label(tab1, text="Description    ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=260)
description_display(1,'')

# processorbar 진행율 Display
lb_hi = Label(tab1, text="Progress       ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=2, justify=[RIGHT])
lb_hi.place(x=30,y=305)
lb_hi = Label(tab1, text=" ", bg='gray90', fg='gray1',width=48, height=1,padx=5, pady=2)
lb_hi.place(x=150,y=305)

# password found Display
lb_hi = Label(tab1, text="Password found ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=350)
password_found_display(1,'')

error_msg_clear(1)

# Start and Cancel Button
comfirm_button1 = Button(tab1, text= " Confirm ",command=ok_function_tab1)
comfirm_button1.place(x=450, y=420)
comfirm_button2 = Button(tab1, text= "  Cancel ",command=cancel_function)
comfirm_button2.place(x=520, y=420)

# tab2 GUI ================================================================================================
# PDF destination  입력
lb_hi = Label(tab2, text=" PDF  Destination ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=40)
lb_hi = Label(tab2, text=find_name_tab2, fg="gray1", bg="gray96", width=48,height=1,padx=5, pady=5,justify=[RIGHT])  # 파일명
lb_hi.place(x=150,y=40)

Select_button_tab2 = Button(tab2, text= " Select file ",command=file_find_fun_tab2)   # File Search Function 기능 구현
Select_button_tab2.place(x=520, y=40)

# PW Text File 선택
find_type_var_tab2 = IntVar()  # 여기에 int형으로 값을 저장한다
btn_find_type_var1_tab2=Radiobutton(tab2,text="PW TXT File  ",value=1, variable=find_type_var_tab2,command=Non_active_check)
btn_find_type_var1_tab2.select()   # default 값으로 선택 지정
btn_find_type_var2_tab2=Radiobutton(tab2,text="PW Data Input",value=2, variable=find_type_var_tab2, command=Non_active_check)

btn_find_type_var1_tab2.pack() 
btn_find_type_var1_tab2.place(x=40,y=80) 
btn_find_type_var2_tab2.pack()
btn_find_type_var2_tab2.place(x=40,y=120)
text_input_flag = find_type_var_tab2.get()

 # Text File 명 Display   
lb_hi = Label(tab2, text=find_text_tab2, fg="gray1", bg="gray96", width=48,height=1,padx=5, pady=5,justify=[RIGHT])  # 파일명
lb_hi.place(x=150,y=80)

# Default Text File 선택
Select_button_tab2 = Button(tab2, text= " Select file ",state = NORMAL,command=text_find_fun_tab2)  
Select_button_tab2.place(x=520, y=80)

# Input Clear button
clear_button_tab2 = Button(tab2, text= " Input Clear ",padx=0, pady=2,state = DISABLED,command=input_clear_fun_tab2,font=font8)  
clear_button_tab2.place(x=520, y=120)

# TEXT file Save button
textsave_button_tab2 = Button(tab2, text= "TextFileSave ",padx=0, pady=1,state = DISABLED,command=textsave_fun_tab2,font=font8) 
textsave_button_tab2.place(x=520, y=150)

# ScrollText List Box PW Data Input  Default : Non-active
text_area=ScrolledText(tab2,width=48,height=9,x=150,y=120,bg='gray91',padx=5, pady=5,state=NORMAL)
text_area.place(x=150,y=120)
# text.bind('<Return>',flist)  #Enter 이벤트시 Flist Function 실행

# Description password Search Display
lb_hi = Label(tab2, text="Description    ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=260)
description_display(2,'')

# processorbar 진행율 Display
lb_hi = Label(tab2, text="Progress       ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=2, justify=[RIGHT])
lb_hi.place(x=30,y=305)
lb_hi = Label(tab2, text=" ", bg='gray90', fg='gray1',width=48, height=1,padx=5, pady=2)
lb_hi.place(x=150,y=305)

# password found Display
lb_hi = Label(tab2, text="Password found ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=350)
password_found_display(2,'')

error_msg_clear(2)

# Start and Cancel Button
comfirm_button1 = Button(tab2, text= " Confirm ",command=ok_function_tab2)
comfirm_button1.place(x=450, y=420)
comfirm_button2 = Button(tab2, text= " Cancel  ",command=cancel_function)
comfirm_button2.place(x=520, y=420)


# tab3 GUI ================================================================================================
# PDF destination  입력
lb_hi = Label(tab3, text=" PDF  Destination ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=40)
lb_hi = Label(tab3, text=find_name_tab3, fg="gray1", bg="gray96", width=48,height=1,padx=5, pady=5,justify=[RIGHT])  # 파일명
lb_hi.place(x=150,y=40)

Select_button_tab3 = Button(tab3, text= " Select file ",command=file_find_fun_tab3)   # File Search Function 기능 구현
Select_button_tab3.place(x=520, y=40)
  
# Password Length  입력
lb_hi = Label(tab3, text="Password Length", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=80)

entry_length_min_tab3 = tk.Entry(tab3,bg="gray94", fg="gray1",  width=50, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_length_min_tab3=2           
entry_length_min_tab3.insert(0,find_length_min_tab3)
entry_length_min_tab3.pack(side=tk.LEFT,padx=10,pady=5)
entry_length_min_tab3.place(x=150,y=80,width=70,height=30)
lb_hi = Label(tab3, text=" ~ ", bg='gray93', fg='gray1',width=5, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=220,y=80)
entry_length_max_tab3 = tk.Entry(tab3,bg="gray94", fg="gray1", width=50, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_length_max_tab3=6          
entry_length_max_tab3.insert(1,find_length_max_tab3)
entry_length_max_tab3.pack(side=tk.LEFT,padx=10,pady=5)
entry_length_max_tab3.place(x=270,y=80,width=70,height=30)
lb_hi = Label(tab3, text=" ", bg='gray94', width=15, height=1,padx=5, pady=5,justify=[RIGHT])
lb_hi.place(x=350,y=80)

# password combination 입력
lb_hi = Label(tab3, text="PW Combination ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=120)
# password combination 숫자형 입력
lb_hi = Label(tab3, text=" N u m ", bg='gray90', fg='gray1',width=8, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=150,y=120)
entry_number_tab3 = tk.Entry(tab3,fg="gray1", bg="gray94", width=100, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_number_tab3='0123456789'              # 찾고자하는 숫자형 선택 맥스 4개까지 check 할것
entry_number_tab3.insert(0,find_number_tab3)
entry_number_tab3.pack(side=tk.LEFT)
entry_number_tab3.place(x=240,y=120,width=260,height=30)

# password combination 문자형 입력
lb_hi = Label(tab3, text=" Char  ", bg='gray90', fg='gray1',width=8, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=150,y=160)
entry_string_tab3 = tk.Entry(tab3,fg="gray1", bg="gray94", width=100, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_string_tab3='abcdefghijklmnopqrstuvwxyz'              # 찾고자하는 문자형 선택 맥스 4개까지 check 할것
entry_string_tab3.insert(0,find_string_tab3)
entry_string_tab3.pack(side=tk.LEFT)
entry_string_tab3.place(x=240,y=160,width=260,height=30)

find_type_var_tab3 = IntVar()  # 여기에 int형으로 값을 저장한다
btn_find_type_var1_tab3=Radiobutton(tab3,text="Ignore",value=1, variable=find_type_var_tab3)
btn_find_type_var2_tab3=Radiobutton(tab3,text="Lower ",value=2, variable=find_type_var_tab3)
btn_find_type_var3_tab3=Radiobutton(tab3,text="Upper ",value=3, variable=find_type_var_tab3)
btn_find_type_var4_tab3=Radiobutton(tab3,text="Both  ",value=4, variable=find_type_var_tab3)
btn_find_type_var4_tab3.select()   # default 값으로 선택 지정

btn_find_type_var1_tab3.pack() 
btn_find_type_var1_tab3.place(x=235,y=190)
btn_find_type_var2_tab3.pack()
btn_find_type_var2_tab3.place(x=305,y=190)
btn_find_type_var3_tab3.pack()
btn_find_type_var3_tab3.place(x=375,y=190)
btn_find_type_var4_tab3.pack()
btn_find_type_var4_tab3.place(x=445,y=190)

# password combination 특수문자 입력
lb_hi = Label(tab3, text="Special", bg='gray90', fg='gray1',width=8, height=1,padx=5, pady=5, justify=[CENTER])
lb_hi.place(x=150,y=220)
entry_special_tab3 = tk.Entry(tab3,fg="gray1", bg="gray94", width=100, relief="ridge") # relief = "flat", "groove", "raised", "ridge", "solid", "sunken"
find_special_tab3='!@#$%^&*()_+-=[]\{}|;:,./<>?'              # 찾고자하는 특수문자형 선택 맥스 4개까지 check 할것
entry_special_tab3.insert(0,find_special_tab3)
entry_special_tab3.pack(side=tk.LEFT)
entry_special_tab3.place(x=240,y=220,width=260,height=30)

# Description password Search Display
lb_hi = Label(tab3, text="Description    ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=260)
description_display(3,'')

# processorbar 진행율 Display
lb_hi = Label(tab3, text="Progress       ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=2, justify=[RIGHT])
lb_hi.place(x=30,y=305)
lb_hi = Label(tab3, text=" ", bg='gray90', fg='gray1',width=48, height=1,padx=5, pady=2)
lb_hi.place(x=150,y=305)

# password found Display
lb_hi = Label(tab3, text="Password found ", bg='gray93', fg='gray1',width=15, height=1,padx=5, pady=5, justify=[RIGHT])
lb_hi.place(x=30,y=350)
password_found_display(3,'')

error_msg_clear(3)

# Start and Cancel Button
comfirm_button1 = Button(tab3, text= " Confirm ",command=ok_function_tab3)
comfirm_button1.place(x=450, y=420)
comfirm_button2 = Button(tab3, text= " Cancel  ",command=cancel_function)
comfirm_button2.place(x=520, y=420)


#text_area.focus()
window.mainloop()  #  창이 닫히지 않도록 함.
#-----------------------------------------------------------------------------------------------------

