/*
対象ゲームのスコアを取得する
 */
function get_score(){
    $.ajax({
        url:"v1/gamescore",
        type:"POST",
        dataType:"json",
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
