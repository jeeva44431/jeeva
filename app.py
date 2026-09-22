import streamlit as st

a = st.chat_input("Enter a command")

if a:
    st.chat_message("user").write(a)

    command = a.lower().strip()

    if command == "hi":
        st.chat_message("AI").write("Hello! 👋")

    elif command == "bye":
        st.chat_message("AI").write("Goodbye! 👋")

    elif command == "help":
        st.chat_message("AI").write(
            "Commands: hi, bye, how are you, name, time, date, "
            "thanks, joke, python, streamlit, who are you, "
            "what can you do, clear, exit"
        )

    elif command == "how are you":
        st.chat_message("AI").write("I'm doing great! 😊")

    elif command == "name":
        st.chat_message("AI").write("My name is Streamlit Bot.")

    elif command == "time":
        from datetime import datetime
        st.chat_message("AI").write(
            datetime.now().strftime("%H:%M:%S")
        )

    elif command == "date":
        from datetime import datetime
        st.chat_message("AI").write(
            datetime.now().strftime("%d-%m-%Y")
        )

    elif command == "thanks":
        st.chat_message("AI").write("You're welcome! 😊")

    elif command == "joke":
        st.chat_message("AI").write(
            "Why do programmers prefer dark mode? "
            "Because light attracts bugs! 🐛"
        )

    elif command == "python":
        st.chat_message("AI").write(
            "Python is a popular programming language."
        )

    elif command == "streamlit":
        st.chat_message("AI").write(
            "Streamlit is a Python framework for building web apps."
        )

    elif command == "who are you":
        st.chat_message("AI").write(
            "I am a simple chatbot built with Streamlit."
        )

    elif command == "what can you do":
        st.chat_message("AI").write(
            "I can respond to commands such as hi, bye, time, date, "
            "joke, python, and streamlit."
        )

    elif command == "clear":
        st.rerun()

    elif command == "exit":
        st.chat_message("AI").write("Goodbye! 👋")

    else:
        st.chat_message("AI").write(
            "I don't understand that command. Type 'help'."
        )
