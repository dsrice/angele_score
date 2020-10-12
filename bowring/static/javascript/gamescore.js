/*
対象ゲームのスコアを取得する
 */
function get_score(){
    token = $("#api-token").val()
    event_id = $("#id_event_id").val()

    base_url = "http://127.0.0.1:8000/v1/gamescore/"
    $.ajax({
        url: base_url,
        type:"GET",
        dataType:"json",
        headers:{
            "Authorization": token
        },
        data: {
            "event_id": event_id
        }
    })
    .done((data) => {
      //成功した場合の処理
      console.log(data);
    })
    .fail((data) => {
      //失敗した場合の処理
      console.log(data.responseText);  //レスポンス文字列を表示
    })
    .always((data) => {
      //成功・失敗どちらでも行う処理
      console.log(data);
    });
}

$(window).on("load", function (){
    get_score()
})
