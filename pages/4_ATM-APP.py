import streamlit as st
st.set_page_config(
    page_title="PERSONAL WEBSITE"
)
b1 , b2 = st.columns(2)
with b1:
    if st.button("Go to Project"):
        redirect_link = "https://github.com/sudhanshu976/ATM_APP"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this project code]({redirect_link})")
with b2:
    if st.button("Go to Website"):
        redirect_link = "https://collegeprojectatm.streamlit.app/"  # Replace with the URL you want to redirect to
        st.markdown(f"[Click here to go to this website]({redirect_link})")


st.title("ATM APP USING PYTHON AND SQL")
st.write("""

#### This is a ATM APP that is made using Python and SQL in Streamlit . It's main features are :
- **REGISTRATION PAGE** : It takes user name and 4-digit pin as input and generates a 10-digit unique id for the user .
         
- **LOGIN PAGE** : For a user to login into account has to enter correct unique_id and pin .
         
- **4 OPTIONS**  : When a user is logged in succesfully . he have 4 options : DEPOSIT , WITHDRAW , CHECK BALANCE and PIN CHANGE.


""")

video_path = 'videos/atm_app.mp4'
st.video(video_path)
