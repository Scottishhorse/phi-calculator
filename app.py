import streamlit as st
import pyphi
import numpy as np

st.title("🧠 Φ 值计算器 (IIT 整合信息理论)")

st.write("这是一个简单版本，先用例子试试看")

# 加载一个经典例子
if st.button("使用 XOR 示例网络（经典测试例子）"):
    network = pyphi.examples.xor_network
    state = (1, 0, 0)
    st.success("示例已加载！正在计算...")
    
    with st.spinner("计算中..."):
        sia = pyphi.compute.sia(network, state)
        st.success(f"**大 Φ 值 = {sia.phi:.4f}**")
        st.write("这个网络的 Φ 值大于0，说明有一定的整合信息。")