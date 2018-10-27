$(function(){
            cytoscape({
              container: document.getElementById('cy'),
              style: [
                { selector: 'node[label = "Person"]', 
                  css: {'background-color': '#6FB1FC', 'content': 'data(name)'}
                },
                { selector: 'node[label = "Movie"]', 
                  css: {'background-color': '#F5A45D', 'content': 'data(title)'}
                },
                { selector: 'edge', 
                  css: {'content': 'data(relationship)', 'target-arrow-shape': 'triangle'}
                }        
              ],
              elements: {
                nodes: [
                  {data: {id: '172', name: 'Tom Cruise', label: 'Person'}},
                  {data: {id: '183', title: 'Top Gun', label: 'Movie'}}
                ],
                edges: [{data: {source: '172', target: '183', relationship: 'Acted_In'}}]
              },
              layout: { name: 'grid'} 
            });
        });