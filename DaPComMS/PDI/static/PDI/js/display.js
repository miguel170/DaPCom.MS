var Date = new Date();

var getDate = Date.getMonth() + 1 + "-" + Date.getDate() + "-" + Date.getFullYear();

$(document).ready(function() {
    $('.pdi-sheet').hide();
    $('.reveal').hide();

    $('#submit-act').click(function() {
        $('.prerequisite').attr('readonly', true);
        $('.reveal').slideDown(2000);
    });

    $('#new').click(function() {
        $('.pdi-sheet').slideDown(2000);
        $(".pdi-sheet, input[type=text], textarea").val("");
    });

    $('tr').click(function() {
        $('.pdi-sheet').slideDown(2000);
    });

    $('#save').click(function() {
        $('.pdi-sheet').slideUp(2000);
        addInventory();
    });

    $('#cancel').click(function() {
        $('.pdi-sheet').slideUp(2000);
    });

    function addInventory() {

        $("#invTable").append(
            "<tr id = 'row'>" +
            "<th>New Element</td>" +
            "<td>" + getDate + "</td>" +
            "<td>" + getDate + "</td>" +
            "<td class ='text-success'>Active</td>" +
            " <td><button class = 'btn btn-danger btn-fill' href='#remove'>Remove</button></td>" +
            "</tr>"
        );
    }

});