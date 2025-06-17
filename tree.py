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
