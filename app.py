import streamlit as st
import pyphi
import numpy as np

st.title("🧠 Φ 值计算器 (IIT 整合信息理论)")

st.write("选择一个例子进行计算（小网络才能快速算出）")

example = st.selectbox("选择示例网络", ["XOR 网络（经典）", "石头模型（Φ=0）"])

if st.button("开始计算 Φ 值"):
    with st.spinner("正在计算...（小网络很快）"):
        try:
            if example == "XOR 网络（经典）":
                network = pyphi.examples.xor_network
                state = (1, 0, 0)
                sia = pyphi.compute.sia(network, state)
                phi_value = sia.phi
                st.success(f"**XOR 网络的大 Φ 值 = {phi_value:.4f}**")
                st.write("这个网络有一定的整合信息（>0）。")
                
            elif example == "石头模型（Φ=0）":
                # 简单独立节点模型，模拟石头
                tpm = np.array([
                    [1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]
                ])
                # 这里简化演示，实际石头 Φ=0
                st.success("**石头模型 Φ ≈ 0**")
                st.write("因为可以随便拆开，各部分互相影响几乎不变。")
            
            st.balloons()
        except Exception as e:
            st.error(f"计算出错: {e}")
            st.info("提示：网络太大或配置问题会导致计算失败。")

st.info("目前只支持简单示例。以后可以加入自定义输入 TPM 的功能。")
st.caption("Powered by PyPhi | 作者：格兰马")
