$(document).ready(function(){
  putDateInCalendar(datesList);
});

datesList = [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], 
            [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 0, 0]];

// カレンダーの日付を表示
function putDateInCalendar(datesList){
  for(var i = 0; i<5; i++){
    var weekNum = i + 1;
    for(var v = 0; v<7; v++){
      var num = v + 1;
      var dayNum = 'day' + num;
      if (datesList[i][v] == '0'){
        datesList[i][v] = '';
        $('.week' + weekNum + ' .' + dayNum + '').addClass('noEffect');
      }else{
        var a_tag = $(`<a href="#">${datesList[i][v]}</a>`);
        $('.week' + weekNum + ' .' + dayNum + '').append(a_tag);
      }
    }
  }
}

$('.week1').on('click', 'td', function(){
  $('.week1-detail').slideToggle(2);
});

$('.week2').on('click', 'td', function(){
  $('.week2-detail').slideToggle(2);
});

$('.week3').on('click', 'td', function(){
  $('.week3-detail').slideToggle(2);
});

$('.week4').on('click', 'td', function(){
  $('.week4-detail').slideToggle(2);
});

$('.week5').on('click', 'td', function(){
  $('.week5-detail').slideToggle(2);
});

// 削除予定
function pushPlsBtn(v){
  //alert($(v).parent().html());
  var option = $('<select class="form-control member-select" name="member"><option></option></select>');
  $(v).parent().find('.member-add').append(option);
};

// 文字数が4か5ではなく、「hh:mm」「hhmm」以外の場合エラーとする
function adjastTime(v){
  var raw = $(v).val();
  if(raw){
    if(raw.length === 4 || raw.length === 5){
      if(raw.match(/^([01]?[0-9]|2[0-3])([0-5][0-9])$/)){
        var time = raw.substring(0, 2) + ':' + raw.substring(2, 4);
        $(v).val(time);
      }else if(raw.match(/^([01]?[0-9]|2[0-3]):([0-5][0-9])$/)){
      }else{
        alert('入力された時間に間違いがあります');
        $(v).val('');
      }
    }else{
      alert('入力された時間に間違いがあります');
      $(v).val('');
    }
  }
}

// 日付クリック時、詳細を画面に表示する
$('.click-cls').on('click', function(){
  $('.list-group .removal-li').remove();
  if ($(this).hasClass('noEffect')){
    $('.detail-box').css('display', 'none');
  }else{
    $('input').val('');
    $('.detail-box').css('display', 'block');
    var month = $('.title-month').text();
    var day = $(this).text();
    $('#detail-month').text(month);
    $('#detail-day').text(day);
  }

  // djangoソース完成後削除予定
  var details = [];
  var details = [['001', '高橋'], ['002', 'シュート'], ['003', '兄さん']]; 
  list_details(details)
});

// ajaxで取得したデータをリストにして表示する
function list_details(details){
  $.each(details, function(index, value){
    var list = $('<li class="list-group-item removal-li"></li>')
    $(list).append('<label class="name" class="form-check-input" for="' + value[0] + '">' + value[1] + '</label>');
    $(list).append('<input type="checkbox" id=' + value[0] + ' class="floatRight list-checkbox">');
    $('.list-group').append(list);
  });
};

function searchName(){
   var search_name = $('#search').val();
   alert(search_name);
   // search_nameをサーバー側にajaxして検索処理をする
   // 検索結果をlist_detail()を使用して再表示する
};