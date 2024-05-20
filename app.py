import streamlit as st
import customer_app
import retailer_dashboard

def main_page():
    # st.title("Nova")
    st.markdown("## hi, we are Novas, your ultimate go-to shopping assistants")
    if st.button("Customer ho toh yaha dabao"):
        st.session_state['page'] = 'customer'
    if st.button("yeh retailers ke liye hai"):
        st.session_state['page'] = 'retailer'

def main():
    if 'page' not in st.session_state:
        st.session_state['page'] = 'main'

    if st.session_state['page'] == 'main':
        main_page()
    elif st.session_state['page'] == 'customer':
        customer_app.main()
    elif st.session_state['page'] == 'retailer':
        retailer_dashboard.main()

if __name__ == "__main__":
    main()
