jQuery(($) => {

    function group(arr) {
        let resarr = [];
        let tmp = [];
        for (let i = 0; i < arr.length; i++) {
            if (tmp.includes(arr[i])) {
                el = resarr.find(el => el.t == arr[i]);
                el.c++;
            } else {
                resarr.push({ t: arr[i], c: 1 });
                tmp.push(arr[i]);
            }
        }
        let resstr = "";
        for (let i = 0; i < resarr.length; i++) {
            if (i !== 0) {
                resstr += '\n';
            }
            resstr += `${resarr[i].t}: ${resarr[i].c}`; 
        }
        return resstr;
    }

    let tickets = [];

    $('.dbtn').first().addClass('activeDate');
    $("#id_sum").prop('disabled', true);
    $("#id_sum").val('0')
    $("#id_date").prop('disabled', true);
    $("#id_date").val($('#date1').text())
    $('#id_tickets').prop('disabled', true);


    $('.tbtn').click(function (e) {
        tmp = e.currentTarget.id
        let id = tmp.includes('btnp') ? tmp.replace(/btnp/, '') : tmp.replace(/btnm/, '');
        id = Number(id);
        if (e.currentTarget.id.includes('btnp')) {
            curval = Number($(`#count${id}`).text());
            $(`#count${id}`).text(++curval);
            let tprice = $(`#price${id}`).text();
            tprice = Number(tprice);
            $(`#sum${id}`).text(tprice * curval)
            $('#id_sum').val(Number($('#id_sum').val()) + tprice)
            tickets.push($(`#tik${id}`).text());
            //console.log(tickets);
            $('#id_tickets').text(group(tickets));
        } else if (e.currentTarget.id.includes('btnm')) {
            curval = Number($(`#count${id}`).text());
            if (curval !== 0)
                $(`#count${id}`).text(--curval);
            let tprice = $(`#price${id}`).text();
            tprice = Number(tprice);
            $(`#sum${id}`).text(tprice * curval)
            $('#id_sum').val(Number($('#id_sum').val()) - tprice)
            let idx = tickets.indexOf($(`#tik${id}`).text());
            tickets.splice(idx, 1);
            $('#id_tickets').text(group(tickets));

        }
    })

    $('.dbtn').click(function (e) {
        tmp = e.currentTarget.id
        id = tmp.replace(/date/, '');
        id = Number(id);
        $('.dbtn').removeClass('activeDate');
        $(`#date${id}`).addClass('activeDate');
        $('#id_date').val($(`#date${id}`).text())
    })

    $('#submit_form').click(function (e) {

    })

    $('#tickets_form').submit(function () {
        $("#id_sum").prop('disabled', false);
        $("#id_date").prop('disabled', false);
        $('#id_tickets').prop('disabled', false);
        return true;
    })
});