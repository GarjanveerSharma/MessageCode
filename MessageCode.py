import streamlit as st
import numpy as np

# TITLE
st.title("🔐 Generate your message in secret code")

# USER INPUT - MESSAGE
st.subheader("✉️ Enter Message")
message = st.text_input("Message")

# FIXED SECRET KEY (learning purpose)
secret_key = 4

# GENERATE CODE BUTTON
if st.button("Generate Secure Code"):

    if message == "":
        st.warning("Please enter a message")

    else:
        # convert message to numbers
        msg_array = np.array([ord(ch) for ch in message])

        # add secret key to secure it
        secure_code = msg_array + secret_key

        # show secure code
        st.success("Secure code generated ✅")
        st.write("Secure Code:")
        st.write(",".join(map(str, secure_code)))


# DECODE SECTION
st.subheader("🔓 Decode Message")

code_input = st.text_area("Paste Secure Code (comma separated)")

if st.button("Decode Secure Code"):

    if code_input == "":
        st.warning("Please paste the secure code")

    else:
        try:
            # convert string to numbers
            code_array = np.array(code_input.split(","), dtype=int)

            # subtract secret key
            original_values = code_array - secret_key

            # convert numbers back to characters
            original_message = "".join([chr(num) for num in original_values])

            st.success("Original Message:")
            st.write(original_message)

        except:
            st.error("Invalid code format ❌")


# FOOTER
st.markdown("---")
st.markdown("Developed by **Garjanveer Sharma 😊**")

# All done 👍
