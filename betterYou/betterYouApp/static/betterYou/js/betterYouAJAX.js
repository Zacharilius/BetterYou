$(document).ready(function() {
$('#likes').click(function() {
	console.log("Fired")
	var challid;
	challid = $(this).attr("data-challengeid");
	$.get('/projects/better-you/like-challenge/', {challenge_id: challid}, function(data){
		$('#vote_count').html(data);
		$('#likes').hide();
	});
});
});