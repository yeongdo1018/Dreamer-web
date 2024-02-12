import streamlit as st

st.write("# Dreamer")
st.subheader("꿈을 꾸는 사람을 위한 간편한 OS")

st.write("Downloads")
downloads = [340, 480, 590, 970, 1548]
downloads
st.bar_chart(downloads)

st.text("Dreamer를 이용해주셔서 감사합니다.")

st.page_link("pages/download.py", label="Download")
