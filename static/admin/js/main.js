$('#searchbar').keydown(function(e){ 
	if( e.which == '13' ){
	  $("#changelist-search").submit(); 
	}
});
$("#searchbar").yourlabsAutocomplete({
	url: search_view,
  choiceSelector: 'a',
}).input.bind('selectChoice', function(e, choice, autocomplete) {
  setTimeout( function(){ window.location.href = choice.attr('href'); }, 500);
});
$(".actions label select[name='action']").change(function(){
	val = $(this).val();
	if(val == 'export_admin_action'){
		label.css("display", "inline");
	}else{
		label.css("display", "none");
	}
})