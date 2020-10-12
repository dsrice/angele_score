/*
対象ゲームのスコアを取得する
 */
function get_score(){
    token = $("#api-token").val()
    event_id = $("#id_event_id").val()
    gamecount = $("#id_gamecount").val()

    base_url = "http://127.0.0.1:8000/v1/gamescore/"
    $.ajax({
        url: base_url,
        type:"GET",
        dataType:"json",
        headers:{
            "Authorization": token
        },
        data: {
            "event_id": event_id,
            "game_count": gamecount
        }
    }).done((data) => {
        if(data["score"] == null){
            // 未入力状態
            $("#id_framecount").val(1)
            $("#id_throwcount").val(1)
        }

        active_frame();

    })
    .fail((data) => {
      //失敗した場合の処理
      console.log(data.responseText);  //レスポンス文字列を表示
    })
}

before_framecount = 1
before_throwcount = 1
/*
編集している投球箇所の表示処理
 */
function active_frame(){
    framecount = $("#id_framecount").val()
    throwcount = $("#id_throwcount").val()

    target_id = "score_" + framecount + "_" + throwcount
    before_id = "score_" + before_framecount + "_" + before_throwcount
    $("[id=" + before_id + "]").removeClass("active_frame")
    $("[id=" + target_id + "]").addClass("active_frame")
}

$(window).on("load", function (){
    get_score()
})
