import os

"""""
U ovoj klasi su implementirane metode staticPrikaz(self) i srediPrikaz(self) koje odredjuju pozicije
child-ova i node-ova kao i njihov celokupan prikaz u browser-u. 
"""""

from ProjekatTim6.services.prikaz import PrikazatiService


class SimpleGraphPrikaz(PrikazatiService):
    def naziv(self):
        return "Simple Graph"

    def identifier(self):
        return "simple_graph_plugin"

    def staticPrikaz(self):
        return """
        var force = null
    var svg = null
    var svg2 = null
    var link =null
    var link2 = null
    var node = null
    var node2 = null

    var zobrd =[];
    var brnod=0;




        function zoom() {
        svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
        }

    function tick(e) {

        node.attr("transform", function(d) {return "translate(" + d.x + "," + d.y + ")";})
            .call(force.drag);

        link.attr('x1', function(d) { return d.source.x; })
            .attr('y1', function(d) { return d.source.y; })
            .attr('x2', function(d) { return d.target.x; })
            .attr('y2', function(d) { return d.target.y; });

        node2.attr("transform", function(d) {return "translate(" + d.x + "," + d.y + ")";})
            .call(force.drag);

        link2.attr('x1', function(d) { return d.source.x; })
            .attr('y1', function(d) { return d.source.y; })
            .attr('x2', function(d) { return d.target.x; })
            .attr('y2', function(d) { return d.target.y; });

    }

        

        """

    @property
    def srediPrikaz(self):
        return """
        MyData.links.forEach(function(link) {
            link.source = nodes[link.source];
            link.target = nodes[link.target];
        });


    force = d3.layout.force() //kreiranje force layout-a
        .size([500, 500]) //raspoloziv prostor za iscrtavanje
        .nodes(d3.values(nodes)) //dodaj nodove
        .links(MyData.links) //dodaj linkove
        .on("tick", tick) //sta treba da se desi kada su izracunate nove pozicija elemenata
        .linkDistance(100) //razmak izmedju elemenata
        .charge(-200)//koliko da se elementi odbijaju
        .start(); //pokreni izracunavanje pozicija


    
    
    svg=d3.select('#svggraph').call(d3.behavior.zoom().scaleExtent([-5, 8]).on("zoom", zoom)).append("g");
    svg2=d3.select('#svgbird').append("g").attr("transform", "translate(120,150)scale(0.5)").append('g');
    //d3.select('#svggraph').call(d3.behavior.zoom().scaleExtent([-5, 8]).on("zoom", zoom))/*.append("g");*/
    

    svg.append("rect")
    .attr("class", "overlay")
    .attr("width", 500)
    .attr("height", 500);
    
    
    //svg2
    /*
    svg2.append("rect")
    .attr("class", "overlay")
    .attr("width", 500)
    .attr("height", 500)
*/

    link = svg.selectAll('.link')
        .data(MyData.links)
        .enter().append('line')
        .attr('class', 'link')


    link2 = svg2.selectAll('.link')
       .data(MyData.links)
       .enter().append('line')
       .attr('class', 'link');

    // add the nodes
    node = svg.selectAll('.node')
        .data(force.nodes()) //add
        .enter().append('g')
        .attr('class', 'node')
        .attr('id', function(d){return d.name;});

    node2 = svg2.selectAll('.node')
        .data(force.nodes()) //add
        .enter().append('g')
        .attr('class', 'node')
        .attr('id', function(d){return d.name;});

    d3.selectAll('.node').each(function(d){prikaz(d);});
        
        
        
        
        
        
        
        
        
            function prikaz(d){

        naslovSize = 17

      //Ubacivanje kruga
      d3.selectAll("g#"+d.name).append('circle').
      attr('cx',0).attr('cy',0-10).attr('r',6*(d.name.length)).attr('fill','black');
      

      //Ubacivanje naziva
      d3.selectAll("g#"+d.name).append('text').attr('x',-24).attr('y',0-5)
      
      .attr('font-size',naslovSize).attr('font-family','sans-serif')
      .attr('fill','white').text(d.name);

    }

        """

"""""
.attr('text-anchor','middle') ne koristiti u 149.
"""""