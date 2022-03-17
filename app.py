import streamlit as st

st.set_page_config( page_title = "CalcGPA", page_icon = None) 
#for page title & favicon


def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade



def calc(sem):
    subjects = {}
    labs = {}
    GPA = 0
    flag = 0  #for the warning message when marks haven't entered
    credits = 0
    col1, col2 = st.columns(2)  #for columns: one for theory sub, and another for lab sub

    if sem == 1 :
        subjects = { 'App. Maths-I' : 4, 'App. Physics-I' : 3, 'Manufacturing Processes' : 3, 'Electrical Tech.' : 3, 'Human Values' : 1, 'Fundamentals of Computing' : 2, 'App. Chemistry' : 3 }
        labs = { 'App. Physics Lab-I' : 1, 'Elecrical Tech. Lab' : 1, 'Workshop' : 2, 'Engg. Graphics Lab' : 2, 'FOC Lab' : 1, 'App. Chemistry Lab' : 1 }
        credits = 27

    elif sem == 2:
        subjects = { 'App. Maths-II' : 4, 'App. Physics-II' : 3, 'Electronic Devices' : 3, 'Intro To Programming' : 3, 'Engineering Mechanics' : 3, 'Communication Skills' : 3, 'Environmental Studies' : 3 }
        labs = { 'App. Physics Lab-II' : 1, 'Programming Lab' : 1, 'Electronics Lab' : 1, 'Engineering Mechanics Lab' : 1, 'EVS Lab' : 1 }
        credits = 27

    elif sem == 3:
        subjects = { 'App. Maths-III' : 4, 'Foundation of CS' : 4, 'Switching Theory & Logic Design' : 4, 'Circuits & Systems' : 4, 'Data Structures' : 4, 'Computer Graphics & Multimedia' : 4, }
        labs = { 'STLD Lab' : 1, 'Data Stucture Lab' : 1, 'Circuits & Systems Lab' : 1, 'CGMM Lab' : 1 }
        credits = 28

    elif sem == 4:
        subjects = { 'App. Maths-IV' : 4, 'Computer Organisation & Architecture' : 4, 'Theory of Computation' : 4, 'Database Management' : 4, 'Object Oriented Programming' : 3, 'Control Systems' : 4 }
        labs = { 'App. Maths Lab' : 1, 'COA Lab' : 1, 'DBMS Lab' : 1, 'OOPS Lab' : 1, 'Control Systems Lab' : 1 }
        credits = 28

    elif sem == 5:
        subjects = { 'Algo. Design & Analysis' : 4, 'Software Engineering' : 4, 'Java Programming' : 4, 'Industrial Management' : 3, 'Communication Systems' : 4, 'Communication Skills' : 1 }
        labs = { 'Algo. Design Lab' : 1, 'Software Engineering Lab' : 1, 'Java Programming Lab' : 1, 'In-house Workshop' : 1, 'Communication Systems Lab' : 1, 'Communication Skills Lab' : 1 }
        credits = 26

    elif sem == 6:
        subjects = { 'Compiler Design' : 4, 'Operating Systems' : 4, 'Data Communication & Networks' : 4, 'Web Engineering' : 3, 'Artificial Intelligence' : 4, 'Microprocessors & Microcontrollers' : 4, }
        labs = { 'Operating Systems Lab' : 1, 'Networks Lab' : 1, 'Web Engineering Lab' : 1, 'Microprocessor & Microcontroller Lab' : 1 }
        credits = 27

    elif sem == 7:
        subjects = { 'Information Security' : 4, 'Software testing and QA' : 3, 'Wireless Communication' : 3, elective1 : 3, elective2 : 3, }
        labs = { 'Information Security Lab' : 1, 'Software testing and QA Lab' : 1, 'Wireless Communication Lab' : 1, 'Lab based on Elective 1 & 2' : 1, 'Summer Training/Industrial Workshop/Certification' : 1, 'Minor Project' : 3 }
        credits = 24

    elif sem == 8:
        subjects = { 'Mobile Computing' : 4, 'Machine Learning' : 3 , 'Human Values & Professional Ethics-II' : 1, elective1 : 3, elective2 : 3 }
        labs = { 'Mobile Computing Lab' : 1, 'Machine Learning Lab' : 1, 'Lab based on Elective 1' : 1, 'Lab based on elective 2' : 1, 'Major Project' : 8 }
        credits = 26

    with col1:
        with st.expander("Theory Subjects"):
            for subject in subjects:
                marks = st.number_input("{}:".format( subject ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * subjects[subject]

    with col2:
        with st.expander("Practical Subjects"):
            for lab in labs:
                marks = st.number_input("{}:".format( lab ), 0, 100)
                if marks == 0 :
                    flag = 1
                num = grades(marks)
                GPA += num * labs[lab]

    if flag:
        st.warning("You haven't entered the marks of all subjects!")

    GPA = GPA / credits
    return GPA



st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(IT)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello {}!".format(name))
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 8)

        if sem == 7 or sem == 8:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Select your Electives</h3>", unsafe_allow_html=True)
            elective1List = []
            elective2List = []
            if sem == 7:
                elective1List = ['Complexity Theory', 'Intellectual property Rights', 'Embedded Systems', 'Data Mining and business Intelligence', 'Advanced Computer Intelligence', 'Natural Language Processing']
                elective2List = ['Digital Signal Processing', 'Simulation and Modelling', 'Advanced DBMS', 'Parallel Computing', 'Advanced Computer Networks', 'Control System', 'Sociology and  Elements of Indian History for Engineers']

            elif sem == 8:
                elective1List = ['Digital Image Processing', 'Microelectronics', 'Ad Hoc and Sensor Networks', 'Soft Computing', 'VLSI Design', 'Distributed Systems', 'Object Oriented Software Engineering', 'Computer Vision', 'Software Project Management']
                elective2List = ['Human Computer Interaction', 'Information theory and Coding', 'Web Intelligence and Big Data', 'Service Oriented Architecture', 'Multiagent Systems', 'Principles of Programming Languages', 'Telecommunication Networks', 'Selected Topics of Recent Trends in  Computer Science and Engineering']

            col3, col4 = st.columns(2)
            with col3:
                elective1 = st.selectbox(
                    'Elective 1',
                    (elective1List))

            with col4:
                elective2 = st.selectbox(
                    'Elective 2',
                    (elective2List))
                

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9) #just for formatting XD
            with cl5:
                ans = st.button("Submit")
                
            
            
    
            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.balloons()
                    st.balloons()



