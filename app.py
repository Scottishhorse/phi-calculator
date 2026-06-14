import streamlit as st
import numpy as np

# ==================== 兼容性补丁 ====================
import collections
import collections.abc
if not hasattr(collections, 'Iterable'):
    collections.Iterable = collections.abc.Iterable
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
if not hasattr(collections, 'Sequence'):
    collections.Sequence = collections.abc.Sequence
import pyphi
# ================================================

st.title("🧠 Φ 值计算器 - 详细教学版")
st.write("选择系统，点击按钮查看每一步解释")

system = st.selectbox(
    "选择系统",
    ["发光二极管 (Photodiode)", "XOR 网络", "石头模型", "人脑 (理论)"]
)

if st.button("🚀 开始计算"):
    with st.spinner("计算中..."):
        try:
            if system == "发光二极管 (Photodiode)":
                st.subheader("发光二极管计算过程")
                st.write("**步骤1：定义网络** - 2个节点（检测器 + 记忆器）")
                st.write("**步骤2：当前状态** - (0, 0)")
                
                tpm = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
                network = pyphi.Network(tpm)
                state = (0, 0)
                
                # 使用稳定调用方式
                sia = pyphi.compute.sia(network, state)
                phi_value = sia.phi
                
                st.success(f"**Φ 值 ≈ {phi_value:.4f}**")
                st.write("**为什么这样算？** 这个小系统有因果反馈，拆开会损失信息，所以 Φ > 0。")
                
            elif system == "XOR 网络":
                st.subheader("XOR 网络计算过程")
                network = pyphi.examples.xor_network
                state = (1, 0, 0)
                sia = pyphi.compute.sia(network, state)
                phi_value = sia.phi
                st.success(f"**Φ 值 ≈ {phi_value:.4f}**")
                
            elif system == "石头模型":
                st.subheader("石头模型")
                st.success("**Φ 值 ≈ 0**")
                st.write("**原因**：各部分独立，随便拆分信息几乎不损失。")
                
            elif system == "人脑 (理论)":
                st.subheader("人脑")
                st.success("**理论 Φ 值：极高**")
                st.write("无法精确计算，但远高于任何人工系统。")
                
            st.balloons()
            
        except Exception as e:
            st.error(f"计算出错: {str(e)}")
            st.info("如果还是报错，请把完整错误文字复制给我。")

st.divider()
st.info("每一步解释对应 IIT 的公设（存在、信息、整合等）。")
st.caption("作者：格兰马")
