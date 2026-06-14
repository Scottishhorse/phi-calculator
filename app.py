import streamlit as st

st.title("🧠 Φ 值计算器 (IIT 整合信息理论)")

st.write("### 欢迎使用！")
st.write("这是一个简单版本，先展示例子。以后会加上真正计算功能。")

st.header("石头 vs 大脑例子")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🪨 石头")
    st.write("Φ 值 ≈ **0**")
    st.write("原因：可以随便劈开，各部分互相影响几乎不变。")
    
with col2:
    st.subheader("🧠 大脑（简化）")
    st.write("Φ 值 **很高**")
    st.write("原因：拆开任何部分都会严重破坏整体的因果关系。")

st.header("经典 XOR 示例网络")
st.write("这是一个著名的简单网络例子：")
st.write("**大 Φ 值 ≈ 0.125** （有一定的整合信息）")

st.info("目前因为技术问题，完整计算功能暂时不可用。")
st.caption("作者：格兰马 | 基于整合信息理论")

if st.button("重新加载例子"):
    st.rerun()
