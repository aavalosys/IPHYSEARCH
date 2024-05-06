        
    function cargarYDibujarRed() {
        const datosRed = {
            nodos: [
            { id: 1, nombre: 'Switch 1', grupo: 1 },
            { id: 2, nombre: 'Router 1', grupo: 2 },
            ],
            enlaces: [
            { source: 1, target: 2 },
            ]
            };

        fetch("/about/cargar_nodos/")  
        .then(response => response.json())
        .then(datosRed => {
        const contenedor = d3.select('#visualizacion-red');
        contenedor.selectAll('*').remove();
        })
        .catch(error => console.error('Error:', error));

            const width = 100;
            const height = 100;
            
            const svg = d3.select('body').append('svg')
            .attr('width', width)
            .attr('height', height);
            
            const simulation = d3.forceSimulation(datosRed.nodos)
            .force('link', d3.forceLink(datosRed.enlaces).id(d => d.id))
            .force('charge', d3.forceManyBody())
            .force('center', d3.forceCenter(width / 3, height / 3));
            
            const link = svg.append('g')
            .attr('class', 'links')
            .selectAll('line')
            .data(datosRed.enlaces)
            .enter().append('line')
            .attr('stroke-width', 5);
            
            const node = svg.append('g')
            .attr('class', 'nodes')
            .selectAll('circle')
            .data(datosRed.nodos)
            .enter().append('circle')
            .attr('r', 5)
            .attr('fill', 'red');
            
            const label = svg.append('g')
            .attr('class', 'labels')
            .selectAll('text')
            .data(datosRed.nodos)
            .enter().append('text')
            .text(d => d.nombre);
            
            simulation.on('tick', () => {
            link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y);
            
            node
            .attr('cx', d => d.x)
            .attr('cy', d => d.y);
            
            label
            .attr('x', d => d.x)
            .attr('y', d => d.y);
            });
            
            simulation.restart();
        
    }