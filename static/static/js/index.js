let table = $('#datatables').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": {
        "url": "/router/relief",
        "type": "GET"
    },
    "columns": [
        {"data": "id"},
        {"data": "relief_details"},
        {"data": "receiver_name"},
        {"data": "mobile"},
        {"data": "father_name"},
        { "data": "mother_name" },
        {
            "data": null,
            "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
            '<button type="button" class="btn btn-danger">Delete</button>'
        }
    ]
});

let id = 0;

$('#datatables tbody').on('click', 'button', function () {
    let data = table.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-info') {
        // EDIT button
        $('#relief_details').val(data['relief_details']);
        $('#receiver_name').val(data['receiver_name']);
        $('#type').val('edit');
        $('#modal_title').text('EDIT');
        $("#myModal").modal();
    } else {
        // DELETE button
        $('#modal_title').text('DELETE');
        $("#confirm").modal();
    }

    id = data['id'];

});

$('form').on('submit', function (e) {
    e.preventDefault();
    let $this = $(this);
    let type = $('#type').val();
    let method = '';
    let url = '/router/relief';
    if (type == 'new') {
        // new
        method = 'POST';
    } else {
        // edit
        url = url + id + '/';
        method = 'PUT';
    }

    $.ajax({
        url: url,
        method: method,
        data: $this.serialize()
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#confirm').on('click', '#delete', function (e) {
    $.ajax({
        url: '/router/relief' + id + '/',
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});


$('#new').on('click', function (e) {
    $('#relief_details').val('');
    $('#receiver_name').val('');
    $('#type').val('new');
    $('#modal_title').text('NEW');
    $("#myModal").modal();
});


