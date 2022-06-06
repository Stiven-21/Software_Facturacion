jQuery(document).ready(function(){
	jQuery("#identificacion").on('input', function (e) {
		jQuery(this).val(jQuery(this).val().replace(/[^0-9]/g, ''));
	});

	jQuery("#identificacion_search").on('input', function (e) {
		jQuery(this).val(jQuery(this).val().replace(/[^0-9]/g, ''));
	});
});