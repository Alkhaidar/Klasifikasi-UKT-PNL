$(document).ready(function () {
    $("#myTable").DataTable({
        "scrollX": true,
        "language": {
            "search": "",
            "searchPlaceholder": "Search...",
            "decimal": ",",
            "thousands": ".",
        },
    });

    $('.dataTables_filter input[type="search"]').css({
        "marginBottom": "10px"
    });
});
