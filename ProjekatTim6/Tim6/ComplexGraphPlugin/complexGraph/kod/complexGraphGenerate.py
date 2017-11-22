import os

from ProjekatTim6.services.prikaz import PrikazatiService


class ComplexGraphPrikaz(PrikazatiService):
    def naziv(self):
        return "Complex graph"
    def identifier(self):
        return "complex_graph_plugin"

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
        .linkDistance(500) //razmak izmedju elemenata
        .charge(-300)//koliko da se elementi odbijaju
        .start(); //pokreni izracunavanje pozicija

    //var zoom2 = d3.behavior.zoom().scale(.5);
    
    svg=d3.select('#svggraph').call(d3.behavior.zoom().scaleExtent([-5, 8]).on("zoom", zoom)).append("g");
    svg2=d3.select('#svgbird').append("g").attr("transform", "translate(120,150)scale(0.5)").append('g');
    
    //svg2.append("g").attr("transform","scale(-1,1)"); 
/*
    svg.append("rect")
    .attr("class", "overlay")
    .attr("width", 600)
    .attr("height", 600);
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
       duzina=170;
       brKategorija=d.attributes.length /22;

        naslovSize = 20
       textSize=14;
       visina=(brKategorija==0)?textSize:brKategorija*textSize;
      visina+=textSize;
      
      

      //Ubacivanje kvadrata
      d3.selectAll("g#"+d.name).append('rect').
      attr('x',0).attr('y',0-10).attr('width',duzina+20).attr('height',visina+30)
      .attr('fill','blue');

      //Ubacivanje naziva
      d3.selectAll("g#"+d.name).append('text').attr('x',duzina/2).attr('y',10)
      .attr('text-anchor','middle')
      .attr('font-size',naslovSize).attr('font-family','sans-serif')
      .attr('fill','white').text(d.name);

      //Ubacivanje razdelnika
      d3.selectAll("g#"+d.name).append('line').
      attr('x1',0).attr('y1',naslovSize).attr('x2',duzina).attr('y2',naslovSize)
      .attr('stroke','black').attr('stroke-width',2);

      //Ubacivanje atributa
      var red = 1;
      var bivsi_zarez=0;
      var string_za_prkaz="";

      if(d.attributes.length>=24)
      {

          for(var i =0; i <d.attributes.length; i++)
          {
    
            if(i % 24 ==0)
            {
                string_za_prikaz=d.attributes.substring(bivsi_zarez,i);
                d3.selectAll("g#"+d.name).append('text').attr('x',0).attr('y',20+ red*textSize)
              .attr('text-anchor','start')
              .attr('font-size',textSize).attr('font-family','sans-serif')
              .attr('fill','white').text(string_za_prikaz);
              bivsi_zarez=i;
              red=red+1;
            }
          }
      }
      else
      {
        string_za_prikaz=d.attributes.substring(bivsi_zarez,d.attributes.length);
            d3.selectAll("g#"+d.name).append('text').attr('x',0).attr('y',20+ red*textSize)
          .attr('text-anchor','start')
          .attr('font-size',textSize).attr('font-family','sans-serif')
          .attr('fill','white').text(string_za_prikaz);
      }

    }
    
        """
