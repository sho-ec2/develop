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
  $('.detail').slideToggle(2);
});

function pushPlsBtn(v){
  //alert($(v).parent().html());
  var option = $('<select class="form-control member-select" name="member"><option></option></select>');
  $(v).parent().find('.member-add').append(option);
};
