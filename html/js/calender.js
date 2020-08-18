$(document).ready(function(){
  putDateInCalendar(datesList);
});

datesList = [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], 
            [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 0, 0]];


function putDateInCalendar(datesList){
  for(var i = 0; i<5; i++){
    var weekNum = i + 1;
    for(var v = 0; v<7; v++){
      if (datesList[i][v] == '0'){
        datesList[i][v] = '';
      }
      var a_tag = $(`<a href="#">${datesList[i][v]}</a>`);
      var num = v + 1;
      var dayNum = 'day' + num;
      $('.week' + weekNum + ' .' + dayNum + '').append(a_tag);
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


function pushPlsBtn(v){
  //alert($(v).parent().html());
  var option = $('<select class="form-control member-select" name="member"><option></option></select>');
  $(v).parent().find('.member-add').append(option);
};

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