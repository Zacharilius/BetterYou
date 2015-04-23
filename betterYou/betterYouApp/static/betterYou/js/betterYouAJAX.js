$(document).delegate('#likes', 'click', function() {
	var challid;
	challid = $(this).attr("data-challengeid");
	$.get('/projects/better-you/like-challenge/', {challenge_id: challid}, function(data){
		console.log(data);
		$("[data-vote=" + challid + "]").html(data)
	});
	$(this).hide();
});

$(document).delegate('#points', 'click', function() {
	var challid;
	challid = $(this).attr("data-challengeid2");
	$.get('/projects/better-you/point-add/', {challenge_id: challid}, function(data){
		console.log(data);
		$("[data-vote=" + challid + "]").html(data)
	});
	$(this).hide();
});