# -*- coding: utf-8 -*-
"""
Use this script to parse an individual's results

Created on Sun Mar 25 13:24:34 2018

@author: Caroline
"""  

import pandas as pd
import pdfkit as pk

#uses question 1, or columns Q3.1-1 through Q3.1-6, to find the user's 
#natural/social capital tendency and ecosystem/species and biodiversity services
def natural_capital_and_ecosystem_services(df1, survey_taker, num_rows, num_cols):
    q1_descr_arr = []  #for natural capital names
    q1_calc_arr = []   #for natural capital calculations(not needed)
    q1_descr_arr2 = [] #for ecosystem tendency names
    user_arr = []
    for i in range(1, 7): 
        Q3_ = "Q3.1_" + str(i)
        #[2] GETS CHANGED BASeD OFF WHICH USER WE WANT
        user_output_q1 = df1.iloc[survey_taker][Q3_]
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
   

def who_should_benefit(df1, survey_taker, num_rows, num_cols):
    q2_descr_arr = []   #holds data for user for people today/tomorrow benefiting
    q2_descr_arr2 = []  #holds data for Us or others benefiting

    user_arr = []
    user_arr2 = []
    for i in range(1, 3): 
        Q4_ = "Q4.1_" + str(i)
        Q5_ = "Q5.1_" + str(i)
        #[2] GETS CHANGED BASeD OFF WHICH USER WE WANT
        user_output_q2_1 = df1.iloc[survey_taker][Q4_]
        user_output_q2_2 = df1.iloc[survey_taker][Q5_]
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
    
def how_to_solve_sustainability_problems(df1, survey_taker, num_rows, num_cols):
    solve_arr = []
    tech_innov = df1.iloc[survey_taker]["Q6.1_1"]
    solve_arr.append(tech_innov)
    free_market = df1.iloc[survey_taker]["Q6.1_2"]
    solve_arr.append(free_market)
    market_fail = df1.iloc[survey_taker]["Q6.1_3"]
    solve_arr.append(market_fail)
    strong_govt = df1.iloc[survey_taker]["Q6.1_7"]
    solve_arr.append(strong_govt)
    new_inst = df1.iloc[survey_taker]["Q6.1_6"]
    solve_arr.append(new_inst)
    education = df1.iloc[survey_taker]["Q6.1_5"]
    solve_arr.append(education)

    return solve_arr

def hotly_debated_beliefs(df1, survey_taker, num_rows, num_cols):
    debated_arr = []
    religion = df1.iloc[survey_taker]["Q7.1_2"]
    debated_arr.append(religion)
    rights = df1.iloc[survey_taker]["Q7.1_4"]
    debated_arr.append(rights)
    limits = df1.iloc[survey_taker]["Q7.1_5"]
    debated_arr.append(limits)
    pop = df1.iloc[survey_taker]["Q7.1_7"]
    debated_arr.append(pop)
    bal = df1.iloc[survey_taker]["Q7.1_8"]
    debated_arr.append(bal)
    sav = df1.iloc[survey_taker]["Q7.1_9"]
    debated_arr.append(sav)
    evol = df1.iloc[survey_taker]["Q7.1_10"]
    debated_arr.append(evol)
    
    return debated_arr
    
    

