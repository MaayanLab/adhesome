var tmp_num;
var cat_colors;
cgm = {};

var default_args = {
  'show_tile_tooltips':true,
  'about':'Zoom, scroll, and click buttons to interact with the clustergram.',
  'row_search_placeholder':'Gene'
  // 'ini_view':{'N_row_sum':100}
};

function make_clust(clust_name) {
  d3.json(clust_name+'_clustergram.json', function(network_data){
    var args = $.extend(true, {}, default_args);
    args.root = '#'+clust_name+'_clustergram';
    args.network_data = network_data;

    cgm['clust'] = Clustergrammer(args);
    d3.select(cgm['clust'].params.root+' .wait_message').remove();
    cat_colors = cgm['clust'].params.cat_colors;
  });

}

function resize_container(){
  var rect = d3.select('#wrap').node().getBoundingClientRect();

  var container_width = rect.width - 30;

  d3.selectAll('.clustergrammer_container')
    .style('width', container_width+'px');

  // var container_height = 700;
  // d3.selectAll('.sim_mat_container')
  //   .style('height', container_height+'px');
}

resize_container();

d3.select(window).on('resize',function(){
  resize_container();

  _.each(cgm, function(inst_cgm){
    inst_cgm.resize_viz();
  })
});
