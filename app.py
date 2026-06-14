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
st.write("**选择系统 → 点击计算 → 查看每一步解释**（专为学习 IIT 设计）")

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
    with st.spinner("正在计算并生成解释..."):
        try:
            if system == "发光二极管 (Photodiode) - 最小正Φ例子":
                st.subheader("🔄 计算过程 - 发光二极管")
                
                st.write("**步骤 1: 定义系统 (存在)**")
                st.write("我们用一个2节点网络建模：一个节点检测光，另一个节点记忆/预测。")
                st.write("目的：建立因果关系模型（TPM转移概率矩阵）。")
                
                st.write("**步骤 2: 当前状态**")
                st.write("假设初始状态 (OFF, OFF)")
                
                st.write("**步骤 3: 计算内在信息 (Information)**")
                st.write("看当前状态对可能原因和结果的约束程度。")
                
                st.write("**步骤 4: 找最小信息分区 (Integration)**")
                st.write("尝试把两个节点拆开，看损失多少信息。")
                
                # 实际计算
                tpm = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
                network = pyphi.Network(tpm, node_labels=('A','B'))
                subsystem = pyphi.Subsystem(network, (0,0))
                sia = pyphi.compute.sia(subsystem)
                phi_value = sia.phi
                
                st.success(f"**最终结果：大 Φ 值 ≈ {phi_value:.4f}**")
                st.write("**为什么 Φ > 0？** 因为拆开两个节点会损失因果信息，这个小系统有‘不可拆的黏性’。")
                
            elif system == "XOR 网络 (3节点经典例子)":
                st.subheader("🔄 计算过程 - XOR 网络")
                st.write("**步骤 1-4 同上**（定义TPM → 当前状态 → 内在信息 → 找最小分区）")
                
                network = pyphi.examples.xor_network
                state = (1, 0, 0)
                subsystem = pyphi.Subsystem(network, state)
                sia = pyphi.compute.sia(subsystem)
                phi_value = sia.phi
                
                st.success(f"**最终结果：大 Φ 值 ≈ {phi_value:.4f}**")
                st.write("这个例子在IIT论文中被反复使用，证明即使简单电路也能有正的Φ。")
                
            elif system == "石头模型 (Φ ≈ 0)":
                st.subheader("🔄 计算过程 - 石头模型")
                st.write("**步骤 1: 定义系统**")
                st.write("石头被建模成多个独立、无相互影响的节点。")
                st.write("**步骤 4: 找最小分区**")
                st.write("随便把石头劈成两半，信息几乎没有损失（分区前后几乎一样）。")
                st.success("**最终结果：Φ ≈ 0**")
                st.write("**目的**：说明没有‘不可约因果整合’的东西就没有意识（按IIT理论）。")
                
            elif system == "人脑 (理论说明，无法精确计算)":
                st.subheader("🧠 人脑 Φ 值（理论说明）")
                st.write("**为什么无法精确计算？**")
                st.write("人脑有860亿神经元，节点数太多，计算复杂度是NP-hard（天文数字）。")
                st.success("**理论上 Φ 值极高（数万甚至更高）**")
                st.write("**计算思路（简化）**：把大脑分成很多小区域，分别算小 Φ 再加总。但实际只能近似。")
                
            st.balloons()
            
        except Exception as e:
            st.error(f"计算出错: {str(e)}")
            st.info("小系统通常能算，大系统只能理论说明。")

st.divider()
st.info("💡 这个版本专门加入了**每一步的目的和解释**，适合学习哲学和意识理论使用。")
st.caption("作者：格兰马 | 基于 PyPhi + 详细教学解释")
