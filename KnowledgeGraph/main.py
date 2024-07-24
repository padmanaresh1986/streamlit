import streamlit as st
from data_loader import load_data
import json
from streamlit_agraph import agraph, Node, Edge, Config

#st.title("Banks Acquisition Data")

df = load_data()

unique_bank_names = df['Bank Name'].unique()
unique_acq_institution = df['Acquiring Institution'].unique()
unique_city = df['City'].unique()
unique_state = df['State'].unique()

st.sidebar.write("Advanced Search")
filter_banks = st.sidebar.multiselect("Select Acquiring Institution",unique_acq_institution,max_selections=5,default=unique_bank_names[:1])
filtered_df = df[df['Acquiring Institution'].isin(filter_banks)]
#st.write(filtered_df)
mgmt_data = filtered_df.to_json(orient='values')
dict_convert = json.loads(mgmt_data)
#st.write(dict_convert)


def make_graph(dict_convert, position_show=False):
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


config = Config(width=800,
                height=400,
                directed=True,
                physics=True,
                hierarchical=False,
                highlightColor='#FF00FF',
                nodeHighlightBehavior=True,
                node={'labelProperty': 'label', 'renderLabel': True}
                )

position_show = st.sidebar.checkbox('Show Acquired Date')
# st.write(position_show)
filter_nodes, filter_edges = make_graph(dict_convert, position_show)

return_value = agraph(nodes=filter_nodes,
                      edges=filter_edges,
                      config=config)