
$(".link_delete").click(function(e){
    e.preventDefault();
    let url_id = $(this).attr('data_id')
    $.ajax({
        type: "get",
        url: "/url/delete/"+url_id+"/"
    }).done(function(){
        window.location.reload();
    });
})



$(".link_update").click(function(e){
     e.preventDefault();
    let url_id = $(this).attr('data_id')
    $.ajax({
        type: "get",
        url: "/url/update/"+url_id+"/"
    }).done(function(){
        window.location.reload();
    });
})


$("#update_all").click(function(){
    $.ajax({
        type: "get",
        url: "/url/all/update/"
    }).done(function(){
        location.reload();
        alert("Links update in process, wait please!")
    });
})