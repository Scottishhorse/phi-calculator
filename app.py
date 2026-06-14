import streamlit as st
import numpy as np

# ==================== 重要补丁：修复 PyPhi 兼容性 ====================
import collections
import collections.abc

# 打补丁，让老代码能运行
if not hasattr(collections, 'Iterable'):
    collections.Iterable = collections.abc.Iterable
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
if not hasattr(collections, 'Sequence'):
    collections.Sequence = collections.abc.Sequence

import pyphi
# ============================================================

st.title("🧠 Φ 值计算器 (IIT 整合信息理论)")

st.write("**现在支持真实计算了！**（仅限小网络）")

example = st.selectbox(
    "选择一个示例网络进行计算",
    ["XOR 网络（经典例子）", "石头模型（Φ ≈ 0）"]
)

if st.button("🚀 开始计算 Φ 值"):
    with st.spinner("计算中... 这可能需要几秒到几十秒"):
        try:
            if example == "XOR 网络（经典例子）":
                network = pyphi.examples.xor_network
                state = (1, 0, 0)
                sia = pyphi.compute.sia(network, state)
                phi_value = sia.phi
                
                st.success(f"**大 Φ 值 = {phi_value:.4f}**")
                st.balloons()
                
            elif example == "石头模型（Φ ≈ 0）":
                st.success("**石头模型 Φ ≈ 0**")
                st.write("因为它的各部分可以随便拆分，整体因果关系几乎没有损失。")
                
            st.write("计算完成！")
            
        except Exception as e:
            st.error(f"计算出错: {str(e)}")
            st.info("提示：网络太大容易超时或内存不够。目前只适合很小的网络。")

st.divider()
st.info("💡 这是一个演示版本。以后可以加入手动输入节点的功能。")
st.caption("Powered by PyPhi + 兼容补丁 | 作者：格兰马")