def print_to_output(df1, survey_taker, num_rows, num_cols):
    q1_descr_arr = natural_capital_and_ecosystem_services(df1, survey_taker, num_rows, num_cols)[0]
    q1_descr_arr2 = natural_capital_and_ecosystem_services(df1, survey_taker, num_rows, num_cols)[1]
    
    q2_descr_arr = who_should_benefit(df1, survey_taker, num_rows, num_cols)[0]
    q2_descr_arr2 = who_should_benefit(df1, survey_taker, num_rows, num_cols)[1]

    solve_sust = how_to_solve_sustainability_problems(df1, survey_taker, num_rows, num_cols)

    hotly_debated = hotly_debated_beliefs(df1, survey_taker, num_rows, num_cols)

    first_name = df1.iloc[survey_taker]["Q8.2"]
    last_name = df1.iloc[survey_taker]["Q8.3"]
    email = df1.iloc[survey_taker]["Q8.4"]
    natural_capital_level = q1_descr_arr[0]
    ecosystem_services_level = q1_descr_arr2[0]
    generation_benefit = q2_descr_arr[0]
    people_benefit = q2_descr_arr2[0]
    print first_name + " " + last_name
    print "    " + natural_capital_level
    print "    " + ecosystem_services_level
    print "    " + generation_benefit
    print "    " + people_benefit
    print "-------------------------------"
    
    user_file = open("Reports/" + first_name + "_" + last_name + "_report.html", 'w')
    message = """<html>
    <head>
    </head>
    <h1><center>Sustainability Values Diagnostic</center></h1>
    
    <body>    
    
    <head>
    <style>   
    
    {# Enlarges the table #}
    table {
        width:75%%;
    }
    {# table border #}
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    {# adds font and left aligned #}
    th, td {
        padding: 15px;
        text-align: left;
    }
    
    <!–– styling for shading correct natural/social capital tendency ––> 
    
    {# colors strong natural capital tendency #}
    table#t01 tr#nc[natural_capital_level="Strong Natural Capital"] td:first-child + td  {
        background-color: #eee;}
    
    {# colors weak natural capital tendency #}
    table#t01 tr#nc[natural_capital_level="Weak Natural Capital"] td:first-child + td+ td  {
        background-color: #eee;}
            
    {# colors neutral natural/social capital tendency #}
    table#t01 tr#nc[natural_capital_level="Neutral Natural/Social Capital"] td:first-child + td+ td + td  {
        background-color: #eee;}
            
    {# colors weak social capital tendency #}
    table#t01 tr#nc[natural_capital_level="Weak Social Capital"] td:first-child + td+ td + td +td  {
        background-color: #eee;}

    {# colors strong social capital tendency #}
    table#t01 tr#nc[natural_capital_level="Strong Social Capital"] td:first-child + td+ td + td +td + td  {
        background-color: #eee;}

    <!–– Styling for strong ecosystem or species/biodiversity ––>        
    
    {# colors strong ecosystem services #}
    table#t01 tr#es[ecosystem_services_level="Strong Ecosystem Services"] td:first-child + td  {
        background-color: #eee;}
    
    {# colors weak ecosystem services #}
    table#t01 tr#es[ecosystem_services_level="Weak Ecosystem Services"] td:first-child + td+ td  {
        background-color: #eee;}
            
    {# colors Neutral Ecosystem Services/Species and Biodiversity #}
    table#t01 tr#es[ecosystem_services_level="Neutral Ecosystem Services/Species and Biodiversity"] td:first-child + td+ td + td  {
        background-color: #eee;}
            
    {# colors Weak Species and Biodiversity #}
    table#t01 tr#es[ecosystem_services_level="Weak Species and Biodiversity"] td:first-child + td+ td + td +td  {
        background-color: #eee;}

    {# colors strong Species and Biodiversity #}
    table#t01 tr#es[ecosystem_services_level="Strong Species and Biodiversity"] td:first-child + td+ td + td +td + td  {
        background-color: #eee;}
            
    <!–– Styling for who should benefit - today or tomorrow ––>
    
    {# colors strong today #}
    table#t02 tr#gb[generation_benefit="Strong belief people today should benefit"] td:first-child + td  {
        background-color: #eee;}
    
    {# colors weak today #}
    table#t02 tr#gb[generation_benefit="Weak belief people today should benefit"] td:first-child + td+ td  {
        background-color: #eee;}
            
    {# colors Neutral today or future #}
    table#t02 tr#gb[generation_benefit="Neutral belief people today and tomorrow should benefit"] td:first-child + td+ td + td  {
        background-color: #eee;}
            
    {# colors Weak future #}
    table#t02 tr#gb[generation_benefit="Weak belief people tomorrow should benefit"] td:first-child + td+ td + td +td  {
        background-color: #eee;}

    {# colors strong future #}
    table#t02 tr#gb[generation_benefit="Strong belief people tomorrow should benefit"] td:first-child + td+ td + td +td + td  {
        background-color: #eee;}
        
    <!–– Styling for who should benefit - us or others ––>
    
    {# colors strong us #}
    table#t02 tr#pb[people_benefit="Strong belief community where I live should benefit"] td:first-child + td  {
        background-color: #eee;}
    
    {# colors weak us  #}
    table#t02 tr#pb[people_benefit="Weak belief community where I live should benefit"] td:first-child + td+ td  {
        background-color: #eee;}
            
    {# colors Neutral us or others #}
    table#t02 tr#pb[gpeople_benefit="Neutral belief community where I live and moving it elsewhere"] td:first-child + td+ td + td  {
        background-color: #eee;}
            
    {# colors Weak others #}
    table#t02 tr#pb[people_benefit="Weak belief moving it elsewhere should benefit"] td:first-child + td+ td + td +td  {
        background-color: #eee;}

    {# colors strong others #}
    table#t02 tr#pb[people_benefit="Strong belief moving it elsewhere should benefit"] td:first-child + td+ td + td +td + td  {
        background-color: #eee;}

    <--! styling for how we should solve sustainability problems -->

    {# colors how we should solve sustainability problems #}
    table#t03 tr[solve_sust="1"] td:first-child + td {
        background-color: #eee;}

    {# chow we should solve sustainability problems #}
    table#t03 tr[solve_sust="2"] td:first-child + td+ td {
        background-color: #eee;}
            
    {# how we should solve sustainability problems #}
    table#t03 tr[solve_sust="3"] td:first-child + td+ td +td {
        background-color: #eee;}

    {# how we should solve sustainability problems #}
    table#t03 tr[solve_sust="4"] td:first-child + td+ td +td +td{
        background-color: #eee;}
    
    {# how we should solve sustainability problems #}
    table#t03 tr[solve_sust="5"] td:first-child + td+ td +td +td +td{
        background-color: #eee;}
      
    <--! styling for hotly debated topics -->
    
    {# colors hotly debated topics #}
    table#t04 tr[hotly_debated="1"] td:first-child + td {
        background-color: #eee;}

    {# colors for hotly debated topics #}
    table#t04 tr[hotly_debated="2"] td:first-child + td+ td {
        background-color: #eee;}
            
    {# hotly debated topics #}
    table#t04 tr[hotly_debated="3"] td:first-child + td+ td +td {
        background-color: #eee;}

    {# hotly debated topics #}
    table#t04 tr[hotly_debated="4"] td:first-child + td+ td +td +td{
        background-color: #eee;}
    
    {# hotly debated topics #}
    table#t04 tr[hotly_debated="5"] td:first-child + td+ td +td +td +td{
        background-color: #eee;}

    }

    </style>
    </head>
    
    <htm>
    <body>
    
    <h2>Prepared for: %s %s</h2>

    <p><b>What should be sustained?</b></p>
    <!-- Everything above that has to do with table is applied here -->
    <table id="t01">

    <!-- The First Row -->
    <tr>
        <td>      </td>
        <td>Strong</td>
        <td>Weak</td>
        <td>Neutral</td>
        <td>Weak</td>
        <td>Strong</td>
        <td>      </td>
    </tr>
    
    <!-- The Second Row -->
    <tr id="nc" natural_capital_level = "%s" > 
        <td>Natural capital</td>
        <td>180</td>
        <td>270</td>
        <td>280</td>
        <td>170</td>
        <td>100</td>
        <td>Social capital</td>
    </tr>
    
    <!-- The Third Row -->
    <tr id="es" ecosystem_services_level = "%s">
        <td>Ecosystem Services</td>
        <td>70</td>
        <td>280</td>
        <td>400</td>
        <td>200</td>
        <td>40</td>
        <td>Species and biodiversity</td>
    </tr>
    
    </table>

    <br>
    <p><b>Who should benefit? </b></p>
    
    <table id="t02">

    <!-- The First Row -->
    <tr>
        <td>      </td>
        <td>Strong</td>
        <td>Weak</td>
        <td>Neutral</td>
        <td>Weak</td>
        <td>Strong</td>
        <td>      </td>
    </tr>
    
    <!-- The Second Row -->
    <tr id="gb" generation_benefit = "%s" > 
        <td>People Today</td>
        <td>150</td>
        <td>260</td>
        <td>150</td>
        <td>340</td>
        <td>100</td>
        <td>People Tomorrow</td>
    </tr>
    
    <!-- The Third Row -->
    <tr id="pb" people_benefit = "%s">
        <td>Us</td>
        <td>560</td>
        <td>50</td>
        <td>100</td>
        <td>50</td>
        <td>230</td>
        <td>Others</td>
    </tr>
    
    </table>
        <br>
    <p><b>How should we solve sustainability problems? </b></p>
    <table id="t03">
    <!-- The First Row -->
    <tr>
        <td>      </td>
        <td>Strongly Disagree</td>
        <td>      </td>
        <td>Neutral</td>
        <td>      </td>
        <td>Strongly Agree</td>
    </tr>
    
    <!-- The Second Row -->
    <tr solve_sust = "%s" > 
        <td>With technological innovation</td>
        <td>20</td>
        <td>40</td>
        <td>130</td>
        <td>5530</td>
        <td>270</td>
    </tr>
    
    <!-- The Third Row -->
    <tr solve_sust = "%s">
        <td>By freeing market forces</td>
        <td>100</td>
        <td>340</td>
        <td>300</td>
        <td>200</td>
        <td>60</td>
    </tr>
    
    <!-- The Forth Row -->
    <tr solve_sust = "%s">
        <td>By fixing market failures</td>
        <td>50</td>
        <td>70</td>
        <td>300</td>
        <td>500</td>
        <td>80</td>
    </tr>    
    
    <!-- The Fifth Row -->
    <tr solve_sust = "%s">
        <td>With strong government actions</td>
        <td>80</td>
        <td>230</td>
        <td>220</td>
        <td>340</td>
        <td>130</td>
    </tr>    

    <!-- The Sixth Row -->
    <tr solve_sust = "%s">
        <td>By educating citizens & consumers</td>
        <td>10</td>
        <td>20</td>
        <td>50</td>
        <td>420</td>
        <td>500</td>
    </tr>
    
    <!-- The Seventh Row -->
    <tr solve_sust = "%s">
        <td>By creating new institutions</td>
        <td>10</td>
        <td>90</td>
        <td>380</td>
        <td>430</td>
        <td>90</td>
    </tr>
    
    </table>
    
    <p><b>Hotly Debated Beliefs </b></p>
    <table id="t04">
    
    <!-- The First Row -->
    <tr>
        <td>      </td>
        <td>Strongly Disagree</td>
        <td>      </td>
        <td>Neutral</td>
        <td>      </td>
        <td>Strongly Agree</td>
    </tr>
    
    <!-- The Second Row -->
    <tr hotly_debated = %s > 
        <td><b>Religion:</b> Because God created the natural
world, stewardship of nature should be my
religious duty.</td>
        <td>200</td>
        <td>220</td>
        <td>100</td>
        <td>350</td>
        <td>120</td>
    </tr>
    
    <!-- The Third Row -->
    <tr hotly_debated = %s >
        <td><b>Rights:</b> Mammals have as much right to exist as
humans.</td>
        <td>20</td>
        <td>80</td>
        <td>110</td>
        <td>360</td>
        <td>420</td>
    </tr>
    
    <!-- The Forth Row -->
    <tr hotly_debated = %s>
        <td><b>Limits:</b> Humanity is pushing the limits of
Earth’s ecological systems, risking ecological
collapse.</td>
        <td>30</td>
        <td>30</td>
        <td>60</td>
        <td>360</td>
        <td>520</td>
    </tr>    

    <!-- The Fifth Row -->
    <tr hotly_debated = %s>
        <td><b>Population: </b>The human population explosion presents the greatest threat to sustainable development.
becomes unbalanced and unhealthy.</td>
        <td>10</td>
        <td>50</td>
        <td>110</td>
        <td>510</td>
        <td>310</td>
    </tr>    
 
    <!-- The Sixth Row -->
    <tr hotly_debated = %s>
        <td><b>Balance: </b>Nature’s ecology has self-correcting
properties that keep it balanced and healthy. It is
only when humans disturb things that nature
becomes unbalanced and unhealthy.</td>
        <td>10</td>
        <td>50</td>
        <td>110</td>
        <td>510</td>
        <td>310</td>
    </tr>    

    <!-- The Seventh Row -->
    <tr hotly_debated = %s >
        <td><b>Nobel savage:</b> Modern Americans have much to
learn about sustainable development from the land
ethics and land management of Native Americans
alive before Columbus.</td>
        <td>10</td>
        <td>60</td>
        <td>260</td>
        <td>310</td>
        <td>360</td>
    </tr>
    
    <!-- The Eighth Row -->
    <tr hotly_debated = %s>
        <td><b>Best Evolved:</b> Survival-of- the-fittest made
humans the best-adapted, highest-evolved species
and we therefore have the right to manage other
species.</td>
        <td>140</td>
        <td>320</td>
        <td>230</td>
        <td>240</td>
        <td>70</td>
    </tr>
    
    </table>
    
    </body>
    </html>"""
    
    
    whole_message = message % (first_name, last_name, natural_capital_level, ecosystem_services_level, 
                               generation_benefit, people_benefit, solve_sust[0], 
                               solve_sust[1], solve_sust[2], solve_sust[3], solve_sust[4], solve_sust[5],
                               hotly_debated[0], hotly_debated[1], hotly_debated[2], hotly_debated[3],
                               hotly_debated[4], hotly_debated[5], hotly_debated[6])
    user_file.write(whole_message)
    user_file.close()  
        

        #UNCOMMENT FOR PDF VERSION
        #pk.from_file(user_file.name, 'ReportsPDF/'+ name + '.pdf')  #can also make pdf from html webpage 

    

def main():

    #runs the script from API that pulls csv from qualtrics
    #execfile("downloadResults.py")
    
    #reads the pulled(updated) csv to parse
    df1=pd.read_csv("MyQualtricsDownload/Updated Survey Final.csv")
    
    #gets number of rows - 1 and columns in the output csv
    #NOTE: the actual 
    num_rows = df1.shape[0]
    num_cols = df1.shape[1]
    
    survey_taker = 2
    
    print_to_output(df1, survey_taker, num_rows, num_cols)
    
main()   

    
