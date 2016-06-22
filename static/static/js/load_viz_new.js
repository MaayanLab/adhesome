function load_viz_new(network_data){

  console.log('load_viz_new')

  var outer_margins = {
      'top':5,
      'bottom':30,
      'left':195,
      'right':2
    };

  var viz_size = {
    'width':1000,
    'height':600
  };

  about_string = 'Zoom, scroll, and click buttons to interact with the clustergram.';

  // define arguments object
  var args = {
    root: '#container-id-1',
    'network_data': network_data,
    // 'row_label':'Input Genes',
    // 'col_label':'Enriched Terms',
    'outer_margins': outer_margins,
    // 'outline_colors':['black','yellow'],
    // 'tile_click_hlight':true,
    'show_label_tooltips':true,
    // 'show_tile_tooltips':true,
    // 'make_tile_tooltip':make_tile_tooltip,
    // 'highlight_color':'yellow',
    // 'super_label_scale':1.25,
    // 'transpose':true,
    // 'ini_expand':true,
    // 'col_label_scale':1.5,
    // 'row_label_scale':0.8
    // 'force_square':1
    // 'opacity_scale':'log',
    // 'input_domain':2,
    // 'do_zoom':false,
    // 'tile_colors':['#ED9124','#1C86EE'],
    // 'bar_colors':['#ff6666','#1C86EE'],
    // 'tile_colors':['#ff6666','#1C86EE'],
    // 'background_color':'orange',
    // 'tile_title': true,
    // 'click_group': click_group_callback,
    // 'size':viz_size
    // 'order':'rank'
    // 'row_order':'clust'
    // 'col_order':'rank',
    // 'ini_view':{'N_row_sum':'25', 'N_col_sum':'10'},
    // 'current_col_cat':'category-one'
    // 'title':'Clustergrammer',
    'about':about_string,
    // 'sidebar_width':150,
    'row_search_placeholder':'Gene'
  };

  function resize_container(){

    var screen_width = window.innerWidth;
    var screen_height = window.innerHeight - 30;

    d3.select(args.root)
      .style('width', screen_width+'px')
      .style('height', screen_height+'px');
  }

  resize_container();

  d3.select(window).on('resize',function(){
    resize_container();
    cgm.resize_viz();
  });  

  cgm = Clustergrammer(args);


  d3.select(cgm.params.root + ' .wait_message').remove();

  d3.select(cgm.params.root+ ' .title_section')
    .append('a')
    .attr('href', 'http://amp.pharm.mssm.edu/clustergrammer/')
    .append('img')
    .classed('title_image',true)
    .attr('src','/static/img/clustergrammer_logo.png')
    .attr('alt','clustergrammer')
    .style('width','163px')
    .style('margin-left','2px')
    .style('margin-top','5px');
}