// ajaxで取得したデータをリストにして表示する
function list_details(details){
  $.each(details, function(index, value){
    var list = $('<li class="list-group-item removal-li"></li>')
    $(list).append('<label class="name" class="form-check-input" for="' + value[0] + '">' + value[1] + '</label>');
    $(list).append('<input type="checkbox" id=' + value[0] + ' class="float-right list-checkbox">');
    $('.list-group').append(list);
  });
};

function searchName(){
   var search_name = $('#search').val();
   alert(search_name);
   // search_nameをサーバー側にajaxして検索処理をする
   // 検索結果をlist_detail()を使用して再表示する
};

// djangoソース完成後削除予定
// var details = [];
var details = [['001', '高橋'], ['002', 'シュート'], ['003', '兄さん']]; 
list_details(details)