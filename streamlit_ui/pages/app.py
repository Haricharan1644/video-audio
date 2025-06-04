
import streamlit as st
import requests


if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()


st.title("🎞️ Video to Audio Converter")
uploaded_file = st.file_uploader("Upload your video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file:
    if st.button("Convert to Audio"):
        with st.spinner("Uploading..."):
            files = {'file': uploaded_file}
            response = requests.post("http://upload_service:5001/upload", files=files)
            if response.status_code == 200:
                filename = response.json()["filename"]
                st.success("Uploaded successfully!")
                with st.spinner("Converting..."):
                    convert_response = requests.post("http://converter_service:5002/convert", json={"filename": filename})
                    if convert_response.status_code == 200:
                        audio_file = filename.rsplit(".", 1)[0] + ".mp3"
                        audio_data = convert_response.content
                        notify_response = requests.get("http://notification_service:5004/notify")
                        st.success(notify_response.json()["message"])
                        # Direct download from converter response
                        st.download_button(
                            label="⬇️ Download Audio File",
                            data=audio_data,
                            file_name=audio_file,
                            mime="audio/mpeg"
                        )
                    else:
                        st.error("Conversion failed!")
            else:
                st.error("Upload failed!")


if st.button("Logout"):
    st.session_state.logged_in = False
    st.success("Logged out successfully.")
    st.switch_page("login.py")
