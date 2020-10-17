let pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

/*
対象ゲームのスコアを取得する
 */
function get_score(){
    let token = $("#api-token").val()
    let event_id = $("#id_event_id").val()
    let gamecount = $("#id_gamecount").val()

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
            $("#id_framecount").val(1);
            $("#id_throwcount").val(1);
            pin_init();
        }

        active_frame();

    })
    .fail((data) => {
      //失敗した場合の処理
      console.log(data.responseText);  //レスポンス文字列を表示
    })
}

let before_framecount = 1
let before_throwcount = 1
/*
編集している投球箇所の表示処理
 */
function active_frame(){
    let framecount = $("#id_framecount").val()
    let throwcount = $("#id_throwcount").val()

    let target_id = "score_" + framecount + "_" + throwcount
    let before_id = "score_" + before_framecount + "_" + before_throwcount
    $("[id=" + before_id + "]").removeClass("active_frame")
    $("[id=" + target_id + "]").addClass("active_frame")
}

/*
ピン情報の初期化処理
 */
function pin_init(){
    pins = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

/*
フレーム情報の更新処理
 */
function update_frame(){
    let token = $("#api-token").val()
    let event_id = $("#id_event_id").val()
    let game_count = $("#id_gamecount").val()
    let frame_count = $("#id_framecount").val()
    let throw_count = $("#id_throwcount").val()

    base_url = "http://127.0.0.1:8000/v1/framescore/"

    let request_data = JSON.stringify({
            event_id: event_id,
            game_count: game_count,
            frame_count: frame_count,
            throw_count: throw_count,
            pins: pins
    })
    console.log(request_data)
    $.ajax({
        url: base_url,
        type:"POST",
        contentType: 'application/json',
        headers:{
            "Authorization": token
        },
        data: request_data
    }).done((data) => {
      console.log(data.responseText);  //レスポンス文字列を表示

    })
    .fail((data) => {
      //失敗した場合の処理
      console.log(data.responseText);  //レスポンス文字列を表示
    })

}

$(window).on("load", function (){
    get_score()

    $("[name=pins]").on("click", function (){
        throwcount = $("#id_throwcount").val()
        $(this).removeClass("rest_1st")
        $(this).removeClass("rest_2nd")
        let target_num = $(this).attr('id').split("pin_")[1] - 1
        let pin_info = pins[target_num]
        if(throwcount == 1){
            if(pin_info!= 1){
                $(this).addClass("rest_1st")
                pins[target_num] = 1
            }else{
                pins[target_num] = 0
            }
        }else if(throwcount == 2){
            if(pin_info!= 2){
                $(this).addClass("rest_2nd")
                pins[target_num] = 2
            }else{
                pins[target_num] = 0
            }
        }
        update_frame()
    })
})
