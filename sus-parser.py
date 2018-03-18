#import numpy as np
import pandas as pd
import pdfkit as pk

def parse_question1(df1, num_rows, num_cols):
    q1_descr_arr = []
    q1_calc_arr = []
    for cell in range(2, num_rows):
        user_arr = []
        for i in range(0, 6):         
            Q1_ = "Q1_" + str(i+1)
            user_output_q1 = df1.iloc[cell][Q1_]
            if pd.isnull(user_output_q1):
                user_output_q1 = 0
            user_arr.append(user_output_q1)
        R = float(user_arr[0])
        LS = float(user_arr[1])
        N = float(user_arr[2])
        P = float(user_arr[3])
        I = float(user_arr[4])
        C = float(user_arr[5])
        calculation = (R+LS+N)-(P+I+C)

        if calculation >= 25 and calculation <= 101:
            q1_descr_arr.append("s_Natural_Capital")
            q1_calc_arr.append(calculation)
            #print "s_Natural_Capital"
        elif calculation <= 24.99 and calculation >= 5:
            q1_descr_arr.append("w_Natural_Capital")
            q1_calc_arr.append(calculation)
            #print "w_Natural_Capital"
        elif calculation <= 4.99 and calculation >= -4.99:
            q1_descr_arr.append("n-Natural_Capital_Social_Capital")
            q1_calc_arr.append(calculation)
            #print "n-Natural_Capital_Social_Capital"
        elif calculation <= -5 and calculation >= -24.99:
            q1_descr_arr.append("w_Social Capital")
            q1_calc_arr.append(calculation)
            #print "w_Social Capital"
        elif calculation <= -25 and calculation >= -100:
            q1_descr_arr.append("s_Social Capital")
            q1_calc_arr.append(calculation)
            #print "s_Social Capital"
        else:
            q1_descr_arr.append("ERROR")
            q1_calc_arr.append(calculation)
            #print "ERROR"
    return(q1_descr_arr, q1_calc_arr)
    
def parse_question2(df1, num_rows, num_cols):
    q2_descr_arr = []
    q2_calc_arr = []
    for cell in range(2, num_rows):
        user_arr = []
        for i in range(0, 6):         
            Q1_ = "Q1_" + str(i+1)
            user_output_q1 = df1.iloc[cell][Q1_]
            if pd.isnull(user_output_q1):
                user_output_q1 = 0
            user_arr.append(user_output_q1)
    

def print_to_output(df1, num_rows, num_cols): 
    q1_descr_arr = parse_question1(df1, num_rows, num_cols)[0]
    for cell in range(2, num_rows): #gets the indvidual cell in the entire COLUMN
        name_comma_vtemail = df1.iloc[cell]["Q6"]
        empty_arr = []
        if pd.isnull(name_comma_vtemail):
            name_comma_vtemail = "survey taker " + str(cell - 1) + " No Personal Info Given"
            name = name_comma_vtemail
        else:
            split_cell = name_comma_vtemail.split(",")
            #only printing name now because of changes needed to survey asking for name and email
            name = split_cell[0]
            if '"' in name: #removes quotes if they're in the name so that we can make an html file
                name = name.replace('"', '')
        q1_descr = q1_descr_arr[cell-2]
        user_file = open("Reports/" + name +"_report.html", 'w')
        message = """<html>
        <head>
        </head>
        <h1>Sustainability Values Diagnostic</h1>
        <body>
        <p>Prepared for</p>
        <h2> %s </h2>
        <p> How you feel about sustainability: %s </p>
        </body>
        </html>"""
        whole_message = message % (name, q1_descr)
        user_file.write(whole_message)
        print name + ": " + q1_descr
        user_file.close()  
        
        #UNCOMMENT FOR PDF VERSION
        #pk.from_file(user_file.name, 'ReportsPDF/'+ name + '.pdf')  #can also make pdf from html webpage 
        
        #do with like the example: pdfkit.from_url('http://google.com', 'out.pdf')

def main():
    df1=pd.read_csv("XMNR18.values.numeric - Copy.csv")
    #gets the number of rows and columns in the csv file
    num_rows = df1.shape[0]
    num_cols = df1.shape[1]
    
    print_to_output(df1, num_rows, num_cols)
    #parse_question1(df1, num_rows, num_cols)
    
main()
