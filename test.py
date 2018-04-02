# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 13:24:34 2018

@author: Caroline
"""

import pandas as pd
import pdfkit as pk

#uses question 1, or columns Q3.1-1 through Q3.1-6, to find the user's
#natural/social capital tendency and ecosystem/species and biodiversity services
def natural_capital_and_ecosystem_services(df1, num_rows, num_cols):
    q1_descr_arr = []  #for natural capital names
    q1_calc_arr = []   #for natural capital calculations(not needed)
    q1_descr_arr2 = [] #for ecosystem tendency names
    for cell in range(2, num_rows):
        user_arr = []
        for i in range(1, 7):
            Q3_ = "Q3.1_" + str(i)
            user_output_q1 = df1.iloc[cell][Q3_]
            if pd.isnull(user_output_q1):
                user_output_q1 = 0
            user_arr.append(user_output_q1)
        R = float(user_arr[0])
        LS = float(user_arr[1])
        N = float(user_arr[2])
        P = float(user_arr[3])
        I = float(user_arr[4])
        C = float(user_arr[5])

        #NATURAL AND SOCIAL CAPITAL CALCULATION-----------------------------------------------

        calculation = (R+LS+N)-(P+I+C)

        #creates 2 arrays: one is the name of the tendency; other is the exact calculation(not needed)
        if calculation >= 25 and calculation <= 101:
            q1_descr_arr.append("Weak Natural Capital")
            q1_calc_arr.append(calculation)
            #print "s_Natural_Capital"
        elif calculation <= 24.99 and calculation >= 5:
            q1_descr_arr.append("Weak Natural Capital")
            q1_calc_arr.append(calculation)
            #print "w_Natural_Capital"
        elif calculation <= 4.99 and calculation >= -4.99:
            q1_descr_arr.append("Neutral Natural/Social Capital")
            q1_calc_arr.append(calculation)
            #print "n-Natural_Capital_Social_Capital"
        elif calculation <= -5 and calculation >= -24.99:
            q1_descr_arr.append("Weak Social Capital")
            q1_calc_arr.append(calculation)
            #print "w_Social Capital"
        elif calculation <= -25 and calculation >= -100:
            q1_descr_arr.append("Strong Social Capital")
            q1_calc_arr.append(calculation)
            #print "s_Social Capital"
        else:
            q1_descr_arr.append("ERROR")
            q1_calc_arr.append(calculation)
            #print "ERROR"

        #ECOSYSTEM SERVICES AND SPECIES/BIODIVERSITY CALCULATION----------------------------------------------

        calculation2 = LS - N

        #creates an array with the ecosystem services tendency
        if calculation2 >= 12 and calculation2 <= 100:
            q1_descr_arr2.append("Strong Ecosystem Services")
        elif calculation2 >= 2 and calculation2 <= 11.99:
            q1_descr_arr2.append("Weak Ecosystem Services")
        elif calculation2 >= -1.99 and calculation2 <= 1.99:
            q1_descr_arr2.append("Neutral Ecosystem Services/Species and Biodiversity")
        elif calculation2 >= -11.99 and calculation2 <= -2:
            q1_descr_arr2.append("Weak Species and Biodiversity")
        elif calculation2 >= -100 and calculation2 <= -12:
            q1_descr_arr2.append("Strong Species and Biodiversity")
        else:
            q1_descr_arr.append("ERROR")

    return(q1_descr_arr, q1_descr_arr2)


def who_should_benefit(df1, num_rows, num_cols):
    q2_descr_arr = []   #holds data for user for people today/tomorrow benefiting
    q2_descr_arr2 = []  #holds data for Us or others benefiting

    for cell in range(2, num_rows):
        user_arr = []
        user_arr2 = []
        for i in range(1, 3):
            Q4_ = "Q4.1_" + str(i)
            Q5_ = "Q5.1_" + str(i)
            user_output_q2_1 = df1.iloc[cell][Q4_]
            user_output_q2_2 = df1.iloc[cell][Q5_]
            user_arr.append(user_output_q2_1)
            user_arr2.append(user_output_q2_2)

        CG = float(user_arr[0])
        FG = float(user_arr[1])
        Us = float(user_arr2[0])
        Oth = float(user_arr2[1])

        #calculations for people today and people tomorrow
        calc1 = CG-FG

        if calc1 <= 100 and calc1 >=25:
            q2_descr_arr.append("Strong belief people today should benefit")
        elif calc1 <= 24.99 and calc1 >= 5:
            q2_descr_arr.append("Weak belief people today should benefit")
        elif calc1 <= 4.99 and calc1 >= -4.99:
            q2_descr_arr.append("Neutral belief people today and tomorrow should benefit")
        elif calc1 <= -5 and calc1 >= -24.99:
            q2_descr_arr.append("Weak belief people tomorrow should benefit")
        elif calc1 <= -25 and calc1 >= -100:
            q2_descr_arr.append("Strong belief people tomorrow should benefit")
        else:
            q2_descr_arr.append("ERROR")


        #calculations for Us and others
        calc2 = Us - Oth

        if calc2 <= 100 and calc2 >=25:
            q2_descr_arr2.append("Strong belief community where I live should benefit")
        elif calc2 <= 24.99 and calc2 >= 5:
            q2_descr_arr2.append("Weak belief community where I live should benefit")
        elif calc2 <= 4.99 and calc2 >= -4.99:
            q2_descr_arr2.append("Neutral belief community where I live and moving it elsewhere")
        elif calc2 <= -5 and calc2 >= -24.99:
            q2_descr_arr2.append("Weak belief moving it elsewhere should benefit")
        elif calc2 <= -25 and calc2 >= -100:
            q2_descr_arr2.append("Strong belief moving it elsewhere should benefit")
        else:
            q2_descr_arr2.append("ERROR")

    return(q2_descr_arr, q2_descr_arr2)



def how_to_solve_sustainability_problems():


def print_to_output(df1, num_rows, num_cols):
    q1_descr_arr = natural_capital_and_ecosystem_services(df1, num_rows, num_cols)[0]
    q1_descr_arr2 = natural_capital_and_ecosystem_services(df1, num_rows, num_cols)[1]

    q2_descr_arr = who_should_benefit(df1, num_rows, num_cols)[0]
    q2_descr_arr2 = who_should_benefit(df1, num_rows, num_cols)[1]


    idx = 0
    for cell in range(2, num_rows):
        first_name = df1.iloc[cell]["Q8.2"]
        last_name = df1.iloc[cell]["Q8.3"]
        email = df1.iloc[cell]["Q8.4"]
        natural_capital_level = q1_descr_arr[idx]
        ecosystem_services_level = q1_descr_arr2[idx]
        generation_benefit = q2_descr_arr[idx]
        people_benefit = q2_descr_arr2[idx]
        idx = idx + 1
        print first_name + " " + last_name
        print "    " + natural_capital_level
        print "    " + ecosystem_services_level
        print "    " + generation_benefit
        print "    " + people_benefit
        print "-------------------------------"

def main():

    #runs the script from API that pulls csv from qualtrics
    #execfile("downloadResults.py")

    #reads the pulled(updated) csv to parse
    df1=pd.read_csv("MyQualtricsDownload/Updated Survey Final.csv")

    #gets number of rows - 1 and columns in the output csv
    #NOTE: the actual
    num_rows = df1.shape[0]
    num_cols = df1.shape[1]

    print_to_output(df1, num_rows, num_cols)
    #parse_question1(df1, num_rows, num_cols)

main()
