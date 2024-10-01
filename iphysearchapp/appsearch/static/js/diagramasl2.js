function diagramal2() {
    fetch('/about/diagramal2/')
    .then(response => response.json())
    .then(data => {
    var svgWidth = 700;
    var svgHeight = 400;
    
    var svg = d3.select("#vis-red").append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);
    
    var simulation = d3.forceSimulation(data.nodes)
    .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-200))
    .force("center", d3.forceCenter(svgWidth / 2, svgHeight / 2));
    
    var links = svg.selectAll(".link")
    .data(data.links)
    .enter().append("line")
    .attr("class", "link")
    .style("stroke", "#999")
    .style("stroke-opacity", 0.6)
    .style("stroke-width", 4);
    
    var nodes = svg.selectAll(".node")
    .data(data.nodes)
    .enter().append("image")
    .attr("class", "node")
    .attr("xlink:href", function(d) { 
    return "/static/img/" + d.tipo + ".png"; 
    })
    .attr("width", 60)
    .attr("height", 60)
    .call(d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended));

    
    simulation.on("tick", () => {
    links.attr("x1", d => d.source.x)
    .attr("y1", d => d.source.y)
    .attr("x2", d => d.target.x)
    .attr("y2", d => d.target.y);

    nodes.attr("x", d => d.x - 15)
    .attr("y", d => d.y - 15);
    });
    
    function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
    }
    
    function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
    }
    
    function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
    }
    })
    .catch(error => console.error('Error:', error));
    }