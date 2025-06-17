# Install: pip install streamlit-tree-select
from streamlit_tree_select import tree_select
import os

def build_file_tree(path):
    nodes = []
    try:
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                nodes.append({
                    'label': f"📁 {item}",
                    'value': item_path,
                    'children': build_file_tree(item_path)
                })
            else:
                nodes.append({
                    'label': f"📄 {item}",
                    'value': item_path
                })
    except PermissionError:
        pass
    return nodes

# Usage
folder_path = "."  # Your folder path
file_tree = build_file_tree(folder_path)

selected = tree_select(
    file_tree,
    check_model="leaf",  # Only files selectable
    expanded=[0],  # Expand first level
    key="file_tree"
)




import streamlit as st
import os

def display_expanded_tree(path, level=0):
    """Display fully expanded file tree without selection"""
    try:
        items = sorted(os.listdir(path))
        for item in items:
            item_path = os.path.join(path, item)
            indent = "&nbsp;" * (level * 4)  # HTML spaces for indentation
            
            if os.path.isdir(item_path):
                # Display folder and recurse
                st.markdown(f"{indent}📁 **{item}/**", unsafe_allow_html=True)
                display_expanded_tree(item_path, level + 1)
            else:
                # Display file
                st.markdown(f"{indent}📄 {item}", unsafe_allow_html=True)
    except PermissionError:
        st.markdown(f"{indent}❌ Permission denied", unsafe_allow_html=True)

# Usage
folder_path = st.text_input("Enter folder path:", ".")
if folder_path and os.path.exists(folder_path):
    st.write("### File Tree (Fully Expanded)")
    display_expanded_tree(folder_path)
