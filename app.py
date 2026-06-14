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

st.title("🧠 Φ 值计算器 - 详细步骤版")
st.write("选择系统后点击按钮，会一步步显示计算过程和大白话解释")

system = st.selectbox(
    "选择系统",
    [
        "发光二极管 (Photodiode) - 最小正Φ例子",
        "XOR 网络 (3节点)",
        "石头模型 (Φ ≈ 0)",
        "人脑 (理论说明)"
    ]
)

if st.button("🚀 开始计算并显示详细过程"):
    with st.spinner("计算中..."):
        try:
            if system == "发光二极管 (Photodiode) - 最小正Φ例子":
                st.subheader("🔄 发光二极管计算过程")
                
                st.write("**步骤1：存在 (Existence)**")
                st.write("建立2节点系统模型（检测光 + 记忆）。")
                
                st.write("**步骤2：当前状态**")
                st.write("当前状态：(0, 0)")
                
                # 正确写法
                tpm = np.array([[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]])
                network = pyphi.Network(tpm, node_labels=('检测器', '记忆器'))
                state = (0, 0)
                
                subsystem = pyphi.Subsystem(network, state)
                sia = pyphi.compute.sia(subsystem)
                phi_value = sia.phi
                
                st.success(f"**最终结果：Φ 值 ≈ {phi_value:.4f}**")
                st.write("**为什么 >0？** 因为两个节点有不可分割的因果关系，拆开会损失信息。")
                
            elif system == "XOR 网络 (3节点)":
                st.subheader("🔄 XOR 网络计算过程")
                network = pyphi.examples.xor_network
                state = (1, 0, 0)
                subsystem = pyphi.Subsystem(network, state)
                sia = pyphi.compute.sia(subsystem)
                phi_value = sia.phi
                
                st.success(f"**最终结果：Φ 值 ≈ {phi_value:.4f}**")
                
            elif system == "石头模型 (Φ ≈ 0)":
                st.subheader("🔄 石头模型")
                st.write("**步骤：** 定义为多个独立节点 → 随便分区 → 信息损失 ≈ 0")
                st.success("**最终结果：Φ ≈ 0**")
                
            elif system == "人脑 (理论说明)":
                st.subheader("🧠 人脑")
                st.success("**理论 Φ 值极高**")
                st.write("无法精确计算，但根据IIT，人脑是已知 Φ 值最高的系统。")
                
            st.balloons()
            
        except Exception as e:
            st.error(f"计算出错: {str(e)}")
            st.info("请把完整错误信息复制给我，我继续修复。")

st.divider()
st.info("这个版本专门为学习者设计，每一步都有解释。")
st.caption("作者：格兰马")
