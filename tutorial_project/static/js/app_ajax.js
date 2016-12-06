$(document).ready(function(){



//like button

$('#likes').click(function(){
	var cat_id;
	cat_id = $(this).attr("data-cat_id");

	$.get('/like_category/', {category_id : cat_id}, function(data){
		$('#like-count').html(data);
		$('#likes').hide();
	});


})





});