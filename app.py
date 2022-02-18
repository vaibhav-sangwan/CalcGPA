import streamlit as st

st.set_page_config( page_title = "CalcGPA", page_icon = None)


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
    flag = 0
    col1, col2 = st.columns(2)

    if sem == 1 :
        subjects = { 'App. Maths-I' : 4, 'App. Physics-I' : 3, 'Manufacturing Processes' : 3, 'Electrical Tech.' : 3, 'Human Values' : 1, 'Fundamentals of Computing' : 2, 'App. Chemistry' : 3 }
        labs = { 'App. Physics Lab-I' : 1, 'Elecrical Tech. Lab' : 1, 'Workshop' : 2, 'Engg. Graphics Lab' : 2, 'FOC Lab' : 1, 'App. Chemistry Lab' : 1 }

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

    GPA = GPA/27
    return GPA

    

st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(IT)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello {}!".format(name))
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 6)

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9)
            with cl5:
                ans = st.button("Submit")
                
            
            
    
            if ans:
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()



