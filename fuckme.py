import ipycytoscape

import json
with open("colaData.json") as fi:
    json_file = json.load(fi)

cytoscapeobj = ipycytoscape.CytoscapeWidget()
cytoscapeobj.graph.add_graph_from_json(json_file)

cytoscapeobj.set_style([{
                            'selector': 'node',
                            'css': {
                                'background-color': 'red'
                            }
                        },

                        {
                            'selector': 'edge',
                            'css': {
                                'line-color': 'pink'
                            }
                        }])

cytoscapeobj
