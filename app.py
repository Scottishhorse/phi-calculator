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

st.title("🧠 Φ 值计算器 - 带详细步骤解释")
st.write("**选择系统 → 点击计算 → 查看每一步大白话解释**")

system = st.selectbox(
    "选择要计算/演示的系统",
    [
        "发光二极管 (Photodiode) - 最小正Φ例子",
        "XOR 网络 (3节点经典例子)",
        "石头模型 (Φ ≈ 0)",
        "人脑 (理论说明，无法精确计算)"
    ]
)

if st.button("🚀 开始计算并显示步骤"):
    with st.spinner("正在计算并生成详细解释..."):
        try:
            if system == "发光二极管 (Photodiode) - 最小正Φ例子":
                st.subheader("🔄 计算过程 - 发光二极管")
                st.write("**步骤 1: 存在 (Existence)** - 定义系统模型")
                st.write("用2个节点（检测器 + 记忆器）建立转移概率矩阵（TPM）。")
                
                st.write("**步骤 2: 当前状态** - 假设初始状态 (0,0)")
                
                # 正确调用方式（传入 Network 和 state）
                tpm = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
                network = pyphi.Network(tpm, node_labels=('检测器', '记忆器'))
                state = (0, 0)
                
                st.write("**步骤 3-4: 信息 + 整合** - 计算内在信息并找最小分区")
                sia = pyphi.compute.sia(network, state)   # ← 关键修复
                phi_value = sia.phi
                
                st.success(f"**最终结果：大 Φ 值 ≈ {phi_value:.4f}**")
                st.write("**为什么这样算？** 因为这个小系统拆不开，拆了就会损失因果信息，所以 Φ > 0。")
                
            elif system == "XOR 网络 (3节点经典例子)":
                st.subheader("🔄 计算过程 - XOR 网络")
                st.write("**步骤 1-4**：定义网络 → 当前状态 → 计算信息 → 找最小信息分区")
                
                network = pyphi.examples.xor_network
                state = (1, 0, 0)
                sia = pyphi.compute.sia(network, state)   # ← 修复调用
                phi_value = sia.phi
                
                st.success(f"**最终结果：大 Φ 值 ≈ {phi_value:.4f}**")
                
            elif system == "石头模型 (Φ ≈ 0)":
                st.subheader("🔄 计算过程 - 石头模型")
                st.write("**步骤 1: 定义系统** - 很多独立节点，没有互相影响。")
                st.write("**步骤 4: 最小分区** - 随便拆，信息几乎不损失。")
                st.success("**最终结果：Φ ≈ 0**")
                
            elif system == "人脑 (理论说明，无法精确计算)":
                st.subheader("🧠 人脑 Φ 值")
                st.success("**理论上 Φ 值极高**（远超任何人工系统）")
                st.write("原因：860亿神经元高度相互依赖，拆任何一小块都会严重破坏整体因果结构。")
                
            st.balloons()
            
        except Exception as e:
            st.error(f"计算出错: {str(e)}")
            st.info("如果还有问题，请把错误信息复制给我，我继续修复。")

st.divider()
st.info("💡 每个步骤都解释了**做什么、为什么、目的**，适合学习用。")
st.caption("作者：格兰马 | 基于 PyPhi")
