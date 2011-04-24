$(document).ready(function (e) {
    function onEditCB(e) {
	var id = parseInt($(this).parents('div.photo').attr('rel'));
	var thumburl = $('div.photo[rel="'+id+'"] img').attr('src');
	var title = $('div.photo[rel="'+id+'"] a.photo').attr('title');
	
	$("div#editwindow").find('input[name="photo_id"]').val(id);
	$("div#editwindow").find('input[name="name"]').val(title);
	$("div#editwindow").find('img.thumbnail').attr('src', thumburl);
	$("div#editwindow").show();
	$.fancybox({'href': '#editwindow',
		    'onClosed'		: function() {
			$("#editwindow").hide();
		    }});
	return false;
    }

    function onDeleteCB(e) {
	var id = parseInt($(this).parents('div.photo').attr('rel'));
	if (!confirm("tem certeza que deseja apagar essa imagem?"))
	    return;

	$.post($('div#editwindow form').attr('action'),
	       {'photo_id': id, 'action': 'delete_image'},
	       function (data) {
		   $('div.photo[rel="'+id+'"]').remove();
	       });
    }

    $('#file_upload').fileUploadUI({
        uploadTable: $('#files'),
        buildUploadRow: function (files, index) {
            return $('<tr><td>' + files[index].name + '<\/td>' +
                     '<td class="file_upload_progress"><div><\/div><\/td>' +
                     '<td class="file_upload_cancel">' +
                     '<button class="ui-state-default ui-corner-all" title="Cancel">' +
                     '<span class="ui-icon ui-icon-cancel">Cancel<\/span>' +
                     '<\/button><\/td><\/tr>');
        },
        buildDownloadRow: function (file) {
	    if (file.error) {
		alert(file.error);
		return;
	    }

	    $('div#album').append('<div class="photo" rel="'+file.id+'"><a class="photo" title="'+file.name+'" href="'+file.url+'" rel="group"><img src="'+file.thumburl+'"/></a><p><a class="edit" href="#">Editar</a> <a class="delete" href="#">Apagar</a></p></div>');
	    $('div.photo[rel="'+file.id+'"] a.edit').click (onEditCB);
	    $('div.photo[rel="'+file.id+'"] a.delete').click (onDeleteCB);
	    setFancyBox();
	    return $('');

	}
    });

    $('div#editwindow form').submit(function (e) {
	function onEdit(data) {
	    if (data.error) {
		alert(data.error);
		return;
	    }
	    
	    $.fancybox.close();
	    $('div#editwindow').hide();
	    $('div.photo[rel="'+data.id+'"] a.photo').attr('title', data.name);
	    $('div.photo[rel="'+data.id+'"] b.title').text(data.name);
	}
	data = $(this).serialize();
	$.post($(this).attr('action'), data, onEdit);
	return false;
    });

    $("div.photo a.edit").click (onEditCB);
    $("div.photo a.delete").click (onDeleteCB);
});