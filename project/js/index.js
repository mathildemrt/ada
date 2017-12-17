function udpateHeatMap(e){
    var genre = e.options[e.selectedIndex].value;
    document.getElementById('heatmap').src = "fig/heatmaps/" + genre + ".html";
}