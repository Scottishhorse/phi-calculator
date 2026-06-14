import streamlit as st
import numpy as np

# ==================== 重要兼容性补丁 ====================
import collections
import collections.abc
if not hasattr(collections, 'Iterable'):
    collections.Iterable = collections.abc.Iterable
if not hasattr(collections, 'Sequence'):
    collections.Sequence = collections.abc.Sequence
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
import pyphi
# =====================================================

st.title("🧠 Φ 值计算器 - 详细步骤教学版")
st.write("选择系统后会一步步解释计算过程")

system = st.selectbox(
    "选择要演示的系统",
    [
        "发光二极管 (Photodiode) - 最小正Φ例子",
        "XOR 网络 (3节点)",
        "石头模型 (Φ ≈ 0)",
        "人脑 (理论说明)"
    ]
)

if st.button("🚀 开始计算并显示每一步"):
    with st.spinner("正在按IIT步骤计算..."):
        try:
            if system == "发光二极管 (Photodiode) - 最小正Φ例子":
                st.subheader("🔄 发光二极管计算过程")
                st.write("**步骤1：存在** - 定义2节点系统（检测器 + 记忆器）")
                st.write("**步骤2：内在性 + 当前状态** - 当前状态 (0,0)")
                
                tpm = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
                network = pyphi.Network(tpm, node_labels=('检测器', '记忆器'))
                state = (0, 0)
                
                st.write("**步骤3：信息 + 整合** - 计算不可约因果信息")
                subsystem = pyphi.Subsystem(network, state)
                sia = pyphi.compute.sia(subsystem)
                phi_value = sia.phi
                
                st.success(f"**大 Φ 值 ≈ {phi_value:.4f}**")
                st.write("**解释**：这个小系统有基本的因果反馈，拆开会损失信息，因此 Φ > 0。")
                
            elif system == "XOR 网络 (3节点)":
                st.subheader("🔄 XOR 网络计算过程")
                network = pyphi.examples.xor_network
                state = (1, 0, 0)
                subsystem = pyphi.Subsystem(network, state)
                sia = pyphi.compute.sia(subsystem)
                phi_value = sia.phi
                st.success(f"**大 Φ 值 ≈ {phi_value:.4f}**")
                
            elif system == "石头模型 (Φ ≈ 0)":
                st.subheader("🔄 石头模型")
                st.write("**步骤**：定义为独立节点 → 任意分区 → 信息损失为0")
                st.success("**大 Φ 值 ≈ 0**")
                st.write("**原因**：没有不可分割的因果整合。")
                
            elif system == "人脑 (理论说明)":
                st.subheader("🧠 人脑")
                st.success("**理论 Φ 值极高**")
                st.write("860亿神经元高度整合，无法用电脑精确计算。")
                
            st.balloons()
            
        except Exception as e:
            st.error(f"计算出错: {str(e)}")

st.divider()
st.info("💡 每一步都对应IIT的公理/公设，目的是帮助理解为什么这样计算。")
st.caption("作者：格兰马")
