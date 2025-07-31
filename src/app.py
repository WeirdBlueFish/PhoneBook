from main import PHONEBOOK 
import streamlit as st

st.title("PHONEBOOK")

# --- 1. Initialize session state ---

if 'view' not in st.session_state:
    st.session_state.view = 'main'

# --- 2. Define functions to change the view ---

def set_view(view_name):
    """A helper function to change the value in session_state."""
    st.session_state.view = view_name


# --- 3. Display content based on the current view ---

# ---- Main View ----
if st.session_state.view == 'main':
    col1, col2, col3 = st.columns([1, 1, 1])
    
    col1.button("Add Phone Number", on_click=set_view, args=['add'])
    col2.button("View Phone Numbers", on_click=set_view, args=['view'])
    col3.button("Search Phone Numbers", on_click=set_view, args=['search'])


# ---- Add Contact View ----
elif st.session_state.view == 'add':
    st.header("Add a New Contact")

    with st.form("add_contact_form"):
        name = st.text_input("Name:").lower()
        lname = st.text_input("Last Name:").lower()
        number = st.text_input("Phone Number:").lower()
        
        submitted = st.form_submit_button("Confirm")
        
        if submitted:
            if not name or not number:
                st.error("Name and Phone Number are required fields.")
            else:
                try:
                    U1 = PHONEBOOK(name, lname, number)
                    U1.add() 
                    st.success(f"Contact '{name} {lname}' added successfully!")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    st.button("Back to Menu", on_click=set_view, args=['main'])


# ---- View Contacts View ----
elif st.session_state.view == 'view':
    st.header("All Phone Numbers")

    U1 = PHONEBOOK('', '', '')
    nums = U1.readAll()
    for i in range(len(nums)):
       phone = nums[i]
       st.info(body=f"{i+1}. {phone[1]}{'-'*10}{phone[2]}{'-'*10}{phone[3]}")

    st.button("Back to Menu", on_click=set_view, args=['main'])

# ---- Search Contacts View ----
elif st.session_state.view == 'search':
    st.header("Search Phone Numbers")

    with st.form("search_form"):

        search = st.text_input('Enter').lower()
        submitted = st.form_submit_button("Search")

        if submitted:
            if not search:
                st.error("Enter your searching please.")
            else:
                try:
                    U1 = PHONEBOOK('', '', '')
                    result = U1.readOne(search)
                    phone = result[0]
                    st.success(f"Contact {phone[1]} {phone[2]} found successfully!\n {phone[3]}")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

    st.button("Back to Menu", on_click=set_view, args=['main'])