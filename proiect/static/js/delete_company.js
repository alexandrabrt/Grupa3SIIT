// console.log('Hello');
$('a[id^="id_delete-"]').on('click', function () {
    // alert($(this).attr('id'));
    $.ajax({
        url: '/location/delete_location/',
        dataType: 'json',
        data: {
            'id_location': $(this).attr('id')
        },
        success: function (data) {
            $(`#row-${data.location}`).hide();
            alert(data.name);
            console.log(data.location);
            location.reload();
        }
    });
});