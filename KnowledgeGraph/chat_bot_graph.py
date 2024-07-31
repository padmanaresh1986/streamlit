import streamlit as st
import ollama
from data_loader import load_data
import json
from streamlit_agraph import agraph, Node, Edge, Config

st.sidebar.title("Ollama Python Chatbot")


df = load_data()
unique_bank_names = df['Bank Name'].unique()
unique_acq_institution = df['Acquiring Institution'].unique()
unique_city = df['City'].unique()
unique_state = df['State'].unique()

config = Config(width=800,
                height=400,
                directed=True,
                physics=True,
                hierarchical=False,
                highlightColor='#FF00FF',
                nodeHighlightBehavior=True,
                node={'labelProperty': 'label', 'renderLabel': True}
                )


def create_graph(acq_name):
    filtered_data_frame = df[df['Acquiring Institution'].isin([acq_name])]
    mgmt_data = filtered_data_frame.to_json(orient='values')
    dict_convert = json.loads(mgmt_data)
    filter_nodes, filter_edges = get_nodes_edges(dict_convert)
    return agraph(nodes=filter_nodes, edges=filter_edges, config=config)


def get_nodes_edges(dict_convert, position_show=False):
    nodes = []
    edges = []
    bank_names = []
    acquiring_institutions = []

    for data in dict_convert:
        # st.write(data)
        bank_name = data[0]
        acquiring_institution= data[4]

        if bank_name not in bank_names:
            node_params = {
                "id": bank_name,
                "title": f"Type : Bank \n Name: {bank_name} \n City: {data[1]} \n State: {data[2]}",
                "label": bank_name,
                "color": "#FF5733",
                "shape": "hexagon",
                "size": 30,
                "City": data[1],
                "State": data[2]
            }
            node = Node(**node_params)
            #node = Node(id=bank_name, label=bank_name, shape='hexagon', color='#FDD00F')
            nodes.append(node)
            bank_names.append(bank_name)

        if acquiring_institution not in acquiring_institutions:
            nodes.append(Node(id=acquiring_institution, label=acquiring_institution, color="#07A7A6"))
            acquiring_institutions.append(acquiring_institution)

        acq_date = f"acquired on {data[5]}"

        if position_show:
            edges.append(Edge(source=bank_name, target=acquiring_institution, label=acq_date))
        else:
            edges.append(Edge(source=bank_name, target=acquiring_institution))

    return [nodes, edges]


#initilize history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            st.dataframe(message["content"]["data_frame"])
            agraph(nodes=message["content"]["nodes"], edges=message["content"]["edges"], config=config)
        else:
            st.markdown(message["content"])

prompt = st.chat_input(placeholder="Type here Acquiring Institution")

if prompt:
    #add latest message to history in format {role, content}

    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        filtered_data_frame = df[df['Acquiring Institution'].isin([prompt])]
        mgmt_data = filtered_data_frame.to_json(orient='values')
        dict_convert = json.loads(mgmt_data)
        filter_nodes, filter_edges = get_nodes_edges(dict_convert)
        st.dataframe(filtered_data_frame)
        agraph(nodes=filter_nodes, edges=filter_edges, config=config)
        st.session_state["messages"].append({"role": "assistant", "content": {"key": prompt,
                                                                             "data_frame": filtered_data_frame,
                                                                             "nodes": filter_nodes,
                                                                             "edges": filter_edges}})
